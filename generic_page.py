import streamlit as st
from utils import generate_summary, read_pdf, read_docx, read_ppt, read_txt

def generic_page(file_type):
    titles = {
        "pdf": "📕 PDF Summarizer",
        "word": "📘 Word Summarizer",
        "txt": "📄 TXT Summarizer",
        "ppt": "📊 PPT Summarizer"
    }
    extensions = {
        "pdf": ["pdf"],
        "word": ["docx"],
        "txt": ["txt"],
        "ppt": ["pptx"]
    }
    readers = {
        "pdf": read_pdf,
        "word": read_docx,
        "txt": read_txt,
        "ppt": read_ppt
    }

    st.title(titles[file_type])

    col1, col2 = st.columns([2, 1])

    with col1:
        uploaded_file = st.file_uploader(f"Upload {file_type.upper()} File", type=extensions[file_type])

    with col2:
        length_option = st.selectbox("Summary Length", ["Short", "Medium", "Long"], index=1)

    if uploaded_file:
        if st.button("✨ Generate Summary"):
            with st.spinner("Analyzing and summarizing content..."):
                try:
                    text = readers[file_type](uploaded_file)
                    if not text.strip():
                        st.error("The uploaded file is empty or could not be read.")
                    else:
                        summary = generate_summary(text, length_option)
                        st.session_state.current_summary = summary
                except Exception as e:
                    st.error(f"Error processing file: {e}")

    if "current_summary" in st.session_state and st.session_state.current_summary:
        st.subheader("Results")
        st.text_area("Summary Output", st.session_state.current_summary, height=400)

        c1, c2, c3 = st.columns([1, 1, 1])
        with c1:
            st.download_button(
                label="📥 Download as TXT",
                data=st.session_state.current_summary,
                file_name="summary.txt",
                mime="text/plain"
            )

    st.markdown("---")
    if st.button("⬅ Back to Home"):
        st.session_state.current_summary = None
        st.session_state.page = "home"
        st.rerun()
