import pickle

nodes = pickle.load(open('english.chow','rb'))
dict = pickle.load(open('english_struct.chow','rb'))

i = 0
n = 1
current = nodes[dict.root.child]
accum = []
for i in range(n):
	while(1):
		if current.sibling == None:
			current = nodes[current.child]
			break
		accum += [current.data]
		current = nodes[current.sibling]
		print(' '.join(accum))