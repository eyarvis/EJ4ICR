import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd

from pylab import savefig

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows',None)
#pd.set_option('display.max_rowwidth',None)
pd.set_option('display.width', None)
#pd.set_option('display.max_colwidth', None)
def plot(corrdf):#Function to plot heatmaps
    sb.heatmap(corrdf)
    plt.show()

def corrPlot(corrdf):#function to plot correlation heatmaps
    plot = corrdf.corr()
    sb.heatmap(plot)
    plt.show()

def plotForState(stateName,stateIndex,colArr):#this will print a heatmap for a given state
    totalDataPoints = len(stateIndex[stateName])
    dataStart = stateIndex[stateName][0]
    print("DATA START",dataStart)
   
    dataEnd = stateIndex[stateName][totalDataPoints-1]
    print("DATA END", dataEnd)
    newColArr = []

    for j in range(0,20):
        newArr = []
        currentFactor = colArr[j]
        for i in range(dataStart,(dataEnd+1)):
            newArr.append(currentFactor[i])
        newColArr.append(newArr)

    testdf = pd.DataFrame(newColArr)

    Tdf = testdf.transpose()
    
    
    print("TESTDF TO COMPARE")
    print(Tdf[0])
    finaldf = Tdf.corr()
    
    plt.figure(figsize=(20,10))
    g =sb.heatmap(finaldf,annot=True,linewidths=0.25, linecolor='white')
    g.set(xlabel = stateName)
   
    plt.show()


def getCorrelationForState(stateName,stateIndex,colArr):#this will print a heatmap for a given state
    totalDataPoints = len(stateIndex[stateName])
    dataStart = stateIndex[stateName][0]
    print("DATA START",dataStart)
   
    dataEnd = stateIndex[stateName][totalDataPoints-1]
    print("DATA END", dataEnd)
    newColArr = []

    for j in range(0,20):
        newArr = []
        currentFactor = colArr[j]
        for i in range(dataStart,(dataEnd+1)):
            newArr.append(currentFactor[i])
        newColArr.append(newArr)

    testdf = pd.DataFrame(newColArr)

    Tdf = testdf.transpose()
    
    
    print("TESTDF TO COMPARE")
    print(Tdf[0])
    finaldf = Tdf.corr()
    print(finaldf)

    return finaldf


def graphFactorsPerState(stateName,stateIndex,colArr):#graphs the correlation of factors for a given state
    totalDataPoints = len(stateIndex[stateName])    
    dataStart = stateIndex[stateName][0]
    dataEnd = stateIndex[stateName][totalDataPoints-1]


    for i in range(0,13):#plots the relationship between all the different factors
        print('i: ',i)
        for j in range(13,20):
            x = colArr[i][dataStart:(dataEnd+1)]
            y=colArr[j][dataStart:(dataEnd+1)]

            print(x)
            print(y)
            plt.plot(x,y,'ro')
            plt.xlabel(tableLabels[i])
            plt.ylabel(tableLabels[j])
            plt.title(stateName)
            print(stateName)
            plt.savefig(f"correlationGraphs/byState2/{stateName}.{tableLabels[i]}VS{tableLabels[j]}.png")
            plt.show()

def findMax(numOfMax,arr):#finds the max values in a data set and returns their index as well
    finalMaxPrint = []
    finalMaxIndexPrint = []
   
    manipulatedArr = arr
    print(manipulatedArr)
    for i in range(0,numOfMax):
        totalItems = len(manipulatedArr)
        currentMax=0
        maxIndex = -1
        for j in range(0,totalItems):
            if currentMax<manipulatedArr[j]:
                currentMax = manipulatedArr[j]
                maxIndex = j
                
        finalMaxPrint.append(currentMax)
        finalMaxIndexPrint.append(maxIndex)
        manipulatedArr[maxIndex] = 0

    print("FINAL MAX")
    print(finalMaxPrint)
    print(finalMaxIndexPrint)

df = pd.read_csv('RPCSV/CSVTables/totalTracts2.csv')#this is the file that holds all of the tracts


