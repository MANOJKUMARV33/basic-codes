
pip install pypng

pip install pyqrcode

import pyqrcode
import png
from pyqrcode import QRCode
s="https://www.instagram.com/_manu_v/"
url=pyqrcode.create(s)
url.png('myqr.png',scale=6)
