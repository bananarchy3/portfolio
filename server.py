from logging import FileHandler, WARNING
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='./template')
file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)


@app.route('/')
def home():
   return render_template('index.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return 'thanks fam'
        except:
            return 'did not save to database'
    else:
        return 'oh no something went wrong'


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=",", quotechar="'", lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
