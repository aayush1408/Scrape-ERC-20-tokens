from bs4 import BeautifulSoup
import requests

token_names = []
token_descriptions = []
token_images = []

#Request the web page
res = requests.get('https://etherscan.io/tokens')

# Use beautiful soup
soup = BeautifulSoup(res.text,'html.parser')
token_name_nodes = soup.select('h5 a')
token_description_nodes = soup.select('small font')
token_images_nodes  = soup.find_all('img')\

for token in token_name_nodes:
  token_names.append(token.getText())
print(token_names)

for token in token_description_nodes:
  token_descriptions.append(token.getText())
print(token_descriptions)

for token in token_images_nodes:
  token_images.append(token.get('src'))
print(token_images)