import sys
input = sys.stdin.readline

# 문제 1
email1 = "cherry1004@gmail.com"
email2 = "cherry01@gmail.com"
email3 = "cherry0@gmail.com"
print(email1[0:10],email2[0:8],email3[0:7],sep = '\n')

# 문제 2
site1 = "www.nave.com"
site2 = "www.daum.net"
site3 = "www.google.com"
domain1 = site1.split('.')[1]
domain2 = site2.split('.')[1]
domain3 = site3.split('.')[1]
print(domain1,domain2,domain3,sep = '\n')