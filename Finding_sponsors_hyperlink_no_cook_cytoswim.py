from bs4 import BeautifulSoup
import requests
import csv

#make if loop only print if description has engineering science or technology

science_park = requests.get("https://www.warwicksciencepark.co.uk/information/company-directory/university-of-warwick-science-park/")

soup = BeautifulSoup(science_park.text,'html.parser')

company_name = soup.find_all('div',attrs={'class':'box_header'})

company_websites=soup.find_all('a',attrs={'target':'_blank'})
 # gets the actual link from website

# removed_cookie = []

# for web in company_websites[1:]:
#    removed_cookie.append(web)

file = open("Sciencepark_businesses_web_hyp_4_3.csv","w",newline='') # gets rid of gaps

writer = csv.writer(file)

writer.writerow(['Name','Website'])

for name,website in zip(company_name,company_websites[1:]):
    print(name.text)
   
    web= website.get('href')
    if web:
        hyperlink = f'=HYPERLINK("{web}","{name.text}")'
    else:
        hyperlink = 'No website'
    
    writer.writerow([name.text,hyperlink]) #do not add text at the end of web ; name one column; web other

file.close()
#cookie policy is getting recognised need to use indexing to remove the first link
#use enumerate

#next steps: some of the rows are off so include a if statement to assign web = ' ' if no website found
#check cytoswim
