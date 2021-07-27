# Prints out all numbers from n to zero
def countdown(n):
	if (n == 0):
		return 

	print(n)
	return countdown(n - 1)


# Generate the nth fibonacci number
# fib(n) = fib(n-2) + fib(n-1)
def fib(n):

	if n == 0:
		return 0

	if n == 1:
		return 1

	# Trying to return fib_n
	# fib_{n-2} = fib(n-2)
	# fib_{n-1} = fib(n-1)
	# fib_n = fib(n-2) + fib(n-1)

	return fib(n - 2) + fib(n - 1)


# There are n steps. You are allowed to jump 1, 2, or 3 steps up. 
# What are the number of ways to reach the top step?

# The number of ways to reach the nth step either jumping 1, 2, or 3
def num_ways(n):
	if n == 0:
		return 1

	if n == 1:
		return 1

	if n == 2:
		return 2

	return num_ways(n-1) + num_ways(n-2) + num_ways(n-3)

"""
You are a professional robber planning to rob houses along a street. 

Each house has a certain amount of money stashed, the only constraint 
stopping you from robbing each of them is that adjacent houses have 
security systems connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each 
house, return the maximum amount of money you can rob tonight without 
alerting the police.

[1, 4, 3, 7, 8, 2]

[1, 3, 8]
[4, 7, 2]
[4, 8]

"""

def house_robber(houses):


	# Up to the ith house, the maximum I can get from robbing
	def DFS(i):
		if i == 0:
			return houses[0]

		if i ==1:
			return max(houses[1], houses[0])

		return max(DFS(i-1), DFS(i-2) + houses[i])

	return DFS(len(houses) - 1)


"""

Given two strings, find the length of the longest common subsequence

s1 = "ABCDEA"
s2 = "ACZEAY"
  
'AB'
'BZ'

DFS('AB', 'BZ')

max(DFS('AB', 'B'), DFS('A', 'BZ'))



i == 1
s1[:1]

  2
'A'
''
 1
"""
def longest_common_subsequence(s1, s2):

	# This function always returns the length of the longest common subsequence
	# of strings s1[:i] and s2[:j]
	@lru_cache(None)
	def DFS(i, j):
		if i == 0 or j == 0:
			return 0

		# If characters match up, add 1 to the previous
		if s1[i-1] == s2[j-1]:
			return 1 + DFS(i-1, j-1)
		else:
			return max(DFS(i-1, j), DFS(i, j-1))

	return DFS(len(s1)+1, len(s2)+1)

	dp = []
	for i in range(len(s1)+1):
		new_row = []
		for j in range(len(s2)+1):
			new_row.append(0)

		dp.append(new_row)

	for i in range(1, len(s1)+1):
		for j in range(1, len(s2)+1):
			if s1[i-1] == s2[j-1]:
				dp[i][j] = dp[i-1][j-1] + 1
			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])

	
	return dp[len(s1)][len(s2)]




