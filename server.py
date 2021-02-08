from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
# print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('WebServer/database.txt', mode='a') as database:
        email = data["Email"]
        subject = data["Subject"]
        message = data["Message"]
        database.write(f'{email}, {subject}, {message}\n')

def write_to_csv(data):
    with open('WebServer/database.csv', mode='a', newline='') as database2:
        email = data["Email"]
        subject = data["Subject"]
        message = data["Message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database!'
    else:
        return 'Something went wrong!'