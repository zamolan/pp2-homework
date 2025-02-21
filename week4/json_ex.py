import json

with open('C:\KBTU\pp2\week4\sample-data.json', 'r') as file:
    data = json.load(file)

print('Interface Status')
print('=' * 80)
print('DN', ' '*47, 'Description', ' '*9, 'Speed', ' ', 'MTU')
print('-'*50, '-'*20, '', '-'*6, '', '-'*6)
for imdata in data['imdata']:
    for i in imdata:
        for j in imdata[i]:
            print(imdata[i][j]['dn'], ' '*28, imdata[i][j]['speed'], '', imdata[i][j]['mtu'])