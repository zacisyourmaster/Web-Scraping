from bs4 import BeautifulSoup
import requests

url="https://www.basketball-reference.com/boxscores/"
result=requests.get(url)
soup=BeautifulSoup(result.text,'html.parser')
game_summaries = soup.find_all("div", class_="game_summary expanded nohover")
for score in game_summaries:
	loser= score.find("tr", class_="loser").text.strip()
	winner= score.find("tr", class_="winner").text.strip()

	lInfo=loser.split('\n')
	wInfo=winner.split('\n')
	print(wInfo[0]+" defeated "+lInfo[0]+" "+wInfo[1]+" to "+lInfo[1])
	print("------------------------------------------------------------------------------------------------------------")
