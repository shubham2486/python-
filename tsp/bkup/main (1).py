from sys import maxsize


# This is distance between the cities


no_of_points = 5


def travelling_salesman_function(graph, starting_point):
    """The task of the this function is to calculate the path."""
    vertex = [] # This variable is use to store the index of the path

    for i in range(no_of_points):
        if i != starting_point:
            vertex.append(i)

    min_path = maxsize # It is used to store the maxsize property


    while True:
        current_distance = 0
        k = starting_point

        for i in range(len(vertex)):
            current_distance += graph[k][vertex[i]]
            #print(f"current_distance: " , current_distance)
            
            k = vertex[i]
        
        
        current_distance += graph[k][starting_point]
        min_path = min(min_path, current_distance)
        #print(f"min path: " , min_path)

        if not next_permutation(vertex):
            #print(vertex)
            break
            
        return min_path


    
def next_permutation(l): 
    """This is used to create the next permutation"""
    n = len(l)
    i = n-2

    while i >= 0 and l[i] > l[i+1]:
        i -= 1
    
    if i == -1:
        return False

    j = i+1
    while j < n and l[j] > l[i]:
        j += 1

    j -= 1

    l[i], l[j] = l[j], l[i]
    left = i+1
    right = n-1

    while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1
    return True


graph = [[0, 61, 140, 106, 93], [61, 0, 80,149, 154], [140, 80, 0, 229, 235], [106,149,229, 0, 75], [93, 154, 235, 75, 0]]
starting_point = 0
res = travelling_salesman_function(graph,starting_point)
print(res)





        





starting_point = 0
print(f"The shortest distance between the given cities is: ", travelling_salesman_function(graph, starting_point))
