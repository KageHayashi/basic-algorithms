class QU:
	id = []
	sz = []
	def __init__(self, n):
		for i in range(n):
			self.id.append(i)

	def root(i):
		while (i != id[i]): 
			i = id[i]
		return i

	def connected(p, q):
		return root(p) == root(q)

	def union(p, q):
		i = root(p)
		j = root(q)
		if (i == j): return
		if (sz[i] < sz[j]):
			id[i] = j
			sz[j] += sz[i]
		else:
			id[j] = i
			sz[i] += sz[j]
				

hi = QU(10)
for i in (hi.id):
	print(i)