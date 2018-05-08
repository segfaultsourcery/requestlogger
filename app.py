from datetime import datetime
from json import dumps
from pprint import pprint
from threading import Lock

from flask import Flask, request, g, abort

app = Flask(__name__)


def get_lock():
    """Obtain a lock that should be shared between all running instances this app."""
    g._log_lock = getattr(g, '_log_lock', Lock())
    return g._log_lock


def write_log(data: dict):
    """Write a log message to a file."""
    with get_lock(), open('/log/log.txt', 'a+') as log:
        log.write(dumps(data) + '\n')


@app.route('/')
@app.route('/<path:path>')
def landing(path=None):
    """
    This is the landing page of our little logger.
    It gathers up some information and logs it, then returns a 404.
    """

    now = datetime.now().isoformat()

    data = {
        'time': now,
        'path': f'/{path}',
        'request': {
            'base_url': request.base_url,
            'remote_addr': request.remote_addr,
            'data': request.data.decode(),
            'args': dict(request.args),
            'form': dict(request.form),
            'files': dict(request.files),
            'method': request.method,
            'cookies': request.cookies,
        }
    }

    write_log(data)
    pprint(data)
    print(flush=True)

    # Let's just tell the offender that the resource was unavailable.
    abort(404)


if __name__ == '__main__':
    app.run(debug=True)
