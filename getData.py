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
def plot(corrdf):#Function to plot heatmaps. pass in the data frame you would like to make a heatmpa of that has already been .corr()
    sb.heatmap(corrdf)
    plt.show()

def corrPlot(corrdf):#function to plot correlation heatmaps from a data frame that has not already been .corr()
    plot = corrdf.corr()
    sb.heatmap(plot)
    plt.title("Correlation of All Tracts")
    plt.show()

def plotTotalTract():
    corrPlot(corrdf)

def plotForState(stateName):#this will print a heatmap for a given state
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


def getCorrelationForState(stateName,stateIndex,colArr):#this is used for another function DO NOT RUN
    totalDataPoints = len(stateIndex[stateName])
    dataStart = stateIndex[stateName][0]
    
   
    dataEnd = stateIndex[stateName][totalDataPoints-1]
  
    newColArr = []

    for j in range(0,20):
        newArr = []
        currentFactor = colArr[j]
        for i in range(dataStart,(dataEnd+1)):
            newArr.append(currentFactor[i])
        newColArr.append(newArr)

    testdf = pd.DataFrame(newColArr)

    #print("HELLO HELLO HELLO")
    Tdf = testdf.transpose()
    #print(Tdf)
    
    
    
    finaldf = Tdf.corr()
    return finaldf


def getCorrForAllTractsInState(stateName,stateIndex,colArr):
    totalDataPoints = len(stateIndex[stateName])
    dataStart = stateIndex[stateName][0]
    
   
    dataEnd = stateIndex[stateName][totalDataPoints-1]
  
    newColArr = []

    for j in range(0,20):
        newArr = []
        currentFactor = colArr[j]
        for i in range(dataStart,(dataEnd+1)):
            newArr.append(currentFactor[i])
        newColArr.append(newArr)

def graphFactors():
    for i in range(0,13):#plots the relationship between all the different factors
        print('i: ',i)
        for j in range(13,20):
            x = colArr[i]
            y=colArr[j]

            
            plt.plot(x,y,'ro')
            plt.xlabel(tableLabels[i])
            plt.ylabel(tableLabels[j])
            
            
            #plt.savefig(f"correlationGraphs/byState2/{stateName}.{tableLabels[i]}VS{tableLabels[j]}.png")
            plt.show()




def graphFactorsPerState(stateName):#graphs the correlation of factors for a given state
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



def graphAvgFactor(factorNum):#makes a US heatmap of the average of a given factor

    df = pd.DataFrame(columns = ['State','geometry','factoravg'])
    df['State'] = stateCol
    df['geometry'] = geometryCol
    df['factoravg'] = avgArr

    print(df)
    factorMap = gpd.GeoDataFrame(df)
    print(factorMap)
    factorMap.plot(figsize=(20,20),column='factoravg', legend=True,cmap = 'inferno')
    plt.title(f"AVERAGE {printLabel[factorNum]}")
    
    plt.show()




def graphSpecificState(path,givenState):#will graph a specific state for you
    state = gpd.read_file(path)#this is the states shapefile
    
    
    gdf = gpd.GeoDataFrame(state)#gdf to match


    nameCol = gdf['County']#makes a list for the counties
    geoCol = gdf['geometry']#makes a list for the corresponding geometry
    factorCol = []
    
    countyDict = {}#holds the data frames for each county
    corrCountyDict = {}#holds the correlation data frames for each county

    for county in simpleStateCounty[givenState]:#creates a data frame for every county in a given state and stores it in countyDict[county]
        countyDF = pd.DataFrame()
        arr = []
        countyDict[county] = countyDF
        corrCountyDict[county] = arr

        

    totalData = len(stateCountyIndex[givenState])#the len of the list so like how many counties there are
    dataStart = stateIndex[givenState][0]#index of beginning of county
    dataEnd = stateIndex[givenState][totalData-1]#index of end of county

    for i in range(0,totalData-1):#makes a data frame of all of the different counties data and stores it in countyDict[county]
        
        dataStart = stateCountyIndex[givenState][i]
        dataEnd = stateCountyIndex[givenState][i+1]
        county = simpleStateCounty[givenState][i]
        df = countyDict[county]

        for j in range(0,20):
            df[j] = colArr[j][dataStart:dataEnd]

        
    for county in simpleStateCounty[givenState]:#creates corrCountyDict[county]
        corrCountyDict[county] = countyDict[county].corr()
    
    totalCounties = len(nameCol)

    arrOne= np.empty(totalCounties)
    arrTwo= np.empty(totalCounties)
    arrThree = np.empty(totalCounties)
    arrFour = np.empty(totalCounties)
    arrFive = np.empty(totalCounties)

    found = False
    index=0
    for county in nameCol:#creates the factor columns for the state
        map = sb.heatmap(corrCountyDict[county])
        map.plot()
        plt.title(f"{county}")
        plt.show()
        found= False
        for countyReal in simpleStateCounty[givenState]:
            
            if county == countyReal:
                found = True
                toAdd = countyReal

        if found == True:
            df = corrCountyDict[toAdd]
            arrOne[index]=df[13][0]
            arrTwo[index]=df[13][1]
            arrThree[index]=df[13][2]
            arrFour[index]=df[13][3]
            arrFive[index]=df[13][4]
        elif found ==False:
            arrOne[index]=np.nan
            arrTwo[index]=np.nan
            arrThree[index]=np.nan
            arrFour[index]=np.nan
            arrFive[index]=np.nan

        index = index+1
   
    
    corrOneCol = pd.Series(arrOne)
    corrTwoCol = pd.Series(arrTwo)
    corrThreeCol = pd.Series(arrThree)
    corrFourCol = pd.Series(arrFour)
    corrFiveCol = pd.Series(arrFive)

    factorArr = [corrOneCol,corrTwoCol,corrThreeCol,corrFourCol,corrFiveCol]
    for i in range(0,5):
            
        df = pd.DataFrame(columns = ['NAME','geometry','FACTOR'])
        df['NAME'] = nameCol
        df['geometry'] = geoCol
        df['FACTOR'] = factorArr[i]
        print(df)
        maps = gpd.GeoDataFrame(df)
        
        maps.plot(figsize=(20,20), column = 'FACTOR', legend=True,cmap = 'inferno',edgecolor = 'black',linewidth = 1)
    
        plt.title(f"{givenState}- Correlation Between Demographic Index and {eLabel[i]}")
        plt.savefig(f"heatMaps/stateSpecific/{givenState}-{printLabel[i]}.png")
        plt.show()
        


