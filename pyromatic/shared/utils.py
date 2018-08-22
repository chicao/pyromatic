import json
import hashlib

def generate_key(**kwargs):
    return hashlib.md5(json.dumps(kwargs, sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest()
