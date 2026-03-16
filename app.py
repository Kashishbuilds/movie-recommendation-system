# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 20:18:41 2026

@author: Acer
"""
import streamlit as st
import pickle
import difflib

# Page configuration
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)

# CSS styling
st.markdown("""
<style>

.recommend-box{
background-color:#f0f2f6;
padding:12px;
border-radius:10px;
margin-bottom:8px;
font-size:18px;
}

</style>
""", unsafe_allow_html=True)

# Load saved files
movies_data = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

# Sidebar
st.sidebar.title("Instructions")
st.sidebar.write("1️⃣ Select a movie from the dropdown")
st.sidebar.write("2️⃣ Click Recommend Movies")
st.sidebar.write("3️⃣ Get similar movie suggestions")

# BIG TITLE (one line)
st.markdown(
"<h1 style='text-align:center; color:#ff4b4b; font-size:55px; white-space:nowrap;'>🎬 Movie Recommendation System</h1>",
unsafe_allow_html=True
)

# Subtitle
st.markdown(
"<p style='text-align:center; font-size:18px; color:#555;'>Discover movies similar to your favourites!</p>",
unsafe_allow_html=True
)

st.write("")

# Movie dropdown
movie_list = movies_data['title'].values
selected_movie = st.selectbox("🎥 Choose a movie:", movie_list)

# Recommendation function
def recommend(movie):

    list_of_all_titles = movies_data['title'].tolist()

    find_close_match = difflib.get_close_matches(movie, list_of_all_titles)

    close_match = find_close_match[0]

    index_of_movie = movies_data[movies_data.title == close_match].index[0]

    similarity_score = list(enumerate(similarity[index_of_movie]))

    sorted_movies = sorted(similarity_score, key=lambda x:x[1], reverse=True)

    recommended_movies = []

    i = 1
    for movie in sorted_movies:

        index = movie[0]

        title = movies_data[movies_data.index==index]['title'].values[0]

        if i < 11:
            recommended_movies.append(title)
            i += 1

    return recommended_movies


# Recommend button
if st.button("⭐ Recommend Movies"):

    recommendations = recommend(selected_movie)

    st.subheader("🎯 Recommended Movies For You")

    num = 1
    for movie in recommendations:

        st.markdown(
            f'<div class="recommend-box">{num}. {movie}</div>',
            unsafe_allow_html=True
        )

        num += 1