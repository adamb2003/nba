# NBA Fantasy

EV Generator and Squad Solver for NBA Fantasy (Salary Cap Edition)

Sign up and play here: https://nbafantasy.nba.com/

## Important Instructions

### team.json

Replace the team.json found in the data file with that of your own team!

You can find this here: https://nbafantasy.nba.com/api/my-team/{YOUR_ID}/

You must be logged in, and you can find your ID in the URL if you navigate to your gameday history.

### HiGHS

This solver uses HiGHS, make sure you have it downloaded and included in your environment path.

### Running the Code

After you've done this, navigate to the code folder and run _run_solve.py_ and it should work.

EV and Solve will be found in the output folder following a successful run.

## Data

Player data in the repository is taken from Hashtag Basketball (as of 6/2/25). If you'd like to update this, you can replace the content in hashtag_Season.csv by copying and pasting from here: https://hashtagbasketball.com/fantasy-basketball-rankings

Team defensive data in the repository is taken from the official NBA stats website (as of 6/10/25). If you'd like to update this, you can replace the content in team_def_data_2425.csv by copying and pasting from here (important that it's PER GAME): https://www.nba.com/stats/teams/opponent

When you first run the code, it will pull player information (Cost, Injury Status, etc) and fixture information from the NBA Fantasy API. This also generates CSV files, however, you can change the setting "info_source" to be blank if you don't want to refresh these, saving time.

## Settings

You can find default settings in run_solve.py

### EV Settings

decay: How much EV is decayed by gameweek

home: Home advantage EV multiplier

away: Away disadvantage EV multiplier

value_cutoff: Average EV divided by Player Cost threshold to be included in solve.

transfer_penalty: Dictionary of EV penalty applied if transfer occurs on that gameday.

### Gameday Range

Here you set the range of gamedays that you would like to solve between (inclusive).

I normally solve for 3 gameweeks at a time, which is usually 21 gamedays.

### Player Settings

locked: List of IDs to lock in team

banned: List of IDs to ban from team

gd_banned: List of IDs to ban from team for only next Game Day

### Chip Settings

wildcard: Use Wildcard (True or False)

allstar: Use All-Star (True or False)

day_solve: Choose to solve just the All-Star day (True) or a normal solve ignoring that day (False)

allstar_day: The gameday that the All-Star chip is used on i.e. "Gameweek 25 - Day 6"

### Solver Settings

max_time: Max time in seconds to allow for the solve.

gap: Optimality Gap

info_source: Default is "API", but make this blank if you just want it to pull from saved CSV files.
