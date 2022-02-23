@echo off

"C:\Program Files\TightVNC\tvnserver.exe" -stop
"C:\Program Files (86)\TightVNC\tvnserver.exe" -stop
reg add "HKLM\SOFTWARE\TightVNC\Server" /v Password /t REG_BINARY /d %1 /f
reg add "HKLM\SOFTWARE\TightVNC\Server" /v ControlPassword /t REG_BINARY /d %1 /f
reg add "HKLM\SOFTWARE\TightVNC\Server" /v UseVncAuthentication /t REG_DWORD /d 0x1 /f
"C:\Program Files\TightVNC\tvnserver.exe" -start
"C:\Program Files (86)\TightVNC\tvnserver.exe" -start