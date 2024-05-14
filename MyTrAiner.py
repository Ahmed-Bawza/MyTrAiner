import streamlit as st

st.title("My TrAiner | مدربي")
exercise = st.selectbox("اختر تمرين من القائمه" , ("none","1-squat","2-knee extention","3-foot ankel extention"))

if (exercise == "none"):
    st.header("عذراً نرجو منك اختيار تمرين")

elif (exercise == "1-squat"):
    # video_file = open('IMG_6038.mp4', 'rb')
    # video_bytes = video_file.read()
    # st.video(video_bytes)
    st.supheader("جاهز؟",divider='red')
    url = 'https://wesam0001.github.io/MyTrainer/'
    st.page_link(url, label="ابدا تمرينك", icon="🏋🏼‍♂️")

elif (exercise == "2-knee extention"):
    st.header("قريباً :)")
   
elif (exercise == "3-foot ankel extention"):
   st.header("قريباً :)")


