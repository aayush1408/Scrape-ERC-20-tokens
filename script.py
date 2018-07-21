from bs4 import BeautifulSoup
import requests
import csv
import sys

# Setup the file
csvfile = open('test4.csv','w+')

# empty lists for storing the scraped data
token_names = []
token_descriptions = []
token_images = []
contract_address = []
decimal = []
supply_amount = []
serial_nos = []
complete_data = []
k = 1
while(k<=12):
    # url to navigate to
    str_token = 'https://etherscan.io/'
    url = 'https://etherscan.io/tokens?p='+str(k)
    # Request the web page
    res = requests.get(url)

    # Use beautiful soup
    soup = BeautifulSoup(res.text,'html.parser')

    # list of nodes for token name
    token_name_nodes = soup.select('h5 a')

    # list of nodes for token description, images and names 
    table = soup.find('table')
    rows = table.find_all('tr')[1:]
    for data in rows:
        serial_no =  data.find_all('td')[0].find('span').getText()
        serial_nos.append(serial_no)
        name_nodes =  data.find_all('td')[2]
        name = name_nodes.find('h5').getText()
        data1 = data.find_all('td')[1]
        img_url = str_token + data1.find('img').get('src')
        data2 = data.find_all('td')[2]
        try:
            description = data2.find('font').getText()
        except AttributeError:
            description = ' '

        token_names.append(name)    
        token_images.append(img_url)
        token_descriptions.append(description) 

    print(token_descriptions)
    print(token_images)
    print(token_names)


    # Message for the command line
    print('---------------------------------------------------------------------------------------------------------------')
    print('Please wait scraping the remaining data')
    print('---------------------------------------------------------------------------------------------------------------')

    # # # navigation to different page and scraping the data
    # # # iterating and getting the link for each erc20 token

    for link in token_name_nodes:

        #appending the link
        link_res = str_token + link.get('href')

        #request to the token page
        res_of_another_page = requests.get(link_res)
        soupy = BeautifulSoup(res_of_another_page.text,'html.parser')

        try:
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

        except AttributeError:
            sys.exit('Something went wrong with the network,please try again!!')



    print(contract_address)
    print(decimal)
    print(supply_amount)


    # Message for the command line
    print('-------------------------------------------------------------------------------------------------------------')
    print('Please wait collecting the whole data...')
    print('-------------------------------------------------------------------------------------------------------------')

    k += 1 

try:
    writer =  csv.writer(csvfile)
    writer.writerow(('Serial-No','Name','Image-Url','Description','Decimal','Contract','Total Supply'))
    for i in range(550):
        writer.writerow((serial_nos[i],token_names[i],token_images[i],token_descriptions[i],decimal[i],contract_address[i],supply_amount[i]))
finally:
    csvfile.close()
        