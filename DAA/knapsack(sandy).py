
def knapSack(W, wt, val, n): 
	K = [[0 for x in range(W + 1)] for x in range(n + 1)] 

	for i in range(n + 1): 
		for w in range(W + 1): 
			if i == 0 or w == 0: 
				K[i][w] = 0
			elif wt[i-1] <= w: 
				K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w]) 
			else: 
				K[i][w] = K[i-1][w] 
	print("DP table is: ")
	for i in range(n+1):
		for j in range(W+1):
			print(K[i][j],end=" ") 
		print()
	
	return K[n][W] 


if __name__ == '__main__': 
	
	n=int(input("Enter number of elements"))
	profit = [0 for i in range(n)] 
	weight = [0 for i in range(n)]

	print("Enter the profit of each element ")

	for i in range(n):
		profit[i]=int(input("enter the profit: "))

	print("Enter the weight of each element: ")

	for i in range(n):
		weight[i]=int(input("enter the weight: "))
	print()

	W = int(input("Enter max capacity: "))

	print()
	import time
	start=time.time()

	print("Max profit is : ",knapSack(W, weight, profit, n)) 

	end=time.time()


	print("Time required to executre the program is: ",end-start)

