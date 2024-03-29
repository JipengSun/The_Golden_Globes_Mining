# The_Golden_Globes_Mining

The entry point of the project is the "awards_mining.ipynb" jupyter notebook file. All configurable parameters of the model are listed in the first code block of the file. Eg. You can modify the data_path to choose the input dataset. After changing parameters you want, click 'Run All' and the results will appear at the last code block no more than 5 minutes.

The output of the project is two files (results.json, and human_readable_result.txt) containing following information: awards name, host name, presenter name of the award, nominees of the award, winner of the award, and tweeter attitude towards them. 

## How to config the project

run "python install -r requirements.txt"<br>
run "python -m nltk.downloader vader_lexicon"<br>
run "python -m nltk.downloader names"<br>

## How to run the project

To run this project and get benchmark score. Please put the dataset under the ./Data folder and follow procedures below:

1. Run ./awards_mining.ipynb python notebook file. You can change the parameters at the first block of code. Remember, all the input data locates in ./Data folder.
2. After 1st step, you can get two types of results under ./Results folder. 

    1. One is human readable format txt file, containing following information: awards name, host name, presenter name of the award, nominees of the award, winner of the award, and tweeter attitude towards them. 

    2. Another type is .json output for autograder, ggapi. It is used for getting benchmark score.

3. Run the ./autograder.py file. It will read the output of the ./awards_mining.ipynb and compare with the global truth.
4. If you want to test with another dataset. Please put your test dataset under ./Data folder. If you want to get benchmark score, you need to change the datapath in ./gg_api.py to find the corresponding output .json files since they are independent parts now.

## Github Link

https://github.com/JipengSun/The_Golden_Globes_Mining

- Jipeng Sun & Aaron Cooper
