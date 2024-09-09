# House Price Prediction Web App

This project is a web application that predicts house prices based on user inputs such as the number of bedrooms, total rooms, house age, population, and proximity to the ocean. The app uses a machine learning model trained on housing data to make predictions.

## Features

- Predicts house prices based on user input.
- Utilizes ocean proximity as an additional feature to enhance predictions.
- Interactive web form for input.
- Displays results directly on the webpage.

## Technologies Used

- Flask: Backend framework for serving the web application.
- Scikit-learn: Machine learning library for model training and prediction.
- Pandas: Data manipulation and analysis.
- HTML/CSS: Frontend for user interaction.

## Project Structure

House_Price_Prediction
- app.py                   # Main Flask application file
- model.pkl                # Trained machine learning model (Ridge regression or another model)
- final_dataset.csv        # Dataset used for training the model
- templates/
  - index.html             # HTML template for the web page
- static/
  - styles.css             # CSS file for styling the webpage
- README.md                # Project README file
  - requirements.txt          

## Setup and Installation

### Prerequisites

- Python 3.x installed on your machine.
- Pip (Python package manager).

### Steps

- Clone the repository:
  git clone https://github.com/yourusername/House_Price_Prediction.git
cd House_Price_Prediction
- Create a virtual environment:
  python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
- Install dependencies:
  pip install -r requirements.txt
- Download the dataset and model:
  Ensure that the final_dataset.csv and model.pkl files are in the root directory of the project.
- Run the application:
  python app.py
- Access the app:
  Open your browser and go to http://127.0.0.1:5000/ to use the web app.

## Usage
  
- Enter the number of bedrooms, total rooms, house age, population, and proximity to the ocean.
- Click on the "Predict" button to get the estimated house price.

## Model Information

- Model used: Ridge Regression
- Dataset: Housing dataset with features like total_bedrooms, total_rooms, housing_median_age, 
  population, and ocean_proximity.
- Performance: The model has shown to provide reasonable predictions, though further tuning and 
  feature engineering may improve accuracy.

## Future Improvements
  
- Explore other machine learning algorithms like Support Vector Regression (SVR), XGBoost, or 
  Neural Networks for better accuracy.
- Improve frontend design and responsiveness.
- Add more features to the model to enhance prediction accuracy.

## License

This project is licensed under the MIT License. See the LICENSE file for more details

## Support

For any questions or feedback, please contact pchithra611@gmail.com

## Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.
