import pickle
from flask import Flask, render_template, request
import pandas as pd
import numpy as np

model1 = pickle.load(open('productivity.pkl', 'rb'))
app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict') # rendering the html template
def index() :
    return render_template('predict.html')


@app.route('/data_predict', methods=['GET','POST'])
def predict() :

    quarter = int(request.form['Quarter'])

    department = request.form['Department']
    if department == 'Sewing':
        department = 1
    if department == 'sewing':
        department = 1
    if department == 'Finishing':
        department = 0
    if department == 'finishing':
        department = 0

    day = request.form['Day of the week']
    if day == 'Monday':
        day = 0
    if day == 'monday':
        day = 0
    if day == 'Tuesday':
        day = 4
    if day == 'tuesday':
        day = 4
    if day == 'Wednesday':
        day = 5
    if day == 'wednesday':
        day = 5
    if day == 'Thursday':
        day = 3
    if day == 'thursday':
        day = 3
    if day == 'Saturday':
        day = 1
    if day == 'saturday':
        day = 1
    if day == 'Sunday':
        day = 2
    if day == 'sunday':
        day = 2
    
    team = int(request.form['Team Number'])
    time = int(request.form['Time Allocated'])
    items = int(request.form['Unfinished Items'])
    over_time = int(request.form['Over time'])
    incentive = int(request.form['Incentive'])
    idle_time = int(request.form['Idle Time'])
    idle_men = int(request.form['Idle Men'])
    style = int(request.form['Style Change'])
    workers = int(request.form['Number of Workers'])

    prediction = model1.predict(pd.DataFrame([[quarter,department,day,team,time,items,over_time,incentive,idle_time,idle_men,style,workers]], columns= ['quarter', 'department', 'day', 'team_number', 'time_allocated', 'unfinished_items',
       'over_time', 'incentive','idle_time','idle_men','style_change', 'no_of_workers']))
    
     
    prediction = (np.round(prediction,4))*100
    
    
    return render_template('productivity.html', prediction_text ="is {}".format(prediction))




if __name__ == '__main__':
    app.run()
