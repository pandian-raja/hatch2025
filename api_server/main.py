import os
import json
import base64
from flask import Flask, request, jsonify
from flask_cors import CORS
import vertexai
from vertexai.generative_models import GenerativeModel, SafetySetting, Part, GenerationConfig

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


def init_vertex_ai():
    vertexai.init(
        project="<project>",
        location="<location>",
        api_endpoint="<api_endpoint>"
    )
    print("Init Completed")
        
    
def get_generation_config():
    return GenerationConfig(
        max_output_tokens=8192,
        temperature=1,
        top_p=0.95,
    )

def get_safety_settings():
    return [
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
    ]

@app.route('/test', methods=['POST'])
def test():
    print("Test")
    return jsonify({"status": "success"})

@app.route('/infer', methods=['POST'])
def infer_image():
    try:
        data = request.json
        image_base64 = data.get('image')
        
        if not image_base64:
            return jsonify({"error": "Image is required"}), 400
        
        image_data = base64.b64decode(image_base64)
        image_part = Part.from_data(mime_type="image/jpeg", data=image_data)
        
        prompt = """You are given a microscopic image of breast tissue. Your task is to analyze the image and determine:
        1. Whether the tissue shows benign or malignant characteristics
        2. The specific type of breast tumor present in the image.
        Provide your analysis in a structured format: Tumor Classification: is Benign or Malignant and Tumor Type is Tubular Adenoma or Phyllodes Tumor or Fibroadenoma or Adenosis or Papillary Carcinoma or Mucinous Carcinoma or Lobular Carcinoma or Ductal Carcinoma"""
        
        model = GenerativeModel("<GenerativeModel Endpoint url>")
        response = model.generate_content(
            [image_part, prompt],
            generation_config=get_generation_config(),
            safety_settings=get_safety_settings()
        )
        
        return jsonify({"output": response.text})
    
    except Exception as e:
        return jsonify({"error": str(e), "status": "error"}), 500

if __name__ == "__main__":

    init_vertex_ai()
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
