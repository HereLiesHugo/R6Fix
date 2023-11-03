import os
os.system("netsh interface teredo show state")
os.system("echo Disabling Teredo...")
os.system("netsh interface teredo set state disabled")
os.system("netsh interface teredo show state")
os.system("echo Flushing DNS...")
os.system("ipconfig /flushdns")
os.system("pause")