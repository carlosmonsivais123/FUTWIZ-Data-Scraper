import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

ut = pd.read_csv("./FUT 2020 Tables/FUT2020_Clean.csv")

############################################################## Player Search Tab: Data ##############################################################
search_data = ut[['Name', 'Rating', 'Position', 'General Position', 'Skills', 'Weakfoot', 'Age', 'Height(cm)',
       'Weight(kg)', 'Workrate', 'Foot', 'Card Type', 'Nation', 'Club', 'League', 'Total Stats',
       'Average Price', 'Median Price', 'Current Price',
       'PAC', 'Acceleration', 'Sprint Speed', 'SHO', 'Positioning',
       'Finishing', 'Shot Power', 'Long Shots', 'Volleys', 'Penalties', 'PAS',
       'Vision', 'Crossing', 'FK.Acc.', 'Short Pass', 'Long Pass', 'Curve',
       'DRI', 'Agility', 'Balance', 'Reactions', 'Ball Control', 'Dribbling',
       'Composure', 'DEF', 'Interceptions', 'Heading Acc.', 'Def. Awareness',
       'Stand Tackle', 'Slide Tackle', 'PHY', 'Jumping', 'Stamina', 'Strength',
       'Aggression']]

search_data.to_csv('./FUT 2020 Tables/Search Data.csv', index = False)

############################################################## PLayer Pricing ##############################################################
dis = ut[["Name", "Card Type", "Rating", "Position", "Club", "Nation", 'Price Date',
          "Prices", "Average Price", "Median Price", 'General Position', 'Skills', 'Weakfoot', 'Age', 'Height(cm)',
       'Weight(kg)', 'Workrate', 'Foot', 'League', 'Total Stats',
        'Current Price', 'Acceleration', 'Sprint Speed', 'Positioning',
       'Finishing', 'Shot Power', 'Long Shots', 'Volleys', 'Penalties',
       'Vision', 'Crossing', 'FK.Acc.', 'Short Pass', 'Long Pass', 'Curve',
 'Agility', 'Balance', 'Reactions', 'Ball Control', 'Dribbling',
       'Composure', 'Interceptions', 'Heading Acc.', 'Def. Awareness',
       'Stand Tackle', 'Slide Tackle', 'Jumping', 'Stamina', 'Strength',
       'Aggression', "PAC", "SHO", "DEF", "PAS", "PHY", "DRI", "PAC"]]

dis["Rating"] = dis["Rating"].apply(str)

dis.to_csv('./FUT 2020 Tables/dis.csv', index = False)

############################################################## Overall in Ultimate Team Tab: Data ##############################################################
# Graph 1
position_counts = pd.DataFrame(ut["Position"].value_counts())
position_counts.reset_index(inplace = True, drop = False)
position_counts.columns = ["Position", "Counts"]

position_counts.to_csv('./FUT 2020 Tables/Position Counts.csv', index = False)


# Graph 2
general_position_counts = pd.DataFrame(ut["General Position"].value_counts())
general_position_counts.reset_index(inplace = True, drop = False)
general_position_counts.columns = ["General Position", "Counts"]

general_position_counts.to_csv('./FUT 2020 Tables/General Position Counts.csv', index = False)

# Graph 4
rating_count = pd.DataFrame(ut["Rating"].value_counts())
rating_count.reset_index(inplace = True, drop = False)
rating_count.columns = ["Rating", "Counts"]
rating_count.sort_values(by = "Rating", inplace = True)

rating_count.to_csv('./FUT 2020 Tables/Rating Count.csv', index = False)

# Graph 5
age_count = pd.DataFrame(ut["Age"].value_counts())
age_count.reset_index(inplace = True, drop = False)
age_count.columns = ["Age", "Counts"]
age_count.sort_values(by = "Age", inplace = True)

age_count.to_csv('./FUT 2020 Tables/Age Count.csv', index = False)

# Graph 6
foot_count = pd.DataFrame(ut["Foot"].value_counts())
foot_count.reset_index(inplace = True, drop = False)
foot_count.columns = ["Foot", "Counts"]
foot_count.sort_values(by = "Foot", inplace = True)

foot_count.to_csv('./FUT 2020 Tables/Foot Count.csv', index = False)

# Graph 7
skills_count = pd.DataFrame(ut["Skills"].value_counts())
skills_count.reset_index(inplace = True, drop = False)
skills_count.columns = ["Skills", "Counts"]
skills_count.sort_values(by = "Skills", inplace = True)

skills_count.to_csv('./FUT 2020 Tables/Skills Count.csv', index = False)

