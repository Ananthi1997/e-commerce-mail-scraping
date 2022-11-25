## Need to install few packages using the following command ##
# pip install imap-tools
# pip install beautifulsoup4 

## Importing the required packages ##
from imap_tools import MailBox
from bs4 import BeautifulSoup
import os
import csv

## Getting email bodies from INBOX ##
with MailBox('imap.gmail.com').login('ttananthi97@gmail.com', 'huqwdkssivuhvxoe', 'INBOX') as mailbox:
    for msg in mailbox.fetch():
        ## Filtering mails only from amazon ##
        if(msg.from_ == 'auto-confirm@amazon.in'):
            # body = msg.text or msg.html
            body = msg.html
            ## Getting the name of the ordered item and seller name ##
            beautifulSoupText = BeautifulSoup(body, 'lxml')
            name_tag = beautifulSoupText.find('td',class_ = "name")
            ordered_item = name_tag.get_text()
            ordered_item = ordered_item.strip()
            if('Sold by' in ordered_item):
                ordered_items = ordered_item.split("Sold by")[0]
                seller_name = ordered_item.split("Sold by")[1]
            ## Getting the price of the ordered item ##
            price_tags = beautifulSoupText.find('td',class_ = "price")
            item_price = price_tags.text
            ## Getting Shipping address ##
            table = beautifulSoupText.find_all('table', {'id':'criticalInfo'})
            for row in table:
                shipping_date_address = row.find('tr').text
                shipping_address = shipping_date_address.split("\n")
                for item in shipping_address:
                    if 'Your order will be sent to' in item:
                        address = item.split(":")[1]
            
            ## Stroring the extracted information in the dictionary ##
            order_detail = {"Ordered Item":ordered_items, "Seller Name":seller_name, "Price of the Item":item_price, "Delivery Address":address}
            print(order_detail)

            ## Storing the information in a csv file ##
            fields = ['Ordered Item',"Seller Name","Price of the Item","Delivery Address"]
            ## File will be stored in the current working directory ##
            ## Nme of the csv file - e-commerce item details.csv ##
            data_filename = os.path.join(os.getcwd(), "e-commerce item details" + ".csv")
            with open(data_filename, 'a', newline='') as csvfile: 
                file_is_empty = os.stat(data_filename).st_size == 0
                csvwriter = csv.writer(csvfile)   
                if file_is_empty:
                    csvwriter.writerow(fields)
                csvwriter.writerow([ordered_items, seller_name, item_price, address])  
            csvfile.close()