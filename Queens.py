"""
Queens.py
July 27, 2014
Description: Takes certain positions and places them on a 2D array representing a chessboard, then recursively searches for the maximum number of queens that
can be placed given the input queens.
"""

#initialize the blank board
board=[[" " for x in range(8)] for x in range(8)]


def getN():
	"""Obtains an integer between 1 and 8, verifies the input, and returns 
it for other functions."""
	n=0 #"dummy integer", allows while loop to start
	while type(n) is not int or n<1 or n>8:
		try:
			n=eval(input("Please input the number of queens to be solved for.\n"))
		except NameError:
			pass
	return n

def getQueensList():
	"""Obtains a 2-element list for each queen in a problem, places them in the space specified by the list, and marks spaces precluded by the inputted
queen.  Note to users: input is in form [x, y]."""
	qlist=[] #list of queen positions
	q=[0, 0] #"dummy list", allows while loop to start
	while type(q) is list:
		q=input("Please input a 2 element integer list [x, y].  A non-list ends the puzzle initialization.\n")
		try:
			q=eval(q)
		except NameError:
			break
		if type(q) is list:
			if len(q)!=2:
				print("List must be 2 elements.\n")
			elif q[0]<1 or q[0]>8 or q[1]<1 or q[1]>8:
				print("Invalid range.\n\n")
			elif type(q[0]) is not int or type(q[1]) is not int:
				print("Both elements must be integers.\n")
			else:
				qlist.append(q)
		else:
			break
	return qlist

def markX(pair, brd):
	"""Takes a position containing a queen and marks every square on the
board that the queen could go in one move.  Returns False if a queen is present in any of the spaces to be marked, returns True otherwise.  The boolean returns
act to end the program through function markQueens if the puzzle is invalid."""
	brdcopy=brd[:]
	noconflict=True
	for i in range(1, 9): #fills the row/diagonals with the queen
		if brdcopy[pair[0]-1][i-1]=="Q" and i!=pair[1]:
			noconflict=False
			break
		elif i==pair[1]:
			pass
		else:
			brdcopy[pair[0]-1][i-1]="x"
			if (pair[0]-1+pair[1]-i)>=0 and (pair[0]-1+pair[1]-i)<=7:
				if brdcopy[pair[0]-1+pair[1]-i][i-1]=="Q":
					noconflict=False
					break
				else:
					brdcopy[pair[0]-1+pair[1]-i][i-1]="x"

			if (pair[0]-1-pair[1]+i)>=0 and (pair[0]-1-pair[1]+i)<=7:
				if brdcopy[pair[0]-1-pair[1]+i][i-1]=="Q":
					noconflict=False
					break
				else:
					brdcopy[pair[0]-1-pair[1]+i][i-1]="x"
	for i in range(1, 9): #fills the column with the queen
		if brdcopy[i-1][pair[1]-1]=="Q" and i!=pair[0]:
			noconflict=False
			break
		elif i==pair[0]:
			pass
		else:
			brdcopy[i-1][pair[1]-1]="x"
	return (noconflict, brdcopy)

def markQueens():
	"""Takes a list of ordered pairs and places a queen for each pair in thespace given by the pair.  After queen is placed, each area that can no longer
legally hold a queen is marked as such.  A queen is marked with a 'Q' and an
invalid space is marked with an 'x'."""
	global board
	lst=getQueensList()
	cnum=0
	n=getN()
	for i in lst:
		board[i[0]-1][i[1]-1]="Q"
		if not markX(i, board)[0]:
			print("Intersecting Queens.\n")
			break
		cnum=cnum+1
	solver(board, cnum, n)

def solver(psol, qcount, n):
	"""Places a new queen in each possible space, marks off each newly invalid space, and try to
solve for the new partial solution."""
	nsol=psol[:]
	for i in range(8):
		if qcount==n:
			print("Count is met.")
			for k in nsol:
				print(k)
			print("About to break") #debug
			break
		for j in range(8):
			if nsol[i][j]==" ":
				nsol[i][j]="Q"
				nsol=markX([i+1, j+1], nsol)[1]
				ncount=qcount+1
				solver(nsol, ncount, n) 


markQueens()
