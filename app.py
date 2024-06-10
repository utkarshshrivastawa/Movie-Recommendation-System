import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from difflib import get_close_matches  # Corrected import

# Error Handling for Data and Model Files
try:
    movie_data = pd.read_csv('movies.csv')
except FileNotFoundError:
    st.error("Error: 'movies.csv' file not found. Please ensure it's in the same directory as this script.")
    exit()

try:
    movie_model = pickle.load(open("movie_model.sav", 'rb'))
except FileNotFoundError:
    st.error("Error: 'movie_model.sav' file not found. Please ensure it's in the same directory as this script.")
    exit()

# Sidebar Menu
with st.sidebar:
    selected = option_menu("Movie Recommendation Assistant",
                            ['Movie Recommendation System'],
                            icons=['film'],
                            default_index=0)

# Movie Recommendation Page
if selected == 'Movie Recommendation System':

    # Page Title
    st.title('Movie Recommendation System Using ML')

    # User Input for Movie Name
    movie_name = st.text_input('Enter your favourite movie name: ')

    # Find Close Matches with Cutoff for Accuracy
    list_of_titles = movie_data['title'].tolist()
    close_matches = get_close_matches(movie_name, list_of_titles, n=1, cutoff=0.8)  # Consider adjusting cutoff

    if close_matches:
        close_match = close_matches[0]
        index_movie = movie_data[movie_data.title == close_match]['index'].values[0]

        try:
            # Handle Potential Errors During Model Prediction
            similarity_scores = movie_model.predict(movie_data.iloc[index_movie].values.reshape(1, -1))
            similarity_list = list(enumerate(similarity_scores))

        except Exception as e:
            st.error(f"Error: An error occurred during movie recommendation. The error message is: {str(e)}")
            st.write("Please check your 'movie_model.sav' file and ensure it's compatible with the data.")

        else:
            sorted_movies = sorted(similarity_list, key=lambda x: x[1], reverse=True)

            # Display Recommended Movies
            st.write('Movies suggested for you:\n')
            i = 1
            for movie in sorted_movies:
                index = movie[0]
                title_from_index = movie_data[movie_data.index == index]['title'].values[0]
                if i <= 10:
                    st.write(f"{i}. {title_from_index}")
                    i += 1

    else:
        st.write(f"No close matches found for '{movie_name}'. Please try a different movie name.")
