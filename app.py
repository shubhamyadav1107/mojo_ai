import streamlit as st
import docx
import fitz  # PyMuPDF
import cohere
import time
import re

# Initialize Cohere client
cohere_client = cohere.Client("DQMTog62FGREW26IWWcFe4MDJrRCao6HVEn1ujHM")

# Function to extract text from documents
def extract_text(file):
    if file.name.endswith('.docx'):
        doc = docx.Document(file)
        return '\n'.join([para.text for para in doc.paragraphs])
    elif file.name.endswith('.pdf'):
        pdf_document = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        for page in pdf_document:
            text += page.get_text()
        return text
    else:
        return "Unsupported file type."

# Function to clean and chunk text
def clean_and_chunk_text(text, chunk_size=200):
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks

# Updated function to get embeddings with batching and delay
def get_embeddings(text_chunks, batch_size=10, delay=1):
    embeddings = []
    for i in range(0, len(text_chunks), batch_size):
        batch = text_chunks[i:i + batch_size]
        try:
            response = cohere_client.embed(texts=batch)
            embeddings.extend(response.embeddings)
            time.sleep(delay)
        except cohere.errors.CohereError:  # Corrected error handling
            st.warning("Rate limit exceeded, retrying after a short pause...")
            time.sleep(5)  # Wait and try again to avoid exceeding rate limit
    return embeddings

# Function to generate answer using Cohere API
def generate_answer(question, context):
    response = cohere_client.generate(
        model="command-xlarge-nightly",
        prompt=f"Answer the question based on the following information:\n{context}\nQuestion: {question}\nAnswer:",
        max_tokens=100,
        temperature=0.3
    )
    return response.generations[0].text.strip()

# Streamlit app setup
st.title("👽Hey! I'm Mojo by Shubham, just ask me🦸🏻‍♂️")

uploaded_file = st.file_uploader("Upload a Document", type=["pdf", "docx"])

if uploaded_file is not None:
    st.write("Document uploaded successfully!")
    file_text = extract_text(uploaded_file)

    if file_text.strip():
        st.write("Extracted Text:")
        st.write(file_text[:500])  # Display a snippet for verification

        # Clean and chunk the extracted text
        text_chunks = clean_and_chunk_text(file_text)
        embeddings = get_embeddings(text_chunks)

        st.write("Ask a question based on the uploaded document:")
        user_question = st.text_input("Enter your question")

        if user_question:
            # Retrieve context based on question and generate an answer
            context = ' '.join(text_chunks[:5])  # Example context, adjust as needed
            answer = generate_answer(user_question, context)
            st.write("Answer:")
            st.write(answer)
    else:
        st.write("No text could be extracted from the document.")
