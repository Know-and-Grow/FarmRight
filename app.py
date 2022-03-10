# Importing essential libraries and modules

import json
from flask import Flask, redirect, render_template, request, url_for
import numpy as np
import pandas as pd
import requests
import config
import pickle

# ==============================================================================================

# -------------------------LOADING THE TRAINED MODELS -----------------------------------------------



# Loading crop recommendation model

crop_recommendation_model_path = 'models/model.pkl'
crop_recommendation_model = pickle.load(
    open(crop_recommendation_model_path, 'rb'))


# =========================================================================================

# Custom functions for calculations

def weather_fetch(city_name):
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    api_key = config.weather_api_key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        temperature = round((y["temp"] - 273.15), 2)
        humidity = y["humidity"]
        return temperature, humidity
    else:
        return None


# ===============================================================================================
# ------------------------------------ FLASK APP -------------------------------------------------


app = Flask(__name__)

# render home page


@ app.route('/')
def home():
    title = 'Know and Grow - Home'
    return render_template('index.html')

# render crop recommendation form page







# ===============================================================================================

# RENDER PREDICTION PAGES

# render crop recommendation result page
@ app.route('/predict', methods=['POST'])
def crop_prediction():
    title = 'Harvestify - Crop Recommendation'

    if request.method == 'POST':
        n = float(request.form['nitrogen'])
        oc = float(request.form['organiccarbon'])
        p = float(request.form['phosphorus'])
        k = float(request.form['potassium'])
        acidic = float(request.form['ph_acidic'])
        basic = float(request.form['ph_basic'])
        neutral = float(request.form['ph_neutral'])

        rainfall = float(request.form['rainfall'])
        temperature=float(request.form['temperature'])
        state = request.form.get("state")
        state_code=config.state_mapping[state]

        district = request.form.get("district")
        district_code=config.district_mapping[district]

        season=request.form["season"]
        season_code=config.season_mapping[season]

        # if weather_fetch(city) != None:
        #     # temperature, humidity = weather_fetch(city)
        #     data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        #     my_prediction = crop_recommendation_model.predict([[]])
        #     # final_prediction = my_prediction[0]
        #     print(my_prediction)
        #     return render_template('crop-result.html', prediction=my_prediction, title=title)

        # else:

        #     return render_template('try_again.html', title=title)
        data = np.array([[state_code,district_code,season_code,n, oc, p, k, acidic,neutral,basic,temperature, rainfall]])
        print(data)
        print(len(data))
        my_prediction = crop_recommendation_model.predict(data)
        my_prediction=my_prediction.todense()
        my_prediction=np.squeeze(np.asarray(my_prediction))
        crop_index=[]
        for i in range(len(my_prediction)):
            if(my_prediction[i]==1):
                crop_index.append(i)
        recommendation=[crop for crop, code in config.crop_mapping.items() if code in crop_index]

        print(recommendation)
        return render_template('output.html', prediction=recommendation, title=title)



# ===============================================================================================
# if __name__ != '__main__':
#     app.run(debug=False)
app.run(debug=True)