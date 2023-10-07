from flask import Flask, render_template, jsonify, request
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

@app.route('/api/course', methods=['GET'])
def get_data():
    # ดึงข้อมูลจาก MongoDB
    data = list(db.course.find({}))

    # แปลงข้อมูลเป็นรูปแบบ JSON
    data_json = []
    for item in data:
        data_json.append({
            '_id': str(item['_id']),  # แปลง ObjectId เป็นสตริง
            'name_course': item['name_course'],
            'credit_course': item['credit_course']
            # เพิ่มฟิลด์อื่น ๆ ตามต้องการ
        })

    return jsonify(data_json)

@app.route('/api/minor', methods=['GET'])
def get_data_minor():
    # ดึงข้อมูลจาก MongoDB
    data = list(db.minor.find({}))

    # แปลงข้อมูลเป็นรูปแบบ JSON
    # data_json = []
    # for item in data:
    #     data_json.append({
    #         '_id': str(item['_id']),  # แปลง ObjectId เป็นสตริง
    #         'name_course': item['name_course'],
    #         'credit_course': item['credit_course']
    #         # เพิ่มฟิลด์อื่น ๆ ตามต้องการ
    #     })

    return jsonify(data)


# @app.route('/api/minor', methods=['GET'])
# def get_data():
#     # ดึงข้อมูลจาก MongoDB
#     data = list(db.minor.find({}))

#     # แปลงข้อมูลเป็นรูปแบบ JSON
#     data_json = []
#     for item in data:
#         data_json.append({
#             '_id': str(item['_id']),  # แปลง ObjectId เป็นสตริง
#             'faculty_name': item['faculty_name'],
#             'branch_name': item['branch_name'],
#             'year_active': item['year_active'],
#             'minor_subject': item['minor_subject'],
#             # เพิ่มฟิลด์อื่น ๆ ตามต้องการ
#         })

#     return jsonify(data_json)




@app.route('/api/saveCourse', methods=['POST'])
def save_course():
    # รับข้อมูลที่ส่งมาจากแอพพลิเคชัน (รหัสวิชา)
    data = request.json
    course_code = data.get('courseCode')

    # ตรวจสอบว่าข้อมูลถูกส่งมาหรือไม่
    if not course_code:
        return jsonify({'message': 'ไม่ได้ระบุรหัสวิชา'}), 400

    # ทำการบันทึกข้อมูลลงใน MongoDB
    # เงื่อนไขในการอัปเดต (ในที่นี้คุณอาจต้องเปลี่ยนตามต้องการ)
    filter_condition = {'_id': '030'}

    # ใช้ $push เพื่อเพิ่มรหัสวิชาในอาร์เรย์ วิชาเลือก
    update_query = {'$push': {'minor_subject.วิชาบังคับ.มีวิชา': course_code}}
    # db.aaa.insert_one({'_id': course_code})

    # ทำการอัปเดตเอกสารและสร้างหากไม่มีเอกสารที่ตรงกับเงื่อนไข
    db.minor.update_one(filter_condition, update_query, upsert=True)

    return jsonify({'message': 'บันทึกข้อมูลสำเร็จ'}), 200



@app.route('/api/saveCredit', methods=['POST'])
def save_credit():
    # รับข้อมูลที่ส่งมาจากแอพพลิเคชัน (รหัสวิชา)
    data = request.json
    course_code = data.get('courseCredit')

    # ตรวจสอบว่าข้อมูลถูกส่งมาหรือไม่
    if not course_code:
        return jsonify({'message': 'ไม่ได้ระบุหน่วยกิตวิชา'}), 400

    # กำหนดเงื่อนไขในการค้นหาเอกสารที่มี '_id' เท่ากับ '030'
    filter_condition = {'_id': '030'}

    # กำหนดข้อมูลที่จะใช้ในการอัปเดตหรือสร้างเอกสารใหม่
    update_data = {
        '_id': '030',  # ระบุ '_id' เพื่อหาเอกสารที่มีหรือสร้างใหม่
        'minor_subject': {
            'วิชาบังคับ': {
                'หน่วยกิตขั้นต่ำ': course_code
            }
        }
    }

    # ใช้คำสั่ง update_one เพื่ออัปเดตหรือสร้างเอกสารใน MongoDB
    db.minor.update_one(filter_condition, {'$set': update_data}, upsert=True)

    return jsonify({'message': 'บันทึกข้อมูลสำเร็จ'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
