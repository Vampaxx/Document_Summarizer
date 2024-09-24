# Document_Summarizer

# Document Summarizer Project


## Introduction

The Document Summarizer Project is a web application designed to efficiently summarize various document formats, including PDF, DOCX, and TXT. By leveraging advanced language models and the Flask framework, this tool simplifies the process of extracting essential information from lengthy documents, making it an invaluable resource for students, professionals, and anyone needing quick insights from their readings.

### The Challenge of Information Overload

In an era of information overload, extracting relevant information from lengthy documents can be time-consuming and tedious. This project addresses the need for a reliable and efficient solution to summarize content quickly, enabling users to focus on the key points without getting lost in unnecessary details.

### Enter the Document Summarizer: Your Efficient Reading Companion

The Document Summarizer acts as a smart assistant that allows users to upload documents and receive concise summaries, saving time and effort while enhancing productivity.

## Features

1. **Multi-format Document Support**
   - Accepts PDF, DOCX, and TXT files for summarization.
  
2. **User-friendly Interface**
   - Simple drag-and-drop file upload functionality.
   - Clean and intuitive HTML frontend for seamless interaction.

3. **Efficient Summarization**
   - Utilizes advanced language models for high-quality summaries.
   - Highlighting of important text within the summarized output.

4. **Download Functionality**
   - Allows users to download the summarized text for later reference.

5. **File Validation and Size Limits**
   - Ensures that only supported file types are processed.
   - Enforces file size limits to maintain performance.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Vampaxx/Document_Summarizer.git
   cd Document_Summarizer
2. **Open VScode:**
   ```bash
   code . 
3. **Set up a virtual environment:**
    ```bash
    conda activate [your environment name]
4. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
5. **Add your API key into .env:**

## Configuration

### 1. params.yaml

This file contains model information, like temperature,MODEL_NAME

- `temperature  : [model temperature]`
- `MODEL_NAME   : [Name of LLM model]`


## Groq API 

Overview

This project utilizes the Groq API for deep learning inference processing in AI applications. Groq's high-performance, low-latency compute architecture makes it ideal for various compute-intensive workloads.
### Advantages of Using Groq

  - High Performance: Designed for deep learning inference, delivering fast processing speeds essential for real-time AI applications.
  - Low Latency: Optimized for low-latency computations, making it suitable for applications where response time is critical.
  - General-purpose Architecture: A Turing-complete compute architecture that handles a diverse range of compute-intensive workloads beyond just deep learning, providing flexibility for various AI applications.
  - Scalability: Allows for easy scaling, enabling applications to handle increasing loads without significant overhead.
  - Ease of Integration: API allows for straightforward integration into existing systems, making it easier to leverage Groq’s capabilities.

Requirements

## Integration Steps

### 1. API Setup
- Create an API key for accessing Groq services and store it in a `.env` file for security.

### 2. Import Groq
Include the following import statement in your Python code:
  
      from langchain_groq import ChatGroq  

## Upload Document
 1. **Upload Files:**
   - Click on the **Browse** button.
   - Select the document you wish to upload. Supported file formats include PDF, DOCX, and TXT.
   - Ensure the document size does not exceed the specified limit (e.g., 5MB). If it does, you will receive a notification.

2.. **View Summaries:**
   - Once the document is uploaded, the application will process the file and generate a summary.
   - The summary will be displayed on the screen under the **Summary** section.

### Handling Unsupported File Types
If you attempt to upload a file type that is not supported, the application will display an error message indicating the file type is not supported. Please ensure you are uploading files in one of the supported formats: PDF, DOCX, or TXT.

### Handling Large Documents
If the document size exceeds the allowed limit, the application will notify you with a message indicating that the file is too large. To proceed, please upload a smaller document or reduce the file size by removing unnecessary content.

### Error Notifications
In case of any errors during the upload or processing, the application will provide clear notifications to guide you on the next steps. Ensure to follow the instructions provided in the notifications.

## Run Application

1. **Run the Flask application:**
  
    ```bash
    flask run
