import pandas as pd
from pymongo import MongoClient

def load_user_data(file_path):
    """Load user financial data from CSV."""
    return pd.read_csv(file_path)

def preprocess_data(data):
    """Preprocess user data for model input."""
    # Example: Normalize numerical data, encode categorical features, etc.
    return data

def load_transaction_data():
    """Load transaction data from MongoDB."""
    client = MongoClient('localhost', 27017)
    db = client['bank_database']
    collection = db['transactions']
    transactions = list(collection.find())
    return pd.DataFrame(transactions)

def analyze_transaction_history(transactions):
    """Analyze user transaction history."""
    # Example: Calculate average monthly expenditure, categorize spending, etc.
    analysis = transactions.groupby('sender_id').agg({
        'amount': ['sum', 'mean', 'count']
    }).reset_index()
    analysis.columns = ['user_id', 'total_spent', 'average_spent', 'transaction_count']
    return analysis
