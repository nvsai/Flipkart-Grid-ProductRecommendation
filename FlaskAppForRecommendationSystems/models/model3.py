# models/model3.py
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer


def get_recommendations(userlocation):
    # Load the data
    data = pd.read_csv("data/data.csv")

    # Create a feature vector for each product
    product_features = TfidfVectorizer(stop_words="english").fit_transform(data["product_description"])
    # Create a nearest neighbors model
    model = NearestNeighbors(n_neighbors=5)
    model.fit(product_features)

    # Get the location of the current user
    user_location = userlocation
    print(user_location)
    # Find similar users in the same location
    user_indices = data[data["user_location"] == user_location].index
    similar_users = model.kneighbors(product_features[user_indices], n_neighbors=5)

    # Get the indices of the products that the similar users bought
    similar_user_product_indices = []
    for indices in similar_users[1]:
        similar_user_product_indices.extend(indices)
    recommendations = []  
    # Recommend products to the current user based on content-based filtering
    content_based_recommendations = []
    recs=[]
    for index in similar_user_product_indices:
        product_id = data["product_id"].iloc[index]
        if product_id not in data.loc[user_indices, "product_id"]:
            content_based_recommendations.append(product_id)
            que=data.query('product_id=='+str(product_id))
            recs.append(que.values.tolist())

    for pro in recs:
      recommendations.append(pro[0][2])
    # Print the recommended products
    print(content_based_recommendations)

    
    return recommendations