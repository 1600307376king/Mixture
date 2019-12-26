from flask import request, render_template, Blueprint


fw_index = Blueprint('fw_page', __name__)


@fw_index.route('/pp/')
def fw_site_redirect():
    enc_value = request.args.get('enc', '')

    filter_obj = 'http://fw.newlifehealth.cn:8099/pp/?enc=' + str(enc_value)
    return render_template('jump.html', url=filter_obj)
