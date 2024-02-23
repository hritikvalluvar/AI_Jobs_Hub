import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title='AI Jobs Hub', page_icon = '🚀', layout = 'wide', initial_sidebar_state = 'collapsed')
# favicon being an object of the same kind as the one you should provide st.image() with (ie. a PIL array for example) or a string (url or local file path)

st.title('🚀 Introducing the AI Jobs Hub: A New Journey Begins! 🌟')
st.toast('Scroll down to continue', icon='⬇️')
st.write("I'm thrilled to unveil my first-ever project in the AI job resources domain – a spreadsheet focusing on AI career opportunities. This endeavor marks the beginning of what I hope will be a continuously expanding project.")
st.write('**Stay Updated and Connect:** Follow me on LinkedIn to keep up with the latest additions and updates: https://www.linkedin.com/in/ethicalrecruiter/')
st.write('**About This Project:** Fueled by my enthusiasm for AI and a commitment to helping professionals and job seekers, I\'ve compiled a detailed list of AI job openings. This hub was inspired by Amir Satvat who created an amazing Video Games Career Resource and helped thousands of people within games industry during dificult times. You can find his project on LinkedIn: https://www.linkedin.com/in/amirsatvat/ \n(this resource is designed to simplify and enhance your job search experience)"')
st.write('**What\'s Inside:** A growing collection of job listings from various AI studios, companies and startups. Jobs are systematically categorized for ease of navigation, spanning a range of roles and sectors in AI. I\'m dedicated to weekly updates, ensuring the most current opportunities are always at your fingertips.')
st.write('**A Call for Collaboration:** As I voluntarily step into this new venture, I invite your suggestions and contributions. If you\'re aware of any AI studios, teams, or companies that should be featured, please let me know.  Together, we can make this resource even more comprehensive and useful for everyone. Turn on screen reader support')
st.write('**The Future Vision:** If the companies list with careers pages will be useful, I will start sorting it out by jobs for all of you! ❤️')
st.write('**Join Me on This Adventure:** This database is more than just a tool, it\'s a stepping stone into the vast world of AI careers. I created this database because I grew frustrated with the limitations of traditional job boards that often prioritize paid job listings and the inefficiency of search platforms with inadequate filtering systems. My goal is to challenge biases and unethical recruitment practices, paving the way for a more inclusive and accurate approach to AI job searches, where talent is genuinely connected with opportunities, transcending the shortcomings of existing platforms. \n I believe that by working together, we can discover the most promising paths in the AI landscape.')
st.write('**Your Voice Matters:** Your feedback and suggestions are vital. Please share your insights or additional information that could enrich this resource.')
st.write('**Together, Let\'s Explore the World of AI:** Wishing you the best in your job search! I eagerly look forward to evolving and enhancing this resource with your support and insights.')
st.markdown('<div style="text-align: center"> Wishing everyone all the best! <br> xx Anna Moss xx</div>', unsafe_allow_html=True)

st.text("")
st.text("")
st.text("")
st.text("")

col1, col2, col3 = st.columns(3)
col2.page_link("pages/Data.py", label="Continue", icon="🚀")
