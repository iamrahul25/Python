import os

def find_pass(wifi):

    data=os.popen("""netsh wlan show profile name="%s" key=clear"""%(wifi,)).readlines()
    #print(data,type(data))

    password=''
    
    for i in data:
        if i[0:29]=="    Key Content            : ":
            password=i[29:-1]
         
    return password


L1=[]
wifi_names=[]

data=os.popen("netsh wlan show profile").readlines()
#print(data,"\n Length:",len(data))


for i in data:
    if i[0:27]=="    All User Profile     : ":
        L1.append(i)
#print(L1)

for j in L1:
    L2=j.split(': ')
    #print(L2)
    wifi_names.append(L2[1][:-1])

#print(wifi_names)

print("S.N:   Wifi names:   Password:")

c=0
for z in wifi_names:
    c=c+1
    print(c,'.   ',z,'    -     ',find_pass(z))





