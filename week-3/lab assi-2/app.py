import sys
import pandas as pd
import matplotlib.pyplot as plt

def generate_student_html(student_id):
    try:
        # Read the CSV file
        data = pd.read_csv('data.csv')
        # Strip spaces from column names (if any)
        data.columns = data.columns.str.strip()
    except FileNotFoundError:
        return generate_error_html("Error: 'data.csv' not found.")

    # Filter data for the given student ID
    student_data = data[data['Student id'] == int(student_id)]

    if student_data.empty:
        return generate_error_html(f"Error: Invalid Student ID {student_id}.")

    # Calculate total marks
    total_marks = student_data['Marks'].sum()

    # HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head><title>Student Details</title></head>
    <body>
        <h1>Student Details</h1>
        <table border="1">
            <tr>
                <th>Student ID</th>
                <th>Course ID</th>
                <th>Marks</th>
            </tr>
    """
    for _, row in student_data.iterrows():
        html_content += f"""
            <tr>
                <td>{row['Student id']}</td>
                <td>{row['Course id']}</td>
                <td>{row['Marks']}</td>
            </tr>
        """
    
    html_content += f"""
            <tr>
                <td colspan="2"><b>Total Marks</b></td>
                <td><b>{total_marks}</b></td>
            </tr>
        </table>
    </body>
    </html>
    """

    # Write to output.html
    with open('output.html', 'w') as f:
        f.write(html_content)

def generate_course_html(course_id):
    try:
        # Read the CSV file
        data = pd.read_csv('data.csv')
        # Strip spaces from column names (if any)
        data.columns = data.columns.str.strip()
    except FileNotFoundError:
        return generate_error_html("Error: 'data.csv' not found.")

    # Filter data for the given course ID
    course_data = data[data['Course id'] == int(course_id)]

    if course_data.empty:
        return generate_error_html(f"Error: Invalid Course ID {course_id}.")

    # Calculate average and maximum marks
    average_marks = course_data['Marks'].mean()
    max_marks = course_data['Marks'].max()

    # Generate HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head><title>Course Details</title></head>
    <body>
        <h1>Course Details</h1>
        <table border="1">
            <tr>
                <th>Average Marks</th>
                <th>Maximum Marks</th>
            </tr>
            <tr>
                <td>{average_marks:.2f}</td>
                <td>{max_marks}</td>
            </tr>
        </table>

        <!-- Histogram -->
        <img src="histogram.png" alt="Histogram of Marks">
    </body>
    </html>
    """

    # Write to output.html
    with open('output.html', 'w') as f:
        f.write(html_content)

    # Generate histogram
    plt.hist(course_data['Marks'], bins=10, color='blue', edgecolor='black')
    plt.title(f"Histogram of Marks for Course {course_id}")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    
    plt.savefig('histogram.png')
    plt.close()

def generate_error_html(error_message):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head><title>Error</title></head>
    <body>
        <h1>Error</h1>
        <p>{error_message}</p>
    </body>
    </html>
    """
    
    with open('output.html', 'w') as f:
        f.write(html_cbontent)

def main():
    if len(sys.argv) != 3:
        generate_error_html("Error: Invalid number of arguments.")
        return

    option = sys.argv[1]
    identifier = sys.argv[2]

    if option == '-s':
        generate_student_html(identifier)
    elif option == '-c':
        generate_course_html(identifier)
    else:
        generate_error_html("Error: Invalid option. Use '-s' for student or '-c' for course.")

if __name__ == "__main__":
    main()
