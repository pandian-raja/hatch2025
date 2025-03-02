import React, { useState } from 'react';
import './App.css';

function App() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [resultMessage, setResultMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false); // Add loading state

  const handleImageChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      setSelectedImage(file);
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onloadend = () => {
        setPreview(reader.result);
        setResultMessage(''); // Clear previous results on new image selection
      };
    } else {
      setSelectedImage(null); // Clear image if no file selected
      setPreview(null);
      setResultMessage('');
    }
  };

  const handleSubmit = async () => {
    if (!selectedImage) {
      setResultMessage('Please select an image to upload.');
      return;
    }

    setIsLoading(true); // Set loading to true
    setResultMessage(''); // Clear previous results

    const reader = new FileReader();
    reader.readAsDataURL(selectedImage);
    reader.onloadend = async () => {
      const base64String = reader.result.split(',')[1];

      try {
        const response = await fetch('<BACKEND_URL>', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ image: base64String }),
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        setResultMessage(result.output || 'No result received.');
      } catch (error) {
        console.error('Error uploading image:', error);
        setResultMessage('Failed to upload image. Please try again.');
      } finally {
        setIsLoading(false); // Set loading to false regardless of success or failure
      }
    };
  };

  return (
    <div className="app-container">
      <div className="content-wrapper">
        <h1 className="app-title">Breast Cancer Detection in Microscopic Image</h1>
        <div className="upload-section">
          <label htmlFor="file-upload" className="custom-file-upload">
            Choose an Image
          </label>
          <input
            id="file-upload"
            type="file"
            accept="image/*"
            onChange={handleImageChange}
            style={{ display: 'none' }}
          />
          {preview && (
            <div className="preview-container">
              <img src={preview} alt="Preview" className="preview-image" />
            </div>
          )}
          <button onClick={handleSubmit} disabled={isLoading} className="submit-button">
            {isLoading ? 'Processing...' : 'Submit'}
          </button>
        </div>
        {resultMessage && (
          <div className="result-message">
            {resultMessage}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;