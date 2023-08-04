import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd

from pylab import savefig

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows',None)

pd.set_option('display.width', None)


def getStateShapeFile():#creates shape files of all the states



    path = 'tl_2022_us_county/tl_2022_us_county.shp'#takes in shape file of all counties in the whole US
    allCounties = gpd.read_file(path)


    gdf = gpd.GeoDataFrame(allCounties)
    print(gdf)

    stateIndexCol = gdf['STATEFP']
    countyCol = gdf['NAME']
    geoCol = gdf['geometry']

    ANSI = ['01','02','04','05','06','08','09','10','11','12','13','15','16','17','18','19','20','21','22','23','24','25','26',
            '27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','44','45','46','47','48',
            '49','50','51','53','54','55','56']

    stateDict = {}#dict that will hold the states and an array of their index in the table
    statedfDict = {}
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
        
        newDict ={}
        countyArr = []
        geometryArr = []
        factorArr = []
        df = pd.DataFrame(columns = ['County','geometry'])
        stateDict[state] = newDict
        stateDict[state]['County'] = countyArr
        stateDict[state]['geometry'] = geometryArr
        stateDict[state]['Factor'] = factorArr
        statedfDict[state] = df
        
    ANSILength = len(ANSI)
    length = len(countyCol)


    for i in range(0,length-1):
        for j in range(0,ANSILength):
            if(ANSI[j] == stateIndexCol[i]):
                state = states[j]
                county = countyCol[i]
                geo = geoCol[i]
                
                stateDict[state]['County'].append(county)
                stateDict[state]['geometry'].append(geo)


    for state in states:
        newCountyCol = pd.Series(stateDict[state]['County'])
        newGeoCol = pd.Series(stateDict[state]['geometry'])
        df = statedfDict[state]
        df['geometry']= newGeoCol
        df['County'] = newCountyCol
        print(df)
        gdf = gpd.GeoDataFrame(df)
        statedfDict[state] = gdf


        toUseDf = statedfDict[state]
        toUseDf.plot()
        plt.title(f'{state}')
        plt.show()
        #toUseDf.to_file(f'statesShapeFile/{state}shapeFile.shp')#uncomment if you want to save the shape files

getStateShapeFile()