import telnetlib
import time


HOST = "10.0.0.80"
user = "Admn"
password = "admn"

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"off .a5\n")
time.sleep(5)
tn.write(b"on .a5\n")
tn.write(b"exit\n")
print(tn.read_all().decode('ascii'))


