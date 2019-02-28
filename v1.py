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


v_set_un = [[0]*len(v_tags) for _ in v_tags]

for r in range(len(v_set_un)):
	for c in range(len(v_set_un)):
		if r == c:
			v_set_un[r][c] = 0
		else:
			v_set_un[r][c] = len(v_tags[r].union(v_tags[c]))


def maxCookies(v_set_un):
	seen = [0] * len(v_set_un)
	curr_max = 0
	index = []
	for r in range(len(v_set_un)):
		temp_max = 0
		curr_index = 0
		for c in range(len(v_set_un)):
			if not seen[c]:
				if v_set_un[r][c] > temp_max:
					temp_max = v_set_un[r][c]
					curr_index = c
		seen[curr_index] = 1
		curr_max += temp_max
		l = [r, curr_index]
		l.sort()
		index.append(tuple(l))
	return set(index)

l = maxCookies(v_set_un)
print(l)


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












#####ignore for now##########
'''def maxCookies(v_set_un, seen, curr_max, marked):
	if not 0 in seen:
		return (curr_max, marked)

	listing = []

	for r in range(len(seen)):
		if seen[r]:
			continue
		for c in range(len(seen)):
			if seen[c]:
				continue
			else:
				seen[c] = 1
				seen[r] = 1
				temp = marked
				temp.append((r,c))
				listing.append(maxCookies(v_set_un, seen, curr_max + v_set_un[r][c], temp))
				seen[c] = 0
				seen[r] = 0

	return listing

seen = [0]*len(v_set_un)
marked = []
curr_max = 0
print('here')
l =maxCookies(v_set_un, seen, curr_max, marked)
for x in l:
	print(x)'''



#print(v_tags)
#print(h_tags)
#print(lines)
#print(v)
#print(h)
