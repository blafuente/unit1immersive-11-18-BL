from random import randint
import os
import time

name = raw_input("Hello player! What is your name? ")
print """
Welcome %s to the game of blackjack!
Try to beat the dealer
and win some money!
          _____
         |A .  | _____
         | /.\ ||10^  | _____
         |(_._)|| / \ ||A _  | _____
ejm98    |  |  || \ / || ( ) ||J_ _ |
         |____V||  .  ||(_'_)||( v )|
                |___10||  |  || \ / |
                       |____V||  .  |
                              |____J|""" % name

min_bet = 5

game_on = True
play_on = True

while play_on:
    chips = int(raw_input("How much chips  do you want to start with? "))
    while game_on == True and chips > 0:
        
        player_total = 0
        dealer_total = 0
        print "You have %d chips" % chips
        print "Minimum bet is 5."
        playing_bet = int(raw_input("Place your bet[0 to quit]:  "))
        if playing_bet > 0 and playing_bet < min_bet:
            print "Please bet the min or more. Thanks"
        if playing_bet == 0:
            print "Come back again and good luck!"
            game_on = False
            play_on = False
        elif playing_bet >= min_bet:
            print "Dealing..."
            print """
.----------------.
|  _ _   MMMMM   |
| ( " ) | o o |  |
|  `.'   \ - /   |
|  |/  ---`W'--. |
|  |\ |     .-') |
|     |  .-'   ) |
|     .-'      ) |
|  .-'      .-'  |
| (      .-'     |
| (   .-'  |     |
| (.-'     | \|  |
| '--.M.---  /|  |
|   / - \   .^.  |
|  | o o | ( . ) |
|   WWWWW   " "  |  VK
`----------------'"""
            time.sleep(1)
            player_total += randint(6,10)
            print "You first card is %d" % player_total
            time.sleep(1)
            dealer_total += randint(5,10)
            print "Dealer has a %d and a face down card" % dealer_total
            time.sleep(1)
            player_total += randint(1,11)
            print "Your total is now: %d" % player_total
            dealer_total += randint(8,10)
            if player_total == 21:
                print "You have 21!"
                chips += playing_bet * 3 
            if player_total > 21:
                print "Bust! You went over 21"
                chips = chips - playing_bet
                print "You have %d chips left" % chips
                raw_input("Hit any key to continue. ")
                os.system("clear")
                break
            if player_total < 21:
                while player_total < 21:
                    choice = raw_input("Do you want to hit or stay? [hit/stay] ")
                    if choice == "hit":
                        print "Dealing..."
                        time.sleep(1)
                        player_total += randint(1,11)
                        print "You now have %d" % player_total
                        if player_total == 21:
                            print "You win!"
                            chips += playing_bet * 2
                            raw_input("Hit any key to continue. ")
                            os.system("clear")
                            break
                        elif player_total > 21:
                            print "Bust! You went over 21"
                            chips = chips - playing_bet
                            print "You have %d chips left" % chips
                            raw_input("Hit any key to continue. ")
                            os.system("clear")
                            break
                    elif choice == "stay":
                        print "You are staying at %d" % player_total
                        break; 
            
           
            if dealer_total >= 13 and dealer_total < 21 and player_total < 21:
                while dealer_total <= 21:
                    print "Dealer has %d" % dealer_total
                    # dealer_total += randint(1,5)
                    # print "Dealing is hitting.."
                    # time.sleep(1)
                    if dealer_total > 21 and player_total < 21:
                        print "Dealer has %d" % dealer_total
                        print "Dealer bust, you win"
                        chips += playing_bet * 2
                        print "You won %d chips" % (playing_bet*2)
                        raw_input("Hit any key to continue. ")
                        os.system("clear")
                    if dealer_total >13 and dealer_total < 16:
                        print "Dealing is hitting.."
                        time.sleep(1)
                        dealer_total += randint(1,5)
                        print "Dealer now has %d" % dealer_total
                    if dealer_total == player_total:
                        # print "Dealer dealt %d" % dealer_total
                        print "Tie. No chips won."
                        raw_input("Hit any key to continue. ")
                        os.system("clear")
                        break
                    if dealer_total > player_total and dealer_total <= 21:
                        # print "Dealer dealt %d" % dealer_total
                        print "Dealer wins"
                        chips = chips - playing_bet
                        print "You lost %d chips" % playing_bet
                        raw_input("Hit any key to continue. ")
                        os.system("clear")
                        break
                    if dealer_total < player_total and dealer_total < 21:
                        # print "Dealer dealt %d" % dealer_total
                        print "You win!"
                        chips += playing_bet * 2
                        print "You won %d chips" % (playing_bet*2)
                        raw_input("Hit any key to continue. ")
                        os.system("clear")
                        break
                    elif dealer_total < player_total and player_total > 21:
                        print "Bust!"
                        chips -= playing_bet
                        raw_input("Hit any key to continue. ")
                        os.system("clear")
        if chips == 0 and chips <= 0:                    
            play_again = raw_input("Do you want to play again? [yes/no] ")
            if (play_again == "no"):
                play_on = False
                game_on = False
                os.system("clear")
            elif play_again == "yes":
                play_on = True 
                os.system("clear")
            else:
                print "huh?"
                    
            