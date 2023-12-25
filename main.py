from bs4 import BeautifulSoup
import requests
import sys


def getList(links: list, site: str, template: str) -> list:
    print(f'Checked: {site}')
    response = requests.get(site)
    soup = BeautifulSoup(response.text, "lxml")
    for lists in soup.find_all('a'):
        if lists.get('href') != None:
            if template in lists.get('href'):
                if lists.get('href') not in links:
                    links.append(lists.get('href'))
                    print(f"Added: {lists.get('href')}")
    return links

# def getLinks(params):

if __name__ == "__main__":
    params = sys.argv
    links = []
    if len(params) > 1:

        for i in range(1, len(params)):
            url = params[i]
            response = requests.get(url)
            links.append(url)

            for link in links:
                links = getList(links, link, url).copy()

        with open('links.txt', 'w') as f:
            for link in links:
                f.write(link + '\n')
    else:
        with open("sites.txt") as sites:
            params = sites.readlines()
            if len(params) > 0:
                for i in range(0, len(params)):
                    url = params[i].strip()
                    response = requests.get(url)
                    links.append(url)

                    for link in links:
                        links = getList(links, link, url).copy()
            else:
                print("Введите сайты через пробел")




