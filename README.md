# LangChain Documentation Helper

## Overview

A professional RAG (Retrieval-Augmented Generation) application that provides rapid insights from LangChain's comprehensive documentation and API references. This intelligent documentation assistant leverages LangChain's powerful capabilities to deliver accurate, context-aware responses to user queries about LangChain functionality, implementations, and best practices.

## Features

- **Intelligent Documentation Search**: Advanced semantic search through LangChain's complete API documentation
- **Interactive Chat Interface**: User-friendly Streamlit-based web interface with chat history
- **Context-Aware Responses**: Maintains conversation history for improved response relevance
- **Source Attribution**: Provides direct links to relevant documentation sources
- **Scalable Architecture**: Built with professional-grade components for reliability and performance

## Architecture

The application follows a modular architecture with the following components:

- **Frontend**: Streamlit web interface (`main.py`)
- **Backend Core**: LangChain processing engine (`backend/core.py`)
- **Data Ingestion**: Documentation processing and vector store management (`ingestion.py`)
- **Configuration**: Centralized constants and settings (`consts.py`)

## Technology Stack

- **LangChain**: Core framework for building the RAG pipeline
- **OpenAI**: Language model and embeddings
- **Pinecone**: Vector database for document storage and retrieval
- **Streamlit**: Web interface framework
- **Python 3.11**: Runtime environment

## Prerequisites

Before running the application, ensure you have:

- Python 3.11 or higher
- OpenAI API key
- Pinecone API key and environment setup
- pip or pipenv for dependency management

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/documentation-helper.git
   cd documentation-helper
   ```

2. **Install dependencies:**
   ```bash
   # Using pipenv (recommended)
   pipenv install
   pipenv shell
   
   # Or using pip
   pip install -r requirements.txt
   ```

3. **Environment Setup:**
   Create a `.env` file in the root directory with your API keys:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   PINECONE_API_KEY=your_pinecone_api_key_here
   PINECONE_ENVIRONMENT=your_pinecone_environment_here
   ```

## Usage

### Data Ingestion (First-time Setup)

Before using the application, you need to ingest the LangChain documentation:

```bash
python ingestion.py
```

This process will:
- Load and process the LangChain documentation
- Split documents into manageable chunks
- Generate embeddings using OpenAI's text-embedding-3-small model
- Store vectors in your Pinecone index

### Running the Application

Launch the Streamlit web interface:

```bash
streamlit run main.py
```

The application will be available at `http://localhost:8501`

### Example Queries

Try these example queries to test the system:
- "How do I create a question-answer RAG application in LangChain?"
- "What are the different types of retrievers available in LangChain?"
- "How do I implement memory in LangChain conversations?"
- "What embedding models does LangChain support?"

## Project Structure

```
documentation-helper/
├── backend/
│   ├── __init__.py
│   └── core.py                 # Core RAG processing logic
├── langchain-docs/             # Downloaded LangChain documentation
├── main.py                     # Streamlit web interface
├── ingestion.py                # Documentation ingestion script
├── consts.py                   # Configuration constants
├── requirements.txt            # Python dependencies
├── Pipfile                     # Pipenv configuration
├── README.md                   # Project documentation
└── .env                        # Environment variables (create this)
```

## Configuration

Key configuration options in `consts.py`:

- `INDEX_NAME`: Pinecone index name for document storage
- Chunk size and overlap settings in `ingestion.py`
- Model parameters in `backend/core.py`

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Troubleshooting

### Common Issues

1. **API Key Errors**: Ensure your `.env` file contains valid OpenAI and Pinecone API keys
2. **Memory Issues**: For large document sets, consider increasing chunk size or processing in smaller batches
3. **Network Timeouts**: Check your internet connection and API service status

### Getting Help

- Check the [LangChain Documentation](https://python.langchain.com/docs/)
- Review the [OpenAI API Documentation](https://platform.openai.com/docs)
- Consult the [Pinecone Documentation](https://docs.pinecone.io/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Original Creator**: Eden Marco ([@emarco177](https://github.com/emarco177))
- **Educational Source**: This project was developed as part of Eden Marco's comprehensive Udemy course on LangChain
- **LangChain Community**: For providing excellent documentation and examples
- **OpenAI**: For the powerful language models and embedding technology
- **Pinecone**: For the scalable vector database solution

## Disclaimer

This project was created for educational purposes as part of Eden Marco's Udemy course on LangChain. It demonstrates practical implementation of RAG applications and serves as a learning resource for developers interested in building similar documentation assistance tools.