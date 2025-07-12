import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample movie dataset
data = {
    'title': ['The Matrix', 'Inception', 'Interstellar', 'The Dark Knight', 'Tenet'],
    'genre': ['Sci-Fi Action', 'Sci-Fi Thriller', 'Sci-Fi Drama', 'Action Crime', 'Sci-Fi Action']
}

df = pd.DataFrame(data)

# Convert genre text to feature vectors
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['genre'])

# Compute similarity scores
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Map indices for quick lookup
indices = pd.Series(df.index, index=df['title'])

# Recommendation function
def recommend(title, num_recommendations=3):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:num_recommendations+1]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices]

# Try it!
print("Recommendations for 'Inception':")
print(recommend('Inception'))