#these arrays hold the lists of factors
printLabel = ['PM-2.5','Ozone(ppb)','Diesel-PM','Cancer-Risk','Resp-Hazard Index']
eLabel = ['PM 2.5','Ozone(ppb)','Diesel PM (ug/m3)','Cancer Risk','Resp. Hazard Index','Toxic Releases To Air','Traffic(prox. & vol.)',
          'Lead Paint Indicator','Superfund Prox.','RMP Prox.','Hazardous Waste Prox.','Underground Storage Tank Indicator','Waste Water Discharge Indicator']
dLabel =['Demo. Index','Supp. Demo. Index ','POC Pop.','Low Income Pop.','Unemployed','Low English Household','Pop. w/ < HS Ed.']
tableLabels=['PM25-F1','OZONE-F2','DSLPM-F3','CANCER-F4','RESP-F5','RSEI_AIR-F6','PTRAF-F7','PRE1960PCT-F8','PNPL-F9','PRMP-F10','PTSDF-F11','UST-F12','PWDIS-F13',
             'DEMOGIDX_2-F14','DEMOGIDX_5-F15','PEOPCOLORPCT-F16','LOWINCPCT-F17','UNEMPPCT-F18','LINGISOPCT-F19','LESSHSPCT-F20']
states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 
          'California', 'Colorado', 'Connecticut', 
          'Delaware', 'District of Columbia', 'Florida', 'Georgia', 
           'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 
          'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 
          'Minnesota',  'Mississippi', 'Missouri', 
          'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 
          'New Mexico', 'New York', 'North Carolina', 'North Dakota', 
          'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 
          'Rhode Island', 'South Carolina', 'South Dakota', 
          'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 
          'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
