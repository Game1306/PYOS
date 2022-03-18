import os, socket

login_pass = open('user/password.pass')
login_name = open('user/dataname.pass')
l_p = login_pass.read()
l_n = login_name.read()


def BIOS():
	while True:
		b_login = input(str("Please Enter The Password To " + l_n + " To Open BioS: "))
		if b_login == l_p:
			print("Opening BioS")
			host_name = socket.gethostname()
			host_ip = socket.gethostbyname(host_name)
			print("[1] USER NAME: " + l_n)
			print("[2] PASSWORD: " + l_p)
			print("[3] DELETE " + l_n)
			print("Hostname:", host_name)
			print("LOCAL IPS: " + host_ip)
			edit_b = input("Enter [?] to change setting: ")
			if edit_b == '1':
				edit_n = input("Enter New Username: ")
				with open('user/dataname.pass', 'w') as f:
					f.writelines(edit_n)
				print("Username Changed To " + edit_n)
				input("Press Enter To Restart: ")
				os.startfile('home.py')
				os.system('exit')
			elif edit_b == '2':
				edit_p = input("Enter New Password: ")
				with open('user/password.pass', 'w') as f:
					f.writelines(edit_p)

				print("Password Changed To " + edit_p)
				input("Press Enter To Restart: ")
				os.startfile('home.py')
				os.system('exit')
			elif edit_b == '3':
				delete_a = input("Are you sure? Y/N: ")
				if delete_a == "y" or delete_a == "Y":
					os.system('exit')
					with open('user/info.data', 'w') as f:
						f.writelines("0")
					os.startfile("setup.pyw")
				else:
					os.system('exit')
					os.startfile("home.py")
			else:
				print("Wrong Password To " + l_n)

	else:
		print("Wrong Password To " + l_n)

BIOS()
