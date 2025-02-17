from flask import Flask, render_template, request, redirect, url_for
import csv
import os
import matplotlib.pyplot as plt
import math



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def details():  
    if request.method=='GET':
        return render_template('index.html')
    elif request.method=='POST':
        type=request.form['ID']
        id=request.form['id_value']
        if id=='':
            return render_template('wrong.html')
        id=int(id)
        data=[ ]
        file_path = os.path.join(os.path.dirname(__file__), 'data.csv')
        with open(file_path, 'r') as file:
            file.readline() 
            if type=='student_id':
                for row in file:
                    row=list(map(int,row.strip().split(',')))
                    if row[0]==id:
                        data.append(row) 
            else:
                pass
        if len(data)==0:
            return render_template('wrong.html')
        elif type=='student_id':
            tm=0
            for x in data:
                tm+=x[2]
            return render_template('studentsdetails.html',data=data,Total_Marks=tm)
        

app.run(debug=True)