# Graph 8
weakfoot_count = pd.DataFrame(ut["Weakfoot"].value_counts())
weakfoot_count.reset_index(inplace = True, drop = False)
weakfoot_count.columns = ["Weakfoot", "Counts"]
weakfoot_count.sort_values(by = "Weakfoot", inplace = True)

weakfoot_count.to_csv('./FUT 2020 Tables/Weakfoot Count.csv', index = False)

# Graph 9
height_count = pd.DataFrame(ut['Height(cm)'].value_counts())
height_count.reset_index(inplace = True, drop = False)
height_count.columns = ['Height(cm)', "Counts"]
height_count.sort_values(by = 'Height(cm)', inplace = True)
height_count.reset_index(inplace = True, drop = True)
height_count.drop(height_count.loc[height_count['Height(cm)']==0].index, inplace=True)

height_count.to_csv('./FUT 2020 Tables/Height Count.csv', index = False)

# Graph 9
weight_count = pd.DataFrame(ut['Weight(kg)'].value_counts())
weight_count.reset_index(inplace = True, drop = False)
weight_count.columns = ['Weight(kg)', "Counts"]
weight_count.sort_values(by = 'Weight(kg)', inplace = True)
weight_count.reset_index(inplace = True, drop = True)
weight_count.drop(weight_count.loc[weight_count['Weight(kg)']==0].index, inplace=True)

weight_count.to_csv('./FUT 2020 Tables/Weight Count.csv', index = False)

# Graph 10
workrate_count = pd.DataFrame(ut['Workrate'].value_counts())
workrate_count.reset_index(inplace = True, drop = False)
workrate_count.columns = ['Workrate', "Counts"]
workrate_count.sort_values(by = 'Counts', inplace = True, ascending = False)

workrate_count.to_csv('./FUT 2020 Tables/Workrate Count.csv', index = False)

# Graph 12
league_count = pd.DataFrame(ut['League'].value_counts())
league_count.reset_index(inplace = True, drop = False)
league_count.columns = ['League', "Counts"]
league_count.sort_values(by = 'Counts', inplace = True, ascending = False)

league_count.to_csv('./FUT 2020 Tables/League Count.csv', index = False)

# Graph 13
nation_count = pd.DataFrame(ut['Nation'].value_counts())
nation_count.reset_index(inplace = True, drop = False)
nation_count.columns = ['Nation', "Counts"]
nation_count.sort_values(by = 'Counts', inplace = True, ascending = False)

nation_count.to_csv('./FUT 2020 Tables/Nation Count.csv', index = False)

# Graph 14
totalstats_count = pd.DataFrame(ut['Total Stats'].value_counts())
totalstats_count.reset_index(inplace = True, drop = False)
totalstats_count.columns = ['Total Stats', "Counts"]
totalstats_count.sort_values(by = 'Total Stats', inplace = True, ascending = False)

totalstats_count.to_csv('./FUT 2020 Tables/Total Stats Count.csv', index = False)

#################################################################### Interesting EDA Tab: Data ####################################################################
# Graph 1
average_price_league = ut[["Average Price", "Position", "League"]].groupby(['League', 'Position']).mean()
average_price_league.reset_index(inplace = True, drop = False)
average_price_league["Average Price"] = average_price_league["Average Price"].round(decimals = 2)

average_price_league.to_csv('./FUT 2020 Tables/Average Price League.csv', index = False)

################################################################## Market Analysis: Data #################################################################
index_creation = dis[["Name", "Card Type", "Rating", "Position", "Club", "Nation", 'Price Date',
                      "Prices", "Average Price", "Median Price", 'General Position',
                      'League', 'Total Stats', 'Current Price']]

index_creation.dropna(subset = ["Current Price"], axis=0, inplace = True)
index_creation.reset_index(drop = True, inplace = True)

prices = pd.DataFrame(index_creation["Prices"])

master_indexes = []
i = 0

while i < len(prices):
    indexes = []
    master_indexes.append(indexes)
    price_list = eval(prices["Prices"][i])
    price_zero = price_list[0]

    for value in price_list:
        index = value/price_zero
        index = index * 100
        index = round(index, 2)
        indexes.append(index)
    i = i + 1

indexed_prices = pd.DataFrame([master_indexes]).T
prices["Price Indexes"] = indexed_prices
index_creation = pd.merge(index_creation, prices, left_on = "Prices", right_on = "Prices")

current_index = []
for index in index_creation["Price Indexes"]:
    current_index.append(index[-1])

index_creation["Current Index"] = current_index

