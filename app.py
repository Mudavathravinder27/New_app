import streamlit as st

st.header("Hello :red[everyone],")
st.subheader("I'am Ravi")
st.subheader("Welcome to my :blue[app]")
st.snow()
option=st.button("click here to connect")
if option==True:
    st.balloons()

    linkedin="www.linkedin.com/in/mudavath-ravinder8179547088"
    var1=st.write(format(linkedin))
    