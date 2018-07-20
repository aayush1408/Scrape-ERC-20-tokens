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

# Message for the command line
print('Please wait scraping the remaining data')


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


# navigation to different page and scraping the data
# iterating and getting the link for each erc20 token
for link in token_name_nodes:

    #appending the link
    link_res = str + link.get('href')

    #request to the token page
    res_of_another_page = requests.get(link_res)
    soupy = BeautifulSoup(res_of_another_page.text,'html.parser')

    # Getting the desired nodes
    table = soupy.findAll('table')
    row1 = soupy.find('tr', {'id':'ContentPlaceHolder1_tr_valuepertoken'})
    row2 = table[1].findAll('tr')

    #handling the received data
    contract_address_value = row2[1].getText()[16:-10]
    decimal_value = row2[2].getText()[14:-2]
    supply_amount_value = row1.find_previous_siblings()[0].findAll('td')[1].getText()[1:-1] 
    print(contract_address_value)
    print(decimal_value)
    print(supply_amount_value)

    #Appending every value to the list
    supply_amount.append(supply_amount_value)
    contract_address.append(contract_address_value)
    decimal.append(decimal_value)
print(contract_address)
print(decimal)
print(supply_amount)
