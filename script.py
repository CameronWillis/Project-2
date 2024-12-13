import pandas as pd
import numpy as np

df = pd.read_csv('AmericanFootball98.csv')

df['team'] = df['team_code'].str.slice(0, 3) 
df['year'] = df['team_code'].str.slice(3) 
del df['team_code']

# Question 1
if False:
	teams_delta_wins = {}
	for team in set(df['team']):	
		team_df = df[df['team'] == team]
		if len(team_df) == 2020 - 1999:
			
			early_total = 0
			late_total  = 0

			for year in range(2015, 2020):
				late_total += int(team_df[ team_df["year"] == str(year)].iloc[0]["wins"])
			
			for year in range(1999, 2004):
				early_total += int(team_df[ team_df["year"] == str(year)].iloc[0]["wins"])

			teams_delta_wins[team] = (late_total - early_total)/5

	teams_delta_wins = dict(sorted(teams_delta_wins.items(), key=lambda item: item[1]))

	print("Question 1: Which team gained/lost the most wins per season between 1999-2003 and 2015-2019")
	print(list(teams_delta_wins.keys())[-1] + " changed " + str(list(teams_delta_wins.values())[-1]))
	print(list(teams_delta_wins.keys())[0]  + " changed " + str(list(teams_delta_wins.values())[0]))

# Question 2
if False:
	early_total = 0
	late_total  = 0

	for year in range(2006, 2013):
		early_total += int(df[df["year"] == str(year)][df["team"] == "kan"].iloc[0]["wins"])
		
	for year in range(2013, 2020):
		late_total += int(df[df["year"] == str(year)][df["team"] == "kan"].iloc[0]["wins"])

	print("\nHow did Kansas City Chiefs stats change with a new coach in 2013?")
	print("Avg wins during 2006 - 2013: " + str(early_total / 7))
	print("Avg wins during 2013 - 2019: " + str(late_total / 7))
	print("Change in avg wins after new coach: " + str((late_total - early_total) / 7))
	   
# Question 3
if False:
	teams_delta_pen = {}
	for team in set(df['team']):	
		team_df = df[df['team'] == team]
		if len(team_df) == 2020 - 1999:
			
			for year in range(1999, 2020):
				late_total += int(team_df[ team_df["year"] == str(year)].iloc[0]["opp penalties"])

			teams_delta_pen[team] = (late_total - early_total)/21

	teams_delta_pen = dict(sorted(teams_delta_pen.items(), key=lambda item: item[1]))
	
	print("Which team get most favor during penalties?")
	for i in range(5):
		print(list(teams_delta_pen.keys())[-i-1] + " get given an average of " + str(int(list(teams_delta_pen.values())[-i-1])) + " penalties")
	
# Question 4
if False:
	teams_ratio_fumble = {}
	for team in set(df['team']):	
		team_df = df[df['team'] == team]
		fumbles = 0
		completions = 0
		if len(team_df) == 2020 - 1999:
			
			for year in range(2015, 2020):
				fumbles += int(team_df[ team_df["year"] == str(year)].iloc[0]["Fumbles Lost"])
				completions += int(team_df[ team_df["year"] == str(year)].iloc[0]["completions"])

			teams_ratio_fumble[team] = fumbles / (completions + fumbles) 

	teams_ratio_fumble = dict(sorted(teams_ratio_fumble.items(), key=lambda item: item[1]))
	
	print("Strongest offensive line measured by fumbles ratio")
	for i in range(3):
		print(list(teams_ratio_fumble.keys())[i] + " has a fumble ratio of " + str(round(list(teams_ratio_fumble.values())[i], 4)) )
	
	print("Weakest offensive line measured by fumbles ratio")
	for i in range(3):
		print(list(teams_ratio_fumble.keys())[-i-1] + " has a fumble ratio of " + str(round(list(teams_ratio_fumble.values())[-i-1], 4)) )

# Question 5
if True:
	teams_best_streak = {}
	for team in set(df['team']):	
		team_df = df[df['team'] == team]
		
		if len(team_df) == 2020 - 1999:
			
			best_score = -1
			best_year = -1
			for year in range(1999, 2015):
				
				score = 0	
				for inc in range(5):
					score += team_df[ team_df["year"] == str(year + inc)].iloc[0]["wins"]
					
				score /= 5
				if score > best_score:
					best_year  = year
					best_score = score
				
			teams_best_streak[team] = (best_score, int(best_year))
			
	teams_best_streak = dict(sorted(teams_best_streak.items(), key=lambda item: item[1][0]))
	print("Best 5-year streak by team")
	for i in range(10):
		start_year = str(list(teams_best_streak.values())[-i-1][1])
		end_year = str(list(teams_best_streak.values())[-i-1][1] + 5)
		print(list(teams_best_streak.keys())[-i-1] + " avg season wins " + str(list(teams_best_streak.values())[-i-1][0]) + " wins over " + start_year + "-" + end_year)
	
# Question 6
if True:
	teams_ratio_fumble = {}
	for team in set(df['team']):	
		team_df = df[df['team'] == team]
		fumbles = 0
		completions = 0
		if len(team_df) == 2020 - 1999:
			
			for year in range(2015, 2020):
				fumbles += int(team_df[ team_df["year"] == str(year)].iloc[0]["Fumbles Lost"])
				completions += int(team_df[ team_df["year"] == str(year)].iloc[0]["completions"])

			teams_ratio_fumble[team] = fumbles / (completions + fumbles) 

	teams_ratio_fumble = dict(sorted(teams_ratio_fumble.items(), key=lambda item: item[1]))
	
	print("Strongest defense measured by opposition yd/play")
	for i in range(3):
		print(list(teams_ratio_fumble.keys())[i] + " has a fumble ratio of " + str(round(list(teams_ratio_fumble.values())[i], 4)) )
	
	print("Weakest offensive line measured by fumbles ratio")
	for i in range(3):
		print(list(teams_ratio_fumble.keys())[-i-1] + " has a fumble ratio of " + str(round(list(teams_ratio_fumble.values())[-i-1], 4)) )
	
