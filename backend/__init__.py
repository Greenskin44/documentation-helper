"""
LangChain Documentation Helper - Backend Package

This package contains the core backend functionality for the LangChain 
Documentation Helper RAG system.

Author: Based on original work by Eden Marco (@emarco177)
Educational Context: Developed as part of Eden Marco's Udemy LangChain course
"""

from .core import run_llm, get_vector_store_info, validate_environment

__version__ = "1.0.0"
__author__ = "Based on Eden Marco's work"

__all__ = [
    "run_llm",
    "get_vector_store_info", 
    "validate_environment"
]