states2 = [ 'Alabama', 'Arizona', 'Arkansas', 
          'California', 'Colorado', 'Connecticut', 
          'Delaware', 'District of Columbia', 'Florida', 'Georgia', 
           'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 
          'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 
          'Minnesota',  'Mississippi', 'Missouri', 
          'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 
          'New Mexico', 'New York', 'North Carolina', 'North Dakota', 
          'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 
          'Rhode Island', 'South Carolina', 'South Dakota', 
          'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 
          'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
orderedStates = ['West Virginia',  'Florida' , 'Illinois' ,'Minnesota' , 'Maryland' ,'Rhode Island', 'Idaho' ,'New Hampshire',  
                 'North Carolina', 'Vermont',  'Connecticut' , 'Delaware' , 'New Mexico',  'California',  'New Jersey' , 'Wisconsin' ,
                'Oregon',  'Nebraska' , 'Pennsylvania',    'Washington' ,  'Louisiana' ,  'Georgia' ,   'Alabama',    'Utah',  'Ohio',  
                'Texas',   'Colorado',   'South Carolina',    'Oklahoma',  'Tennessee',   'Wyoming','North Dakota' , 'Kentucky' ,  
                'Maine',  'New York',  'Nevada'  , 'Michigan',   'Arkansas',   'Mississippi' , 'Missouri',  'Montana',   'Kansas' ,  
                'Indiana',  'South Dakota'  , 'Massachusetts'  , 'Virginia',  'District of Columbia' , 'Iowa' , 'Arizona'  ]
stateTract={}#hold state name and all corresponding tracts
stateIndex={}#holds state names and all correspondindg row index of data
stateCounty = {}#holds all the state names and all the correspondng countys
stateCountyIndex = {}
colArr = []#array of all the factors values from the tab;le
index = 0
for label in tableLabels:#creates an array of all the factors and excludes the state and tract stuff
    ls = df[label]
    colArr.append(ls)

#Prints heatmap of every single different tract
newDf = pd.DataFrame(colArr)
corrdf = newDf.transpose()#this is the data frame that has the factors as the columns so it is ready to do .corr() on 
#corrPlot(corrdf)



#invert the data fram and then make a function that will look for whatever state I want and then  plot that
totalCount=0
stateCol = df['STATE_NAME']
tractCol = df['ID']
countyCol = df['CNTY_NAME']
totalTractCount = len(stateCol)
totalCountyCount = len(stateCol)

for state in states:#createsa bunch of arrays to index stuff for the dicts
    stateArr= []
    indexArr = []
    countyArr = []
    countyIndexArr = []
    stateIndex[state]=indexArr
    stateTract[state] = stateArr
    stateCounty[state] = countyArr

for i in range(0,totalTractCount):#creates the dicts to hold tract and county info so functions work
    for state in states:
        if stateCol[i] == state:
            tract = tractCol[i]
            county = countyCol[i]
            stateIndex[state].append(i)
            stateTract[state].append(tract)
            stateCounty[state].append(county)

    totalCount=totalCount+1

correlationOne = []
correlationTwo = []
correlationThree = []
correlationFour = []
correlationFive = []


for state in orderedStates:
    stateCorrDf = getCorrelationForState(state,stateIndex,colArr)

    correlationOne.append(stateCorrDf[13][0])
    correlationTwo.append(stateCorrDf[13][1])
    correlationThree.append(stateCorrDf[13][2])
    correlationFour.append(stateCorrDf[13][3])
    correlationFive.append(stateCorrDf[13][4])

corOneCol=pd.Series(correlationOne)
corTwoCol=pd.Series(correlationTwo)
corThreeCol=pd.Series(correlationThree)
corFourCol=pd.Series(correlationFour)
corFiveCol=pd.Series(correlationFive)


dfdf = pd.DataFrame(columns = ['One','Two','Three','Four','Five'])
dfdf['One']=corOneCol
dfdf['Two']=corTwoCol
dfdf['Three']=corThreeCol
dfdf['Four']=corFourCol
dfdf['Five']=corFiveCol












##############################################################################################################################
#Doing the shape heatmaps


#gets the shape file
path = 'tl_2022_us_state/tl_2022_us_state.shp'
newMap = gpd.read_file(path)

#extracts the state and geometry columns since they are the only ones we need
stateCol = pd.Series(newMap['NAME'])
geometryCol = pd.Series(newMap['geometry'])


#creating data frame for my new geopandas map

deletedf = pd.DataFrame(columns = ['NAME','geometry'])

deletedf['NAME'] = stateCol
deletedf['geometry'] = geometryCol

#finding the states we dont want and getting rid of them#######################
index = 0
arr = []
arrName = []
found = False
for item in stateCol:#finding the ones to delete
    found=False
    for state in states2:
        if item == state:
            found = True
    if found!=True :
        arr.append(index)
        arrName.append(item)

    index = index+1
for i in arrName:#deleting them
    deletedf = deletedf.drop(deletedf[deletedf['NAME'] == f'{i}'].index)
#####################################################################################

stateCol = pd.Series(deletedf['NAME'])
geometryCol = pd.Series(deletedf['geometry'])

#deals with the weird dropping of certain index thing to make the table actually 48 long
newarr = np.array(stateCol)
stateCol = pd.Series(newarr)
newarr = np.array(geometryCol)
geometryCol = pd.Series(newarr)


df = pd.DataFrame(columns=['NAME','geometry','One','Two','Three','Four','Five'])

df['NAME'] = stateCol
df['geometry'] = geometryCol

factors = ['One','Two','Three','Four','Five']
df['One']=corOneCol
df['Two']=corTwoCol
df['Three']=corThreeCol
df['Four']=corFourCol
df['Five']=corFiveCol





#creating the final map
thisMap = gpd.GeoDataFrame(df)
print(thisMap)
#thisMap.plot(figsize=(10,15))

for i in range(0,5):
    thisMap.plot(figsize=(10,15),column=f'{factors[i]}', legend=True)
    plt.title(f"Demographic Index vs {eLabel[i]}")
    
    plt.savefig(f"heatMaps/USMaps/DemographicIndexVS{printLabel[i]}.png")
    



plt.show()