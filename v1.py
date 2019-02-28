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

v_set_un = [[0]*len(v_tags) for _ in v]

for r in range(len(v_set_un)):
	for c in range(len(v_set_un)[0]):
		v_set_un[r][c] = v_tags[r] + v_tags[c]

print(v_tags)
print(h_tags)
#print(lines)
print(len(v))
print(len(h))
print(v)
print(h)

def cost(i1, i2, slides):

	# indices as input
	intersect = 

#given list of vertical slides, 
def createSlides(v):
	print(v)
