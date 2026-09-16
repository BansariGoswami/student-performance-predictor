from flask import Flask,render_template,request

import pickle
import numpy as np
import sklearn

app = Flask(__name__)

model = pickle.load(open('preprocessed.pkl','rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict",methods=['POST'])
def predict():
    if request.method == 'POST':
        Study_Hours = float(request.form['Study_Hours'])
        Attendance_Pct = float(request.form['Attendance_Pct'])
        Previous_Score = float(request.form['Previous_Score'])
        Sleep_Hours = float(request.form['Sleep_Hours'])

        prediction = model.predict([[Study_Hours,Attendance_Pct,Previous_Score,Sleep_Hours]]) 
        output = round(float(prediction[0]),2)


        if output<0:
            return render_template('index.html',pred = "Predicted score is too low")
        elif output>100:
            return render_template('index.html',pred = "Predicted is 100/100")
        else:
            return render_template('index.html',pred = f"Predicted Final Score : {output}/100")

if __name__ == '__main__':
    app.run(debug=True)