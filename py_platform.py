#To get the system info
import platform

platform.mac_ver()
a = platform.architecture()
print  a[0]
b = platform.dist(distname='2', version='1', id='5')
print b
c = platform.version()
print c
d = platform.system()
print d

