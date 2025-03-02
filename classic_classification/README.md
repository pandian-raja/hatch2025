#Breast Cancer Histopathology Image Classification

This project focuses on classifying breast cancer histopathology images into eight distinct subtypes using a deep learning model. The model is trained on the BreakHis dataset, which contains a variety of breast histology images.

##Dataset
The dataset used in this project is the BreakHis dataset, available on Kaggle: [BreakHis Dataset](https://www.kaggle.com/datasets/ambarish/breakhis)

##Project Structure
1.  **Data Loading and Preprocessing:**
    -      Images are loaded and resized.
    -      Data augmentation is applied.
    -      The dataset is split into training, validation, and test sets.
    -      Data is converted into TensorFlow datasets for efficient training.
2.  **Model Architecture:**
    -      A DenseNet121 model is used as the base model.
    -      Intermediate layers are extracted and processed through separate branches.
    -      Branch outputs are concatenated and passed through dense layers for final classification.
    -      The model is compiled with the Adam optimizer and categorical cross-entropy loss.
4.  **Model Training:**
    -      The model is trained using the training dataset.
    -      Early stopping and learning rate reduction callbacks are used.
    -   The trained model weights are saved.
5.  **Model Evaluation:**
    -      The model's performance is evaluated on the test dataset.
    -   Accuracy, precision, recall, and F1-score are calculated.
    -   A confusion matrix is generated.
6.  **Prediction on a single image:**
    -   Example code to load and predict a single image is added.
7.  **Download model:**
    -   Code to zip and download the trained model is added.
8.  **Plotting training and validation accuracy:**
    -   Plotting the training and validation accuracy over the training epochs.

##Model Performance
The model achieved the following performance metrics on the test dataset:
Precision: 0.8958 (Macro-average)
Recall: 0.8990 (Macro-average)
F1 Score: 0.8928 (Macro-average)


Reference:
-  [BreakHis Dataset](https://www.kaggle.com/datasets/ambarish/breakhis)
-  [Breast Cancer Classification Notebook](https://www.kaggle.com/code/patrickgeorgeskromil/breast-cancer-classification#Calculating-Other-Evaluation-Metrics-(Precision,-Recall,-and-F1-Score))



