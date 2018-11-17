import os

num = 54
num = str(num)

os.chdir('/home/user/Downloads/' + num)

f_list = os.listdir(os.getcwd())
f_list.sort()

for i in range(len(f_list)):
    old = f_list[i]
    new = 'conv' + num + '_d2_' + str(i+28) + '.png'
    os.rename(old, new)
    print (old, '===>', new)