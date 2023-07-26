import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd

from pylab import savefig



allCountiesPath = 'RPCSV/testCounties.csv'#CSV table of all counties in US
allCountiesdf = pd.read_csv(allCountiesPath)#making it into a data frame

stateIndexCol = allCountiesdf['STATEFP']#defining the column that holds the state index so you can tell what row is what state
length = len(stateIndexCol)#getting the length of the col/how many data points their are
print(stateIndexCol)


stateDict = {}#dict that will hold the states and an array of their index in the table
states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', #names of all the states
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

for state in states:#goes through the states and puts them into the dict and assigns an array to them
    arr = []
    stateDict[state] = arr

print(length)#debugging
for i in range(0,(length-1)):#goes through and prints out the col 
    index = stateIndexCol[i]
    print(i,',',index)

for i in range(0,(length-1)):# supposed to go through and append stuff to the dictionary by state(but it doesnt)
    index = stateIndexCol[i]
    num = index-1
    print(num)
    theState = states[num]
    stateDict[theState].append(i)




