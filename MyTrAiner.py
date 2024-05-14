import streamlit as st

st.title("My TrAiner")
exercise = st.selectbox("Choose exercise" , ("none","squat","knee extention","foot ankel extention"))

if (exercise == "none"):
    st.header("Please Choose an exercise")

elif (exercise == "squat"):
    # video_file = open('IMG_6038.mp4', 'rb')
    # video_bytes = video_file.read()
    # st.video(video_bytes)
    url = 'https://wesam0001.github.io/MyTrainer/'
    st.page_link(url, label="ابدا تمرينك", icon="🏋🏼‍♂️")

elif (exercise == "knee extention"):
    st.header("Coming SOON :)")
   
elif (exercise == "foot ankel extention"):
   st.header("Coming SOON :)")


