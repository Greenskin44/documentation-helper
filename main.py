"""
LangChain Documentation Helper - Main Application

This module provides a Streamlit web interface for interacting with the LangChain
Documentation Helper RAG system. It enables users to ask questions about LangChain
functionality and receive contextual answers with source citations.

Author: Based on original work by Eden Marco (@emarco177)
Educational Context: Developed as part of Eden Marco's Udemy LangChain course
"""

from typing import Set
import streamlit as st
from backend.core import run_llm
from consts import APP_TITLE, APP_DESCRIPTION, SIDEBAR_EXAMPLE_QUESTIONS


def initialize_session_state() -> None:
    """Initialize Streamlit session state variables for chat history management."""
    session_vars = [
        "chat_answers_history",
        "user_prompt_history", 
        "chat_history"
    ]
    
    for var in session_vars:
        if var not in st.session_state:
            st.session_state[var] = []


def create_sources_string(source_urls: Set[str]) -> str:
    """
    Format source URLs into a numbered list string.
    
    Args:
        source_urls: Set of source URLs to format
        
    Returns:
        Formatted string with numbered source list or empty string if no sources
    """
    if not source_urls:
        return ""
        
    sources_list = sorted(source_urls)
    sources_string = "\n**Sources:**\n"
    
    for i, source in enumerate(sources_list, 1):
        sources_string += f"{i}. {source}\n"
        
    return sources_string


def process_user_query(prompt: str) -> None:
    """
    Process user query through the LangChain RAG system and update session state.
    
    Args:
        prompt: User's input query
    """
    with st.spinner("🔍 Searching documentation and generating response..."):
        try:
            generated_response = run_llm(
                query=prompt,
                chat_history=st.session_state["chat_history"]
            )
            
            # Extract and format sources
            sources = {
                doc.metadata["source"] 
                for doc in generated_response["source_document"]
            }
            
            formatted_response = (
                f"{generated_response['result']}\n\n"
                f"{create_sources_string(sources)}"
            )
            
            # Update session state with new interaction
            st.session_state["user_prompt_history"].append(prompt)
            st.session_state["chat_answers_history"].append(formatted_response)
            st.session_state["chat_history"].append(("human", prompt))
            st.session_state["chat_history"].append(("ai", generated_response["result"]))
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.error("Please check your API keys and try again.")


def display_chat_history() -> None:
    """Display the chat history in the Streamlit interface."""
    if st.session_state["chat_answers_history"]:
        for user_query, assistant_response in zip(
            st.session_state["user_prompt_history"],
            st.session_state["chat_answers_history"]
        ):
            with st.chat_message("user"):
                st.write(user_query)
            with st.chat_message("assistant"):
                st.write(assistant_response)


def main() -> None:
    """Main application function."""
    # Page configuration
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon="📚",
        layout="wide"
    )
    
    # Header and description
    st.title(f"📚 {APP_TITLE}")
    st.markdown(APP_DESCRIPTION)
    
    # Initialize session state
    initialize_session_state()
    
    # User input
    prompt = st.text_input(
        "Your Question:",
        placeholder="e.g., How do I create a RAG application with LangChain?",
        help="Enter your question about LangChain functionality or implementation"
    )
    
    # Process query when submitted
    if prompt:
        process_user_query(prompt)
    
    # Display chat history
    display_chat_history()
    
    # Sidebar with additional information
    with st.sidebar:
        st.markdown("### About")
        st.markdown(
            "This tool uses advanced RAG technology to provide accurate answers "
            "from LangChain's comprehensive documentation."
        )
        
        st.markdown("### Example Questions")
        
        for question in SIDEBAR_EXAMPLE_QUESTIONS:
            if st.button(question, key=f"example_{hash(question)}"):
                st.session_state.example_query = question
        
        if "example_query" in st.session_state:
            process_user_query(st.session_state.example_query)
            del st.session_state.example_query
        
        st.markdown("---")
        st.markdown("**Created by:** Eden Marco")
        st.markdown("**Educational Project:** LangChain Udemy Course")


if __name__ == "__main__":
    main()