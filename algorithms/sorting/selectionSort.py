# Time Complexity:
# Best: Ω(n^2)  
# Average: Θ(n^2)   
# Worst: O(n^2) 
# 
#Space Complexity:
# Worst: O(1)



def selectionSort(a):
    for i in range(len(a)):
        min_index = i
        for j in range(i + 1, len(a)):
            if a[min_index] > a[j]:
                min_index = j

        a[i], a[min_index] = a[min_index], a[i]

test = [2, 9, 7, 5, 8, 3, 1, 5, 0, 6, 4]
selectionSort(test)
for i in test:
    print(i)