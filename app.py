import streamlit as st
import requests

st.title('Movie Minia')

import pickle
import pandas as pd
similarity=pickle.load(open('similarity.pkl','rb'))


def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=0bc5c14536f2afc88fd2139052feff45&&language=en-US'.format(movie_id))
    data=response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']


def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distance=similarity[movie_index]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recom_list=[]
    recom_movies_poster=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        #fetch poster from api
        recom_list.append(movies.iloc[i[0]].title)
        recom_movies_poster.append(fetch_poster(movie_id))
    return recom_list,recom_movies_poster

movies_dict=pickle.load(open('movoie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)


selected_movie = st.selectbox(
"Select the movies I will recommend 5 similar",
movies['title'].values)


if st.button("Recommend"):
    names,poster=recommend(selected_movie)
    col1,col2,col3,col4,col5=st.columns(5)

    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])