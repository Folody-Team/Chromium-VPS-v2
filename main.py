import os
os.system("pip install selenium==3.141.0")
from webbot import Browser
web = Browser()
web.go_to('https://folody.tk')
website = input('Trang web có hỗ trợ Âm thanh')
