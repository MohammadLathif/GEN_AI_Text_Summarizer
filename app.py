import streamlit as st
from generic_page import generic_page

# ====================================
# PAGE CONFIG
# ====================================

st.set_page_config(
    page_title="Generative AI Document Summarizer",
    layout="wide"
)

# ====================================
# SESSION STATE INIT
# ====================================

if "page" not in st.session_state:
    st.session_state.page = "home"

# ====================================
# STYLING
# ====================================

st.markdown("""
<style>
/* Background Gradient */
.stApp {
    background: linear-gradient(135deg, #1e293b, #0f172a);
    color: white;
}

/* Custom Card Effect */
.card {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 15px;
    padding: 2rem;
    border: 1px solid rgba(255, 255, 255, 0.1);
    text-align: center;
    transition: transform 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
    border-color: #4CAF50;
    background: rgba(255, 255, 255, 0.08);
}

/* Title Styling */
h1 {
    font-weight: 800 !important;
    text-align: center;
}

.subtitle {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 3rem;
}
</style>
""", unsafe_allow_html=True)

# ====================================
# HOME PAGE
# ====================================

if st.session_state.page == "home":

    st.markdown("<h1> Generative AI Text Summarizer</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Summarize Word,PDF,TXT & PPT files using Generative AI.</p>", unsafe_allow_html=True)

    # Use a cleaner grid for the buttons
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("<div class='card'><h3>📄</h3><h4>Word</h4></div>", unsafe_allow_html=True)
        if st.button("Upload Word", key="btn_word", use_container_width=True):
            st.session_state.page = "word"
            st.rerun()

    with col2:
        st.markdown("<div class='card'><h3>📕</h3><h4>PDF</h4></div>", unsafe_allow_html=True)
        if st.button("Upload PDF", key="btn_pdf", use_container_width=True):
            st.session_state.page = "pdf"
            st.rerun()

    with col3:
        st.markdown("<div class='card'><h3>📝</h3><h4>Text</h4></div>", unsafe_allow_html=True)
        if st.button("Upload TXT", key="btn_txt", use_container_width=True):
            st.session_state.page = "txt"
            st.rerun()

    with col4:
        st.markdown("<div class='card'><h3>📊</h3><h4>PPT</h4></div>", unsafe_allow_html=True)
        if st.button("Upload PPT", key="btn_ppt", use_container_width=True):
            st.session_state.page = "ppt"
            st.rerun()

# ====================================
# PAGE ROUTING
# ====================================

elif st.session_state.page in ["pdf", "word", "txt", "ppt"]:
    generic_page(st.session_state.page)
