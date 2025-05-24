import requests
from bs4 import BeautifulSoup

# Need to:
# Search desired role
# Needs to go through each posting and nab titles and descriptions
# Need to grab tech/tools to learn for tabulation and ranking
# Need to be able to go through each role on the left, go to next page

url = "https://ca.indeed.com/jobs?q=data+engineer&l=calgary%2C+ab&from=searchOnHP&vjk=1b2f6844bff4b399"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

title = soup.title.text
print("Page title:", title)



