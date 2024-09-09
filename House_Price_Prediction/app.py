from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

# Load the dataset and the model
data = pd.read_csv('final_dataset.csv')  # Replace with your dataset
pipe = pickle.load(open("forest.pkl", 'rb'))  # Replace with your model file


@app.route('/')
def index():
    # Extract unique values for form options
    bedrooms = sorted(data['total_bedrooms'].unique())
    total_rooms = sorted(data['total_rooms'].unique())
    house_age = sorted(data['housing_median_age'].unique())
    population = sorted(data['population'].unique())
    ocean_proximity = sorted(data['ocean_proximity'].unique())  # Added ocean proximity

    return render_template('index.html', bedrooms=bedrooms, total_rooms=total_rooms, house_age=house_age,
                           population=population, ocean_proximity=ocean_proximity)


@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    bedrooms = request.form.get('total_bedrooms')
    total_rooms = request.form.get('total_rooms')
    house_age = request.form.get('housing_median_age')
    population = request.form.get('population')
    ocean_proximity = request.form.get('ocean_proximity')  # Get ocean proximity from the form

    # Safely convert form data to proper data types
    try:
        bedrooms = int(float(bedrooms))  # Convert to float first, then int
        total_rooms = float(total_rooms)  # Keep as float
        house_age = float(house_age)  # Keep as float
        population = int(float(population))  # Convert to float first, then int
    except ValueError as e:
        return f"Error in input conversion: {e}"

    # Encode ocean proximity
    ocean_proximity_encoded = {
        'NEAR BAY': [1, 0, 0, 0, 0],
        'NEAR OCEAN': [0, 1, 0, 0, 0],
        'ISLAND': [0, 0, 1, 0, 0],
        'INLAND': [0, 0, 0, 1, 0],
        '<1H OCEAN': [0, 0, 0, 0, 1],
    }.get(ocean_proximity, [0, 0, 0, 0, 0])

    # Prepare features
    features = np.array([
                            np.log(total_rooms + 1),
                            np.log(bedrooms + 1),
                            np.log(population + 1),
                            np.log(house_age + 1)
                        ] + ocean_proximity_encoded).reshape(1, -1)

    # Predict the house price
    prediction = pipe.predict(features)[0]

    # Return the prediction to be displayed on the webpage
    return render_template('index.html', prediction=prediction, bedrooms=sorted(data['total_bedrooms'].unique()),
                           total_rooms=sorted(data['total_rooms'].unique()), house_age=sorted(data['housing_median_age'].unique()),
                           population=sorted(data['population'].unique()), ocean_proximity=sorted(data['ocean_proximity'].unique()))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
