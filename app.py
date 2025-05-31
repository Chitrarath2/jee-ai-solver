from flask import Flask, request, jsonify, render_template
from jee_ai_model import JEEWebSolver
import os

app = Flask(__name__)
solver = JEEWebSolver()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve_problem():
    data = request.json
    question = data.get('question', '')
    subject = data.get('subject', '')
    
    result = solver.get_solution(question, subject)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
