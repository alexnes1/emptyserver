""" Empty Server
A web server that accepts all kinds of URLs an arguments and prints gathered info
to response and stdout.
Can be used for testing and observing client behaviour.
"""
from flask import Flask, request
import datetime

version = "1.0"

app = Flask(__name__)
ALLOWED_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']

def dict_pprint(d):
    s = ""
    for k in sorted(d):
        s += "{}: {}\n".format(k, d.get(k))
    return s

@app.route('/', defaults={'path': ''}, methods=ALLOWED_METHODS)
@app.route('/<path:path>', methods=ALLOWED_METHODS)
def all(path):
    info = {
        'dt':       datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S.%f"),
        'req':      request.method,
        'url':      request.base_url,
        'cookie':   request.cookies,
        'headers':  request.headers,
        'from':     request.remote_addr,
    }

    info_str = "AT {i[dt]}\n"
    info_str += "{i[req]} request to {i[url]}\n"
    info_str += "FROM: {i[from]}\n\n"
    info_str += "=== ARGS ===\n{}=== ARGS END ===\n\n".format(dict_pprint(request.args))
    info_str += "=== DATA ===\n{}=== DATA END ===\n\n".format(dict_pprint(request.form))
    info_str += "=== HEADERS ===\n{i[headers]}\n=== HEADERS END===\n\n"

    info_str = info_str.format(i=info)
    print("\n" + "-" * 50 + "\n")
    print("\n\n{}\n".format(info_str))
    print("-" * 50 + "\n")
    return info_str

logo = r"""
  ___            _          ___                     
 | __|_ __  _ __| |_ _  _  / __|___ _ ___ _____ _ _ 
 | _|| '  \| '_ |  _| || | \__ / -_| '_\ V / -_| '_|
 |___|_|_|_| .__/\__|\_, | |___\___|_|  \_/\___|_|  
           |_|       |__/                           """
print("{} v{}".format(logo, version))