df = pd.read_csv('RPCSV/CSVTables/totalTracts2.csv')#this is the file that holds all of the tracts

df=df.fillna(0)

#these arrays hold the lists of factors
printLabel = ['PM-2.5','Ozone(ppb)','Diesel-PM','Cancer-Risk','Resp-Hazard Index','Toxic-Releases-To-Air','Traffic(prox.&vol.)',
          'Lead-Paint-Indicator','Superfund-Prox.','RMP-Prox.','Hazardous-Waste-Prox.','Underground-Storage-Tank-Indicator',
          'Waste-Water-Discharge-Indicator','Demo.-Index','Supp.-Demo.-Index ','POC-Pop.','Low-Income-Pop.','Unemployed','Low-English-Household','Pop.-w/-< HS Ed.']
dLabel =['Demo. Index','Supp. Demo. Index ','POC Pop.','Low Income Pop.','Unemployed','Low English Household','Pop. w/ < HS Ed.']
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
simpleStateCounty = {}
colArr = []#array of all the factors values from the tab;le
index = 0
for label in tableLabels:#creates an array of all the factors and excludes the state and tract stuff
    ls = df[label]
    colArr.append(ls)


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
    simpleCountyArr = []
    countyIndexArr = []
    CountyIndex = []
    stateIndex[state]=indexArr#has a list of all the indexes of every tract in a given state
    stateTract[state] = stateArr#has a list of all the tracts in every state
    stateCounty[state] = countyArr#has a list of all the counties(repeated) in every state by tract
    stateCountyIndex[state] = CountyIndex#has a list of the index of every new county
    simpleStateCounty[state]= simpleCountyArr#has a list of all the counties(never repeated) per state
    


for i in range(0,totalTractCount):#creates the dicts to hold tract and county info so functions work
    for state in states:
        if stateCol[i] == state:
            tract = tractCol[i]
            county = countyCol[i]
            stateIndex[state].append(i)
            stateTract[state].append(tract)
            stateCounty[state].append(county)
            
            countyIndex = len(stateCounty[state])
           
            if stateCounty[state][countyIndex-2] != county or countyIndex == 1:
                simpleStateCounty[state].append(county)
                stateCountyIndex[state].append(i)


    totalCount=totalCount+1


total = 0



for state in states:
    value =len(stateCounty[state])
    total = value+total
    stateCountyIndex[state].append(total)






####################################################################testcode#####################

factorAvgDict = {} #creates a dict that holds each factor and then what the average is of that factor for every state

for j in range(0,20):#creates a dict that holds all the different factors and a corresponding arrays with the averages for those factors of every state
    avgArr = []
    
    for state in orderedStates:
        totalData = len(stateIndex[state])
        dataStart = stateIndex[state][j]
        dataEnd = stateIndex[state][totalData-1]
        sum =0
        avg = 0
        for i in range(dataStart,(dataEnd+1)):
            sum = sum+colArr[j][i]
        
        avg = sum / totalData
        avgArr.append(avg)
    factorAvgDict[printLabel[j]] = avgArr
        











###################################to create geoMaps########################################

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

####UNCOMMENT THE FUNCTIONS YOU WOULD LIKE TO RUN BELOW###################



#plotTotalTract()

#plotForState('INSERT STATE NAME')

#graphFactors()

#graphFactorsPerState('Alabama')

#graphAvgFactor(INSERT_FACTOR_NUMBER)


############################################################################



