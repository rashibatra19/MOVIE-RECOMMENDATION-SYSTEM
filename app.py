import streamlit as st
import pickle
movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
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
