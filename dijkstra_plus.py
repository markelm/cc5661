print("digite o numero de nos\n")
n = int(input())
dist = []
for e in range(n):
	dist.append(0)

X = ['a', 'b', 'c']

min_distanes = []

for e in X:
	char = 97
	nodes = []
	for node in range(n):
		nodes.append(chr(char))
		char += 1
	temp = nodes[0]
	index = nodes.index(e)
	nodes[0] = e
	nodes[index] = temp
	#for i in nodes[1:]:
	#	if i == nodes[0]:
	#		i = temp
	M = []
	for i in range(n):
		collum = []
		for j in range(n):
			print("insira o valor da celula "+str(nodes[i])+"-"+str(nodes[j])+"\n")
			cell = int(input())  
			collum.append(cell)
		M.append(collum)

	for i in range(n):
		for j in range(n):
			if M[i][j] != -1:
				if(dist[j] > (M[i][j] + dist[i]) and dist[j] != 0) or dist[j] == 0:
					dist[j] = M[i][j] + dist[i]
					M[i][j] = -1
					M[j][i] = -1

	tem = []
	for j in range(n):
		if (nodes[j] in X) and (nodes[j] != e):
			tem.append(dist[j])
	min_distanes.append(tem)

	for i in range(n):
		dist[i] = 0

print(min_distanes)

shortest = min_distanes[0][0] + min_distanes[1][1]
if shortest > min_distanes[0][1] + min_distanes[2][1]:
	shortest = min_distanes[0][1] + min_distanes[2][1]

if shortest > min_distanes[1][0] + min_distanes[0][1]:
	shortest = min_distanes[1][0] + min_distanes[0][1]

if shortest > min_distanes[1][1] + min_distanes[2][0]:
	shortest = min_distanes[1][1] + min_distanes[2][0]

if shortest > min_distanes[2][0] + min_distanes[0][0]:
	shortest = min_distanes[2][0] + min_distanes[0][0]

if shortest > min_distanes[2][1] + min_distanes[1][0]:
	shortest = min_distanes[2][1] + min_distanes[1][0]

print(shortest)
