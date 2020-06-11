from itertools import combinations

def pythagorean_triplet(array):
    squared_num = dict((num**2, num) for num in array)
    # above - num**2 = number squared, num = number in array
    # 1. print(squared_num) used to print sum of squared number in console 
    """
    x,y in combinations ensures that the returned value pairings will be
    unique with no duplicate combinations in the console 
    """
    # 2. for x,y in combinations(squared_num,2):
    """
    Solution to solving the pythagorean triplet is below
    Answer = [(3, 4, 5)]
    """
    triplet = [(squared_num[x], squared_num[y], squared_num[x+y]) \
               for x,y in combinations(squared_num,2)
               if x+y in squared_num.keys()]
    # print(x,y) used for 1 & 2 steps only
    
    return triplet
    
print(pythagorean_triplet([1,2,3,4,5,6,7,8]))