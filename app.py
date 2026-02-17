from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import os

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for Angular

# Mock logic since we don't have a trained model file
def predict_quality_mock(image_filename):
    # In a real scenario, we would load the image and pass it to TensorFlow
    # Here we simulate a result
    
    # Deterministic mock based on filename length or random
    grades = ['A', 'B', 'C']
    grade = random.choice(grades)
    
    confidence = random.randint(70, 99)
    
    messages = {
        'A': 'Premium quality. Suitable for export.',
        'B': 'Standard quality. Good for local market.',
        'C': 'Low quality. Suitable for processing.'
    }
    
    return {
        "grade": grade,
        "confidence": confidence,
        "message": messages[grade]
    }

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file:
        # We don't save the file to disk in this mock to save space, 
        # but in real life you'd save it or process stream
        result = predict_quality_mock(file.filename)
        return jsonify(result)

if __name__ == '__main__':
    print("Starting AI Module on port 5000...")
    app.run(port=5000, debug=True)
