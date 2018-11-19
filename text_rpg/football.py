# Making a football game using text_rpg mechanis

import os
import random

user_player = raw_input("Hello player, what is your name? ")
home_team = raw_input("Enter your football team: ")
away_team = raw_input("Who's the oppopsing team: ")
homeScore = 0
awayScore = 0
yards_gained = 0
downs = 1

print """
First team to 21 wins!!!
%s vs %s 
""" % (home_team, away_team)

gamemode = raw_input("Offense or Defense first? ")

if gamemode == 'offense':
    home_field_pos = random.randint(1, 51)
    print home_field_pos

    print "%s are starting on their own %d." % (home_team, home_field_pos)
    while home_field_pos < 100:
        home_play = raw_input("Select play: rush or pass ")
        if home_play == 'rush':
            run_yard = random.randint(1,11)

            if run_yard % 2 == 0:
                yards_gained += run_yard
                home_field_pos += run_yard
                print "%s gained %d yards, and now on the %d" % (home_team, run_yard, home_field_pos)
            else:
                home_field_pos -= run_yard
                print "%s lost %d yards, and now on the %d" % (home_team, run_yard,home_field_pos)

            if yards_gained >= 10:
                print "First Down %s" % home_team

            if home_field_pos == 100:
                homeScore += 1
                print "%s %d - %d %s" % (home_team, homeScore, awayScore, away_team)

        elif home_play == 'pass':
            pass_yard = random.randint(1,11)
            
            if pass_yard % 2 == 0:
                yards_gained += pass_yard
                home_field_pos += pass_yard
                print "%s gained %d yards, and now on the %d" % (home_team, pass_yard, home_field_pos)
            else:
                home_field_pos -= pass_yard
                print "%s lost %d yards, and now on the %d" % (home_team, pass_yard,home_field_pos)

            if yards_gained >= 10:
                print "First Down %s" % home_team

            if home_field_pos == 100:
                homeScore += 1
                print "%s %d - %d %s" % (home_team, homeScore, awayScore, away_team)   
            
        
    
if gamemode == 'defense':
    away_field_pos = random.randint(1, 51)
    print "%s starting on the %d yard line" % (away_team, away_field_pos)
    playType = raw_input("Defense play: Rush or Man Coverage ")
    dplay = random.randint(1,101)
    print dplay
    # if dplay % 2 == 0:
        