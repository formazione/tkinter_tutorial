# from csv to dictionary

def get_csv(csv_filename: str) -> list:
	''' return a list with an item for each line of the file '''
	with open(csv_filename) as file:
		itemslist = file.readlines()
	return itemslist


def create_dic(content):
	coldic = {}
	for k in content:
		id,name,hx,r,g,b = k.split(",")
		name = name.replace("\"","")
		b = b.replace("\n","")
		coldic[f"{r},{g},{b}"] = name
	return coldic


content = get_csv("colors.csv")
dic = create_dic(content)
# print(*dic.items(), sep="\n")
print(dic[f"0,0,0"])
