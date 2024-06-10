import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import difflib

# Load the data
movie_data = pd.read_csv('movies.csv')

# Load the saved model
movie_model = pickle.load(open("movie_model.sav", 'rb'))

# Sidebar menu
with st.sidebar:
    selected = option_menu("Movie Recommendation Assistant",
                           ['Movie Recommendation System'],
                           icons=['film'],
                           default_index=0)

# Movie Recommendation Page
if selected == 'Movie Recommendation System':

    # Page title
    st.title('Movie Recommendation System Using ML')

    # User input for movie name
    movie_name = st.text_input('Enter your favourite movie name: ')

    if movie_name:
        list_of_titles = movie_data['title'].tolist()
        close_matches = difflib.get_close_matches(movie_name, list_of_titles)

        if close_matches:
            closest_match = close_matches[0]
            index_movie = movie_data[movie_data.title == closest_match]['index'].values[0]

            # Assuming similarity is a precomputed similarity matrix or use model to get similarity
            similarity = movie_model  # this should be your similarity matrix or model
            similarity_score = list(enumerate(similarity[index_movie]))
            sorted_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

            # Display recommended movies
            st.write('Movies suggested for you:\n')
            i = 1
            for movie in sorted_movies:
                index = movie[0]
                title_from_index = movie_data[movie_data.index == index]['title'].values[0]
                if i <= 10:
                    st.write(f"{i}. {title_from_index}")
                    i += 1
        else:
            st.write("No close matches found. Please try a different movie.")
