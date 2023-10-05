from flask import Flask, render_template, jsonify
import pymongo
from pymongo import MongoClient




app = Flask(__name__)


#Database
client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                        authSource="admin")
db = client["test_db"]

@app.route('/')
def index():
    # Retrieve data from MongoDB (you can modify this part according to your needs)
    data = db.mycollection.find()
    return render_template('index.html', data=data)

@app.route('/api/data', methods=['GET'])
def get_data():
    # ดึงข้อมูลจาก MongoDB
    data = list(db.minor.find({}))

    # แปลงข้อมูลเป็นรูปแบบ JSON
    data_json = []
    for item in data:
        data_json.append({
            '_id': str(item['_id']),  # แปลง ObjectId เป็นสตริง
            'first_name': item['first_name'],
            'last_name': item['last_name']
            # เพิ่มฟิลด์อื่น ๆ ตามต้องการ
        })

    return jsonify(data_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
