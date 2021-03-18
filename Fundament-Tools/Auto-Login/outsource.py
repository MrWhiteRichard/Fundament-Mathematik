# ---------------------------------------------------------------- #

import csv
import os
import time

from selenium import webdriver

from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)

# ---------------------------------------------------------------- #

def get_site():
    return input('Where do you want to log into? (tiss / tuwel / webmail) ... ')

def get_discord_name(site):

    discord_name = input(f'Who is trying to open {site}? Please enter your discord name ... ')

    discord_aliases = {
        'MrRichardWhite': 'MrWhiteRichard',
        'Tabletcam': 'salli',
        'Dokumentenkamera': 'Deklaminius',
        'pwin_tab': 'pwin_99'
    }

    if discord_name in discord_aliases.keys():
        discord_name = discord_aliases[discord_name]
        print(f'Your real discord name is actually {discord_name}!')

    return discord_name

# ---------------------------------------------------------------- #

def get_login_data(site, discord_name):

    while os.path.basename(os.getcwd()) != 'Fundament-Mathematik':
        os.chdir('..')

    matriculation_number = None
    private_path = None

    with open('fundamentalsystem.csv', 'r') as file:
        for line in csv.DictReader(file):
            if line['discord_name'] == discord_name:
                matriculation_number = line['matriculation_number']
                private_path = line['private_path']

    if matriculation_number == None:
        print('ERROR: You need to provide your matriculation number in fundamentalsystem.csv!')

    if private_path == None:
        print('ERROR: You need to provide your private path in fundamentalsystem.csv!')

    password = None

    with open(os.path.join(private_path, 'passwords.csv'), 'r') as file:
        for line in csv.DictReader(file):
            if line['site'] == site:
                password = line['password']

    if password == None:
        print('ERROR: You need to provide your tuwel password in passwords.csv (at your private path)!')

    return matriculation_number, private_path, password

# ---------------------------------------------------------------- #

def drive(site, discord_name, matriculation_number, private_path, password):

    if 'chromedriver.exe' not in os.listdir(private_path):
        print('ERROR: You need to provide a proper version of chromedriver.exe in your private path!')

    driver = webdriver.Chrome(os.path.join(private_path, 'chromedriver.exe'), options = options)
    driver.maximize_window()

    url = {
        'tiss':    r'https://tiss.tuwien.ac.at/education/favorites.xhtml?dswid=8921&dsrid=479',
        'tuwel':   r'https://tuwel.tuwien.ac.at/auth/saml2/login.php',
        'webmail': r'https://mail.student.tuwien.ac.at/webmail/?_task=mail&_mbox=INBOX'
    }[site]

    driver.get(url)

    time.sleep(1)

    if site in {'tiss', 'tuwel'}:

        username = str(matriculation_number)
        driver.find_element_by_id('username').send_keys(username)
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_id('samlloginbutton').click()

        if site == 'tuwel':

            time.sleep(1)
            driver.find_element_by_id('yesbutton').click()

    elif site == 'webmail':

        username = 'e' + str(matriculation_number)
        driver.find_element_by_id('rcmloginuser').send_keys(username)
        driver.find_element_by_id('rcmloginpwd').send_keys(password)
        driver.find_element_by_id('rcmloginsubmit').click()

# ---------------------------------------------------------------- #
