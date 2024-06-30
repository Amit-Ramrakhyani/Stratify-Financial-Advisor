import matplotlib.pyplot as plt

def explain_recommendation(user_id, recommendation):
    """Generate visual explanation for investment recommendations."""
    labels = list(recommendation['allocation'].keys())
    sizes = list(recommendation['allocation'].values())

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title(f'Investment Strategy for User {user_id}')
    plt.show()