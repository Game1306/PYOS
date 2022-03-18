import os

data_info = open('user/info.data')
data = data_info.read()

if data == '0':
	os.startfile("setup.pyw")
elif data == '1':
	os.startfile("login.pyw")