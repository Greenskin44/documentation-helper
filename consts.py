"""
LangChain Documentation Helper - Configuration Constants

This module contains centralized configuration constants used throughout
the application for consistency and easy maintenance.

Author: Based on original work by Eden Marco (@emarco177)
Educational Context: Developed as part of Eden Marco's Udemy LangChain course
"""

# Vector Database Configuration
INDEX_NAME = "langchain-doc-index"

# Model Configuration
EMBEDDING_MODEL = "text-embedding-3-small"
CHAT_MODEL = "gpt-3.5-turbo"

# Document Processing Configuration
CHUNK_SIZE = 600
CHUNK_OVERLAP = 50
BATCH_SIZE = 100

# Application Configuration
APP_TITLE = "LangChain Documentation Helper"
APP_DESCRIPTION = """
Ask questions about LangChain functionality, implementation patterns,
and best practices. Get accurate answers with source documentation links.
"""

# File Paths
DOCS_PATH = "langchain-docs/api.python.langchain.com/en/latest"

# UI Configuration
SIDEBAR_EXAMPLE_QUESTIONS = [
    "How do I implement memory in conversations?",
    "What are the different types of retrievers?",
    "How do I use custom embedding models?",
    "What is the best way to handle long documents?",
    "How do I create a RAG application with LangChain?",
]
