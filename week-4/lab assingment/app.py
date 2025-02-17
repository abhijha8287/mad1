from flask import Flask, render_template, request, redirect, url_for
import csv
import os
import matplotlib.pyplot as plt
import math



app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static/images'

def calculate_student_data(student_id):
    with open('data.csv', 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader if row['Student ID'] == 'Student id']
        total = sum(int(row['Marks']) for row in data)
        return data, total

def calculate_course_data(course_id):
    with open('data.csv', 'r') as file:
        file.readline()
        reader = csv.DictReader(file)
        data = [row for row in reader if row['Course ID'] == course_id]
        marks = [int(row['Marks']) for row in data]
        if not marks:
            return 0, 0, None
        avg = math.ceil(sum(marks)/len(marks))
        max_marks = max(marks)
        return avg, max_marks, marks

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        id_type = request.form.get('ID')
        id_value = request.form.get('id_value').strip()
        
        if not id_type or not id_value:
            return render_template('error.html', message="Invalid input!")
            
        if id_type == 'student_id':
            data, total = calculate_student_data(id_value)
            if not data:
                return render_template('error.html', message="Student ID not found!")
            return render_template('student.html', 
                                 student_id=id_value,
                                 data=data,
                                 total=total)
                                 
        elif id_type == 'course_id':
            avg, max_marks, marks = calculate_course_data(id_value)
            if not marks:
                return render_template('error.html', message="Course ID not found!")
                
            # Generate histogram
            plt.hist(marks, bins=10, range=(0,100))
            plt.xlabel('Marks')
            plt.ylabel('Frequency')
            img_path = os.path.join(app.config['STATIC_FOLDER'], f'{id_value}.png')
            plt.savefig(img_path)
            plt.close()
            
            return render_template('course.html',
                                 course_id=id_value,
                                 avg=avg,
                                 max_marks=max_marks,
                                 img_path=f'images/{id_value}.png')
    
    return render_template('index.html')


app.run(debug=True)
