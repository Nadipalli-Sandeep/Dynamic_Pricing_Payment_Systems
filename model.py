# model.py

import pandas as pd
import joblib

# Load the model and preprocessor
model = joblib.load('dynamic_pricing_model.pkl')
preprocessor = joblib.load('data_preprocessor.pkl')

def dynamic_pricing(transaction_amount, payment_method, hour_of_day, day_of_week, competitor_fee, customer_segment):
    # Create input data for prediction
    input_data = pd.DataFrame([[transaction_amount, payment_method, hour_of_day, day_of_week, competitor_fee, customer_segment]],
                               columns=['transaction_amount', 'payment_method', 'hour_of_day', 'day_of_week', 'competitor_fee', 'customer_segment'])
    
    # Transform the input data using the preprocessor
    input_processed = preprocessor.transform(input_data)
    
    # Predict transaction fee using the trained model
    predicted_fee = model.predict(input_processed)
    
    return predicted_fee[0]
