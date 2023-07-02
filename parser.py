#src = image[0]['src']
import requests
from bs4 import BeautifulSoup

base_url='https://github.com/'
account=input('Введите название аккаунта :')
modifed_url=base_url+account

main_responce=requests.get(modifed_url)
main_soup=BeautifulSoup(main_responce.text,'html.parser')

name_account=main_soup.find('h1',class_='vcard-names')
for name in name_account:
    print(name.text)

image = main_soup.find_all('img', class_='avatar avatar-user width-full border color-bg-default')
if image:
    src = image[0]['src']
    print(src)


pined_repositories=main_soup.find_all('div',class_='pinned-item-list-item-content')
for pined in pined_repositories:
    print(pined.text)

repositories_url=modifed_url+'?tab=repositories'
rep_responce=requests.get(repositories_url)
rep_soup=BeautifulSoup(rep_responce.text,'html.parser')

repositories=rep_soup.find_all('h3',class_='wb-break-all')
for repo in repositories:
    print(repo.text)


achivments_url=modifed_url+'?tab=achievements'
ach_responce=requests.get(achivments_url)
ach_soup=BeautifulSoup(ach_responce.text,'html.parser')

name_of_achivment=ach_soup.find_all('h3',class_='f4 ws-normal')
for achivment in name_of_achivment:
    print(achivment.text)

star_url=modifed_url+'?direction=desc&sort=stars&tab=stars'
star_responce=requests.get(star_url)
star_soup=BeautifulSoup(star_responce.text,'html.parser')

name_star=star_soup.find_all('div',class_='d-inline-block mb-1')
for name_for_star in name_star:
    print(name_for_star.text)
count_stars = star_soup.find_all('a', class_='Link--muted mr-3')
for stars in count_stars:
    print(stars.text)

#<div class="d-inline-block mb-1">
