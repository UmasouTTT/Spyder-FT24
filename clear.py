fout1 = open('FT24-20180207-00h.txt','r')
mid = []
allKey = []
data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
data6 = []
data7 = []

data12 = {}
data22 = {}
data32 = {}
data42 = {}
data52 = {}
data62 = {}
data72 = {}


for line in fout1:
    line = str(line).replace('\n','')
    if line not in data1:
        data1.append(line)
        mid = line.split(',')
        if mid[1] not in allKey:
            allKey.append(mid[1])

fout2 = open('FT24-20180208-00h.txt','r')
data2 = []
for line in fout2:
    line = str(line).replace('\n','')
    if line not in data2:
        data2.append(line)
        mid = line.split(',')
        if mid[1] not in allKey:
            allKey.append(mid[1])

fout3 = open('FT24-20180209-00h.txt','r')
data3 = []
for line in fout3:
    line = str(line).replace('\n','')
    if line not in data3:
        data3.append(line)
        mid = line.split(',')
        if mid[1] not in allKey:
            allKey.append(mid[1])

fout4 = open('FT24-20180210-00h.txt','r')
data4 = []
for line in fout4:
    line = str(line).replace('\n','')
    if line not in data4:
        data4.append(line)
        mid = line.split(',')
        if mid[1] not in allKey:
            allKey.append(mid[1])

fout5 = open('FT24-20180211-00h.txt','r')
data5 = []
for line in fout5:
    line = str(line).replace('\n','')
    if line not in data5:
        data5.append(line)
        mid = line.split(',')
        if mid[1] not in allKey:
            allKey.append(mid[1])

fout6 = open('FT24-20180212-00h.txt','r')
data6 = []
for line in fout6:
    line = str(line).replace('\n','')
    if line not in data6:
        data6.append(line)
        mid = line.split(',')
        if mid[1] not in allKey:
            allKey.append(mid[1])


fout7 = open('FT24-20180213-00h.txt','r')
data7 = []
for line in fout7:
    line = str(line).replace('\n','')
    if line not in data7:
        data7.append(line)
        mid = line.split(',')
        if mid[1] not in allKey:
            allKey.append(mid[1])


print len(allKey)






result = open('result.txt','a')

for planeCode in allKey:
    result.write(str(planeCode) + ':')
    for couple in data1:
        if planeCode in couple:
            mid = str(couple).split(',')
            result.write(str('(0205)') + str(mid[0]) + ';')

    for couple in data2:
        if planeCode in couple:
            mid = str(couple).split(',')
            result.write(str('(0206)') + str(mid[0]) + ';')

    for couple in data3:
        if planeCode in couple:
            mid = str(couple).split(',')
            result.write(str('(0207)') + str(mid[0]) + ';')

    for couple in data4:
        if planeCode in couple:
            mid = str(couple).split(',')
            result.write(str('(0208)') + str(mid[0]) + ';')

    for couple in data5:
        if planeCode in couple:
            mid = str(couple).split(',')
            result.write(str('(0209)') + str(mid[0]) + ';')

    for couple in data6:
        if planeCode in couple:
            mid = str(couple).split(',')
            result.write(str('(0210)') + str(mid[0]) + ';')

    for couple in data7:
        if planeCode in couple:
            mid = str(couple).split(',')
            result.write(str('(0211)') + str(mid[0]) + ';')

    result.write('\n')

