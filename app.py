from flask import Flask, request, jsonify
import openai
import ast
import os

app = Flask(__name__)

# Set OpenAI API Key (Use environment variable for security)
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_code(code):
    """Analyze Python code using Abstract Syntax Tree (AST)"""
    try:
        tree = ast.parse(code)
        analysis = {
            "functions": [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)],
            "classes": [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)],
            "variables": [node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]
        }
        return analysis
    except Exception as e:
        return {"error": str(e)}

def refactor_code_with_ai(code):
    """Use OpenAI GPT-4 to refactor code"""
    prompt = f"""
    Optimize the following Python code while preserving its functionality:
    
    {code}
    
    Ensure the code follows best practices, improves readability, and removes redundancies.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an expert software refactoring assistant."},
                  {"role": "user", "content": prompt}]
    )

    optimized_code = response['choices'][0]['message']['content']
    return optimized_code

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    code = data.get("code", "")

    if not code:
        return jsonify({"error": "No code provided"}), 400

    analysis = analyze_code(code)
    return jsonify({"analysis": analysis})

@app.route("/refactor", methods=["POST"])
def refactor():
    data = request.json
    code = data.get("code", "")

    if not code:
        return jsonify({"error": "No code provided"}), 400

    optimized_code = refactor_code_with_ai(code)
    return jsonify({"original": code, "optimized": optimized_code})

if __name__ == "__main__":
    app.run(debug=True)
