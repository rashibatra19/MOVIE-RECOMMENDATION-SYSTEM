from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import streamlit as st

movies=pd.read_csv('dataset.csv')
movies=movies[['id', 'title', 'overview', 'genre']]
movies['tags'] = movies['overview']+movies['genre']
new_data  = movies.drop(columns=['overview', 'genre'])
cv=CountVectorizer(max_features=10000, stop_words='english')
vector=cv.fit_transform(new_data['tags'].values.astype('U')).toarray()
similarity=cosine_similarity(vector)
movies_list=movies['title'].values
st.header("Movie Recommender System")
st.write("🎥 Discover your next favorite film with our smart Movie Recommender System! 🍿 Get personalized recommendations based on your taste. 🎬")
st.write("👉 Simply enter the name of a movie you've already watched ")


selectvalue=st.selectbox("Select movie from dropdown", movies_list)


def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie=[]
    for i in distance[1:9]:
        recommend_movie.append(movies.iloc[i[0]].title)
    return recommend_movie

if st.button("Show Recommend"):
    movie_name = recommend(selectvalue)
    for name in movie_name:
        st.text(name)






