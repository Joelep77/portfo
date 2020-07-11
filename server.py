from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def initial():
    return render_template('index.html')


@app.route('/index.html')
def home():
    return render_template('index.html')


def save_contact(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def save_contact_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file2 = csv.writer(database2, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        file2.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_contact_csv(data)
    else:
        print('invalid data')

    return redirect('/index.html')
