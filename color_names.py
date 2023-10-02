# from csv to dictionary

def get_csv(file: str) -> list:
	with open(file) as file:
		content = file.readlines()
	return content


def create_dic(content):
	coldic = {}
	for k in content[:5]:
		id,name,hx,r,g,b = k.split(",")
		name = name.replace("\"","")
		coldic[name] = hx
	return coldic


content = get_csv("colors.csv")
dic = create_dic(content)
print(*dic.items(), sep="\n")
