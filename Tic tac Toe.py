'''The Following is a TIC TAC TOE game designed for users to enjoy playing the game both with the AI and with their friends...
Enjoy Playing the game...
Author....VJ 13 SS
Last modified.... 3:45 21 December 2023
'''
def user1turn(board):
	pos=int(input('Enter X"s position[1,2,3...9]: '))
	if(board[pos-1]!=0):
		print('Wrong Move....')
		exit(0)
	board[pos-1]=-1

def user2turn(board):
	pos=int(input('Enter O"s position[1,2,...9]: '))
	if(board[pos-1]!=0):
		print('Wrong Move....')
		exit(0)
	board[pos-1]=1

def Current_board(board):
	print('Current board state....')
	for i in range(0,9):
		if(i>0 and i%3==0):
			print('\n')
		if(board[i]==0):
			print('_',end=' ')
		if(board[i]==-1):
			print('X',end=' ')
		if(board[i]==1):
			print('O',end=' ')
	print('\n\n')

def Compturn(board):
	pos=-1
	value=-2#possible values -1,1,0
	for i in range(0,9):
		if(board[i]==0):
			board[i]=1
			score=-minmax(board,-1)
			board[i]=0
			if(score>value):
				value=score
				pos=i
	board[pos]=1
def minmax(board,player):
	x=analyseboard(board)
	if(x!=0):
		return x*player
	pos=-1
	value=-2#possible values -1,1,0
	for i in range(0,9):
		if(board[i]==0):
			board[i]=player
			score=-minmax(board,player*-1)#next player..current player*-1..x=-1..for O...-1*-1
			board[i]=0
			if(score>value):
				value=score
				pos=i
	if(pos==-1):#if board is filled or anyone has won
		return 0
	return value#propagating highest value to the top of the tree(back tracking using recursion)
def analyseboard(board):
	cb=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
	for i in range(0,8):#8 winning conditions
		if((board[cb[i][0]])!=0 and (board[cb[i][0]])==(board[cb[i][1]]) and (board[cb[i][1]])==(board[cb[i][2]])):
			return board[cb[i][0]]
	return 0

def main():
	choice=int(input('\nEnter 1 for single player and 2 for miltiplayer: '))
	board=[0,0,0,0,0,0,0,0,0]
	if(choice==1):#code for ai
		print('Computer:O vs. You:X')
		player=int(input('Enter to play 1st or 2nd: '))
		for i in range(0,9):
			if(analyseboard(board)!=0):
				break
			if((i+player)%2==0):
				Compturn(board)
			else:
				Current_board(board)
				user1turn(board)								
	if(choice==2):#code for multiplayer
		for i in range(0,9):
			if(analyseboard(board)!=0):
				break
			if(i%2==0):
				Current_board(board)
				user1turn(board)
			else:
				Current_board(board)
				user2turn(board)
					
	x=analyseboard(board)
	
	if(x==0):
		Current_board(board)
		print('Draw...')
	if(x==-1):
		Current_board(board)
		print('X has won')
	if(x==1):
		Current_board(board)
		print('O has won')
main()