def initialiseDist(s):
    for i in range(v):
        dist[i] = float('inf')
    dist[s] = 0
    
def relax(vFrom, vTo, w):
    if dist[vFrom] + w < dist[vTo]:
        dist[vTo] = dist[vFrom] + w
        pred[vTo] = vFrom


def bellman(s):
    initialiseDist(s)
    for _ in range(v - 1):
        for i in range(v):
            for j in range(v):
                if graph[i][j] != 0:
                    relax(i, j, graph[i][j])

                    
def pathTrace(source, target):
	if target == source:
	    print(str(source + 1))
	else:
		pathTrace(source, pred[target])
		print(str(target + 1))

v = 10
graph = []
pred = []
dist = []

input = open("data.txt")
dataStrings = input.readlines()

def Main():
	for _ in range(v):
		buf = []
		pred.append(0)
		dist.append(0)
		for _ in range(v):
			buf.append(0)
		graph.append(buf)

	for item in dataStrings:
		data = item.split(' ')
		start = int(data[0])
		end = int(data[1])
		weight = int(data[2])
		graph[start - 1][end - 1] = weight

	source = 0
	target = 9
	bellman(source)
	print("Shortest path from " + str(source + 1) + " to " + str(target + 1) + " is:")
	pathTrace(source, target)
	print("Weight: " + str(dist[target]))

Main()