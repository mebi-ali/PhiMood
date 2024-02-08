import time
import re
import streamlit as st
from backend.model import Model


@st.cache_resource
class Start:

    def __init__(self, text=None, prompt=None) -> None:
        self.text = text
        self.prompt = prompt
        self.model = Model()

    def process_text(self, text):
        joke_string = "".join(text)
        start_index = joke_string.find("Output") + len("Output :")
        end_index = joke_string.find('"""')
        return joke_string[start_index:end_index].strip()

    def stream_data(self, prompt=""):
        for word in prompt.split():
            yield f"{word} "
            time.sleep(0.02)
