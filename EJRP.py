import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations
from scipy.stats import pearsonr
import sys
import seaborn as sns

cities = ['Houston', 'Detroit', 'Portland']
datasets = ['1', '2', '3', '4', '5']#in string form
newDataSets = [ 1, 2, 3, 4, 5]#in num form

# Create a dictionary to store the data
data = {}#this is where all the cities data will be stored
valueData={}#this is where the value column for all the cities data will be stored
# Loop through cities and datasets
for city in cities:#this defines data and makes it useable
    city_data = []
    for dataset in datasets:
        file_path = f"RPCSV/CSVTables/{city}/{city}{dataset}.csv"
        df = pd.read_csv(file_path, header=1, index_col=0, skiprows=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49])
        city_data.append(df)
    data[city] = city_data

    #print("HERE")
    #print(data)


for city in cities:#this defines valueData and makes it useable as an array of the cities "Value" values
    tractData = []
    for i in newDataSets:
        var = (data[city][i-1])["Value"]
        toAppend = np.array(var)
        tractData.append(toAppend)
    valueData[city]=tractData




'''''#old way of doing something
houston1 = data['Houston'][0]
houston2 = data['Houston'][1]
houston3 = data['Houston'][2]
houston4 = data['Houston'][3]
houston5 = data['Houston'][4]

portland1 = data['Portland'][0]
portland2 = data['Portland'][1]
portland3 = data['Portland'][2]
portland4 = data['Portland'][3]
portland5 = data['Portland'][4]

detroit1 = data['Detroit'][0]
detroit2 = data['Detroit'][1]
detroit3 = data['Detroit'][2]
detroit4 = data['Detroit'][3]
detroit5 = data['Detroit'][4]
'''



test = data['Portland'][4]
factorsCol = test["Category"]
variablesCol = test["Selected Variables"]


''''#tract names
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
'''

'''''#old p1value declaration
p1value = (data['Portland'][0])["Value"]
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
'''

'''#old table
table = {"Factors":factorsCol,"Variables":variablesCol,"P1":p1value,"P2":p2value,"P3":p3value,"P4":p4value,"P5":p5value,
         "H1":h1value,"H2":h2value,"H3":h3value,"H4":h4value,"H5":h5value,
         "D1":d1value,"D2":d2value,"D3":d3value,"D4":d4value,"d5":d5value}
table = pd.DataFrame(table)
print(table)
'''

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


'''old arrays for all the cities
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
'''



#creates array that holds all the different tracts and factors in one table
###tractArr=np.array([p1value,p2value,p3value,p4value,p5value,h1value,h2value,h3value,h4value,h5value,d1value,d2value,d3value,d4value,d5value])
arr=[]
for city in cities:
    for i in newDataSets:
        arr.append(valueData[city][i-1])

tractArr=np.array(arr)
print("HELOOLOLO")
print(tractArr)

#creates pretty data frame for that table
tractdf = pd.DataFrame(tractArr, columns = ['Factor 1','Factor 2','Factor 3','Factor 4','Factor 5',
                                            'Factor 6','Factor 7','Factor 8','Factor 9','Factor 10',
                                            'Factor 11','Factor 12','Factor 13','Factor 14','Factor 15',
                                            'Factor 16','Factor 17','Factor 18','Factor 19','Factor 20',])

dFactorDict = ['Factor 14','Factor 15','Factor 16','Factor 17','Factor 18','Factor 19','Factor 20']
for d in dFactorDict:#gets rid of the percentages and changes percent in dfactors to decimals
    tractdf[d]=tractdf[d].str.rstrip("%").astype(float)/100


print("TRACTDF")
print(tractdf)


#Enviormental Factors
factor1 = np.array(tractdf['Factor 1'],dtype=float)
factor2 = np.array(tractdf['Factor 2'],dtype=float)
factor3 = np.array(tractdf['Factor 3'],dtype=float)
factor4 = np.array(tractdf['Factor 4'],dtype=float)
factor5 = np.array(tractdf['Factor 5'],dtype=float)
factor6 = np.array(tractdf['Factor 6'],dtype=float)
factor7 = np.array(tractdf['Factor 7'],dtype=float)
factor8 = np.array(tractdf['Factor 8'],dtype=float)
factor9 = np.array(tractdf['Factor 9'],dtype=float)
factor10 = np.array(tractdf['Factor 10'],dtype=float)
factor11 = np.array(tractdf['Factor 11'],dtype=float)
factor12 = np.array(tractdf['Factor 12'],dtype=float)
factor13 = np.array(tractdf['Factor 13'],dtype=float)

