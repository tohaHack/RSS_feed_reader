import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
import urllib.request
import urllib.error

url: str = input("Input link to news site: ") + "/feed"

try:
    with urllib.request.urlopen(url=url) as f:
        xml_bytes: bytes = f.read()

        try:
            root: Element = ET.fromstring(xml_bytes)
        except ET.ParseError:
            print("Invalid XML/Feed")

        titles: list = []
        links: list = []
        for item in root.findall("./channel/item"):
            title: str | None = item.findtext("title")
            link: str | None = item.findtext("link")
            print(f"{title}: \n{link} \n")

            titles.append(title)
            links.append(link)

        try:
            with open(file='saved_feeds.txt', mode='w', encoding = 'utf-8') as f:
                for i in range(len(titles)):
                    f.write(f"{titles[i]}: \n{links[i]} \n")
        except FileNotFoundError as e:
            print('Error accure {e}')

except urllib.error.HTTPError as e:
    print(e.code)

except urllib.error.URLError:
    print("Connection Lost")
