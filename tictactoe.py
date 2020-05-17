# A simple tic-tac-toe game
#Spring 2020 
#Dil Rawat : YSU

#list of 3 by 3 grid
import itertools


#checking winner horizantally
def win(current_game):

	def all_same(l):
		if l.count(l[0]) == len(l) and l[0] != 0:
			return True
		else:
			return False

	for row in game:
		print(row)
		if all_same(row):
			print ("Won horizantally by Player: %s"  %row[0])
			return True
		#diagonal winner
	diags = []
	for col, row in enumerate(reversed(range(len(game)))):
		diags.append(game[row][col])
	if all_same(diags):
		#print(f"Player {diags[0]} is the winner diagonally (/)")
		print ("Won diagonally(/) by Player: %s"  %diags[0])
		return True

	diags = []
	for counter in range(len(game)):
		diags.append(game[counter][counter])
	if all_same(diags):
		#print(f"Player {diags[0]} is the winner diagonally (\\)")
		print ("Won diagonally(\\) by Player: %s"  %diags[0])
		return True

	#checking winner vertically
	for col in range(len(current_game)):
		check = []
		
		for row in current_game:
			check.append(row[col])

		if all_same(check):
			#print(f"Player {check[0]} is the winner vertically")
			print ("Won vertically by Player: %s"  %check[0])
			return True
	return False

def game_board(game_map, player = 0, row= 0, column= 0,display= False):
	try:
		if game_map[row][column] !=0: 
			print("This position is occupied. choose another.")
			return game_map, False
		#column index (  0  1  2)
		print("   "+"  ".join([str(i) for i in range(len(game_map))]))
		if not display:
			game_map[row][column] = player
		for count, row in enumerate(game_map):
			print(count, row)
		return game_map, True

	except IndexError as e:
		print("Error: make sure to enter 0, 1 ,or 2", e)
		return game_map, False
	except Exception as e:
		print("Something went wrong",e)
		return game_map, False

play = True
players = [1,2]
while play:
	game_size = int(input("Choose size for the Tic Tac Toe? : "))
	game = [[0 for i in range(game_size)] for i in range(game_size)]

	game_won = False
	game, _ = game_board(game, display = True)
	player_choice = itertools.cycle([1,2])
	while not game_won:
		current_player = next(player_choice)
		print("Current Player:%s " % current_player)
		played = False

		while not played:
			column_choice = int(input("Enter column you want to play (0,1,2):"))
			row_choice = int(input("Enter row you want to play (0,1,2):"))
			game, played = game_board(game, current_player, row_choice, column_choice)
		if win(game):
			game_won = True
			again = input("The game is over. Want to play again? (y/n)")
			if again.lower() == "y":
				print("restarting")
			elif again.lower() == "n":
				print("See you next time.")
				play= False
			else: 
				print("Not a valid answer. See you later.")
				play = False


#game = game_board(game, display = True)
#game = game_board(game_board, player= 1, row= 2, column=1)