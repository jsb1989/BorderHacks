from bs4 import BeautifulSoup
import requests

url = "https://www.nationsonline.org/oneworld/IATA_Codes/airport_code_list.htm"
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'html.parser')
table = soup.find("table")
