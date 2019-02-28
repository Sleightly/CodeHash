file = 'c.txt'
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

v_set_un = [[0]*len(v_tags) for _ in v]

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


#given list of vertical slides, 
def createSlides(v):
	print(v)
