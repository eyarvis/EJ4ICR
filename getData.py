import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from pylab import savefig

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows',None)
#pd.set_option('display.max_rowwidth',None)
#pd.set_option('display.width', None)
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


def graphFactorsPerState(stateName,stateIndex,colArr):
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


df = pd.read_csv('RPCSV/CSVTables/totalTracts2.csv')#this is the file that holds all of the tracts


#these arrays hold the lists of factors
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
states2 = [ 'West Virginia', 'Wisconsin', 'Wyoming']
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

for i in range(0,totalTractCount):#creates the dicts to hold tract and ocunty info
    for state in states:
        if stateCol[i] == state:
            tract = tractCol[i]
            county = countyCol[i]
            stateIndex[state].append(i)
            stateTract[state].append(tract)
            stateCounty[state].append(county)

    totalCount=totalCount+1

for state in states2:
    graphFactorsPerState(state,stateIndex,colArr)

#print("2")
#print(corrdf[tableLabels[2]])
#print("9")
#print(corrdf[tableLabels[8]])

#def findMax(numOfMax,arr,)