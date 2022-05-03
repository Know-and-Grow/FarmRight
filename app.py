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
import random
import re


import nltk
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

from keras.models import load_model

# -------------------------LOADING THE TRAINED MODELS -----------------------------------------------



# Loading crop recommendation model

crop_recommendation_model_path = 'models/model.pkl'
crop_recommendation_model = pickle.load(
    open(crop_recommendation_model_path, 'rb'))

# Loading chatbot model

chatbot_model = load_model('models/model.h5')



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

intents = json.loads(open('utils/intents.json').read())
words = pickle.load(open('utils/texts.pkl','rb'))
classes = pickle.load(open('utils/labels.pkl','rb'))

def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

def chatbot_response(msg):
    ints = predict_class(msg, chatbot_model)
    res = getResponse(ints, intents)
    return res


def findName(string):
  length = len(string)
  newstring=""
  # traversing from last
  for i in range(length-1, 0, -1):
      
      # if space is occurred then return
      if(string[i] == " "):
          
          # return reverse of newstring
          return newstring[::-1]
      else:
          newstring = newstring + string[i]
# ===============================================================================================
# ------------------------------------ FLASK APP -------------------------------------------------


app = Flask(__name__)

# render home page


@ app.route('/')
def home():
    title = 'Know and Grow - Home'
    return render_template('index.html')

@ app.route('/get',methods=['GET'])
def get_bot_response():
    
    userText = request.args.get('msg')
    if (bool(re.match("i am",userText.lower()))):
        n=findName(userText)
        return chatbot_response(userText).format(n=n)
    else:
        return chatbot_response(userText)
    








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
    app.run(debug=True)





