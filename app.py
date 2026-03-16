# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 20:18:41 2026

@author: Acer
"""
import streamlit as st
import pickle
import difflib
import gdown
import os

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)

# -------------------------
# CSS Styling
# -------------------------
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

# -------------------------
# Load Movies Data
# -------------------------
movies_file = "movies.pkl"
movies_data = pickle.load(open(movies_file, "rb"))

# -------------------------
# Download Similarity File from Google Drive
# -------------------------
SIMILARITY_FILE_ID = "1o7CswtvLH5uGwnZYasdcgVl7rtqDuNYE"
similarity_file = "similarity.pkl"

if not os.path.exists(similarity_file):
    gdown.download(f"https://drive.google.com/uc?id={SIMILARITY_FILE_ID}", similarity_file, quiet=False)

with open(similarity_file, "rb") as f:
    similarity = pickle.load(f)

# -------------------------
# Sidebar Instructions
# -------------------------
st.sidebar.title("Instructions")
st.sidebar.write("1️⃣ Select a movie from the dropdown")
st.sidebar.write("2️⃣ Click 'Recommend Movies'")
st.sidebar.write("3️⃣ Get a list of similar movies")

# -------------------------
# App Title
# -------------------------
st.markdown(
    "<h1 style='text-align:center; color:#ff4b4b; font-size:55px;'>🎬 Movie Recommendation System</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center; font-size:18px; color:#555;'>Discover movies similar to your favourites!</p>",
    unsafe_allow_html=True
)

# -------------------------
# Movie Dropdown
# -------------------------
movie_list = movies_data['title'].values
selected_movie = st.selectbox("🎥 Choose a movie:", movie_list)

# -------------------------
# Recommendation Function
# -------------------------
def recommend(movie):
    all_titles = movies_data['title'].tolist()
    close_match = difflib.get_close_matches(movie, all_titles)[0]
    index = movies_data[movies_data.title == close_match].index[0]

    similarity_scores = list(enumerate(similarity[index]))
    sorted_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    recommended = []
    for i, (idx, score) in enumerate(sorted_movies):
        if i == 0:  # skip the selected movie itself
            continue
        recommended.append(movies_data.iloc[idx]['title'])
        if len(recommended) == 10:  # top 10 recommendations
            break
    return recommended

# -------------------------
# Recommend Button
# -------------------------
if st.button("⭐ Recommend Movies"):
    recommendations = recommend(selected_movie)
    st.subheader("🎯 Recommended Movies For You")

    for i, movie in enumerate(recommendations, start=1):
        st.markdown(f'<div class="recommend-box">{i}. {movie}</div>', unsafe_allow_html=True)
    
