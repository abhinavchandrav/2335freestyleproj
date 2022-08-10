# Final Project: Stock Momentum Indicator

This is an easy to use Stock Momentum Inidcator to help investors, or individuals, make investment decisions. Momentum is frequently used when making portfolio rebalancing decisions.  

- Positive Momentum: the stock has excess annual return compared to the return of Treasury bills
- Negative Momentum: the Treasury bill has excess annual return compared to the stock

Simply put, if a stock has Positive Momentum, you will likely be better off investing in the stock than a Treasury bill (a "safe" investment).  

*Assumption: Momentum is indicative of future returns*

## Set Up

1. Navigate via web browser to the [repository](https://github.com/abhinavchandrav/2335freestyleproj)

2. The repo can either be: 
    - Forked (creating a copy of the repository) then cloned to create the remote repository on your local computer, or
    - Cloned directly from the repository 

3. Save the repository locally.  ***REMEMBER WHERE YOU SAVED THE REPOSITORY ON YOUR LOCAL COMPUTER***

4. Using the command line, navigate to the relevant local repository.  For the sake of this README file, we will assume we used the "Documents" folder:

```sh
cd ~/Documents/2335freestyleproj
```

5. Create a virtual environement (suggested naming is momentum-indicator-env). This step is only required the first time you run the program.  

```sh
conda create -n momentum-indicator-env
```
6. Activate the environment:

```sh 
conda activate momentum-indicator-env
```

## Usage

1. Install the required packages: 

```sh
pip install -r requirements.txt
```

2. Run the program:

```sh
python main.py
```

3. When prompted, enter your desired ticker symbol.  If you ticker symbol is valid, you will learn if the stock has positive or negative momentum and recieve a recommendation on your investment.  If your ticket symbol is invalid, you will be notified as such. 

## Demo

Here is a demo output of a valid ticker symbol:

    Please enter a ticker:TSLA
    2022-08-10 adjusted close price: $883.07
    2021-08-11 adjusted close price: $707.82
    percent change in TSLA 24.759119550168123
    Treasury yield is 1.33
    TSLA has positive momentum.
    Recommendation: Invest in TSLA

Here is a demo output of an invalid ticker symbol:

    Please enter a ticker:lkhljk
    OPPS! That ticker is not available.  Please check your symbol and try again.

## Testing 

There is testing available for the symbol input to ensure valid and invalid symbols are handled appropriately.  This testing is applicable for the API calls ensuring a csv file is recieved and the user input of a ticket symbol. 

```sh 
pytest
```