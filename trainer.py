import matplotlib.pyplot as plt
import csv
from numpy.lib.type_check import common_type
import pandas as pd
from collections import Counter
import random

weather_data = pd.read_csv('updated_date_weather_2009-2018.csv')
weather_data_frame = pd.DataFrame(weather_data)

shares_data = pd.read_csv('NewData_SPY_2009-2018.csv')
shares_data_frame = pd.DataFrame(shares_data)

test_weather_data = pd.read_csv('weather_2019.csv')
# test_weather_data_frame = pd.DataFrame(test_weather_data)
test_weather_data_frame = weather_data_frame

test_shares_data = pd.read_csv('SPY_2019.csv')
# test_shares_data_frame = pd.DataFrame(test_shares_data)
test_shares_data_frame = shares_data_frame


test_data_collection = {}




data_collection = {}

for i in range(len(shares_data_frame['Time'])):
    # print(shares_data_frame['%Chg'][i])
    perc = shares_data_frame['%Chg'][i]
    if type(perc) == str and '%' in perc:
        perc = (perc.replace('%',''))
        perc = float(perc)
    data_collection[shares_data_frame['Time'][i]] = [(perc), shares_data_frame['Volume'][i],0,0,0,shares_data_frame['Classification'][i]]

for i in range(len(weather_data_frame['DATE'])):
    if weather_data_frame['DATE'][i] in data_collection.keys():
        data_collection[weather_data_frame['DATE'][i]][2] = weather_data_frame['PRCP'][i]
        data_collection[weather_data_frame['DATE'][i]][3] = weather_data_frame['AWND'][i]
        data_collection[weather_data_frame['DATE'][i]][4] = (weather_data_frame['TMAX'][i]+weather_data_frame['TMIN'][i])/2


for i in range(len(test_shares_data_frame['Time'])):
    # print(shares_data_frame['%Chg'][i])
    perc = test_shares_data_frame['%Chg'][i]
    if type(perc) == str and '%' in perc:
        perc = (perc.replace('%',''))
        perc = float(perc)
    # print(test_shares_data['Classification'][i])
    test_data_collection[test_shares_data_frame['Time'][i]] = [(perc), test_shares_data_frame['Volume'][i],0,0,0,test_shares_data_frame['Classification'][i]]
    # print(type(test_data_collection[test_shares_data['Time'][i]][5]))
for i in range(len(test_weather_data_frame['DATE'])):
    if test_weather_data_frame['DATE'][i] in test_data_collection.keys():
        test_data_collection[test_weather_data_frame['DATE'][i]][2] = test_weather_data_frame['PRCP'][i]
        test_data_collection[test_weather_data_frame['DATE'][i]][3] = test_weather_data_frame['AWND'][i]
        test_data_collection[test_weather_data_frame['DATE'][i]][4] = (test_weather_data_frame['TMAX'][i]+test_weather_data_frame['TMIN'][i])/2

# print(data_collection)
get_unique_wind = []
get_unique_prcpt = []
get_unique_temp = []


for i in data_collection:
    get_unique_prcpt.append(data_collection[i][2])
    get_unique_wind.append(data_collection[i][3])
    get_unique_temp.append(data_collection[i][4])

max_temp = max(get_unique_temp)
min_temp = min(get_unique_temp)
temp_diff = max_temp - min_temp

max_wind = max(get_unique_wind)
min_wind = min(get_unique_wind)
wind_diff = max_wind - min_wind

max_prcpt = max(get_unique_prcpt)
min_prcpt = min(get_unique_prcpt)
prcpt_diff = max_prcpt - min_prcpt
# print(len(get_unique_prcpt),len(get_unique_wind),len(get_unique_temp))
n = len(get_unique_temp)
for i in range(n):
    get_unique_prcpt[i] =  round((get_unique_prcpt[i]-min_prcpt)/prcpt_diff ,2)
    get_unique_wind[i] = round((get_unique_wind[i]-min_wind)/wind_diff, 2)
    get_unique_temp[i] = round((get_unique_temp[i]-min_temp)/temp_diff,2)





get_unique_wind = list(set(get_unique_wind))
get_unique_prcpt = list(set(get_unique_prcpt))
get_unique_temp = list(set(get_unique_temp))


# print(data_collection)


# wind = dict.fromkeys(get_unique_wind, [0,0])
# # prcpt = dict.fromkeys(get_unique_prcpt, [0,0])
# temp = dict.fromkeys(get_unique_temp, [0,0])
wind = {}
prcpt = {}
temp = {}
for i in get_unique_prcpt:
    prcpt[i] = [0,0]

