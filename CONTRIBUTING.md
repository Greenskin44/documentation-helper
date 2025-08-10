# Contributing to LangChain Documentation Helper

Thank you for your interest in contributing to the LangChain Documentation Helper! This document provides guidelines for contributing to this educational project.

## Project Background

This project was originally created by Eden Marco ([@emarco177](https://github.com/emarco177)) as part of his comprehensive Udemy course on LangChain. The project serves as an educational resource demonstrating practical RAG application development.

## How to Contribute

### Reporting Issues

- Use GitHub Issues to report bugs or suggest enhancements
- Provide detailed information including:
  - Steps to reproduce the issue
  - Expected vs actual behavior
  - Environment details (OS, Python version, etc.)
  - Error messages or logs

### Submitting Changes

1. **Fork the Repository**
   ```bash
   git fork https://github.com/yourusername/documentation-helper.git
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**
   - Follow the existing code style
   - Add appropriate documentation
   - Include tests if applicable

4. **Test Your Changes**
   ```bash
   # Install dependencies
   pipenv install --dev
   
   # Run the application
   streamlit run main.py
   
   # Test ingestion (if applicable)
   python ingestion.py
   ```

5. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "feat: add your descriptive commit message"
   ```

6. **Push and Create Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

### Development Guidelines

#### Code Style
- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and modular

#### Documentation
- Update README.md for significant changes
- Add inline comments for complex logic
- Update requirements.txt if adding dependencies

#### Environment Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/documentation-helper.git
   cd documentation-helper
   ```

2. **Set up virtual environment**
   ```bash
   pipenv install --dev
   pipenv shell
   ```

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. **Run the application**
   ```bash
   streamlit run main.py
   ```

### Types of Contributions Welcome

- **Bug fixes**: Fix existing issues or improve error handling
- **Documentation**: Improve README, add examples, or create tutorials
- **Features**: Add new functionality (discuss in issues first)
- **Performance**: Optimize existing code or reduce resource usage
- **Testing**: Add unit tests or integration tests
- **UI/UX**: Improve the Streamlit interface

### Areas for Improvement

Some areas where contributions would be particularly valuable:

- **Error Handling**: More robust error handling and user feedback
- **Testing**: Unit tests and integration tests
- **Performance**: Optimization for large document sets
- **Features**: Additional retrieval methods or response formats
- **Documentation**: More detailed setup guides or tutorials

## Getting Help

- **Issues**: Check existing GitHub issues or create a new one
- **Discussions**: Use GitHub Discussions for general questions
- **Documentation**: Refer to the main README.md for setup instructions

## Recognition

Contributors will be recognized in the project README and release notes. All contributions help make this educational resource better for the community.

## Educational Context

Remember that this project serves as an educational resource for learning LangChain and RAG applications. When contributing, consider how changes might benefit others learning from this codebase.

Thank you for helping improve this project!
