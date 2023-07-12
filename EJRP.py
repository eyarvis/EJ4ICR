import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations
from scipy.stats import pearsonr
import sys
import seaborn as sb

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows',None)
#pd.set_option('display.max_rowwidth',None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

eLabel = ['PM 2.5','Ozone(ppb)','Diesel PM (ug/m3)','Cancer Risk','Resp. Hazard Index','Toxic Releases To Air','Traffic(prox. & vol.)',
          'Lead Paint Indicator','Superfund Prox.','RMP Prox.','Hazardous Waste Prox.','Underground Storage Tank Indicator','Waste Water Discharge Indicator']
dLabel =['Demo. Index','Supp. Demo. Index ','POC Pop.','Low Income Pop.','Unemployed','Low English Household','Pop. w/ < HS Ed.']

cities = ['Portland', 'Houston', 'Detroit']
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




#creates array that holds all the different tracts and factors in one table
###tractArr=np.array([p1value,p2value,p3value,p4value,p5value,h1value,h2value,h3value,h4value,h5value,d1value,d2value,d3value,d4value,d5value])
arr=[]

factorDataPerCity = {}
for city in cities:
    specificCityFactorData = []
    for i in newDataSets:
        arr.append(valueData[city][i-1])
        specificCityFactorData.append(valueData[city][i-1])
    factorDataPerCity[city]=specificCityFactorData

tractArr=np.array(arr)


#creates pretty data frame for that table

cityDataFrames = {}
#creates data frame for all tracts factors
tractdf = pd.DataFrame(tractArr, columns = ['Factor 1','Factor 2','Factor 3','Factor 4','Factor 5',
                                            'Factor 6','Factor 7','Factor 8','Factor 9','Factor 10',
                                            'Factor 11','Factor 12','Factor 13','Factor 14','Factor 15',
                                            'Factor 16','Factor 17','Factor 18','Factor 19','Factor 20',])


for city in cities:#creates data frame for one cities tract factors
    df =pd.DataFrame(factorDataPerCity[city], columns = ['Factor 1','Factor 2','Factor 3','Factor 4','Factor 5',
                                            'Factor 6','Factor 7','Factor 8','Factor 9','Factor 10',
                                            'Factor 11','Factor 12','Factor 13','Factor 14','Factor 15',
                                            'Factor 16','Factor 17','Factor 18','Factor 19','Factor 20',])
    cityDataFrames[city]=df
    
    


dFactorDict = ['Factor 14','Factor 15','Factor 16','Factor 17','Factor 18','Factor 19','Factor 20']
eFactorDict = ['Factor 1','Factor 2','Factor 3','Factor 4','Factor 5','Factor 6','Factor 7','Factor 8','Factor 9','Factor 10','Factor 11','Factor 12','Factor 13']


for d in dFactorDict:#gets rid of the percentages and changes percent in dfactors to decimals
    tractdf[d]=tractdf[d].str.rstrip("%").astype(float)/100
    for city in cities:
        df = cityDataFrames[city]
        df[d]=df[d].str.rstrip("%").astype(float)/100
        #houstondf[d]=houstondf[d].str.rstrip("%").astype(float)/100
        #detroitdf[d]=detroitdf[d].str.rstrip("%").astype(float)/100

print("PORTLAND")
print(cityDataFrames['Portland'])
#Enviormental Factors
factorArrDict = {}

for e in eFactorDict:
    factorArrDict[e] = np.array(tractdf[e],dtype=float)

for d in dFactorDict:
    factorArrDict[d] = np.array(tractdf[d],dtype=float)


#factorArr = np.array([factor1,factor2,factor3,factor4,factor5,factor6,factor7,factor8,factor9,factor10,factor11,factor12,factor13,factor14,factor15,factor16,factor17,factor18,factor19,factor20])
#testFactorArr =[factor1,factor2,factor3,factor4,factor5,factor6,factor7,factor8,factor9,factor10,factor11,factor12,factor13,factor14,factor15,factor16,factor17,factor18,factor19,factor20] 


#stores only the enviormental factor data
eConvertArr = []
for e in eFactorDict:
   eConvertArr.append(factorArrDict[e])
enviormentalFactorArr = np.array(eConvertArr)

#stores only demographic factor data
dConvertArr = []
for d in dFactorDict:
    dConvertArr.append(factorArrDict[d])
demographicFactorArr = np.array(dConvertArr)


#factordf = pd.DataFrame(columns=(['e#','d#','r']))

corrFactorAll = tractdf.corr()#also a perfectly good representation of the correlation coefficient between ALL factors
#print("CORRRRERER")
#print(corrFactor)
#plot all individual cities

#dataplot = sb.heatmap(corrFactorAll,annot=True,linewidths=0.5, linecolor='white')

#plt.show()



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



#creates the df to display all the r values 
correlationdf = pd.DataFrame(columns=(['e#','d#','r']))
correlationdf['e#']=pd.Series(efactor)
correlationdf['d#']=pd.Series(dfactor)
correlationdf['r']=pd.Series(pearsonCorrelationResults)


variables = np.array(variablesCol)
efactorName= []
dfactorName= []

for i in range(0,13):
    efactorName.append(variables[i])
    

for i in range(0,7):
    dfactorName.append(variables[13+i])
    


efactorNameFinal = []
dfactorNameFinal = []

for i in range(0,91):
    efactorNameFinal.append(efactorName[efactor[i]])
    dfactorNameFinal.append(dfactorName[dfactor[i]])



#creating new df to display correlation stuff
correlationdf = pd.DataFrame(columns=(['E#','Enviormental Factor','D#','Demographic Factor','r']))
correlationdf['E#']=pd.Series(efactor)
correlationdf['D#']=pd.Series(dfactor)
correlationdf['Enviormental Factor']=pd.Series(efactorNameFinal)
correlationdf['Demographic Factor']=pd.Series(dfactorNameFinal)
correlationdf['r']=pd.Series(pearsonCorrelationResults)
print(correlationdf)



#Creating new df to display correlation stuff in matrix form
'''''Seaborn Heat Map That Doesnt Really Work
efactorData = []
totalCount=0
for i in range(0,13):
    d = []
    for j in range(0,7):
        d.append(pearsonCorrelationResults[totalCount])
        totalCount = totalCount+1
    efactorData.append(d)
        
    


matrixCorr = pd.DataFrame()
matrixCorr['Demographic Factors'] = pd.Series(dLabel)
for i in range(0,13):
    matrixCorr[eLabel[i]] = pd.Series(efactorData[i])


print(matrixCorr)
'''
################################################################################################
#Creating heatmaps of all diff cities

''''Heres how the below works
##############################################################
#Heres how this Works:
#fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12,12))
#fig, (first plot,second plot) = plt.suibplots(# of plots, # of columns,figsize=(what ,by what))
###################################################
'''
a= []
fig, ax = plt.subplots(1, 3, figsize=(24,24))
graphs=0
plt.yticks(rotation=45)
#plt.margins(x=1)
for city in cities:
    plot = cityDataFrames[city]
    g = sb.heatmap(plot.corr(),ax=ax[graphs],linewidths=0.25, linecolor='white',square = True)
    g.set(xlabel = city)
    graphs = graphs+1
''''
portland = (cityDataFrames['Portland'])
Houston = (cityDataFrames['Houston'])
Detroit = (cityDataFrames['Detroit'])
sb.heatmap(portland.corr(),ax=ax[0])
sb.heatmap(Houston.corr(),ax=ax[1])
sb.heatmap(Detroit.corr(),ax=ax[2])
'''
plt.margins(x=0)
plt.show()