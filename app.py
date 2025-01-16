import streamlit as st
import pickle
import pandas as pd
import numpy as np


st.title('Anime Recommended System')
anime_dict=pickle.load(open('anime_list.pkl','rb'))
anime_df_main=pd.DataFrame(anime_dict)
similarity=pickle.load(open('similarity.pkl','rb'))

def recommend(anime):
    if anime not in anime_df_main['English name'].values:
        print(f"Anime '{anime}' not found in the dataset.")
        return
    
    index=anime_df_main[anime_df_main['English name']==anime].index[0]
    distances=similarity[index]
    anime_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[0:6]
    list_of_anime=[]
    for i in anime_list:
        list_of_anime.append((anime_df_main.iloc[i[0]].Name))
    
    return list_of_anime


selected_anime_name = st.selectbox(
     'Enter the anime name',
      anime_df_main['Name'].values
)

if st.button('Recommend'):
    reccomendations=recommend(selected_anime_name)

    for i in reccomendations:
        st.write(selected_anime_name)

