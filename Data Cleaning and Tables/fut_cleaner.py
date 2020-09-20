############################################ Reading in Libraries ############################################
import pandas as pd
import numpy as np
import time

############################################ Reading in File ############################################
ut = pd.read_csv("FUT2020.csv")

############################################ Sorting by Rating ############################################
ut.sort_values(by = ["Rating"], inplace = True, ascending = False)
ut.reset_index(drop = True, inplace = True)

############################################ Exploding Price Lists ############################################
from ast import literal_eval
ut["Prices"] = ut['Prices'].apply(literal_eval)

############################################### Fixing Prices ###############################################
ut_temporary = ut.explode("Prices")
ut_temporary.reset_index(inplace = True, drop = False)

prices = pd.DataFrame(ut_temporary["Prices"])
for i in [0,1]:
    prices['num{}'.format(str(i+1))]=[k[i] if isinstance(k,list) else k for k in prices['Prices']]

prices["num1"] = prices["num1"]/1000
prices["num1"] = prices["num1"].astype(str)
prices['num1'] = prices['num1'].str.split('.').str[0]
prices['num1'] = pd.to_numeric(prices["num1"], errors='coerce').fillna(0).astype(np.int64)

times = []
def epoch_time(df):
    for i in df["num1"]:
        i = time.strftime("%d %b %Y %H:%M:%S %Z", time.localtime(i))
        times.append(i)

epoch_time(prices)
prices["format times"] = times

prices = prices[["format times", "num2"]]

ut_temporary[["Formatted Times", "Price"]] = prices

prices_fixed = ut_temporary.groupby('index')['Price'].apply(list)
prices_fixed = pd.DataFrame(prices_fixed)

dates_fixed = ut_temporary.groupby('index')['Formatted Times'].apply(list)
dates_fixed = pd.DataFrame(dates_fixed)

ut["Prices"] = prices_fixed
ut["Price Date"] = dates_fixed

############################################### Average Price ###############################################
ut["Average Price"] = [np.array(x).mean() for x in ut["Prices"].values]
ut["Average Price"] = round(ut["Average Price"], 2)

############################################### Median Price ###############################################
median_price = []
for row in ut["Prices"]:
    med_value = np.median(row)
    median_price.append(med_value)

ut["Median Price"] = median_price
############################################### Current Price ###############################################
last_price = []
for price in ut["Prices"]:
    last_price.append(price[-1])

ut["Current Price"] = last_price

################################### Converting Positions to General Positions ###################################
forwards = ["ST", "RW", "LW", "CF", "RF", "LF"]
midfielders = ["CM", "CAM", "CDM", "LM", "RM"]
defenders = ["CB", "RB", "LB", "RWB", "LWB"]
goalkeepers = ["GK"]

general_position_list = []
for value in ut["Position"]:
    if value in forwards:
        general = "Forward"
        general_position_list.append(general)

    elif value in midfielders:
        general = "Midfielder"
        general_position_list.append(general)

    elif value in defenders:
        general = "Defender"
        general_position_list.append(general)

    elif value in goalkeepers:
        general = "Goalkeeper"
        general_position_list.append(general)

    else:
        general = None
        general_position_list.append(general)

ut["General Position"] = general_position_list

################################### Converting Positions: RWB and LWB ###################################
ut["Position"].replace({"RWB": "RB", "LWB": "LB"}, regex = True, inplace = True)

################################### Total Stats Turned to Integer ###################################
ut['Total Stats'] = ut['Total Stats'].str.replace(',', '').astype(int)

################################### Cleaning Height ###################################
ut['Height'] = ut['Height'].str.replace('cm TALL', '').astype(int)

################################### Cleaning Weight ###################################
ut['Weight'] = ut['Weight'].str.replace('kg', '')

################################### Cleaning Card Type ###################################
ut['Card Type'] = ut['Card Type'].str.replace(' | ', '')
ut['Card Type'] = ut['Card Type'].str.replace('|', '')

################################### Only Want these Columns ###################################
ut = ut[['Name', 'Rating', 'Position', 'Skills', 'Weakfoot', 'Age',
       'Height', 'Weight', 'Workrate', 'Foot', 'Card Type', 'Nation', 'Club',
       'League', 'PAC', 'Acceleration', 'Sprint Speed', 'SHO', 'Positioning',
       'Finishing', 'Shot Power', 'Long Shots', 'Volleys', 'Penalties', 'PAS',
       'Vision', 'Crossing', 'FK.Acc.', 'Short Pass', 'Long Pass', 'Curve',
       'DRI', 'Agility', 'Balance', 'Reactions', 'Ball Control', 'Dribbling',
       'Composure', 'DEF', 'Interceptions', 'Heading Acc.', 'Def. Awareness',
       'Stand Tackle', 'Slide Tackle', 'PHY', 'Jumping', 'Stamina', 'Strength',
       'Aggression', 'Total Stats', 'General Position', 'Prices', 'Price Date',
       'Average Price', "Median Price", "Current Price"]]

################################### Renaming the Columns ###################################
ut = ut.rename(columns = {'Height':'Height(cm)', "Weight": "Weight(kg)"})

################################### Converting to a CSV File ###################################
ut.to_csv('./FUT 2020 Tables/FUT2020_Clean.csv', index = False)
