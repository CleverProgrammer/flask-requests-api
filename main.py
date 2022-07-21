from flask import Flask, render_template
import requests
import json
from replit import db

if 'page_visits' not in db:
  db['page_visits'] = 0

# counter app
# guess the number
# tip calculator
# rock paper scissors (database)

app = Flask('app')
@app.route('/')
def hello_world():
  response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
  data = response.json()
  db['page_visits'] += 1
  return render_template('index.html', data=data, page_visits=db['page_visits'])

app.run(host='0.0.0.0', port=8080)
