"""
LangChain Documentation Helper - Core Backend Module

This module contains the core RAG (Retrieval-Augmented Generation) processing logic
for the LangChain Documentation Helper. It handles document retrieval, question
answering, and conversation history management.

Author: Based on original work by Eden Marco (@emarco177)
Educational Context: Developed as part of Eden Marco's Udemy LangChain course
"""

from typing import Dict, List, Any, Optional
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from langchain import hub
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from consts import INDEX_NAME, EMBEDDING_MODEL, CHAT_MODEL


def validate_environment() -> None:
    """
    Validate that required environment variables are set.
    
    Raises:
        ValueError: If required environment variables are missing
    """
    required_vars = ["OPENAI_API_KEY", "PINECONE_API_KEY"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        raise ValueError(
            f"Missing required environment variables: {', '.join(missing_vars)}"
        )


def create_retrieval_chain_components():
    """
    Create and configure the retrieval chain components.
    
    Returns:
        Tuple of (retrieval_qa_chain, embeddings, chat_model, docsearch)
    """
    # Initialize embeddings and chat model
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
    chat = ChatOpenAI(
        model=CHAT_MODEL,
        verbose=True, 
        temperature=0
    )
    
    # Initialize vector store
    docsearch = PineconeVectorStore(
        index_name=INDEX_NAME, 
        embedding=embeddings
    )
    
    # Create document processing chain
    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    stuff_document_chain = create_stuff_documents_chain(
        chat, 
        retrieval_qa_chat_prompt
    )
    
    # Create history-aware retriever
    rephrase_prompt = hub.pull("langchain-ai/chat-langchain-rephrase")
    history_aware_retriever = create_history_aware_retriever(
        llm=chat,
        retriever=docsearch.as_retriever(),
        prompt=rephrase_prompt,
    )
    
    # Create full retrieval chain
    qa_chain = create_retrieval_chain(
        retriever=history_aware_retriever,
        combine_docs_chain=stuff_document_chain,
    )
    
    return qa_chain, embeddings, chat, docsearch


def run_llm(query: str, chat_history: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    """
    Process a user query using the RAG system and return structured results.
    
    Args:
        query: The user's question or prompt
        chat_history: Previous conversation history for context
        
    Returns:
        Dictionary containing:
            - query: The original user query
            - result: The generated answer
            - source_document: List of relevant source documents
            
    Raises:
        ValueError: If environment variables are not properly configured
        Exception: If the retrieval chain fails to process the query
    """
    # Validate environment setup
    validate_environment()
    
    # Handle default chat history
    if chat_history is None:
        chat_history = []
    
    try:
        # Create retrieval chain components
        qa_chain, _, _, _ = create_retrieval_chain_components()
        
        # Process the query
        result = qa_chain.invoke({
            "input": query, 
            "chat_history": chat_history
        })
        
        # Structure the response
        structured_result = {
            "query": result["input"],
            "result": result["answer"],
            "source_document": result["context"]
        }
        
        return structured_result
        
    except Exception as e:
        raise RuntimeError(f"Failed to process query: {str(e)}")


def get_vector_store_info() -> Dict[str, Any]:
    """
    Get information about the current vector store configuration.
    
    Returns:
        Dictionary with vector store information
    """
    try:
        embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
        PineconeVectorStore(
            index_name=INDEX_NAME, 
            embedding=embeddings
        )
        
        return {
            "index_name": INDEX_NAME,
            "embedding_model": EMBEDDING_MODEL,
            "status": "connected"
        }
    except Exception as e:
        return {
            "index_name": INDEX_NAME,
            "embedding_model": EMBEDDING_MODEL,
            "status": "error",
            "error": str(e)
        }


if __name__ == "__main__":
    # Example usage and testing
    try:
        test_query = "How do users create question-answer RAG applications in LangChain?"
        response = run_llm(query=test_query)
        
        print("=" * 50)
        print("LANGCHAIN DOCUMENTATION HELPER - TEST")
        print("=" * 50)
        print(f"Query: {response['query']}")
        print("-" * 50)
        print(f"Answer: {response['result']}")
        print("-" * 50)
        print(f"Sources found: {len(response['source_document'])}")
        print("=" * 50)
        
    except Exception as e:
        print(f"Error during testing: {e}")
        print("Please ensure your environment variables are properly configured.")