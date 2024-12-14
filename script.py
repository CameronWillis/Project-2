import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import into Pandas DataFrame
df = pd.read_csv('AmericanFootball98.csv')

df['team'] = df['team_code'].str.slice(0, 3) 
df['year'] = df['team_code'].str.slice(3) 


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
	
	plt.bar(range(2006,2020), df[df["team"] == "kan"][df["year"].astype(int) > 2005].sort_values(by="year", ascending=True)["wins"], color="skyblue")
	plt.title("Number of Wins by Year for Kansas City Chiefs")
	plt.xlabel("Year")
	plt.ylabel("Wins")
	plt.xticks(rotation=45)
	plt.tight_layout()

	plt.axvline(x=2012.5, color="red", linestyle="--", linewidth=1.5, label="new coach")

	plt.show()


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
	
	print("Strongest offensive line measured by fumbles ratio")
	for i in range(3):
		print(list(teams_ratio_fumble.keys())[i] + " has a fumble ratio of " + str(round(list(teams_ratio_fumble.values())[i], 4)) )
	
	print("Weakest offensive line measured by fumbles ratio")
	for i in range(3):
		print(list(teams_ratio_fumble.keys())[-i-1] + " has a fumble ratio of " + str(round(list(teams_ratio_fumble.values())[-i-1], 4)) )

# Question 5
if False:
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
if False:
	teams_avg_opp_points = {}
	for team in set(df['team']):	
		team_df = df[df['team'] == team]
		given = 0
		if len(team_df) == 2020 - 1999:
			
			for year in range(2015, 2020):
				given += int(team_df[ team_df["year"] == str(year)].iloc[0]["opp PF"])

			teams_avg_opp_points[team] = given / 5

	teams_avg_opp_points = dict(sorted(teams_avg_opp_points.items(), key=lambda item: item[1]))
	
	print("\n\nWhich defenses were the strongest between 2015-2019?")
	print("\nStrongest defense measured by opposition points given")
	for i in range(3):
		print(list(teams_avg_opp_points.keys())[i] + " gave an average of " + str(round(list(teams_avg_opp_points.values())[i], 4)) + " points" )
	
	print("\nWeakest defense measured by opposition points given")
	for i in range(3):
		print(list(teams_avg_opp_points.keys())[-i-1] + " gave an average of " + str(round(list(teams_avg_opp_points.values())[-i-1], 4)) + " points")

# Question 7
if False:
	teams_avg_opp_points = {}
	for team in set(df['team']):	
		team_df = df[df['team'] == team]
		given = 0
		if len(team_df) == 2020 - 1999:
			
			for year in range(1999, 2020):
				given += int(team_df[ team_df["year"] == str(year)].iloc[0]["opp PF"])

			teams_avg_opp_points[team] = given / 5

	teams_avg_opp_points = dict(sorted(teams_avg_opp_points.items(), key=lambda item: item[1]))
	
	print("\n\nWhich defenses were the strongest between 2015-2019?")
	print("\nStrongest defense measured by opposition points given")
	for i in range(3):
		print(list(teams_avg_opp_points.keys())[i] + " gave an average of " + str(round(list(teams_avg_opp_points.values())[i], 4)) + " points" )
	
	print("\nWeakest defense measured by opposition points given")
	for i in range(3):
		print(list(teams_avg_opp_points.keys())[-i-1] + " gave an average of " + str(round(list(teams_avg_opp_points.values())[-i-1], 4)) + " points")

if True:
	plt.figure(figsize=(10, 6))

	yearly_avg = df.groupby("year")["opp PF"].mean().reset_index()
	print(yearly_avg)
	plt.plot(range(1999,2020), yearly_avg["opp PF"], marker="o", color="blue", label="Average opp PF")

	print("Are defense getting stronger compared to offenses over time?")
	plt.title("Are defense getting stronger compared to offenses over time?")
	plt.xlabel("Year")
	plt.ylabel("Opposition Total Points")
	plt.xticks(range(1999,2020), rotation=45)
	plt.legend(title="Teams", loc="upper right")
	plt.grid(True, linestyle='--', alpha=0.5)

	# Show plot
	plt.tight_layout()
	plt.show()

# Question 8
if True:
	teams_year_int_ratio = []
	for code in df['team_code']:	

		row = df[code == df["team_code"]].iloc[0]
		value = row["pass td"] / row["int"]
		teams_year_int_ratio.append((value, row["team"], row["year"]))

	teams_year_int_ratio = sorted(teams_year_int_ratio, key=lambda x: -x[0])
	

	print("\n\nWhich team and year had the best td/int ratio?")
	for i in range(5):
		print(teams_year_int_ratio[i][1] + " in " + teams_year_int_ratio[i][2] + " had a td/int ratio of " + str(round(teams_year_int_ratio[i][0], 4)))
	



