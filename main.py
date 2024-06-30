from src.utils.data_utils import load_user_data, preprocess_data, analyze_transaction_history, load_transaction_data
from src.models.recommender import generate_recommendations, gauge_financial_behavior
from src.models.explainAI import explain_recommendation
from src.monitoring import monitor_transactions

def main():
    # Load user data
    user_data_path = 'data/user_data.csv'
    user_data = load_user_data(user_data_path)
    
    # Preprocess data
    processed_data = preprocess_data(user_data)
    
    # Load and analyze transaction data
    transactions = load_transaction_data()
    transaction_analysis = analyze_transaction_history(transactions)
    
    # Generate recommendations
    recommendations = generate_recommendations(processed_data, transaction_analysis)
    
    # Gauge financial behavior
    behavior_analysis = gauge_financial_behavior(transaction_analysis)
    
    # Display recommendations and explanations
    for rec in recommendations:
        user_id = rec['user_id']
        print(f"Investment Recommendations for User {user_id}:")
        print(f"Strategy: {rec['strategy']}")
        print(f"Allocation: Stocks={rec['allocation']['stocks']}%, Bonds={rec['allocation']['bonds']}%, Cash={rec['allocation']['cash']}%")
        print(f"Expected Return: {rec['expected_return']}")
        print(f"Risk Level: {rec['risk_level']}")
        
        explain_recommendation(user_id, rec)
    
    # Start continuous monitoring (commented out for now)
    # monitor_transactions()

if __name__ == "__main__":
    main()
