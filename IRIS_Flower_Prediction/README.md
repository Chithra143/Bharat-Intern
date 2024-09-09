# IRIS Flower Prediction Web App
This repository contains a simple machine learning web application that predicts the species of an IRIS flower based on four input features: sepal length, sepal width, petal length, and petal width. The prediction is powered by a trained deep learning model using the TensorFlow and Keras libraries.

## Introduction

The IRIS Flower Prediction app is a user-friendly web interface that leverages a deep learning model to classify IRIS flowers into three species: Setosa, Versicolor, and Virginica. Users can input the four flower measurements, and the app returns the predicted species.

The application demonstrates a simple deployment of machine learning models using Flask, HTML and CSS for the frontend.

## Features

- IRIS Species Prediction: Predicts one of the three IRIS species based on user input.
- User-Friendly Interface: Responsive design with a simple and attractive UI.
- Real-time Prediction: The prediction is computed and displayed instantly upon form submission.

## Technologies Used

- Frontend: HTML, CSS
- Backend: Flask (Python)
- Machine Learning: TensorFlow, Keras
- Data: IRIS dataset (from Kaggel)

## Installation

- Clone the Repository:
  git clone https://github.com/yourusername/iris-flower-prediction.git
cd iris-flower-prediction
- Set Up the Virtual Environment:
  python -m venv venv
source venv/bin/activate
- Install Dependencies:
  pip install -r requirements.txt
- Download the Dataset:
   Make sure that the IRIS dataset is present in your working directory or specify the path in your Jupyter notebook for training the model.
- Run the Flask App:
  flask run
  The app will be accessible at http://127.0.0.1:5000/.

  ## Project Structure

- IRIS_Flower_Prediction/
  - static/
     - styles.css
  - templates/
    - index.html
  - app.py
  - iris_model.pkl
  -  iris_scaler.pkl
  -  requirements.txt
  -  README.md
 - app.py: The Flask app code.
- index.html: The frontend code for the web page.
- styles.css: Custom styles for the app UI.
- iris_model.pkl: Pickle file containing the trained IRIS flower prediction model.
- iris_scaler.pkl: Pickle file containing the scaler for data normalization.
- requirements.txt: File listing all required dependencies.
  
##   Model Details

The model used in this project is a fully connected feedforward neural network (Sequential model) built with Keras and TensorFlow. It consists of the following layers:

- Dense layers with ReLU activation
- Dropout layers to prevent overfitting
- Output layer with softmax activation to predict the probabilities of the three IRIS species.
The model is trained on the IRIS dataset, which contains 150 samples and 3 species of flowers.

## License

This project is open-source and available under the MIT License.

## Support

For any questions or feedback, please contact pchithra611@gmail.com

## Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.
