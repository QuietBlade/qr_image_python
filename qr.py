#coding=utf-8
#python 3.6.5
#from MyQR import myqr #不支持中文
import qrcode
from PIL import Image
from PIL import ImageGrab
from pyzbar.pyzbar import decode
import time #控制文件名
import pyperclip #剪切板控制

def convert_qr(text):
	file_name = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
	file_dir = 'D:/' # 存储文件的路径
	file_type = ".jpg"
	qr = qrcode.QRCode(
		version=6,
		error_correction=qrcode.constants.ERROR_CORRECT_L,
		box_size=10,
		border=4,
	)
	qr.add_data(text)
	qr.make(fit=True)
	img = qr.make_image(fill_color="black", back_color="white")
	img.save(file_dir+file_name+file_type)
	img.show() #调用默认图片显示，建议安装

def conv_code(img): #二维码转换文字
	qrcode = decode(img)
	qrcode = qrcode[0].data.decode("utf-8")
	print(qrcode)
	pyperclip.copy(qrcode)
	#解析二维码


if __name__ == '__main__':
	types = ImageGrab.grabclipboard()
	if(types == None):
		convert_qr(pyperclip.paste()) #文字转QR
	else:
		conv_code(types) #QR转文字
	