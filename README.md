# AI-Powered Code Auto-Refactoring System

This project provides an AI-powered code analysis and refactoring system using OpenAI GPT-4 and Flask.

## Features
- Analyzes Python code for functions, classes, and variables using AST.
- Uses AI to optimize and refactor code while maintaining logic.
- REST API endpoints for easy integration.

## Installation

1. Clone the repository:
   ```sh
   git clone <repo-link>
   cd AI_Code_Refactoring_System
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   ```sh
   export OPENAI_API_KEY="your_api_key_here"
   ```

4. Run the Flask app:
   ```sh
   python app.py
   ```

5. Use the API with `test_api.py`.

## API Endpoints
- **POST /analyze**: Analyzes provided Python code.
- **POST /refactor**: Optimizes and refactors provided Python code.

## Example Usage
Run `test_api.py` to test the API endpoints.
