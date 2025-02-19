import pandas as pd
import numpy as np

def generate_customer_data(num_rows=1000, output_file="customer_data.csv"):
    # Set seed for reproducibility
    np.random.seed(42)
   
    # Define sample data
    names = ["John Doe", "Jane Smith", "Alice Johnson", "Bob Lee"]
    data = {
        "customer_name": np.random.choice(names, size=num_rows),
        "age": np.random.randint(18, 80, size=num_rows).astype(float),
        "quantity": np.random.randint(1, 10, size=num_rows),
        "price": np.round(np.random.uniform(5, 200, size=num_rows), 2)
    }
   
    # Introduce missing values in the 'age' column (5% of rows)
    missing_indices = np.random.choice(num_rows, size=int(num_rows * 0.05), replace=False)
    for idx in missing_indices:
        data["age"][idx] = np.nan

    # Create DataFrame and save as CSV
    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
    print(f"Dataset generated: {output_file}")

if __name__ == "__main__":
    generate_customer_data()
