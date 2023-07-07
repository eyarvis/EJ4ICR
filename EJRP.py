import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

houston1 = pd.read_csv("RPCSV/CSVTables/Houston/Houston1.csv",header=1,index_col=0,skiprows=[2,3,4,5,6,7,8,9,10,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49])
houston2 = pd.read_csv("RPCSV/CSVTables/Houston/Houston2.csv",header=1,index_col=0,skiprows=[2,3,4,5,6,7,8,9,10,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49])
houston3 = pd.read_csv("RPCSV/CSVTables/Houston/Houston3.csv",header=1,index_col=0,skiprows=[2,3,4,5,6,7,8,9,10,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49])
houston4 = pd.read_csv("RPCSV/CSVTables/Houston/Houston4.csv",header=1,index_col=0,skiprows=[2,3,4,5,6,7,8,9,10,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49])
houston5 = pd.read_csv("RPCSV/CSVTables/Houston/Houston5.csv",header=1,index_col=0,skiprows=[2,3,4,5,6,7,8,9,10,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49])

detroit1 = pd.read_csv("RPCSV/CSVTables/Detroit/Detroit1.csv",header=1,index_col=0,skiprows=[2,3,4,5,6,7,8,9,10,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49])
detroit2 = pd.read_csv("RPCSV/CSVTables/Detroit/Detroit2.csv",header=1,index_col=0,skiprows=[2,3,4,5,6,7,8,9,10,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49])
detroit3 = pd.read_csv("RPCSV/CSVTables/Detroit/Detroit3.csv",header=1,index_col=0,skiprows=[2,3,4,5,6,7,8,9,10,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49])
detroit4 = pd.read_csv("RPCSV/CSVTables/Detroit/Detroit4.csv",header=1,index_col=0,skiprows=[2,3,4,5,6,7,8,9,10,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49])
detroit5 = pd.read_csv("RPCSV/CSVTables/Detroit/Detroit5.csv",header=1,index_col=0,skiprows=[2,3,4,5,6,7,8,9,10,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49])

portland1 = pd.read_csv("RPCSV/CSVTables/Portland/Portland1.csv",header=1,index_col=0,skiprows=[2,3,4,5,6,7,8,9,10,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49])
portland2 = pd.read_csv("RPCSV/CSVTables/Portland/Portland2.csv",header=1,index_col=0,skiprows=[2,3,4,5,6,7,8,9,10,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49])
portland3 = pd.read_csv("RPCSV/CSVTables/Portland/Portland3.csv",header=1,index_col=0,skiprows=[2,3,4,5,6,7,8,9,10,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49])
portland4 = pd.read_csv("RPCSV/CSVTables/Portland/Portland4.csv",header=1,index_col=0,skiprows=[2,3,4,5,6,7,8,9,10,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49])
portland5 = pd.read_csv("RPCSV/CSVTables/Portland/Portland5.csv",header=1,index_col=0,skiprows=[2,3,4,5,6,7,8,9,10,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49])

factorsCol = portland5["Category"]
variablesCol=portland5["Selected Variables"]

p1Tract= "41051009204"
p2Tract= "41051010602"
p3Tract= "41051007400"
p4Tract= "41051004700"
p5Tract= "41051000902"

h1Tract= "48201410102"
h2Tract= "48201411200"
h3Tract= "48201310500"
h4Tract= "48201310500"
h5Tract= "48201221301"

d1Tract= "26163519100"
d2Tract= "26163512800"
d3Tract= "26163531800"
d4Tract= "26163501500"
d5Tract= "26163535000"


p1value = portland1["Value"]
p2value = portland2["Value"]
p3value = portland3["Value"]
p4value = portland4["Value"]
p5value = portland5["Value"]

h1value = houston1["Value"]
h2value = houston2["Value"]
h3value = houston3["Value"]
h4value = houston4["Value"]
h5value = houston5["Value"]

d1value = detroit1["Value"]
d2value = detroit2["Value"]
d3value = detroit3["Value"]
d4value = detroit4["Value"]
d5value = detroit5["Value"]



table = {"Factors":factorsCol,"Variables":variablesCol,"P1":p1value,"P2":p2value,"P3":p3value,"P4":p4value,"P5":p5value,
         "H1":h1value,"H2":h2value,"H3":h3value,"H4":h4value,"H5":h5value,
         "D1":d1value,"D2":d2value,"D3":d3value,"D4":d4value,"d5":d5value}
table = pd.DataFrame(table)
print(table)

'''Print table with tract names
tableTract = {"Factors":factorsCol,"Variables":variablesCol,
         p1Tract:p1value,p2Tract:p2value,p3Tract:p3value,p4Tract:p4value,p5Tract:p5value,
         h1Tract:h1value,h2Tract:h2value,h3Tract:h3value,h4Tract:h4value,h5Tract:h5value,
         d1Tract:d1value,d2Tract:d2value,d3Tract:d3value,d4Tract:d4value,d5Tract:d5value}
tableTract = pd.DataFrame(tableTract)
print(tableTract)
'''

''''print every table seperatley
print("Houston 1")
print(houston1)
print("Houston 2")
print(houston2)
print("Houston 3")
print(houston3)
print("Houston 4")
print(houston4)
print("Houston 5")
print(houston5)

print("Detroit 1")
print(detroit1)
print("Detroit 2")
print(detroit2)
print("Detroit 3")
print(detroit3)
print("Detroit 4")
print(detroit4)
print("Detroit 5")
print(detroit5)

print("Portland 1")
print(portland1)
print("Portland 2")
print(portland2)
print("Portland 3")
print(portland3)
print("Portland 4")
print(portland4)
print("Portland 5")
print(portland5)

print(col)

'''



p1arr =np.array(p1value)
p2arr =np.array(p2value)
p3arr =np.array(p3value)
p4arr =np.array(p4value)
p5arr =np.array(p5value)

h1arr=np.array(h1value)
h2arr=np.array(h2value)
h3arr=np.array(h3value)
h4arr=np.array(h4value)
h5arr=np.array(h5value)

d1arr=np.array(d1value)
d2arr=np.array(d2value)
d3arr=np.array(d3value)
d4arr=np.array(d4value)
d5arr=np.array(d5value)
print(p1arr)
tractArr= [p1arr,p2arr,p3arr,p4arr,p5arr,h1arr,h2arr,h3arr,h4arr,h5arr,d1arr,d2arr,d3arr,d4arr,d5arr]

#plt.plot([p1arr[0],p2arr[0],p3arr[0],p4arr[0],p5arr[0]], [p1arr[1],p2arr[1],p3arr[1],p4arr[1],p5arr[1]],'ro')
#plt.axis([0, 20, 0, 70])
#plt.ylim([0,60])
#plt.xlim([0,20])
#plt.show()

plt.plot([tractArr[0]],[tractArr[1]])
plt.show()