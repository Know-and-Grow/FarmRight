# Importing essential libraries and modules
import joblib
import json
from flask import Flask, redirect, render_template, request, url_for
import numpy as np
import pandas as pd
import requests
import config
import requests
import pickle

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
@ app.route('/recommendations', methods=['POST'])
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

        data = np.array([[state_code,district_code,season_code,n, oc, p, k, acidic,neutral,basic,temperature, rainfall]])
        my_prediction = crop_recommendation_model.predict(data)
        my_prediction=my_prediction.todense()
        my_prediction=np.squeeze(np.asarray(my_prediction))
        crop_index=[]
        for i in range(len(my_prediction)):
            if(my_prediction[i]==1):
                crop_index.append(i)
        recommendation=[crop for crop, code in config.crop_mapping.items() if code in crop_index]
        
        master_df=pd.read_csv('Datasets/MasterDB.csv')
        
        master_df=master_df[(master_df['Crop'].isin(recommendation))]
        df_current=master_df.loc[(master_df['State_Name']==state) & \
                                (master_df['District_Name']==district) \
                                & (master_df['Season']==season)]
        df_current=df_current.drop(columns=['Crop_Year','N','OC','P','K','ACIDIC','NEUTRAL','BASIC','Temperature','Rainfall'])
        avg_prod_area=df_current.groupby(['Crop'])['Prod/Area'].mean().reset_index()
        avg_prod_area=avg_prod_area.sort_values(by=['Prod/Area'],ascending=False)
    
        recommendation=avg_prod_area['Crop'].to_numpy()
        print(recommendation==[])
        return render_template('output.html', prediction=recommendation, title=title)



# ===============================================================================================
if __name__ == '__main__':
    app.run(debug=False)