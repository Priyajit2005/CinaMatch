
import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load pickled data
movies = pickle.load(open('movies_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))


movies_list = movies['title'].values

st.header('Movie Recommender System')
selectvalue = st.selectbox('Select movies from the list', movies_list)

def recommend(movie_name):
    index = movies[movies['title'] == movie_name].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommended_movie = []
    for i in distance[1:6]:  # Skip the movie itself
        recommended_movie.append(movies.iloc[i[0]].title)
    return recommended_movie  


if st.button('Recomendation Movies'):
    movie_name = recommend(selectvalue)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
    with col2:
        st.text(movie_name[1])
    with col3:
        st.text(movie_name[2])
    with col4:
        st.text(movie_name[3])
    with col5:
        st.text(movie_name[4])

