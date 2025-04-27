from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from classifier import classify_text

# Initialize Flask app and CORS
app = Flask(__name__)
CORS(app)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///poc_corrections.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Function to implement the API endpoint for text classification
@app.route('/api/classify', methods=['POST'])
def api_classify():
    data = request.get_json()
    if not data or 'text' not in data:
        abort(400, 'Invalid input. Please provide text to classify.')

    text = data['text']
    try:
        result = classify_text(text)
        return jsonify({'result': result})
    except Exception as e:
        abort(500, str(e))
    
# Function to implement the API endpoint for submitting corrections
@app.route('/api/submit_correction', methods=['POST'])
def api_submit_correction():
    data = request.get_json()
    if not data or 'text' not in data or 'correction' not in data:
        abort(400, 'Invalid input. Please provide text and correction.')

    text = data['text']
    correction = data['correction']
    try:
        # Here you would typically save the correction to a database
        # For this example, we'll just return a success message
        return jsonify({'message': 'Correction submitted successfully!'})
    except Exception as e:
        abort(500, str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)