import json
def tup2num (tup):
	ans =  []
	string = str(tup)
	lasPos=1
	temp =""
	for x in range(len(string)):
		if string[x] == ")" or string[x]== ",":
			for y in range(lasPos,x):
				temp += string[y]
			ans.append(temp)
			lasPos = x+2
			temp = ""
	return ans

def writable(list,gap):
	string = "[ "
	for x in list:
		if x != gap:
			string += str(x)+" "
		if x == gap:
			string += "\n "

	string+="]"
	return string 


def redable(string):
	lis = []
	q =0
	e=""
	for x in range(2,len(string)):
		e+=string[x]


	temp = ""
	for x in range(2,len(e)-1):
		if e[x]== " ":
			for z in range(q,x):
				temp+=e[z]
			q=x+1
			lis.append(temp)
			temp =""
	return lis

def usable(lis):
	ans = []
	temp = []
	r=0
	for x in range(len(lis)):
		if lis[x] == "<BL>":
			for q in range(r,x):
				temp.append(lis[q])
			ans.append(temp)
			r=x+1
			temp =[]

	return ans

with open("data.json") as inp:
    data = json.load(inp)

level = data["Levels"]["First"]["Layout"]
level_done = usable(redable(level))


def platformizer(data,vaccum,img_size):
	platform = []
	content = []
	x=0
	y=0
	final = []
	for row in data:
		for col in row:
			if col != vaccum:
				content = []
				content.append(x)
				content.append(y)
				platform.append(content)
			x+=1
		y+=1
		x=0

	x=0
	xval =x
	y=0
	yval = y
	width = 0
	height = 1
	dumb = []
	
	while platform != []:
		oo = platform[0]
		if oo[1] != y:
			dic = {"x":xval,"y":yval,"width":width,"height":height}
			final.append(dic)
			width = 0
			y = oo[1]
			yval = oo[1]
			x = oo[0]
			xval= oo[0]

			
		if oo[1] == y:
			if oo[0] == x:
				width+=1
			if oo[0] != x:
				dic = {"x":xval,"y":yval,"width":width,"height":height}
				final.append(dic)
				width = 1
				x = oo[0]
				xval= x
			x+=1
			platform.remove(oo)
	dic = {"x":xval,"y":yval,"width":width,"height":height}
	final.append(dic)

	
	xpos = final[0]["x"]
	ypos = final[0]["y"]
	widpos = final[0]["width"]

	yare = []
	height=1
	x = 0
	remove =[]
	gomen = final
				
	for a in final:
		for b in gomen:
			if a != b:
				if a["x"] == b["x"] and a["y"] + height == b["y"] and a["width"] == b["width"]:					
					height += 1		
					remove.append(b)
	
		l3 = [x for x in gomen if x not in remove]
		gomen = l3

		if a in gomen:		
			ansic = {"x":a["x"],"y":a["y"],"width":a["width"],"height":height}
			height = 1
			yare.append(ansic)	
	
	for gio in yare:
		gio["x"]= gio["x"]*img_size
		gio["y"]= gio["y"]*img_size
		gio["width"]= gio["width"]*img_size
		gio["height"]= gio["height"]*img_size

	return(yare)

