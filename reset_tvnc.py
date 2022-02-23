#!/usr/bin/env python2

import sys,os

TightVNC = r"C:\PROGRA~1\TightVNC\tvnserver.exe" or r"C:\PROGRA~2\TightVNC\tvnserver.exe"

def reset(password = None):
	if not password:
		password = raw_input("PASSWORD: ")
	import vncpasswd
	hexpasswd = password.encode('hex')
	crypted = vncpasswd.do_crypt(password, False)
	# crypted = crypted.encode('hex')
	print("\n")
	print("  [*] TightVNC password has been reset to: %s == %s"%(password, crypted.encode('hex')))
	os.system(TightVNC + " -stop")
	os.system(r'reg add "HKLM\SOFTWARE\TightVNC\Server" /v Password /t REG_BINARY /d {} /f'.format(crypted.encode('hex')))
	os.system(r'reg add "HKLM\SOFTWARE\TightVNC\Server" /v ControlPassword /t REG_BINARY /d {} /f'.format(crypted.encode('hex')))
	os.system(r'reg add "HKLM\SOFTWARE\TightVNC\Server" /v UseVncAuthentication /t REG_DWORD /d 0x1 /f')
	os.system(TightVNC + " -start")

# tvnserver.exe -stop
# reg add "HKLM\SOFTWARE\TightVNC\Server" /v Password /t REG_BINARY /d F0E43164F6C2E373 /f
# reg add "HKLM\SOFTWARE\TightVNC\Server" /v UseVncAuthentication /t REG_DWORD /d 0x1 /f
# tvnserver.exe -start

if __name__ == '__main__':
	if len(sys.argv) == 1:
		print("\n")
		print("\tUSAGE: {} PASSWORD_TO_CHANGE".format(os.path.basename(__file__)[:-3]))
	else:
		reset(sys.argv[1])
