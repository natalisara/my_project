import pandas as pd
from logger_helper import log_decorator  # Import the logger decorator


@log_decorator
def load_data(filepath="customer_data.csv") -> pd.DataFrame:
    """Load CSV data into a DataFrame."""
    return pd.read_csv(filepath)


@log_decorator
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing 'age' values with the mean age."""
    mean_age = df["age"].mean()
    df["age"] = df["age"].fillna(mean_age)
    return df


@log_decorator
def add_total_spend(df: pd.DataFrame) -> pd.DataFrame:
    """Add a new column 'total_spend' computed as quantity * price."""
    df["total_spend"] = df["quantity"] * df["price"]
    return df


@log_decorator
def aggregate_data(df: pd.DataFrame) -> pd.DataFrame:
    """Group data by 'customer_name' and sum the 'total_spend'."""
    return df.groupby("customer_name", as_index=False)["total_spend"].sum()


@log_decorator
def run_pipeline(filepath="customer_data.csv") -> pd.DataFrame:
    """
    Execute the full data pipeline:
      1. Load data.
      2. Clean data.
      3. Add a total spend column.
      4. Aggregate data by customer.
    """
    return (
        load_data(filepath).pipe(clean_data).pipe(add_total_spend).pipe(aggregate_data)
    )


if __name__ == "__main__":
    result_df = run_pipeline()
    print("Aggregated Total Spend by Customer:")
    print(result_df.head())
