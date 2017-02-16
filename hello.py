import requests
from flask import Flask
from flask import render_template

from jinja2 import Template

app = Flask(__name__)

@app.route("/")
def hello():
    url = 'https://www.opm.gov/json/operatingstatus.json'
    r = requests.get(url)

    data = r.json()
    # data['StatusType'] = 'Closed'
    if data.get('StatusType', None) == 'Open':
        data['background'] = 'red'
    else:
        data['background'] = 'green'


    return render_template('opm.html', **data)
if __name__ == "__main__":
    app.run(debug=True)
