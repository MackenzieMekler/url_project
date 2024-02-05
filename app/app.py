from flask import Flask, request, redirect, render_template
import mysql.connector
import random
import datetime
import json


cnx = mysql.connector.connect(
                user="root",
                password="Insert Password Here",
                host="db",
                port="3306",
                database="urlshorten",
                auth_plugin='mysql_native_password'
)
cursor = cnx.cursor()


app = Flask(__name__)

add_link = ("INSERT INTO urlsh (url, code, day) VALUES ( %s, %s, %s)")
search_link = ("SELECT url, code FROM urlsh")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    date = datetime.date.today().strftime('%Y-%m-%d')
    rand = random.randint(10000, 99999)
    new_link = (request.form['url'], rand, date)
    cursor.execute(add_link, new_link)
    cnx.commit()
    return json.dumps({'message': 'added new link to db', 'link information': {'code': rand, 'url': request.form['url'], 'date': date}})

@app.route('/code/<code_ref>')
def reroute(code_ref):
    cursor.execute(search_link)
    for (url, code) in cursor:
        if code == code_ref:
            return redirect(url)
    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
