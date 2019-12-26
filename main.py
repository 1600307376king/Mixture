from flask import Flask
from fw_api.view.link_images import images_index
from fw_api.view.site_rediect import fw_index


app = Flask(__name__)
app.config.from_pyfile('./config/setting.py')

app.register_blueprint(images_index, url_prefix='')
app.register_blueprint(fw_index, url_prefix='')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8099)
