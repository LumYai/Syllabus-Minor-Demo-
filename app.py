from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://mongodb:27017/')
db = client.mydatabase

@app.route('/')
def index():
    # Retrieve data from MongoDB (you can modify this part according to your needs)
    data = db.mycollection.find()
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
