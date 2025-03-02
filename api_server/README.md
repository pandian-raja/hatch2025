# Breast Cancer Diagnosis with Vertex AI
This project demonstrates how to use Vertex AI's Generative Models to analyze microscopic images of breast tissue and classify them as benign or malignant.


## Getting Started

Server should run automatically when starting a workspace. To run manually, run:
```sh
./devserver.sh
```

## Project Structure

main.py: Contains the Flask application code for handling image uploads and interacting with the Vertex AI API.
requirements.txt: Lists the project dependencies.

## Setup

Install dependencies:

```Bash

pip install -r requirements.txt
```
Set environment variables:

GOOGLE_APPLICATION_CREDENTIALS: Path to your service account key file.
Initialize Vertex AI:

Replace project and location in main.py with your actual project ID and location.
Running the application
Start the Flask development server:

```Bash

python main.py
```

Send a POST request to the /infer endpoint with an image:

```Bash

curl -X POST -H "Content-Type: application/json" -d '{"image": "base64_encoded_image"}' http://localhost:8080/infer
```

## Functionality
The application exposes a single endpoint /infer that accepts a base64-encoded image in the request body. It then sends this image to a pre-trained Vertex AI Generative Model for analysis. The model returns a classification of the tissue as either benign or malignant, along with the specific type of tumor detected.

## Note
This is a basic example and can be further extended to include features like:

User authentication
Image preprocessing
More detailed analysis of the model's output
Integration with other healthcare systems