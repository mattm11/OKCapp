import pandas as pd
import numpy as np

shots_data = pd.read_csv("/Users/17027/Desktop/OKCapp/shots_data.csv")


teamA = shots_data.loc[(shots_data['team'] == "Team A")]
teamB = shots_data.loc[(shots_data['team'] == "Team B")]

# Corner 3 is where Y <= 7.8 and X >= 22
Corner3 = (abs(shots_data['x']) >= 22) & (abs(shots_data['y']) <= 7.8)

# Non Corner 3 is where Y > 7.8 and x^2 + y^2 > 23.75^2
NonCorner3 = ((shots_data['x'] ** 2) + (shots_data['y'] ** 2) >= 23.75 ** 2) & (abs(shots_data['y']) > 7.8)

TwoPoint = ~Corner3 & ~NonCorner3

total_C3 = shots_data.loc[Corner3]
total_NC3 = shots_data.loc[NonCorner3]
total_2PT = shots_data.loc[TwoPoint]

teamA_C3 = total_C3.loc[total_C3['team'] == "Team A"]
teamA_NC3 = total_NC3.loc[total_NC3['team'] == "Team A"]
teamA_2PT = total_2PT.loc[total_2PT['team'] == "Team A"]

teamB_C3 = total_C3.loc[total_C3['team'] == "Team B"]
teamB_NC3 = total_NC3.loc[total_NC3['team'] == "Team B"]
teamB_2PT = total_2PT.loc[total_2PT['team'] == "Team B"]

teamA_C3_made = (np.sum(teamA_C3['fgmade'] == 1))
teamA_C3_missed = (np.sum(teamA_C3['fgmade'] == 0))
teamA_C3_attempted = teamA_C3_made + teamA_C3_missed
teamA_C3_pct = teamA_C3_made / teamA_C3_attempted

teamA_NC3_made = (np.sum(teamA_NC3['fgmade'] == 1))
teamA_NC3_missed = (np.sum(teamA_NC3['fgmade'] == 0))
teamA_NC3_attempted = teamA_NC3_made + teamA_NC3_missed
teamA_NC3_pct = teamA_NC3_made / teamA_NC3_attempted

teamA_2PT_made = (np.sum(teamA_2PT['fgmade'] == 1))
teamA_2PT_missed = (np.sum(teamA_2PT['fgmade'] == 0))
teamA_2PT_attempted = teamA_2PT_made + teamA_2PT_missed
teamA_2PT_pct = teamA_2PT_made / teamA_2PT_attempted

teamB_C3_made = (np.sum(teamB_C3['fgmade'] == 1))
teamB_C3_missed = (np.sum(teamB_C3['fgmade'] == 0))
teamB_C3_attempted = teamB_C3_made + teamB_C3_missed
teamB_C3_pct = teamB_C3_made / teamB_C3_attempted

teamB_NC3_made = (np.sum(teamB_NC3['fgmade'] == 1))
teamB_NC3_missed = (np.sum(teamB_NC3['fgmade'] == 0))
teamB_NC3_attempted = teamB_NC3_made + teamB_NC3_missed
teamB_NC3_pct = teamB_NC3_made / teamB_NC3_attempted

teamB_2PT_made = (np.sum(teamB_2PT['fgmade'] == 1))
teamB_2PT_missed = (np.sum(teamB_2PT['fgmade'] == 0))
teamB_2PT_attempted = teamB_2PT_made + teamB_2PT_missed
teamB_2PT_pct = teamB_2PT_made / teamB_2PT_attempted

print("Team A Corner 3 eFG: ", teamA_C3_pct * 100, "%")
print("Team A Corner 3 shot distribution: ", (teamA_C3_attempted / (teamA_C3_attempted + teamA_NC3_attempted + teamA_2PT_attempted) * 100), "%")

print("Team A Non-Corner 3 eFG: ", teamA_NC3_pct * 100, "%")
print("Team A Non-Corner 3 shot distribution: ", (teamA_NC3_attempted / (teamA_C3_attempted + teamA_NC3_attempted + teamA_2PT_attempted) * 100), "%")

print("Team A 2-Pointer eFG: ", teamA_2PT_pct * 100, "%")
print("Team A 2-Pointer shot distribution: ", (teamA_2PT_attempted / (teamA_C3_attempted + teamA_NC3_attempted + teamA_2PT_attempted) * 100), "%")

print("Team B Corner 3 eFG: ", teamB_C3_pct * 100, "%")
print("Team B Corner 3 shot distribution: ", (teamB_C3_attempted / (teamB_C3_attempted + teamB_NC3_attempted + teamB_2PT_attempted) * 100), "%")

print("Team B Non-Corner 3 eFG: ", teamB_NC3_pct * 100, "%")
print("Team B Non-Corner 3 shot distribution: ", (teamB_NC3_attempted / (teamB_C3_attempted + teamB_NC3_attempted + teamB_2PT_attempted) * 100), "%")

print("Team B 2-Pointer eFG: ", teamB_2PT_pct * 100, "%")
print("Team B 2-Pointer shot distribution: ", (teamB_2PT_attempted / (teamB_C3_attempted + teamB_NC3_attempted + teamB_2PT_attempted) * 100), "%")