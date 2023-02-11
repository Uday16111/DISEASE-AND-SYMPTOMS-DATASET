import flask
from pymongo import MongoClient
from flask import Flask, request, render_template, url_for,redirect

client = MongoClient('mongodb://localhost:27017')
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

 
# Creating a symptom index dictionary to encode the
# input symptoms into numerical form

@app.route('/disease_predict',methods=['POST','GET'])
def disease_predict():
    selected_symptoms = []
    if(request.form['Symptom1']!="") and (request.form['Symptom1'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom1'])
    if(request.form['Symptom2']!="") and (request.form['Symptom2'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom2'])
    if(request.form['Symptom3']!="") and (request.form['Symptom3'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom3'])
    if(request.form['Symptom4']!="") and (request.form['Symptom4'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom4'])
    if(request.form['Symptom5']!="") and (request.form['Symptom5'] not in selected_symptoms):
        selected_symptoms.append(request.form['Symptom5'])

    class my_dictionary(dict): 
        def __init__(self): 
            self = dict()   
        def add(self, key, value): 
            self[key] = value 
        
    dict_obj = my_dictionary() 
    p=sorted(selected_symptoms)
    limit = len(p)

    for i in range(limit):
        dict_obj.key = p[i]
        dict_obj.value = '1'
        dict_obj.add(dict_obj.key, dict_obj.value) 

#print(dict_obj)

    filter=dict_obj

#print(filter)

    result = client['PANACE']['testing'].find(filter=filter)
#print(result)
    str1='''Not Found, please select correct symptoms '''
    for i in result:
        str1=i['label_dis']
   # print(i['prognosis'])

    return render_template('disease.html',prediction_text='{}'.format(str1))

if __name__ == "__main__":
    app.run(debug=True)


