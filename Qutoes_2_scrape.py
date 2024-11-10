from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get("https://quotes.toscrape.com/tag/love/")
soup = BeautifulSoup(page_to_scrape.text,'html.parser')
quotes = soup.findAll("span",attrs={"class":"text"})
authors = soup.findAll("small",attrs={"class":"author"})

# for quote in quotes:
#     print(quote.text)

# for author in authors :
#     print(f"author: {author.text}")
file = open("Scraped_Quotes.csv","w")//uncomment
writer = csv.writer(file)

writer.writerow(['Quotes','Authors'])


for quote,author in zip(quotes,authors):
    print(f"Quote:{quote.text}\n by {author.text}")
    #writer.writerow([quote.text,author.text])

#file.close()

#save it into csv with one column for quotes and another for author
