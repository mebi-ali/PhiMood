import streamlit as st

from backend.main import Start

st.set_page_config(page_title="PhiMood", layout="centered")


def start():
    s = Start()
    st.markdown("<h1 style='text-align: center;'>PhiMood</h1>", unsafe_allow_html=True)
    st.subheader("", divider="gray")

    if prompt := st.chat_input("Give a phrase"):
        with st.chat_message("user"):
            st.write(prompt)

        text = s.model.process(prompt)
        text = s.process_text(text)
        with st.chat_message("ai"):
            st.write_stream(s.stream_data(prompt=text))


start()
