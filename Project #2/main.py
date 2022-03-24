from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

countriesFile = open("./countries.txt","r")
reportFile = open("./final_report.csv","w")
reportFile.write("Country,Coronavirus Cases,Deaths,Recovered,Death Percentage\n")
countries = countriesFile.readlines()[0].split(",")
print(countries)
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")

for country in countries:
    driver.get("https://www.worldometers.info/coronavirus/country/{}".format(country))
    cases = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[4]/div/span').get_attribute("innerHTML")
    cases = cases.replace(",","")
    deaths = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[5]/div/span').get_attribute("innerHTML")
    deaths = deaths.replace(",","")
    recoverd = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[6]/div/span').get_attribute("innerHTML")
    recoverd = recoverd.replace(",","")
    deathPer = (int(deaths) / int(cases))*100
    reportFile.write(f"{country.capitalize()},{cases},{deaths},{recoverd},{deathPer}%\n")

countriesFile.close()
driver.close()
reportFile.close()