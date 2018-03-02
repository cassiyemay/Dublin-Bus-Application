from flask import Flask, render_template, g, jsonify, request
#from dbus import config
import sqlalchemy as sqla
from sqlalchemy import create_engine
import pymysql
#import MySQLdb
import json
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn import model_selection
import pickle
import re
import datetime
app = Flask(__name__)

    
def connect_to_database():
    db_str = "mysql+mysqldb://{}:{}@{}:{}/{}"
    engine = create_engine(db_str.format(config.USER,
                                        config.PASSWORD,
                                        config.URI,
                                        config.PORT,
                                        config.DB),
                         echo=True)
    return engine

def get_db():
    engine = getattr(g, 'engine', None)
    if engine is None:
        engine = g.engine = connect_to_database()
    return engine



@app.route("/")
def main():
    with open('static/routes.json') as data_file:
        json_file_routes = json.load(data_file)
        
    with open('static/routes.json') as data_file:
        json_routes = json.load(data_file)
        
    with open('static/routes_and_stops.json') as data_file:
        json_file_stops = json.load(data_file)
    
    return render_template("index.html", json_file_routes = json_file_routes, json_file_stops = json_file_stops, json_routes = json_routes)

@app.route("/routes", methods=['GET','POST'])
def routes():
    chosenroute = request.form.get('chosenroute')

    chosenorigin = request.form.get('chosenorigin')
    chosendestination = request.form.get('chosendestination')
    chosenday = request.form.get('chosenday')
    chosentime = request.form.get('chosentime')
    chosentemp = request.form.get('chosentemp')
    chosenhumid = request.form.get('chosenhumid')
    chosenpres = request.form.get('chosenpres')
    #run the prediction model
    dataframe = pd.read_csv('cleangps.csv')
    array = dataframe.values
    X = array[:,0:7]
    Y = array[:,7]
    test_size = 0.33
    seed = 7
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)
    # Fit the model on 33%
    model = RandomForestRegressor()  
    model.fit(X_train, Y_train)
    # save the model to disk
    filename = 'finalized_model.sav'
    pickle.dump(model, open(filename, 'wb'))
    #calculating the average time between two adjacent stops
    chosend=float(re.search(r'\d+', chosenday).group())
    chosent=float(re.search(r'\d+', chosentime).group())
    chosenro=float(re.search(r'\d+', chosenroute).group())
    chosenro1=str(re.search(r'\d+', chosenroute).group())
    #chosenro1=chosenroute.split(":")
    #value= str(chosenro1[0])
    chosenorig =float(re.search(r'\d+', chosenorigin).group())
    chosendest=float(re.search(r'\d+', chosendestination).group())
    data =[]
    for i in range(0,len(X)):
            if X[i][0]==chosenro and X[i][2]==chosent and X[i][3]==chosend:
                data.append(X[i])
        
    # load the model from disk
    loaded_model = pickle.load(open(filename, 'rb'))
    #calculating the time between adjacent stops
    result = loaded_model.predict(data)
    total = 0
    for j in range(len(result)):
        total += (result[j])
    seconds = (total//len(result))
    
    
    #calculating the number of stops between origin and destination
    df = pd.read_csv('stops.csv')
    arr = df.values
    list=[]
    for j in range(len(arr)):
        if (arr[j][0])==chosenorig or (arr[j][0])==chosendest:
            list.append(arr[j])
    
        
    list1=[]
    for i in range(len(list)):
        if (list[i][4]) ==chosenro1:
            list1.append(list[i])
    nums = abs(list1[0][6] -list1[1][6])
    second = seconds * nums
    times = str(datetime.timedelta(seconds=second))
    #calculating the predict time between origin and destination
    #list =[]
    #for i in range(len(data)):
        #if data[i][1]==chosenorig:
            #list.append(i)
        #if data[i][1]==chosendest:
            #list.append(i)
    
    #result = loaded_model.predict(data[list[0]:list[1]])
    #total = 0
    #for i in range(len(result)):
        #total += (result[i])
    #time = total//60
    #create variables for time +1 hour and time -1hour
    chosentime1 = chosent + 1
    chosentime2 = chosent - 1
    data1 =[]
    for i in range(0,len(X)):
            if X[i][0]==chosenro and X[i][2]==chosentime1 and X[i][3]==chosend:
                data1.append(X[i])
        
    # load the model from disk
    loaded_model = pickle.load(open(filename, 'rb'))
    #calculating the time between adjacent stops
    result1 = loaded_model.predict(data1)
    total1 = 0
    for j in range(len(result1)):
        total1 += (result1[j])
    seconds = (total1//len(result1))
    second1 = seconds * nums
    time1 = str(datetime.timedelta(seconds=second1))
    
    # model 3
    data2 =[]
    for i in range(0,len(X)):
            if X[i][0]==chosenro and X[i][2]==chosentime1 and X[i][3]==chosend:
                data2.append(X[i])
        
    # load the model from disk
    loaded_model = pickle.load(open(filename, 'rb'))
    #calculating the time between adjacent stops
    result2 = loaded_model.predict(data2)
    total2 = 0
    for j in range(len(result2)):
        total2 += (result2[j])
    seconds = (total2//len(result2))
    second2 = seconds * nums
    time2 = str(datetime.timedelta(seconds=second2))

    
    return render_template("display.html", chosenroute = chosenroute,chosenorigin=chosenorigin,chosendestination=chosendestination,chosent=chosent, chosentime1=chosentime1, chosentime2=chosentime2,times=times,time1=time1,time2=time2)


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        


if __name__ == "__main__":
    app.run(debug=True)