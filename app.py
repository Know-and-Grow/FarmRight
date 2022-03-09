# Importing essential libraries and modules

from flask import Flask, render_template, request
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
    return render_template('index.html', title=title)

# render crop recommendation form page


@ app.route('/crop-recommend')
def crop_recommend():
    title = 'Know and Grow - Crop Recommendation'
    return render_template('form1.html',title=title)






# ===============================================================================================

# RENDER PREDICTION PAGES

# render crop recommendation result page


@ app.route('/load_properties', methods=['POST'])
def load_properties():
    title = 'Harvestify - Crop Recommendation'
    if request.method == 'POST':
        state = request.form.get("state").upper()
        state_code=config.state_mapping[state]

        district = request.form.get("district").upper()
        district_code=config.district_mapping[district]

        season=request.form["season"].upper()
        

        soil_df=pd.read_csv('Data/Soil_DB.csv')
        soil_df = soil_df.iloc[: , 2:]
        soil=soil_df.loc[(soil_df['State']==state) & (soil_df['District']==district)]
        soil['N'] = soil['N'].astype(str).str[:-1].astype(float, errors = 'raise')
        soil['OC'] = soil['OC'].astype(str).str[:-1].astype(float, errors = 'raise')
        soil['P'] = soil['P'].astype(str).str[:-1].astype(float, errors = 'raise')
        soil['K'] = soil['K'].astype(str).str[:-1].astype(float, errors = 'raise')
        soil['ACIDIC']=soil[['AS%','SrAc%','HAc%','MAc%','SlAc%']].sum(axis=1)
        soil['NEUTRAL']=soil['N%']
        soil['BASIC']=soil[['MAl%','SlAl%']].sum(axis=1)
        soil=soil.drop(columns=['AS%','SrAc%','HAc%','MAc%','SlAc%','N%','MAl%','SlAl%','State','District'])
        soil=np.array(soil).reshape(1,-1)
        print(soil)
        return render_template('form2.html', soil=soil,state=state,district=district,season=season,title=title)




@ app.route('/crop-predict', methods=['POST'])
def crop_prediction():
    title = 'Harvestify - Crop Recommendation'

    if request.method == 'POST':
        
        n = float(request.form['nitrogen'])
        oc = float(request.form['organiccarbon'])
        p = float(request.form['phosphorus'])
        k = float(request.form['potassium'])
        # acidic = float(request.form['acidic'])
        # basic = float(request.form['basic'])
        # neutral = float(request.form['neutral'])

        rainfall = float(request.form['rainfall'])
        temperature=float(request.form['temperature'])
        state = request.form.get("state").upper()
        state_code=config.state_mapping[state]

        district = request.form.get("district").upper()
        district_code=config.district_mapping[district]

        
        # season_code=config.season_mapping[season]

        # if weather_fetch(city) != None:
        #     # temperature, humidity = weather_fetch(city)
        #     data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        #     my_prediction = crop_recommendation_model.predict([[]])
        #     # final_prediction = my_prediction[0]
        #     print(my_prediction)
        #     return render_template('crop-result.html', prediction=my_prediction, title=title)

        # else:

        #     return render_template('try_again.html', title=title)
        data = np.array([[state_code,district_code,n, oc, p, k, temperature, rainfall]])
        print(len(data))
        data = np.array([[10.  , 498.  ,   1.  ,  99.92,  99.47,  74.47,  42.38,   0.74,
        0.98,  98.27, 300.  ,   8.]])
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