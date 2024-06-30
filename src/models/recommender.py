def generate_recommendations(user_data, transaction_data):
    """Generate investment recommendations based on user data and transaction data."""
    
    recommendations = []
    
    for _, user in user_data.iterrows():
        # Example: Tailor the strategy based on the user's risk tolerance
        if user['risk_tolerance'] == 'low':
            strategy = 'Low risk, conservative portfolio'
            allocation = {'stocks': 20, 'bonds': 50, 'cash': 30}
            expected_return = '3-5%'
            risk_level = 'Low'
        elif user['risk_tolerance'] == 'medium':
            strategy = 'Moderate risk, diversified portfolio'
            allocation = {'stocks': 50, 'bonds': 30, 'cash': 20}
            expected_return = '5-7%'
            risk_level = 'Medium'
        else:  # High risk tolerance
            strategy = 'High risk, aggressive portfolio'
            allocation = {'stocks': 70, 'bonds': 20, 'cash': 10}
            expected_return = '7-10%'
            risk_level = 'High'
        
        # Collect recommendations
        recommendations.append({
            'user_id': user['user_id'],
            'strategy': strategy,
            'allocation': allocation,
            'expected_return': expected_return,
            'risk_level': risk_level
        })
    
    return recommendations

def gauge_financial_behavior(transaction_analysis):
    """Gauge user's financial behavior and stress points."""
    behavior_analysis = []
    
    for _, row in transaction_analysis.iterrows():
        stress_level = 'Low'
        if row['average_spent'] > 0.5 * row['total_spent']:
            stress_level = 'High'
        elif row['average_spent'] > 0.3 * row['total_spent']:
            stress_level = 'Medium'
        
        behavior_analysis.append({
            'user_id': row['user_id'],
            'stress_level': stress_level
        })
    
    return behavior_analysis

