# models/model2.py
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def get_recommendations(user_id):
    # Calculate recommendations based on the model
    # Sample user app time data (hours spent on each app)
    users = {
        "User1": [5, 2, 0, 0, 1],  # [Gaming, JobSearch, Social, Shopping, Entertainment]
        "User2": [1, 0, 4, 2, 3],
        # ... Add more users
    }

    # Sample product categories and their corresponding features
    products = {
        "GamingKeyboard": [1, 0, 0, 0, 0],  # [Gaming, JobSearch, Social, Shopping, Entertainment]
        "FormalTie": [0, 1, 0, 0, 0],
        "GamingMouse": [1, 0, 0, 0, 0],
        "FormalShirt": [0, 1, 0, 0, 0],
        "Perfume": [0,0,1,0,0],
        "display": [1,0,0,0,1]
        # ... Add more products
    }

    # Convert user and product data into numpy arrays
    user_matrix = np.array([users[user] for user in users])
    product_matrix = np.array([products[product] for product in products])

    # Compute cosine similarity between user preferences and product features
    similarities = cosine_similarity(user_matrix, product_matrix)

    # Recommend products for each user based on highest similarity
    num_recommendations = 3
    """ for i, user in enumerate(users):
        similar_products_indices = np.argsort(similarities[i])[::-1][:num_recommendations]
        recommended_products = [list(products.keys())[idx] for idx in similar_products_indices] """
    similar_products_indices = np.argsort(similarities[user_id])[::-1][:num_recommendations]
    recommended_products = [list(products.keys())[idx] for idx in similar_products_indices]
    print(f"Recommendations for {user_id}: {recommended_products}")
    recommendations = recommended_products
    return recommendations