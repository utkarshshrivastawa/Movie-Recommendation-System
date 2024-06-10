# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 13:52:56 2024

@author: utkar
"""

import pickle 
import streamlit as st
from streamlit_option_menu import option_menu


# loding the saved model 

movie_model = pickle.load(open("movie_model.sav",'rb'))

with st.sidebar:
    
    selected = option_menu("Movie Recommendation Assistant",
                           ['Movie Recommendation System'],
                           
                           icons =['film'],
                           defailt_index = 0)
    
# Diabetes Prediction Page 
if (selected == 'Movie Recommendation Assistant'):
    
    # page title 
    st.title('Movie Recommendation System Using ML')
    
    movie_name = st.text_input('Enter your favourite movie nmae :  ')
    
    list_of_title = movie_data['title'].tolist()
    close_match = difflib.get_close_matches(movie_name , list_of_title)
    close_matches = close_match[0]
    index_movie =movie_data[ movie_data.title == close_matches]['index'].values[0]
    similarity_score = list(enumerate(similarity[index_movie]))
    sorted_movie = sorted(similarity_score, key= lambda x:x[1], reverse =True)
    print('Movies suggest for you : \n')
    i = 1 
    for movie in sorted_movie :
        index = movie[0]
        title_from_index = movie_data[movie_data.index==index]['title'].values[0]
        if (i<11):
            print(i , '.', title_from_index)
            i+=1