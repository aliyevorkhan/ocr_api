import requests
import base64
import sys

r = requests.post('http://127.0.0.1:8000/ocr/', json={"data": base64.b64encode(open(sys.argv[1], 'rb').read())})

print(r.json())