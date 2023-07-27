""" The main flask code"""

from flask import Flask, request, jsonify
from generator import Generator

app = Flask(__name__)
generator = Generator()

@app.route('/pascals-triangle', methods=['POST'])
def pascals_triangle():
    try:
        data = request.json
        rows = data.get('rows', 0)
        if not isinstance(rows, int) or rows < 0:
            return jsonify({"error": "Invalid input"}), 400

        triangle = generator.generate(rows)
        response = {f"row_{i+1}": row for i, row in enumerate(triangle)}
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
