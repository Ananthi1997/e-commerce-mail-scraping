Task:
To successfully deliver for a client requirement, you have been assigned two HTMLs to extract ALL the
useful information available namely (but not limited to), product name, address, unit-price etc which can
be used for market analysis.
For the HTML to be parsed, consider any two email receipts you may have received from e-commerce
companies like Amazon, Uber, Zomato etc.
You are required to write a parser with code that is structured, efficient and properly commented on.
Once the HTML has been scraped, you are required to save this information as a key value pair in CSV file
format. This will helpthe Team to enhance the quality of data & deliver as committed.



Steps need to be done before running the script:
1. First need to enable IMAP in gamil settings before running the script. 
2. Secondly need to create an application specific password by logging into gmail settings instead of two factor authentication.

Python packages list to install:
1. pip install imap-tools
2. pip install beautifulsoup4
3. pip install lxml

To execute script:
python fetching_items_from_amazon.py

Output CSV file:
e-commerce item details.csv
