from flask import Flask, request, render_template
from view.link_images import images_index


app = Flask(__name__)
app.config.from_pyfile('./config/setting.py')

app.register_blueprint(images_index, url_prefix='')

# http://fw.newlifehealth.cn:8099/pp/?enc=58918e22003003000003


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8099)
