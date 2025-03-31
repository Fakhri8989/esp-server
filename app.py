from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to your Flask server!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
from flask import Flask, request, send_file
import os

app = Flask(__name__)

# مسیر برای آپلود تصاویر
@app.route('/upload', methods=['POST'])
def upload_image():
    # دریافت داده‌های تصویر از ESP8266 و ذخیره به عنوان فایل
    image = request.data
    with open('latest_image.jpg', 'wb') as f:
        f.write(image)
    return "Image received!", 200

# مسیر برای نمایش تصویر آپلود شده
@app.route('/view', methods=['GET'])
def view_image():
    # بررسی وجود فایل تصویر و ارسال آن به کاربر
    if os.path.exists('latest_image.jpg'):
        return send_file('latest_image.jpg', mimetype='image/jpeg')
    else:
        return "No image found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)