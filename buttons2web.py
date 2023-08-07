import os


#list of links
listb = [
	("pygame tut. 1, nuova serie di tutorial su pygame 28.7.2023",
		"https://pythonprogramming.altervista.org/wp-admin/post.php?post=12925&action=edit")
]

with open("wip.html", 'a') as file:
	for link in listb:
		print(f"<div style='font-size:20'><a href='{link[1]}'>{link[0]}</a></div>", file=file)

os.system("start wip.html")