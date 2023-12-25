from bs4 import BeautifulSoup
import requests
import sys
import re

except_file = []

def getList(links: list, site: str, template: str) -> list:
    # print(f'Checked: {site}')
    response = requests.get(site)
    soup = BeautifulSoup(response.text, "lxml")
    for lists in soup.find_all('a'):
        if lists.get('href') != None:
            if template in lists.get('href'):
                if not set(except_file) & set(lists.get('href').split('.')):
                    if lists.get('href') not in links:
                        links.append(lists.get('href'))
                        # print(f"Added: {lists.get('href')}")
    return links

def getUrlSite(url: str):
    url = re.match('.*\/\/(.*?)\/', url)
    return url

if __name__ == "__main__":
    params = sys.argv
    main_links = []
    with open("exept.txt") as f:
        except_format = f.readlines()
        except_file = [line.rstrip() for line in except_format]
    if len(params) > 1:
        for i in range(1, len(params)):
            print(f"Start parse : {params[i]}")
            url = getUrlSite(params[i]).group(0)
            links = []
            links.append(params[i])
            for link in links:
                links = getList(links, link, url).copy()
            main_links = list(set(main_links + links))
            print("===============================================================\n=================================================")
    else:
        with open("sites.txt") as sites:
            params = sites.readlines()
            if len(params) > 0:
                for i in range(0, len(params)):
                    print(f"Start parse : {params[i].rstrip()}")
                    url = getUrlSite(params[i].rstrip()).group(0)
                    links = []
                    links.append(params[i].rstrip())

                    for link in links:
                        links = getList(links, link, url).copy()
                    print(links)
                    main_links = list(set(main_links + links))
                    print("===============================================================\n=================================================")
            else:
                print("Введите сайты через пробел или в файл")
    with open('links.txt', 'w') as f:
        for link in main_links:
            f.write(link + '\n')

