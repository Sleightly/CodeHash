import numpy as np
import heapq

def cost(i1, i2, slides):

	s1 = slides[i1]
	s2 = slides[i2]
	# indices as input
	intersect = s1.intersection(s2)
	s1_diff = s1.difference(s2)
	s2_diff = s2.difference(s1)

	return min(len(intersect), len(s1_diff), len(s2_diff))

file = 'a_example.txt'
f = open(file, 'r')
lines = f.readlines()

lines = [l.strip().split() for l in lines]

v = [l for l in lines if l[0] == 'V']
h = [l for l in lines if l[0] == 'H']

v_tags = []
h_tags = []
for x in v:
	v_tags.append(set(x[2:]))
for x in h:
	h_tags.append(set(x[2:]))


slides = h_tags
print(slides)

for i in range(len(v_tags), 2):
	if i is len(v_tags) - 1:
		break
	union = v_tags[i].union(v_tags[i+1])
	slides.append(union)

print(slides)
print(v_tags, h_tags)
#slides = [set(["a", "b", "c"]), set(["b","c","g"]), set(["d", "f"])]

adj = []

for i in range(len(slides)):
	x = []
	for j in range(len(slides)):
		if i is not j:
			x.append(j)
	adj.append(x)

dist = [np.inf for i in range(len(slides))]

prev = [None for i in range(len(slides))]

visited = [False for i in range(len(slides))]

start = 0
curr = start
dist[start] = 0
pq = []
heapq.heappush(pq, (0, start))

while len(pq):
    curr = heapq.heappop(pq)
    node = curr[1]
    visited[node] = True
    
    for n in adj[node]:
        if not visited[n]:
            dist[n] = dist[node] - cost(n, node, slides)
            heapq.heappush(pq, (-1 * cost(n, node, slides), n))
            prev[n] = node

print(dist)
print(prev)

# print(v_tags)
# print(h_tags)
# #print(lines)
# print(len(v))
# print(len(h))
# print(v)
# print(h)




#given list of vertical slides, 
def createSlides(v):
	print(v)
