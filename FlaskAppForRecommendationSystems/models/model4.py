# models/model4.py
import cv2
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def get_recommendations():
    pathc="images/"
# Example images of red t-shirts
    image_paths = [
        "red_tshirt_1.jpg",
        "red_tshirt_2.jpg",
        "red_tshirt_3.jpg",
        # Add more image paths here
    ]
    def extract_features(image_path):
        image = cv2.imread(pathc+image_path)
        # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        resized_image = cv2.resize(image, (100, 100))  # Resize for consistent features
        print(image_path)
        return resized_image.flatten()  # Flatten the image into a 1D vector
    # Extract features for all images
    image_features = [extract_features(path) for path in image_paths]
    # Convert the features into a numpy array
    image_features_array = np.array(image_features)
    # Calculate cosine similarity between images
    similarities = cosine_similarity(image_features_array)
    # Recommend similar products based on a given image
    def recommend_similar_products(query_image_features, num_recommendations=3):
        query_image_features = query_image_features.flatten().reshape(1, -1)
        query_similarity = cosine_similarity(query_image_features, image_features_array)
        similar_indices = np.argsort(-query_similarity)[0][:num_recommendations]

        return [image_paths[idx] for idx in similar_indices]
        

    # Example query image (you can replace this with your own query image)
    query_image_path = "query_red_tshirt.jpg"
    query_image_features = extract_features(query_image_path)
    # Recommend similar products based on the query image
    recommended_products = recommend_similar_products(query_image_features)
    print("Recommended similar products:")
    for product in recommended_products:
        print(product)
    recommendations = recommended_products
    return recommendations