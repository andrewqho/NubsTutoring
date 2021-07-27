"""
You are given an integer array cost where cost[i] is the cost of ith step 
on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Input: cost = [10,15,20]
Output: 15
Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.

"""

def minCost(costs):

	# the minimum cost of reaching the ith step
	# either come from step before (i - 1) or two steps before (i - 2)
	costs.append(0)
	states = {}
	def DFS(i):
		if (i < 2):
			return costs[i]
		if i in states:
			return states[i]

		states[i] = min(DFS(i - 2) + costs[i], DFS(i - 1) + costs[i])

		return states[i]

	return DFS(len(costs) - 1)

def minCost_dp(costs):
	#dp[i] == DFS(i)
	costs.append(0)
	dp = list(range(0, len(costs)))

	for i in range(len(dp)):
		if (i < 2):
			dp[i] = costs[i]
		else:
			dp[i] = min(dp[i - 2] + costs[i], dp[i - 1] + costs[i])

	return dp[-1]	


def minCost_dp_opt(costs):
	#dp[i] == DFS(i)
	costs.append(0)
	
	# prev_i stands for i steps back
	prev1 = costs[1]
	prev2 = costs[0]
	
	for i in range(2, len(costs)):
		curr = min(prev2 + costs[i], prev1 + costs[i])

		prev2 = prev1
		prev1 = curr

	return prev1

	dp = list(range(0, len(costs)))

	for i in range(len(dp)):
		if (i < 2):
			dp[i] = costs[i]
		else:
			dp[i] = min(dp[i - 2] + costs[i], dp[i - 1] + costs[i])

	return dp[-1]	