#these ones are the percent and thus the Demographic Factors
factor14 = np.array(tractdf['Factor 14'],dtype=float)
factor15 = np.array(tractdf['Factor 15'],dtype=float)
factor16 = np.array(tractdf['Factor 16'],dtype=float)
factor17 = np.array(tractdf['Factor 17'],dtype=float)
factor18 = np.array(tractdf['Factor 18'],dtype=float)
factor19 = np.array(tractdf['Factor 19'],dtype=float)
factor20 = np.array(tractdf['Factor 20'],dtype=float)

factorArr = np.array([factor1,factor2,factor3,factor4,factor5,factor6,factor7,factor8,factor9,factor10,factor11,factor12,factor13,factor14,factor15,factor16,factor17,factor18,factor19,factor20])
#stores only the enviormental factor data
enviormentalFactorArr = np.array([factor1,factor2,factor3,factor4,factor5,factor6,factor7,factor8,factor9,factor10,factor11,factor12,factor13,])
#stores only the demographic data
demographicFactorArr = np.array([factor14,factor15,factor16,factor17,factor18,factor19,factor20])

'''#playing with plotting
x=factor1
y=factor16
plt.plot(x,y,'ro')
#plt.show()
'''#################################



pearsonCorrelationResults = []

#combinations between the two sets #the number of combinations between the 2 sets is 91

#when paired efactor and dfactor hold the correspondindg pairs of combinations
efactor=[]#holds the index of the factor data set in enviormentalFactoArr 
dfactor=[]#holds the index of the factor data set in demographicFactoArr
for i in range(0,13):#adds all combinations to the lists to be used to find r later
    for j in range(0,7):
        efactor.append(i)
        dfactor.append(j)
        #print(i,',',j)



#gets r for all combinations and prints
for i in range(0,91):
    
    x=efactor[i]
    y=dfactor[i]
    p,_=pearsonr(enviormentalFactorArr[x],demographicFactorArr[y])
    pearsonCorrelationResults.append(p)
    #print(i,': ',x,',',y,':',p)
    #print('Pearsons correlation: %.3f' % p)

#print(pearsonCorrelationResults)
#print(enviormentalFactorArr)
#need to make a table of the data and the corresponding factors to coefficients and stuff
#df['column_name']=pd.Series(arr)

#creates the df to display all the r values 
correlationdf = pd.DataFrame(columns=(['e#','d#','r']))
correlationdf['e#']=pd.Series(efactor)
correlationdf['d#']=pd.Series(dfactor)
correlationdf['r']=pd.Series(pearsonCorrelationResults)

#print(correlationdf)
#print(variablesCol)
variables = np.array(variablesCol)
efactorName= []
dfactorName= []

for i in range(0,13):
    efactorName.append(variables[i])
    print(i)

for i in range(0,7):
    dfactorName.append(variables[13+i])
    print(i)


efactorNameFinal = []
dfactorNameFinal = []

for i in range(0,91):
    efactorNameFinal.append(efactorName[efactor[i]])
    dfactorNameFinal.append(dfactorName[dfactor[i]])


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows',None)
#pd.set_option('display.max_rowwidth',None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

#creating new df to display correlation stuff
correlationdf = pd.DataFrame(columns=(['E#','Enviormental Factor','D#','Demographic Factor','r']))
correlationdf['E#']=pd.Series(efactor)
correlationdf['D#']=pd.Series(dfactor)
correlationdf['Enviormental Factor']=pd.Series(efactorNameFinal)
correlationdf['Demographic Factor']=pd.Series(dfactorNameFinal)
correlationdf['r']=pd.Series(pearsonCorrelationResults)
print(correlationdf)

#Creating new df to display correlation stuff in matrix form
