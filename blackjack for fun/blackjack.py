from random import randint
import os

name = raw_input("Hello player! What is your name? ")
print """
Welcome %s to the game of blackjack!
Try to beat the dealer
and win some money!""" % name
chips = int(raw_input("How much do you want to start with? "))
min_bet = 5

game_on = True
play_on = True


# Pull a random number from 1 to 13
# deck1 = randint(7,10)
# deck2 = randint(2,11)
# deck3 = randint(2,11)
while play_on:
    while game_on:
        player_total = 0
        dealer_total = 0
        print "You have %d chips" % chips
        print "Minimum bet is 5."
        playing_bet = int(raw_input("Place your bets: "))
        if playing_bet < min_bet:
            print "Please bet the min or more. Thanks"
        elif playing_bet >= min_bet:
            player_total += randint(1,10)
            print "You have a %d" % player_total
            dealer_total += randint(1,10)
            print "Dealer has a %d" % dealer_total
            player_total += randint(1,11)
            print "Your total is now: %d" % player_total
            dealer_total += randint(1,11)
            if player_total == 21:
                print "You have 21!"
                chips += playing_bet * 3 
            if player_total < 21:
                while player_total < 21:
                    choice = raw_input("Do you want to hit or stay? [hit/stay] ")
                    if choice == "hit":
                        player_total += randint(1,11)
                        print "You now have %d" % player_total
                        if player_total == 21:
                            print "You win!"
                            chips += playing_bet * 2
                        elif player_total > 21:
                            print "Bust! You went over 21"
                            chips = chips - playing_bet
                            print "You have %d chips left" % chips
                            raw_input("Hit any key to continue. ")
                            os.system("clear")
                            break
                    elif choice == "stay":
                        print "You are staying at %d" % player_total
                        break
            elif player_total > 21:
                print "Bust! You went over 21"
                chips = chips - playing_bet
                print "You have %d chips left" % chips
                raw_input("Hit any key to continue. ")
                os.system("clear")
                break
            print dealer_total
            if dealer_total <= 16:
                while dealer_total <= 16:
                    print "Dealer has %d" % dealer_total
                    dealer_total += randint(1,11)
                    if dealer_total <= 16:
                        dealer_total += randint(1,11)
                    if dealer_total == player_total:
                        print "Dealer dealt %d" % dealer_total
                        print "Tie"
                        raw_input("Hit any key to continue. ")
                        os.system("clear")
                        break
                    if dealer_total > player_total and dealer_total < 21:
                        print "Dealer dealt %d" % dealer_total
                        print "Dealer wins"
                        chips = chips - playing_bet
                        print "You lost %d chips" % playing_bet
                        raw_input("Hit any key to continue. ")
                        os.system("clear")
                        break
                    if dealer_total < player_total and dealer_total < 21:
                        print "Dealer dealt %d" % dealer_total
                        print "You win!"
                        chips += playing_bet * 2
                        raw_input("Hit any key to continue. ")
                        os.system("clear")
                        break
                    elif dealer_total < player_total and player_total > 21:
                        print "Bust!"
                        chips -= playing_bet    
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
                    
            