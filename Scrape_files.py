import requests
from bs4 import BeautifulSoup
import html5lib
from urllib.parse import urlparse
import os


URL =" https://www.education.gov.in/statistics-new?shs_term_node_tid_depth=384"
HEADERS=({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'})


def fetch_page( url ,headers):
  try:
      response = requests.get(url, headers = headers)
      response.raise_for_status()
      return response
  except requests.RequestException as e:
    print( " COuld not request ")
    return None
  
def parse_page( response):
  return BeautifulSoup(response.text , 'html.parser')\
  

def get_urls( soup , base_url = " https://www.education.gov.in"):

  anchors = soup.find_all('a')
  all_urls= []

  for url in anchors:
    links = url.get('href')
    if links != None:

     if 'pdf' in links:
      if links.startswith('https'):
        all_urls.append(links)
      else:
        all_urls.append(base_url + links)
      
     if 'xlsx' in links:
      if links.startswith('https'):
        all_urls.append(links)
      else:
        all_urls.append(base_url + links)
     if 'xls' in links:
      if links.startswith('https'):
        all_urls.append(links)
      else:
        all_urls.append(base_url + links)


  return all_urls

def download(pdf_urls , output_dir):
  for url in pdf_urls:
    try:
      file_name = url.split('/')[-1]
      pdf_response = requests.get(url)
      pdf_response.raise_for_status()
      pdf_name = os.path.join(output_dir , file_name)

      with open(pdf_name ,'wb') as f :
        f.write(pdf_response.content)
    except requests.RequestException as e:
      print("failed to download")
    except IOError as e:
      print("failed to save pdf_name")

output_dir = os.path.join('C:', 'Users', 'DELL', 'Flutter', 'Factly_assignment')
os.makedirs(output_dir)

  


web_page =fetch_page(URL , HEADERS)
if web_page:
 soup = parse_page(web_page)
 all_urls1 = get_urls(soup)

 download(all_urls1, output_dir)




next_page_tag = soup.find('a' , title = "Go to page 2")
if next_page_tag:
  next_page_url = 'https://www.education.gov.in' + next_page_tag.get('href')
  print(next_page_url)
  next_page = fetch_page( next_page_url , HEADERS)

  if next_page:
    soup2 = parse_page(next_page)
    all_urls2 = get_urls(soup2)
    download(all_urls2 , output_dir)

