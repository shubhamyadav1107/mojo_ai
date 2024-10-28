
### Quick Description

**Mojo** is an intelligent, retrieval-augmented question-answering app. Upload documents in various formats, and Mojo extracts and indexes the content, providing accurate, context-driven answers to user queries. With a blend of advanced embeddings and generative language models, Mojo offers real-time, document-based insights—ideal for research, analysis, and instant information retrieval.


### README for GitHub

# Mojo: Intelligent Document-Based Q&A Bot

## Overview
Mojo is an AI-driven question-answering application designed to simplify information retrieval from uploaded documents. By integrating retrieval-augmented generation (RAG) with Cohere’s advanced language models and FAISS embeddings, Mojo offers fast and accurate responses to your queries based on the document's content, making it perfect for researchers, analysts, and enthusiasts who need instant insights.

## Features
- **Multi-Format Document Uploads**: Mojo supports PDFs, DOCX, and other popular formats.
- **Automatic Text Extraction & Cleaning**: Converts document content into structured, clean text for smooth processing.
- **Efficient Indexing and Retrieval**: Leverages FAISS embeddings for high-speed similarity matching and information retrieval.
- **Real-Time Responses**: Uses Cohere’s language models to generate answers on-the-fly, providing fast and reliable information.

## How It Works
1. **Upload a Document**: Load a document through Mojo’s intuitive interface.
2. **Ask Questions**: Enter questions based on the document content.
3. **Get Accurate Answers**: Mojo retrieves relevant information and generates responses using the context extracted from your document.

## Getting Started
Follow these steps to set up and run Mojo:

1. Clone the Repository
   ```bash
   
2. Install Dependencies
   - Mojo requires Streamlit, PyMuPDF, docx, FAISS, and Cohere SDK.
   - Run the following command to install:
     ```bash
     pip install -r requirements.txt
     ```

3. **Set Up API Keys**:
   - Cohere: Obtain an API key from Cohere.ai, then store it in your environment or code securely.
   - ngrok: Generate an ngrok auth token to expose your app online.

4. Run Mojo:
   Launch Mojo on Streamlit:
   ```bash
   streamlit run app.py
   ```

5. Access Your App:
   - Mojo will display a URL to access the app in a browser. For remote access, use the generated ngrok link.

## Potential Use Cases
- Research: Quickly search for answers within lengthy research papers.
- Business Analysis: Retrieve key information from reports or project files.
- Personal Productivity: Streamline information extraction from personal documents.

## Troubleshooting & FAQ
- Rate Limits: If you encounter an API limit (e.g., TooManyRequestsError), adjust the document size or increase API limits through Cohere.
- ngrok Reconnection: ngrok links expire, so re-run the ngrok command or consider upgrading for persistent links.

## Contributing
Contributions to Mojo are welcome! Whether fixing bugs or adding new features, please feel free to submit a pull request.

## License
This project is licensed under the MIT License. 

