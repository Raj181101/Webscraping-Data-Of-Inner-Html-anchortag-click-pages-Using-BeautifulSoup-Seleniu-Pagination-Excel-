#### Scraping Companies Data Of Outer Pages and Inner Pages of ANchor tags Using Beautiful Soup

'''from bs4 import BeautifulSoup
import xlsxwriter
import requests 

url = 'https://www.zaubacorp.com/company-list/city-HYDERABAD/p-1-company.html'


Details =[]

def detail(url1,name):
    t = requests.get(url1) 
    soup = BeautifulSoup(t.content, 'lxml')
    comps = soup.findAll('p')
    try:
        cnt2=1
        for co in comps:
            try: 
                if co.b:
                    #print(cnt2)
                    if cnt2 == 1:
                        #print(co.text)
                        email = co.text.strip()
                    

                    cnt2+=1
            except:
                pass
    except:
        pass
    
    #Table data for extracting register number,company status
    table = soup.find("table")
    rows = table.findAll('tr')
    cnt3 = 1
    status = rows[2].findAll('td')[1].text.strip()
    location = rows[3].findAll('td')[1].text.strip()
    reg_num = rows[4].findAll('td')[1].text.strip()
    
    
    #table data for extracting contact person
    # table1 = soup.findAll("table")
    # cd =table1[7].findAll('tr')[2]
    # print(cd.find('table'))
    # print("---------------------")


    # print(name)
    # print(email)
    # print(status)
    # print(location)
    # print(reg_num)
    print()
    print()
    
    
    
    
    # #print(name,emails,mobiles,address)
    # Writing Scraped Data To Excel Files
    
    # Details.extend([[name,emails,mobiles,address]])
    # with xlsxwriter.Workbook('Details2.xlsx') as workbook:
    #     worksheet = workbook.add_worksheet()
    #     for row_num, data in enumerate(Details):
    #         worksheet.write_row(row_num, 0, data)

    # print()
    # print()
	
count = 0
def Mains(urls):
    r = requests.get(urls) 
    soup = BeautifulSoup(r.content, 'lxml')
    y = soup.findAll('tr')
    for x in y:
        ab =x.findAll('td')
        #print(len(x))
        try:
            name = ab[1].a.text
            comp = ab[1].a['href']
            detail(comp,name)
            #print(name,comp)
        except:
            pass

    # else:
    #     global count
    #     count =count+1
    #     print(count)
    #     print("Page {} Completed Successfully".format(count))
    #     url2 = 'https://www.zaubacorp.com/company-list/city-HYDERABAD/p-'+str(cnt)+'-company.html'
    #     print("url-",url2)
        #Mains(url2)

Mains(url)   '''




############# Second way - Scraping Javascript Rendered Data Using Selenium and Beautiful soup#############

'''   from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import xlsxwriter

Details = []
count =0

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome('/home/medeaz/chromedriver',options=options)

def detail(x,name):
    r = requests.get(x) 
    soup = BeautifulSoup(r.content, 'lxml')
    y = soup.findAll('span', attrs = {'itemprop':'address'})
    z = soup.findAll('div', attrs = {'class':'span8'})
    b = soup.findAll('span', attrs = {'itemprop':'url'})
    #a = soup.findAll('div', attrs = {'class':'content'})


    
    if y == []:
            Address = "NA"
    else:
            add = y[0].text
            Address = add.rstrip()

    if z == []:
            Mobile_Number = "NA"
    else:
        #Mobile_Number = z[2].text
        try:
            Mobile_Number = z[2].text
            mob = int(Mobile_Number)
        except:
            Mobile_Number = z[1].text
            

    if b == []:
            website = "NA"
    else:
            website = b[0].text
        #Contact_person = z[1].text



    print('Name  -----   ',name)
    #print('Website  -----   ',website)
    #print('Address  -----   ',add.rstrip())
    # print('Contact_Person  -----  ',Contact_person)
    print('Mobile_Number  -----   ',Mobile_Number)
    #print('Company Desc  -----   ',a[2].text)
    print()

    
    Details.extend([[name,website,Mobile_Number,Address]])

    with xlsxwriter.Workbook('RealEstate_Companies1.xlsx') as workbook:
        worksheet = workbook.add_worksheet()
                    
        for row_num, data in enumerate(Details):
            #print('Row',row_num,data)
            worksheet.write_row(row_num, 0, data)



cnt = 1

def Links(url):
	driver.get(url)
	ps = driver.find_elements_by_xpath("//a[@class='link']")
	for p in ps:
		x = p.get_attribute("href")
		c=p.text
		detail(x,c)
	else:
		global cnt
		cnt = cnt+1
		print(cnt)
		if(cnt == 22):
			print("All pages completed")
		else:
			url1 = 'http://www.companiesinhyderabad.com/realestate_companies_hyderabad.php?tot_page=8&company_name=&location=Hyderabad&sort_by=&turn_by=&emp_by=&sec_by=&category=Construction%20/%20Real%20%20Estate&page='+str(cnt)
			print('All Items Are Completed Successfully')
			Links(url1)


url = 'http://www.companiesinhyderabad.com/realestate_companies_hyderabad.php?tot_page=8&company_name=&location=Hyderabad&sort_by=&turn_by=&emp_by=&sec_by=&category=Construction%20/%20Real%20%20Estate&page=1'
Links(url)   '''




