"""
Solver for Light Up puzzles
"""

def pretty_print(shaded,nums,lights,x_dim,y_dim):
	for y in range(y_dim):
		for x in range(x_dim):
			if (x,y) in lights:
				print('*',end='')
			elif (x,y) in nums:
				print(nums[(x,y)],end='')
			elif (x,y) in shaded:
				print('#',end='')
			else:
				print(' ',end='')
		print()

def num_check(lights,nums):
	for pt,count in nums.items():
		x,y = pt
		if count != sum((x+dx,y+dy) in lights for dx,dy in ((0,1),(0,-1),(1,0),(-1,0))):
			return False
	return True

def illuminate(pt,shaded,x_dim,y_dim):
	x,y = pt
	lit = { pt }
	for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)):
		nx,ny = x+dx,y+dy
		while nx >= 0 and nx < x_dim and ny >= 0 and ny < y_dim and (nx,ny) not in shaded:
			lit.add((nx,ny))
			nx,ny = nx+dx,ny+dy
	return lit

def search(opens,shaded,nums,lights,litup,x_dim,y_dim,i):
	if set(opens) == litup and num_check(lights,nums):
		pretty_print(shaded,nums,lights,x_dim,y_dim)
	elif i < len(opens):
		if opens[i] not in litup:
			next_lights = { *lights,opens[i] }
			next_litup  = { *litup,*illuminate(opens[i],shaded,x_dim,y_dim) }
			search(opens,shaded,nums,next_lights,next_litup,x_dim,y_dim,i+1)
		search(opens,shaded,nums,lights,litup,x_dim,y_dim,i+1)

def solve(board):

	x_dim,y_dim = len(board[0]),len(board)

	shaded = set()
	opens  = set()
	nums   = dict()

	for idx,char in enumerate(''.join(board)):
		pt = (idx%x_dim,idx//x_dim)
		if char == '.':
			opens.add(pt)
		elif char == '#':
			shaded.add(pt)
		elif char in '0123456789':
			shaded.add(pt)
			nums[pt] = int(char)

	search(sorted(opens),shaded,nums,set(),set(),x_dim,y_dim,0)

if __name__ == "__main__":

	solve(	['.......',
			 '#.....2',
			 '.#0.1#.',
			 '.......',
			 '.0#.02.',
			 '#.....#',
			 '.......'] )
