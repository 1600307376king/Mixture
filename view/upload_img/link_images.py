from flask import Blueprint, request, render_template
import os
import time


images_index = Blueprint('image_page', __name__)


@images_index.route('/', methods=['POST', 'GET'])
def return_images():
    if request.method == 'POST':
        f = request.files.get('image')
        print(f)
        print(f.filename)
    # if f:
    #     image_name = f.filename.split('.')[0] + str(int(time.time())) + '.jpg'
    #     image_url = os.getcwd() + '/static/image/matplotlib/straight/' + image_name
    #     f.save(image_url)
    #     print(image_url)

    return render_template('./upload_img/index.html')


