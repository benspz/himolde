#H1 - Minimun amount of eggs
#H2 - Max ^
#K - How many that can survive the river
#M1 and 2 are min and max to take the horses
#Design a function that receives N and a list with the values H1, H2, K, M1, M2 and returns how much the farmer makes. 
#(The returned value is 0 if the trip is not made or less than 3 eggs survived) 

def egg_profit(N, numlist) -> int:
    H1, H2, K, M1, M2 = tuple(numlist)
    if N >= H1:
        N = min(N, H2, K)  
    if M1 <= N <= M2:
        return N // 3
    else: return 0


print(egg_profit(19, [10, 14, 4, 5, 6]))
print(egg_profit(100, [10,14, 4, 5, 16]))
print(egg_profit(100, [10,14, 9, 0, 16]))
