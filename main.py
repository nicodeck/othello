import classes.randomGamePlayer as randomGP
import classes.naiveGamePlayer as naiveGP
import classes.minimaxGamePlayer as minimaxGP

print("This program shows the different features of the project on the game Othello.\nSee the report for the rules of the game.\n\n");

print("The first bot is a random bot, which plays random turns.\n")
print("Here, the first bot is player 1, and is playing against another random bot.\n")
print("Let's play 100 games and see who wins most!")
input("Press Enter to run the games...")

randomgp = randomGP.RandomGamePlayer()
randomgp.playNRandomGames(100)

print("The game is quite balanced, though player 2 gets a slight advantage when playing randomly")
input("Press Enter to continue to the next bot...")

print("The second bot is a naive player, which plays the turn that gives the best gain for that one turn, not predicting future outcome.")
print("Here, the naive player is player 1, which plays against a random bot")
input("Press Enter to run the games...")

naivegp = naiveGP.NaiveGamePlayer()
naivegp.playNNaiveGames(100)

print("Even a naive player wins a lot against a random player")
print("However, does a naive player win that much against a more advanced player?")
print("The third bot uses the minimax algorithm to predict the best turn with a greater depth")
print("Let's see how the minimax bot wins against the naive player with a depth of 2")
input("Press Enter to run the games...")

minimaxgp = minimaxGP.MinimaxGamePlayer()
minimaxgp.playNMinimaxGames(100, 2)

print("With the depth of 2, the minimax bot already has a great win rate against a naive player")
print("Let's see if a minimax bot with a depth of 3 has a greater win rate against the same naive player")
input("Press Enter to run the games...")

minimaxgp.playNMinimaxGames(100, 3)

print("The depth-of-3 minimax bot crushes the naive player!")
