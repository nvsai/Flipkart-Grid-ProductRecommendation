# Flipkart-Grid-5.0-ProductRecommendation
This a repository that has ML code to our solution for Flipkart Grid challenge on Product Recommendation
PLease See the particular .ipynb for code level explanation of concepts

In UserRecommendationbyMovies we used pearson similarity between different users and their ratings for movies in categories like Barbie,Disney,Marvel,DC,TRansformers. This a User-Based Collborative filtering technique for product merchendise recommendation based on movie ratings of similar users.

In UserRecommendationbyAppUsage we used cosine similarity between users and products to find relevent products for different users. This a Item-Based Collborative filtering technique for product recommendation based on Mobile apps usage.
we have 5 categories in the code namely Gaming, JobSearch, Social, Shopping, Entertainment for users and products.we can collect more products and map them with categories and then collect more user app usage data to implement a high end recommendation system.

In UserRecommendationbylocation we take a location and then get similar users to the current userin the location ,then recommends products necessary in the location.
THis code uses User-based collaborative filtering approach with content-based filtering technique.

UserRecommendationbyimages takes a image input ,extract features then find cosine similarity between existing products in database then recommend users similar products.This is item-based collaborative filtering technique.
