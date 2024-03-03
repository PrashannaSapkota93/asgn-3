import streamlit as st
from langchain.llms import OpenAI

st.title(' Quickstart App')

# Placeholder for your actual OpenAI API key (REMOVE before sharing)
openai_api_key = "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"  # Replace with your actual key

def generate_response(input_text):
  """Generates response using OpenAI with the provided API key."""
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')

  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  elif submitted:
    generate_response(text)
