# EJ4ICR

Summer 2023 Project for ICR.

This repo was created with the intent to compare the correlation between enviormental justice indexes and demographic indexes across the US. Included in this REPO is a csv table 'totalTracts.csv' that contains the demographic and enviormental indexes for every single tract in the united states. Also included is various heatmaps and plots that compare these demographic and enviormental indexes to one another as well as displaying their correlation.




## Accessing Initial Heatmaps and Results from EJRP.py:

The file EJRP.py contains my intital research and findings on the first 15 tracts I tested(5 tracts from 3 different cities: Portland, Houston, and Detroit). The file EJRP.py will build 2 different heatmaps. The first of which is a heatmap of Portland Houston and detroit respectivley, all on the same axis. 

The second of which is a heatmap of the total tracts (all 15 tracts combined) on one axis. This table cna be reproduced




## Accessing Final Report and Final Presentation:

My final presentation slides and final research paper can be found in the folder FinalReport. My final slides are "EmilyYarvisSlides.odp". These slides can be opened with the following command:

```libreoffice --headless --convert-to pdf EmilyYarvisSlides.odp```

You may need to install libreoffice(a free and open scource version of google slides or powerpoint) in order for this to work. 

My final written report is located in the FinalReport folder in the ResearchPaper Folder, the tex file is called "ResearchPaper.tex"

To open the research paper as a pdf type

```pdflatex main.tex```

followed by

b``biber HIV``

Now, recompile the file again

```pdflatex HIV.tex```

Open the created pdf by typing

```open HIV.pdf```