index_datatable = index_creation[["Name", "Card Type", "Rating", "Current Index", 'Current Price',
                                  'General Position', "Position", "Nation", "Club", 'League']]

top_20_index = index_creation[["Name", "Card Type", "Rating", "Position", "Current Index", "Current Price"]].sort_values("Current Index", ascending = False).head(n =20)
top_20_index.reset_index(inplace = True, drop = True)
top_20_index["Number"] = list(range(1,21))
top_20_index.set_index("Number", inplace = True)

bottom_20_index = index_creation[["Name", "Card Type", "Rating", "Position", "Current Index", "Current Price"]].sort_values("Current Index", ascending = True).head(n =20)
bottom_20_index.reset_index(inplace = True, drop = True)
bottom_20_index["Number"] = list(range(1,21))
bottom_20_index.set_index("Number", inplace = True)

index_overtime = index_creation[["Price Date", "Price Indexes", "Rating","League", "Card Type", "Position", "Club"]]
index_overtime = index_overtime[index_overtime['Price Indexes'].map(lambda d: len(d)) > 0]
index_overtime = index_overtime[index_overtime['Price Date'].map(lambda d: len(d)) > 0]
index_overtime['List Length'] = index_overtime['Price Indexes'].str.len()

i = 0
full_date_list = []
while i < len(index_overtime):
    date_list = list(eval(index_overtime["Price Date"].iloc[i]))
    full_date_list.extend(date_list)
    i = i + 1

i = 0
full_index_list = []
while i < len(index_overtime):
    index_list = list(index_overtime["Price Indexes"].iloc[i])
    full_index_list.extend(index_list)
    i = i + 1

i = 0
full_league_list = []
while i < len(index_overtime):
    league_list = [index_overtime["League"].iloc[i]]*index_overtime["List Length"].iloc[i]
    full_league_list.extend(league_list)
    i = i + 1

i = 0
full_rating_list = []
while i < len(index_overtime):
    rating_list = [index_overtime["Rating"].iloc[i]]*index_overtime["List Length"].iloc[i]
    full_rating_list.extend(rating_list)
    i = i + 1

i = 0
full_cardtype_list = []
while i < len(index_overtime):
    card_list = [index_overtime["Card Type"].iloc[i]]*index_overtime["List Length"].iloc[i]
    full_cardtype_list.extend(card_list)
    i = i + 1

i = 0
full_club_list = []
while i < len(index_overtime):
    club_list = [index_overtime["Club"].iloc[i]]*index_overtime["List Length"].iloc[i]
    full_club_list.extend(club_list)
    i = i + 1


index_exploded = pd.DataFrame()
index_exploded["Dates Overtime"] = full_date_list
index_exploded["Indexes Overtime"] = full_index_list
index_exploded["League"] = full_league_list
index_exploded["Rating"] = full_rating_list
index_exploded["Club"] = full_club_list
index_exploded["Card Type"] = full_cardtype_list
index_exploded['Dates Overtime'] = index_exploded['Dates Overtime'].astype('datetime64[ns]')
index_exploded['Dates Overtime'] = index_exploded['Dates Overtime'].dt.date

median_index_overtime = index_exploded.groupby('Dates Overtime')['Indexes Overtime'].median()
median_index_overtime = pd.DataFrame(median_index_overtime)
median_index_overtime.reset_index(inplace = True, drop = False)
median_index_overtime.sort_values(by = "Dates Overtime", inplace = True)

rating_indexes_ovt = pd.DataFrame(index_exploded.groupby(['Rating', 'Dates Overtime'])['Indexes Overtime'].median())
rating_indexes_ovt.reset_index(inplace = True, drop = False)
rating_indexes_ovt['Dates Overtime'] = rating_indexes_ovt['Dates Overtime'].astype('datetime64[ns]')


index_creation.to_csv('./FUT 2020 Tables/Index Creation.csv', index = False)
index_datatable.to_csv('./FUT 2020 Tables/Index Data Table.csv', index = False)
top_20_index.to_csv('./FUT 2020 Tables/Top 20 Index.csv', index = False)
bottom_20_index.to_csv('./FUT 2020 Tables/Bottom 20 Index.csv', index = False)
index_overtime.to_csv('./FUT 2020 Tables/Index Overtime.csv', index = False)
index_exploded.to_csv('./FUT 2020 Tables/Index Exploded.csv', index = False)
median_index_overtime.to_csv('./FUT 2020 Tables/Median Index Overtime.csv', index = False)
rating_indexes_ovt.to_csv('./FUT 2020 Tables/Rating Index Overtime.csv', index = False)
