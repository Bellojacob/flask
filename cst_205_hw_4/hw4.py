"""
NAME: Jacob Bello
DATE: 7/7/2024
CLASS: CST 205
flask --app hw4 --debug run
"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
import os, random
from image_info import image_info
from PIL import Image


my_info = image_info
random.shuffle(my_info)
# for i in my_info:
#     print(i, '\n')



# print(image_info)

app = Flask(__name__)
bootstrap = Bootstrap5(app)

def image_prop(img_path):
    with Image.open(img_path) as img:
        return f'{img.mode} image in {img.format} format with width {img.width} and height {img.height}'

@app.route('/')
def index():
    random.shuffle(my_info)
    imgs_sel = my_info[:3]
    return render_template('index.html', imgs_sel=imgs_sel)

@app.route('/detail/<id>/<title>/<author>')
def detail(id, title, author):
    print("My image is: " r"cst_205_hw_4/static/images/"+id+".jpg")
    img_prop = image_prop(r"C:\Users\jacob\cst_205\flask\cst_205_hw_4\static\images\\" + id + ".jpg")
    return render_template('detail.html', id=id, title=title, author=author, img_prop=img_prop)


        