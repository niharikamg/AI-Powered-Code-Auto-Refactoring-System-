import requests

BASE_URL = "http://127.0.0.1:5000"

def test_analyze():
    code = """
def add_numbers(a, b):
    return a + b
"""
    response = requests.post(f"{BASE_URL}/analyze", json={"code": code})
    print("Analyze Response:", response.json())

def test_refactor():
    code = """
def multiply_numbers(a, b):
    result = a * b
    return result
"""
    response = requests.post(f"{BASE_URL}/refactor", json={"code": code})
    print("Refactor Response:", response.json())

if __name__ == "__main__":
    test_analyze()
    test_refactor()
