# 🧠 Generative AI Document Summarizer

A powerful Streamlit-based web application that summarizes PDF, Word, TXT, and PPT documents using a Generative AI model (DistilBART).

---

## 🚀 Features

- 📕 PDF Summarization
- 📘 Word (DOCX) Summarization
- 📄 TXT File Summarization
- 📊 PPT (PowerPoint) Summarization
- ⚡ GPU Support (if available)
- 🎯 Adjustable Summary Length (Short / Medium / Long)
- 📥 Download Summary as TXT

---

## 🛠️ Tech Stack

- Python
- Streamlit
- PyTorch
- HuggingFace Transformers
- PyPDF2
- python-docx
- python-pptx

---

## 📂 Project Structure
GenAI-Document-Summarizer/


├── app.py # Main entry file

├── generic_page.py # Upload & UI logic

├── utils.py # Model loading & summarization logic

├── requirements.txt # Dependencies

├── .gitignore

└── assets/

## 🧠 Model Used

This project uses:

**sshleifer/distilbart-cnn-12-6**

A distilled version of Facebook BART fine-tuned for summarization tasks.

---

## 📌 How It Works

1. Upload a supported document.
2. The text is extracted.
3. The model processes the content.
4. A structured summary is generated.
5. The summary can be downloaded.

---

## ⚠️ Note

- Very large documents are truncated to the model's maximum token limit.
- GPU acceleration is automatically enabled if available.

---
