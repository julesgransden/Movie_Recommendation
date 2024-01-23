from Movie_reco import *
import streamlit as st

st.title('Movie Recommendation')

user_input = st.text_input('Entere Movie Name', 'Barbie')

st.subheader('Recomended Movies')
try:
    x = recommend(user_input)
    st.write(x)
except:
    st.write('We have no recommendations for that movie')
