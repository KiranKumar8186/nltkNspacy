import streamlit as st
import nltk
import spacy
from nltk.tokenize import sent_tokenize

st.set_page_config(
    page_title="Elite Notes",
    page_icon=":clipboard:",
    layout="wide",
)

st.markdown("<h1 style='text-align: center; color: red; font-size: 55px;'>Elite Notes</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='padding: 10px; text-align: center; color: lightblack; font-size: 15px; margin : 15px auto;'>At EliteNotes, we believe everyone is a note-taker because every conversation matters</h1>", unsafe_allow_html=True)
st.markdown("---")


text = st.text_area("Enter text to summarize:")
if text:
    library = st.selectbox("Which library would you like to use for summarization?", ["nltk", "spacy"])
    summary_ratio = st.slider("Select the summary ratio (in %)", min_value=10, max_value=50, step=5, value=30)

    if library == "nltk":
        nltk.download('punkt')
        sentences = sent_tokenize(text)
        total_sentences = len(sentences)
        summary_length = int(total_sentences * summary_ratio / 100)
        summary = sentences[:summary_length]
        st.write("Summary:")
        for sent in summary:
            st.write("- " + sent)

    elif library == "spacy":
        
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        summary_length = int(len(doc.sents) * summary_ratio / 100)
        summary = [sent.text for sent in doc.sents[:summary_length]]
        st.write("Summary:")
        for sent in summary:
            st.write("- " + sent)

