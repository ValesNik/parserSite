from bs4 import BeautifulSoup
import requests
import sys


def getLinks(links: list, site: str, template: str) -> list:
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


if __name__ == "__main__":
    params = sys.argv
    if len(params) > 1:
        links = []
        for i in range(1, len(params)):
            url = params[i]
            response = requests.get(url)
            links.append(url)

            for link in links:
                # print(links)
                # print('\n============================\n')
                links = getLinks(links, link, url).copy()

        with open('links.txt', 'w') as f:
            for link in links:
                f.write(link + '\n')
    else:
        print("Введите сайты через пробел")
