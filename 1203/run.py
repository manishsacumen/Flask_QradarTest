from app.qpylib import qpylib
from app import app
from app.flask_keys import get_flask_keys

qpylib.create_log()
qpylib.register_jsonld_endpoints()

app.config.from_mapping(
    SECRET_KEY=get_flask_keys()['secret_key'],
)

app.run(host='0.0.0.0')


