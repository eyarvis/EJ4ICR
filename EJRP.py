import pandas as pd

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

''''
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