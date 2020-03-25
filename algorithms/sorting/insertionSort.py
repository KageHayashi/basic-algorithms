# Time Complexity:
# Best: Ω(n)
# Average: Θ(n^2)
# Worst: O(n^2)
# 
# Space Complexity:
# Worst: O(1)

def insertionSort(a):
	for i in range(1, len(a)):
		key = a[i]

		j = i - 1
		while j >= 0 and key < a[j]:
			a[j + 1] = a[j]
			j -= 1
		a[j + 1] = key

test = [2, 9, 7, 5, 8, 3, 1, 5, 0, 6, 4]
insertionSort(test)
for i in test:
	print(i)
