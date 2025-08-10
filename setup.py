"""
Setup configuration for LangChain Documentation Helper
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="langchain-documentation-helper",
    version="1.0.0",
    author="Based on Eden Marco's work",
    author_email="",
    description="A RAG application for LangChain documentation assistance",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/documentation-helper",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.11",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "langchain-helper=main:main",
            "langchain-ingest=ingestion:ingest_docs",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/yourusername/documentation-helper/issues",
        "Source": "https://github.com/yourusername/documentation-helper",
        "Documentation": "https://github.com/yourusername/documentation-helper#readme",
    },
)
