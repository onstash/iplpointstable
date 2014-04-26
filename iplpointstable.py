import requests
from lxml import html

url = "http://www.espncricinfo.com/indian-premier-league-2014/engine/series/695871.html?view=pointstable"
page = requests.get(url)
tree = html.fromstring(page.text)

head = tree.xpath(".//*[@id='ciHomeContentlhs']/div[3]/div/table[1]/thead/tr/th/text()")
team_head = head[0]+"\t\t\t\t"+head[1]+"\t\t"+head[2]+"\t\t"+head[3]+"\t\t\t"+head[4]+"\t\t\t"+head[5]+"\t\t"+head[6]+"\t\t"+head[7]
print team_head

for i in range(1,9):
	body_string = ".//*[@id='ciHomeContentlhs']/div[3]/div/table[1]/tbody/tr[" + str(i) + "]/td/text()"
	body = tree.xpath(body_string)
	#print body
	if len(body[0].rstrip())==13:
		team_body = body[0].rstrip()+"\t\t\t"+body[1]+"\t\t"+body[2]+"\t\t"+body[3]+"\t\t\t"+body[4]+"\t\t\t"+body[5]+"\t\t"+body[6]+"\t\t"+body[7]
	else:
		team_body = body[0].rstrip()+"\t\t\t"+body[1]+"\t\t"+body[2]+"\t\t"+body[3]+"\t\t\t"+body[4]+"\t\t\t"+body[5]+"\t\t"+body[6]+"\t\t"+body[7]
	print team_body