from flask import Flask,render_template,request
from flask_cors import cross_origin
import pandas as pd
import numpy as np
import datetime
import pickle



app = Flask(__name__, template_folder="template")
model = pickle.load(open("model.pkl", "rb"))
print("Model Loaded")

@app.route("/",methods=['GET'])
@cross_origin()
def home():
	return render_template("index.html")

@app.route("/predict",methods=['GET', 'POST'])
@cross_origin()
def predict():
	if request.method == "POST":
		# try:
			# MinTemp
			MinTemp = float(request.form['mintemp'])
			# MaxTemp
			MaxTemp = float(request.form['maxtemp'])
			# Rainfall
			Rainfall = float(request.form['rainfall'])
			# Evaporation
			Evaporation = float(request.form['evaporation'])
			# Sunshine
			Sunshine = float(request.form['sunshine'])
			# Wind Gust Speed
			WindGustSpeed = float(request.form['windgustspeed'])
			# Wind Speed 9am
			WindSpeed9am = float(request.form['windspeed9am'])
			# Wind Speed 3pm
			WindSpeed3pm = float(request.form['windspeed3pm'])
			# Humidity 9am
			Humidity9am = float(request.form['humidity9am'])
			# Humidity 3pm
			Humidity3pm = float(request.form['humidity3pm'])
			# Pressure 9am
			Pressure9am = float(request.form['pressure9am'])
			# Pressure 3pm
			Pressure3pm = float(request.form['pressure3pm'])
			# Temperature 9am
			Temp9am = float(request.form['temp9am'])
			# Temperature 3pm
			Temp3pm = float(request.form['temp3pm'])
			# Cloud 9am
			Cloud9am = float(request.form['cloud9am'])
			# Cloud 3pm
			Cloud3pm = float(request.form['cloud3pm'])
			# Cloud 3pm
			Location = float(request.form['location'])
			# Wind Dir 9am
			WinddDir9am = float(request.form['winddir9am'])
			# Wind Dir 3pm
			WinddDir3pm = float(request.form['winddir3pm'])
			# Wind Gust Dir
			WindGustDir = float(request.form['windgustdir'])
			# Rain Today
			RainToday = float(request.form['raintoday'])

			pred = model.predict([[Location , MinTemp , MaxTemp , Rainfall , Evaporation , Sunshine ,
						 WindGustDir , WindGustSpeed , WinddDir9am , WinddDir3pm , WindSpeed9am , WindSpeed3pm ,
						 Humidity9am , Humidity3pm , Pressure9am , Pressure3pm , Cloud9am , Cloud3pm , Temp9am , Temp3pm ,
						 RainToday]])
			output = pred
			if output == 0:
				return render_template("after_sunny.html")
			else:
				return render_template("after_rainy.html")
		# except:
		# 	error_message = "Invalid input. Please enter valid values."
		# 	return render_template("predictor.html", error_message=error_message)
	return render_template("predictor.html")

if __name__=='__main__':
	app.run(debug=True)