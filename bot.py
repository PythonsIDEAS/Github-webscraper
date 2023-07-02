import requests
import telebot
from bs4 import BeautifulSoup

token='5783807409:AAGhnYhhg09U7gw47w92819zloqvqEalHmo'
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    input=bot.send_message(message.chat.id,'Введи название аккаунта: ')
    bot.register_next_step_handler(input, test)
def test(message):
    base_url = 'https://github.com/'
    account = message.text
    modified_url = base_url + account

    account_requests = requests.get(modified_url)
    account_soup = BeautifulSoup(account_requests.text, 'html.parser')

    account_name = account_soup.find_all('h1', class_='vcard-names')
    for name in account_name:
        bot.send_message(message.chat.id,name.text)

    image = account_soup.find_all('img', class_='avatar avatar-user width-full border color-bg-default')
    if image:
        src = image[0]['src']
        bot.send_photo(message.chat.id, photo=src, caption="Фото аккаунта")

    pined_repositories = account_soup.find_all('div', class_='js-pinned-items-reorder-container')
    for pined in pined_repositories:
        bot.send_message(message.chat.id, pined.text)

    all_repositories_url = modified_url + '?tab=repositories'
    repositories = requests.get(all_repositories_url)
    repositories_soup = BeautifulSoup(repositories.text, 'html.parser')

    name_of_repositories = repositories_soup.find_all('h3', class_='wb-break-all')
    for reps in name_of_repositories:
        bot.send_message(message.chat.id, reps.text)

    achievements_url = modified_url + '?tab=achievements'
    achievements = requests.get(achievements_url)
    achievements_soup = BeautifulSoup(achievements.text, 'html.parser')

    all_achivments = achievements_soup.find_all("h3", class_='f4 ws-normal')
    for achievement in all_achivments:
        bot.send_message(message.chat.id, achievement.text)

    more_stared_url = modified_url + '?direction=desc&sort=stars&tab=stars'
    more_stared_responce = requests.get(more_stared_url)
    stars_soup = BeautifulSoup(more_stared_responce.text, 'html.parser')

    name_of_most_stared_repositories = stars_soup.find_all('div', class_='d-inline-block mb-1')
    count_stars = stars_soup.find_all('a', class_='Link--muted mr-3')
    for most_stared in name_of_most_stared_repositories:
        bot.send_message(message.chat.id, most_stared.text)
    for stars in count_stars:
        bot.send_message(message.chat.id, stars.text)

bot.polling()