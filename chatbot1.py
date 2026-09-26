import streamlit as st
st.title("AI CHATBOT")
you=st.text_input("Enter your prompt:",placeholder="ask me anything")
if st.button("click"):
    if you:
        st.write(you)
        st.success("success")
    else:
        st.error("error")
        
        