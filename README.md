# EJ4ICR

Summer 2023 Project for ICR.

This repo was created with the intent to compare the correlation between enviormental justice indexes and demographic indexes across the US. Included in this REPO is a csv table 'totalTracts2.csv' that contains the demographic and enviormental indexes for every single tract in the united states. Also included is various heatmaps and plots that compare these demographic and enviormental indexes to one another as well as displaying their correlation.




## Accessing Initial Heatmaps and Results from EJRP.py:

The file EJRP.py contains my intital research and findings on the first 15 tracts I tested(5 tracts from 3 different cities: Portland, Houston, and Detroit). The file EJRP.py will build 2 different heatmaps. The first of which is a heatmap of Portland Houston and Detroit respectivley, all on the same axis. The second of which is a heatmap of the total tracts (all 15 tracts combined) on one axis. Both of these graphs can be reproduced by simply running the file using the command:

```python3 EJRP.py```

you may need to install python3 by running the following command

```sudo apt install python3```


## Accessing all models and tables that are created from entire dataset in getData.py:

The file getData.py contains all of my exploratory research in which I used the full data set 'totalTracts2.csv' to create my heatmaps and tables of the correlation between factors. In order to recreate heatmaps there are several functions you can use to recreate these maps. They are listed and described below:

plotTotalTract(): This function will create a heatmap that displays the correlation between factors 1-20 using the full data set(every single tract within the US).
    
plotForState(stateName): This function will create a heatmap that displays the correlation between factors 1-20 using the full data set within a given state. You must pass in the state name for which you want to display a heatmap for.
    
graphFactors: This function will plot every combination of the different factors on an x and y axis to visually explore the correlation between the two factors. This function uses the full data set.

graphFactorsPerState(stateName): This function will plot every combination of the different factors on an x and y axis to visually explore the correlation between the two factors within a single state(that is passed into the function). This function uses the full state data set.

graphAvgFactor(factorNum): This function will display a heatmap overlayed on a map of the United States that shows the average of the given factor(factorNum) by state within the US.
   

To run any of the above functions simply download "getData.py" and use your preffered editor to uncomment the function you would like to run at the bottom of the file. 

## To Download Shape Files of All the States Using the File testShapeFile.py:

The file testShapeFile.py has one purpose, to create shape files of every state to allow the user to download them. By running the file using the following command:

```python3 testShapeFile.py```

You will be able to download a shape file for every state.

you may need to install python3 by running the following command in order for the previous command to work

```sudo apt install python3```



## Accessing Final Report and Final Presentation:

My final presentation slides and final research paper can be found in the folder FinalReport. 



My final slides are "EmilyYarvisSlides.odp". These slides can be opened with the following command:

```libreoffice --headless --convert-to pdf EmilyYarvisSlides.odp```

You may need to install libreoffice(a free and open scource version of google slides or powerpoint) in order for this to work. 

My final written report is located in the FinalReport folder in the ResearchPaper Folder, the tex file is called "ResearchPaper.tex"

To open the research paper as a pdf type

```pdflatex main.tex```

followed by

``biber main``

Now, recompile the file again

```pdflatex main.tex```

Open the created pdf by typing

```open main.pdf```

