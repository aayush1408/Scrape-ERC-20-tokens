from bs4 import BeautifulSoup
import requests
import lxml

# empty lists for storing the scraped data
token_names = []
token_descriptions = []
token_images = []
contract_address = []
decimal = []
supply_amount = []
final_data = []

# url to navigate to
str = 'https://etherscan.io/'

#Request the web page
res = requests.get('https://etherscan.io/tokens')

# Use beautiful soup
soup = BeautifulSoup(res.text,'html.parser')

# list of nodes for token name
token_name_nodes = soup.select('h5 a')

# list of nodes for token description
token_description_nodes = soup.select('small font')

# list of nodes for token images
token_images_nodes  = soup.find_all('img')

# Storing the values in the empty lists
# list of nodes for token description
for token in token_name_nodes:
  token_names.append(token.getText())
print(token_names)

for token in token_description_nodes:
  token_descriptions.append(token.getText())
print(token_descriptions)

for token in token_images_nodes:
  token_images.append(token.get('src'))
print(token_images)

# Message for the command line
print('-------------------------------------------------------------------------------')
print('Please wait scraping the remaining data')
print('-------------------------------------------------------------------------------')

# navigation to different page and scraping the data
# iterating and getting the link for each erc20 token
for link in token_name_nodes:

    #appending the link
    link_res = str + link.get('href')

    #request to the token page
    res_of_another_page = requests.get(link_res)
    soupy = BeautifulSoup(res_of_another_page.text,'html.parser')

    # Getting the desired nodes
    row1 = soupy.find('tr', {'id':'ContentPlaceHolder1_tr_valuepertoken'})
    row2 = soupy.find('tr', {'id':'ContentPlaceHolder1_trContract'})
    row3 = soupy.find('tr', {'id':'ContentPlaceHolder1_trDecimals'})

    #Appending every value to the list
    supply_amount.append(row1.find_previous_siblings()[0].findAll('td')[1].getText()[1:-1])
    contract_address.append(row2.findAll('td')[1].getText())
    decimal.append(row3.findAll('td')[1].getText()[1:-1])
    print(row1.find_previous_siblings()[0].findAll('td')[1].getText()[1:-1])    
    print(row2.findAll('td')[1].getText()[1:-1])
    print(row3.findAll('td')[1].getText()[1:-1])

print(contract_address)
print(decimal)
print(supply_amount)
