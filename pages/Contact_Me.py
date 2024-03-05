import streamlit as st
import send_email

st.header("Contact Me!!")
with st.form(key="my_form"):
    sender = st.text_input("Your email adress")
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {sender}

From: {sender}
{raw_message}
    """
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_email.send_email(message)
        st.info("Your email was sent successfully!")