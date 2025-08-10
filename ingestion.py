"""
LangChain Documentation Helper - Data Ingestion Module

This module handles the ingestion of LangChain documentation into a vector database.
It processes documentation files, splits them into chunks, generates embeddings,
and stores them in Pinecone for efficient retrieval.

Author: Based on original work by Eden Marco (@emarco177)
Educational Context: Developed as part of Eden Marco's Udemy LangChain course
"""

import os
from typing import List
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import ReadTheDocsLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from consts import (
    INDEX_NAME, 
    EMBEDDING_MODEL, 
    CHUNK_SIZE, 
    CHUNK_OVERLAP, 
    BATCH_SIZE, 
    DOCS_PATH
)


def validate_environment() -> None:
    """
    Validate that required environment variables and files are present.
    
    Raises:
        ValueError: If required environment variables are missing
        FileNotFoundError: If documentation directory doesn't exist
    """
    required_vars = ["OPENAI_API_KEY", "PINECONE_API_KEY"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        raise ValueError(
            f"Missing required environment variables: {', '.join(missing_vars)}"
        )
    
    if not os.path.exists(DOCS_PATH):
        raise FileNotFoundError(
            f"Documentation directory not found: {DOCS_PATH}\n"
            "Please ensure you have downloaded the LangChain documentation."
        )


def load_and_process_documents():
    """
    Load and process documentation files into manageable chunks.
    
    Returns:
        List of processed document chunks with metadata
    """
    print("📚 Loading LangChain documentation...")
    
    # Initialize document loader
    loader = ReadTheDocsLoader(
        DOCS_PATH,
        encoding="utf-8",
        errors="ignore",
    )
    
    # Load raw documents
    raw_documents = loader.load()
    print(f"✅ Loaded {len(raw_documents)} raw documents")
    
    # Initialize text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE, 
        chunk_overlap=CHUNK_OVERLAP
    )
    
    # Split documents into chunks
    documents = text_splitter.split_documents(raw_documents)
    print(f"✅ Split into {len(documents)} chunks")
    
    # Fix URLs in metadata to point to actual web documentation
    for doc in documents:
        doc.metadata["source"] = doc.metadata["source"].replace(
            "langchain-docs", 
            "https:/"
        )
    
    return documents


def create_vector_store(documents: List) -> None:
    """
    Create vector embeddings and store documents in Pinecone.
    
    Args:
        documents: List of processed document chunks
    """
    print("🔗 Creating vector embeddings and storing in Pinecone...")
    
    # Initialize embeddings
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
    
    # Create initial vector store (empty)
    store = PineconeVectorStore.from_texts(
        [], 
        embeddings, 
        index_name=INDEX_NAME
    )
    
    print(f"📊 Processing {len(documents)} documents in batches of {BATCH_SIZE}")
    
    # Process documents in batches to avoid rate limits
    for i in range(0, len(documents), BATCH_SIZE):
        batch = documents[i:i + BATCH_SIZE]
        
        # Extract texts and metadata
        texts = [doc.page_content for doc in batch]
        metadatas = [doc.metadata for doc in batch]
        
        # Add to vector store
        store.add_texts(texts, metadatas=metadatas)
        
        batch_end = min(i + len(batch) - 1, len(documents) - 1)
        print(f"  ✅ Processed documents {i}–{batch_end}")
    
    print("🎉 Successfully completed ingestion to Pinecone!")


def ingest_docs() -> None:
    """
    Main ingestion function that orchestrates the entire process.
    
    This function:
    1. Validates the environment setup
    2. Loads and processes documentation files
    3. Creates embeddings and stores them in Pinecone
    """
    try:
        print("🚀 Starting LangChain Documentation Ingestion")
        print("=" * 50)
        
        # Validate environment
        validate_environment()
        print("✅ Environment validation passed")
        
        # Load and process documents
        documents = load_and_process_documents()
        
        # Create vector store
        create_vector_store(documents)
        
        print("=" * 50)
        print("✅ Ingestion completed successfully!")
        print(f"📈 Total chunks processed: {len(documents)}")
        print(f"🗂️  Index name: {INDEX_NAME}")
        print(f"🤖 Embedding model: {EMBEDDING_MODEL}")
        
    except Exception as e:
        print(f"❌ Error during ingestion: {e}")
        print("Please check your configuration and try again.")
        raise


if __name__ == "__main__":
    ingest_docs()
