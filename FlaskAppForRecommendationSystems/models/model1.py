# models/model1.py
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def get_recommendations(user_id):
    # Calculate recommendations based on the model
    movie_ratings_df = pd.read_csv("data/movie_ratings.csv")
    user_item_rating_matrix = movie_ratings_df.pivot_table(
    index="user_id", columns="movie_id", values="rating"
    )
    user_similarities = user_item_rating_matrix.corr(method="pearson")
    user_similarity_threshold = 0.3
    user_similarities.loc[user_id, user_id] = np.NAN
    top_3_similar_users = {}
    top_3_similar_users[user_id] = user_similarities[user_id].sort_values(
        ascending=False
    )[:3]
    
    similar_users = top_3_similar_users[user_id]
    merchandise_products = movie_ratings_df[
        movie_ratings_df["user_id"].isin(similar_users.index)
    ]
    merchandise_product_ratings = merchandise_products.groupby(
        "movie_id"
    )["rating"].mean()
    recommended_merchandise_products = merchandise_product_ratings.sort_values(
        ascending=False
    )
    print("Recommended merchandise products for user ID {}".format(user_id))
    for movie_id, rating in recommended_merchandise_products.items():
        print("- {}".format(movie_id))
    recs = []
    for movie_id, rating in recommended_merchandise_products.items():
        que=movie_ratings_df.query('user_id=='+str(user_id)+'and movie_id=='+str(movie_id))
        print("- {}".format(movie_id))
        recs.append(que.values.tolist())
    recommendations=[]
    for pro in recs:
      recommendations.append(pro[0][3])
    return recommendations
