# The_Golden_Globes_Mining

The entry point of the project is the "awards_mining.ipynb" jupyter notebook file. All configurable parameters of the model are listed in the first code block of the file. Eg. You can modify the data_path to choose the input dataset. After changing parameters you want, click 'Run All' and the results will appear at the last code block no more than 5 minutes.

The output of the project is two files (results.json, and human_readable_result.txt) containing following information: awards name, host name, presenter name of the award, nominees of the award, winner of the award, and tweeter attitude towards them. 

## How to config the project

run "python install -r requirements.txt"<br>
run "python -m nltk.downloader vader_lexicon"<br>
run "python -m nltk.downloader names"<br>

## Github Link

https://github.com/JipengSun/The_Golden_Globes_Mining

- Aaron Cooper & Jipeng Sun
