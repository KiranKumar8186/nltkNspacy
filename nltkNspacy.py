# import nltk
# import spacy
# from nltk.corpus import stopwords
# from nltk.cluster.util import cosine_distance
# import numpy as np
# import streamlit as st
# import networkx as nx

# nlp = spacy.load("en_core_web_sm")

# st.set_page_config(page_title="Summarizer", page_icon=":memo:", layout="wide")

# st.markdown("<h1 style='text-align: center; color: red; font-size: 55px;'>Elite Notes</h1>", unsafe_allow_html=True)
# st.markdown("<h2 style='padding: 10px; text-align: center; color: lightblack; font-size: 15px; margin : 15px auto;'>At EliteNotes, we believe everyone is a note-taker because every conversation matters</h1>", unsafe_allow_html=True)
# st.markdown("---")

# text = st.text_area("Enter your text:", "")

# summary_method = st.selectbox("Select summarization method:", ["nltk", "spacy"])

# if text:
#     if summary_method == "nltk":
#         sentences = nltk.sent_tokenize(text)
#         word_embeddings = {}
#         for word in nltk.word_tokenize(text):
#             if word not in stopwords.words("english"):
#                 word_embeddings[word] = nlp(word).vector

#         similarity_matrix = np.zeros([len(sentences), len(sentences)])
#         for idx1 in range(len(sentences)):
#             for idx2 in range(len(sentences)):
#                 if idx1 != idx2:
#                     similarity_matrix[idx1][idx2] = cosine_distance(word_embeddings[nltk.word_tokenize(sentences[idx1])[0]], word_embeddings[nltk.word_tokenize(sentences[idx2])[0]])

#         nx_graph = nx.from_numpy_array(similarity_matrix)
#         scores = nx.pagerank(nx_graph)
#         ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
            
#         if ranked_sentences:
#             summary = ranked_sentences[0][1]
#             for sent_score in ranked_sentences[1:5]:
#                 summary += " " + sent_score[1]
            
#             # summarized_text = " ".join([ranked_sentences[i][1] for i in range(5)])
#             # st.write("Summary:", summarized_text)
            
#             st.write("Summary:")
#             for i, sentence in enumerate(ranked_sentences[:5]):
#                 st.write("- " + sentence[1])
        
#     elif summary_method == "spacy":
#         doc = nlp(text)
#         summarized_text = " ".join([sent.text for sent in doc.sents if sent.has_vector and sent.vector_norm])
#         # st.write("Summary:", summarized_text)
#         st.write("Summary:")
#         for sent in doc.sents:
#             if sent.has_vector and sent.vector_norm:
#                 st.write("- " + sent.text)






import streamlit as st
import nltk
import spacy
from nltk.tokenize import sent_tokenize


st.markdown("<h1 style='text-align: center; color: red; font-size: 55px;'>Elite Notes</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='padding: 10px; text-align: center; color: lightblack; font-size: 15px; margin : 15px auto;'>At EliteNotes, we believe everyone is a note-taker because every conversation matters</h1>", unsafe_allow_html=True)
st.markdown("---")


text = st.text_area("Enter text to summarize:")
if text:
    library = st.selectbox("Which library would you like to use for summarization?", ["nltk", "spacy"])
    summary_ratio = st.slider("Select the summary ratio (in %)", min_value=10, max_value=50, step=5, value=30)

    if library == "nltk":
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

if st.button("Submit"):
    st.write("Text summarized!")
