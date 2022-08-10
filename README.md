# Final Project: Stock Momentum Indicator

talk about why we did this idea! 

## Steps to Run:

1. Navigate via web browser to the [repository](https://github.com/abhinavchandrav/2335freestyleproj)

2. Click the "green button" to open the repository via GitHub Desktop

3. Save the repository locally.  ***REMEMBER WHERE YOU SAVED THE REPOSITORY ON YOUR LOCAL COMPUTER***

4. Using the command line, navigate to the relevant local repository.  For the same of this README file, we will assume we used the "Documents" folder:

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
7. Install the required packages: 

```sh
pip install -r requirements.txt
```
8. Import and configure the necessary pandas packages using:

from pandas import read_csv
import pandas as pd

9. Run the program:

```sh
python momentum.py
```

10. When prompted, enter the desired ticker symbol

## Testing 

pytest