for i in get_unique_wind:
    wind[i] = [0,0]

for i in get_unique_temp:
    temp[i] = [0,0]


# for i in prcpt:
#     prcpt[i][0] +=1
#     print(prcpt)

# print(wind)
for i in data_collection:
    # print(i)
    if data_collection[i][5]:
        # print(data_collection[i])
        # print(wind[data_collection[i][3]],data_collection[i][3])
        # print(prcpt[data_collection[i][2]][0],data_collection[i][2],prcpt[data_collection[i][2]])
        p = round((data_collection[i][2]-min_prcpt)/prcpt_diff ,2)
        w = round((data_collection[i][3]-min_wind)/wind_diff,2)
        t = round((data_collection[i][4]-min_temp)/temp_diff,2)
        prcpt[p][0]+=1
        wind[w][0]+=1
        temp[t][0]+=1
    else:
        # print('--------------------',data_collection[i],'----------------------')
        # print(data_collection[i])
        # print(wind[data_collection[i][3]],data_collection[i][3])
        p = round((data_collection[i][2]-min_prcpt)/prcpt_diff,2)
        w = round((data_collection[i][3]-min_wind)/wind_diff,2)
        t = round((data_collection[i][4]-min_temp)/temp_diff,2)
        prcpt[p][1]+=1
        wind[w][1]+=1
        temp[t][1]+=1
# print(wind)

# print(temp,wind,prcpt)


for i in wind:
    total = wind[i][0] + wind[i][1]
    wind[i][0] = wind[i][0]/total
    wind[i][1] = wind[i][1]/total

for i in prcpt:
    total = prcpt[i][0] + prcpt[i][1]
    prcpt[i][0] = prcpt[i][0]/total
    prcpt[i][1] = prcpt[i][1]/total

for i in temp:
    total = temp[i][0] + temp[i][1]
    temp[i][0] = temp[i][0]/total
    temp[i][1] = temp[i][1]/total


############------------TEST---------------###################

correct = 0
wrong = 0

correct_base = 0
wrong_base = 0
# print(data_collection)
print(wind)

for i in test_data_collection:
    # c1 = wind[test_data_collection[i][3]][0]*prcpt[test_data_collection[i][2]][0]
    # c2 = wind[test_data_collection[i][3]][1]*prcpt[test_data_collection[i][2]][1]
    p = round((test_data_collection[i][2]-min_prcpt)/prcpt_diff,2)
    w = round((test_data_collection[i][3]-min_wind)/wind_diff,2)
    t = round((test_data_collection[i][4]-min_temp)/temp_diff,2)
    # c1 = wind.get(w,[1,1])[0]*prcpt.get(p,[1,1])[0]
    # c2 = wind.get(w,[1,1])[1]*prcpt.get(p,[1,1])[1]

    c1 = prcpt.get(p,[1,1])[0]
    c2 = prcpt.get(p,[1,1])[1]

    prediction_base = random.choice([True, False])

    # c1 = temp.get(t,[1,1])[0]
    # c2 = temp.get(t,[1,1])[1]

    # c1 = wind.get(w,[1,1])[0]
    # c2 = wind.get(w,[1,1])[1]

    # c1 = prcpt.get(p,[1,1])[0]*temp.get(t,[1,1])[0]
    # c2 = prcpt.get(p,[1,1])[1]*temp.get(t,[1,1])[1]

    # c1 = wind.get(w,[1,1])[0]*temp.get(t,[1,1])[0]
    # c2 = wind.get(w,[1,1])[1]*temp.get(t,[1,1])[1]

    c1 = wind.get(w,[1,1])[0]*temp.get(t,[1,1])[0]*prcpt.get(p,[1,1])[0]
    c2 = wind.get(w,[1,1])[1]*temp.get(t,[1,1])[1]*prcpt.get(p,[1,1])[1]


    
    
    prediction = c1 > c2
    # print(test_data_collection[i][5], prediction)
    if test_data_collection[i][5] == prediction:
        correct+= 1
    else:
        wrong+=1
    
    if test_data_collection[i][5] == prediction_base:
        correct_base+= 1
    else:
        wrong_base+=1

accuracy = correct/(correct+wrong)

# print(temp,wind,prcpt)
# print(wind,temp,prcpt)
accuracy_base = correct_base/(correct_base+wrong_base)
print(correct, wrong, accuracy)
print(correct_base, wrong_base, accuracy_base)
# print(wind,temp,prcpt)