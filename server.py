from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)
print(app)

@app.route("/") 
def home():
    return render_template('index.html')

# @app.route("/index.html")
# def index():
#     return render_template('index.html')

# @app.route("/works.html")
# def works():
#     return render_template('works.html')

# @app.route("/about.html")
# def about():
#     return render_template('about.html')

# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')


@app.route("/<string:page_html>")
def page_name(page_html):
    return render_template(page_html)


def write_to_file(data):
    with open('database.txt', 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database:
        # When opening the CSV file, we added a new line after the headers already present.
        # Alterntively, use the .writeheader() method of the csv.writer below
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    # return 'Form submitted'
    if request.method == 'POST':
        try:
            # data = request.form['email']
            # data = request.form['message']
            # Grab all together in a dict:
            data = request.form.to_dict()
            # print(data)
            # return 'Form submitted'
            # write_to_file(data)
            write_to_csv(data)
            return redirect('./thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong'