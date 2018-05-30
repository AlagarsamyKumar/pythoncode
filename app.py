import requests
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from config import Configuration

# create Flask app
app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)

# GET request to ip.jsontest.com
def home():
    # My microservice!
    return render_template('home.html')

def rest_request_example():
    print (requests.get("http://ip.jsontest.com/").text)
    print(requests.get("http://129.157.179.180:3000/reactorCore/320/650/blue/AlagarsamyKumar").text)
  #  for (i=0; i <=10; i++):
    for i in range(10):
        print(requests.get("http://129.157.179.180:3000/fighters/45/" + str(i) + "/blue/AlagarsamyKumar").text)
			   

def read_db_SQL_example():
    conn = db.get_engine().connect()
    sql = "SELECT * FROM SecretTable"
    results = conn.execute(sql)
    rows = ""
    for row in results:
        rows = rows + ','.join(row) + "<br/>"
    print(rows)
	
rest_request_example()
try:
	read_db_SQL_example()
except:
	print ('Could not connect to database')
	
if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])
