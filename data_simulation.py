# data_simulation.py

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

def simulate_transaction_data(num_records=10000):
    np.random.seed(42)
    
    data = {
        'transaction_id': np.arange(num_records),
        'transaction_amount': np.random.randint(50, 1000, num_records),
        'payment_method': np.random.choice(['Credit Card', 'UPI', 'Wallet'], num_records),
        'transaction_time': pd.date_range(start='2023-01-01', periods=num_records, freq='h'),
        'customer_segment': np.random.choice(['Regular', 'Premium'], num_records),
        'competitor_fee': np.random.uniform(0.5, 3.0, num_records)
    }

    df = pd.DataFrame(data)

    # Extract features
    df['hour_of_day'] = df['transaction_time'].dt.hour
    df['day_of_week'] = df['transaction_time'].dt.dayofweek
    df['month'] = df['transaction_time'].dt.month

    return df

def train_model(df):
    # Separate features and target (simulate fees)
    X = df[['transaction_amount', 'payment_method', 'hour_of_day', 'day_of_week', 'customer_segment', 'competitor_fee']]
    y = np.random.uniform(1, 5, len(df))  # Simulated transaction fees

    # One-hot encoding for categorical features
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), ['transaction_amount', 'competitor_fee', 'hour_of_day', 'day_of_week']),
            ('cat', OneHotEncoder(), ['payment_method', 'customer_segment'])
        ]
    )

    X_processed = preprocessor.fit_transform(X)

    # Split into training and test data
    X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)

    # Build the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save the model and preprocessor
    joblib.dump(model, 'dynamic_pricing_model.pkl')
    joblib.dump(preprocessor, 'data_preprocessor.pkl')

if __name__ == "__main__":
    # Simulate data and train model
    df = simulate_transaction_data()
    train_model(df)
