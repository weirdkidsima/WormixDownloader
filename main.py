import os
import sys
import urllib.error
import progressbar
from urllib.request import urlretrieve
from pip._vendor.distlib.compat import raw_input


version = "1.0.1"
pbar = None

#Data files
file_extensions = ['xml', 'swf']
main_folders = ['data', 'common', 'lang', 'resconfigs', 'social']
common_folders = ['bosses', 'chars', 'general', 'objects', 'rooms']
resconfigs_folder = ['resconfig', 'bosses_config', 'battle_stuff_config']
social_folders = ['vkontakte', 'lang']
data_main_folder = ['serializers']
common_main_folder = ['chat']
common_bosses_folder = ['alchemist', 'ancientGhost', 'archbot', 'archdemon', 'archivist', 'arcticwarrior', 'blacksmith', 'cyborg', 'darkKnight', 'devotee', 'druid', 'emperor', 'enchanter', 'engineer', 'farmer', 'gravitymaster', 'guardiansDepths', 'hacker', 'hunter', 'jarl', 'madRobot', 'miner', 'paladin', 'phantom', 'pharaon', 'psionic', 'queenSpidersFix', 'scientist', 'solarpriest', 'soulmaster', 'symbiote', 'thieves', 'wanderingSoul']
common_chars_folder = ['alien', 'boar', 'boxer', 'cat', 'demon', 'dragon', 'rabbit', 'rhino', 'robot', 'zombie']
common_general_folder = ['arena', 'mainMenu', 'news', 'wormix_ui']
common_objects_folder = ['artifacts', 'battleStuff', 'boosters', 'charActions', 'clans_icons', 'clans_ui', 'hats', 'OK_action', 'reagent_icons', 'returnFriendObjects', 'rip', 'shopMenu', 'topRatingObjects', 'viral_stuff', 'weapon_upgrades', 'weapons']
common_rooms_folder = ['achiev_icons', 'achiev_room', 'armory_room', 'craft_room', 'fullscreenCommonObjects', 'race_room', 'team_room']
lang_main_folder = ['achievments_ru', 'ban_ru', 'boss.achievments_ru', 'bosses_ru', 'bot.names_ru', 'chat_en', 'chat_ru', 'chat_ua', 'clan_ru', 'craft_ru', 'date_ru', 'help_ru', 'items_ru', 'messages_ru', 'news_ru', 'taunts_ru', 'tutorials_ru', 'upgrades_ru', 'viral_ru', 'weapons_ru']
social_vkontakte_folder = ['bank']
social_vkontakte_lang_folder = ['messages_ru', 'avatar.messages_ru']

#Urls
def markus():
    return "https://markus.rmart.ru/"
def ssl():
    return "https://ssl.rmart.ru/"
def lord():
    return "https://lord.rmart.ru/"
def error():
    return "Incorrect url"

switcher_urls = {
    1: markus,
    2: ssl,
    3: lord
    }

def switch_url(server_url):
    return switcher_urls.get(server_url, error)()

#Version folders

def engine():
    return "engine"
def wormix_ok():
    return "wormix_ok"
def wormix_mm():
    return "wormix_mm"
def snailbob():
    return "snailbob"
def superjet():
    return "superjet"
def polygon():
    return "polygon"
def incorrect_folder():
    return "Incorrect folder"

switcher_folders = {
    1: engine,
    2: wormix_ok,
    3: wormix_mm,
    }

def switch_folder(server_folder):
    return switcher_folders.get(server_folder, incorrect_folder)()

#Yes/no

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' ""(or 'y'/'n').\n")


def download_progress_bar(block_num, block_size, total_size):
    global pbar
    if pbar is None:
        pbar = progressbar.ProgressBar(maxval=total_size)
        pbar.start()

    downloaded = block_num * block_size
    if downloaded < total_size:
        pbar.update(downloaded)
    else:
        pbar.finish()
        pbar = None

def DownloadViaUrl (url, path):
    while True:
        try:
            print("Download" + " " + url + "...")
            urlretrieve(url, path, reporthook=download_progress_bar)
            break
        except urllib.error.HTTPError as err:
            print("Error", err.code)
            break

print("Wormix Version Loader" + "\n" + "Version: " + version + "\n" + "Coded by Weirdkidsima" + "\n")

while True:
    try:
        choice_num = int(input("Please, enter server url..." + "\n" + "1 — https://markus.rmart.ru/" + "\n" + "2 — https://ssl.rmart.ru/" + "\n" + "3 — https://lord.rmart.ru/" + "\n\n" + "Enter number of choice: "))
        base_url=switch_url(choice_num)
        print("Your choice: " + base_url + "\n")
        question_main_url = bool(query_yes_no("Are you sure of your choice?"))
        print("\n")
        if question_main_url == True:
            break
        elif question_main_url == False:
            print("Make choice again..." + "\n")
    except ValueError:
        print ("Numbers only!")

while True:
    try:
        choice_num = int(input("Please, enter base folder: " + "\n" + "1 — engine" + "\n" + "2 — wormix_ok" + "\n" + "3 — wormix_mm" + "\n\n" + "Enter number of choice: "))
        base_folder=switch_folder(choice_num)
        print("Your choice: " + base_folder)
        print("Final url: " + base_url + base_folder + "/" + "\n")
        question_base_folder = bool(query_yes_no("Are you sure of your choice?"))
        print("\n")
        if question_base_folder == True:
            break
        elif question_base_folder == False:
            print("Generating choice again..." + "\n")
    except ValueError:
        print("Numbers only!1")

while True:
        try:
            ver = str(input("Please, enter version: "))
            print("Version folder is: " + ver + "\n")
            print("Final url: " + base_url + base_folder + "/" + ver + "\n\n")
            question_folder = bool(query_yes_no("Version folder is correct?"))
            print("\n")
            if question_folder == True:
                break
            elif question_folder == False:
                print("Okay, then...")
        except:
            print("Version unknown, try again")


question_file = bool(query_yes_no("Do you want to download \"Wormix.swf\"?"))
print("\n")

if question_file == True:
    while True:
        try:
            wormix_file = str(input("Enter file name: "))
            url = base_url + base_folder + "/" + ver + "/" + wormix_file + '.' + file_extensions[1]
            if not os.path.isdir(ver):
                os.makedirs(ver)
            print("Download" + " " + url + "...")
            urlretrieve(url, '.' + "/" + ver + "/" + wormix_file + '.' + file_extensions[1], reporthook=download_progress_bar)
            print("\n")
            break
        except urllib.error.HTTPError as err:
            print("Error", err.code)
            question_precision = bool(query_yes_no("Do you want try to download \"Wormix.swf\" again?"))
            if question_precision == True:
                print("Okay, return to previous step...")
                print("\n")
            elif question_precision == False:
                break

elif question_file == False:
    print("Okay, next step...")
else:
    print("Answer is unknown")

question = bool(query_yes_no("Start download data files?"))
print("\n")

pathx_part = ver + "/" + main_folders[0]

if question == True:
    for x in data_main_folder:
        pathx = "/" + pathx_part + "/" + x + '.' + file_extensions[0]
        url = base_url + base_folder + pathx
        if not os.path.isdir(pathx_part):
            os.makedirs(pathx_part)
        DownloadViaUrl(url, '.' + pathx)
    for x in resconfigs_folder:
        dirpart = "/" + main_folders[3]
        pathx = "/" + pathx_part + dirpart + "/" + x + '.' + file_extensions[0]
        url = base_url + base_folder + pathx
        if not os.path.isdir(pathx_part + dirpart):
            os.makedirs(pathx_part + dirpart)
        DownloadViaUrl(url, '.' + pathx)
    for x in common_main_folder:
        dirpart = "/" + main_folders[1]
        pathx = "/" + pathx_part + dirpart + "/" + x + '.' + file_extensions[0]
        url = base_url + base_folder + pathx
        if not os.path.isdir(pathx_part + dirpart):
            os.makedirs(pathx_part + dirpart)
        DownloadViaUrl(url, '.' + pathx)
    for x in common_bosses_folder:
        dirpart = "/" + main_folders[1] + "/" + common_folders[0]
        pathx = "/" + pathx_part + dirpart + "/" + x + '.' + file_extensions[1]
        url = base_url + base_folder + pathx
        if not os.path.isdir(pathx_part + dirpart):
            os.makedirs(pathx_part + dirpart)
        DownloadViaUrl(url, '.' + pathx)
    for x in common_chars_folder:
        dirpart ="/" + main_folders[1] + "/" + common_folders[1]
        pathx = "/" + pathx_part + dirpart + "/" + x + '.' + file_extensions[1]
        url = base_url + base_folder + pathx
        if not os.path.isdir(pathx_part + dirpart):
            os.makedirs(pathx_part + dirpart)
        DownloadViaUrl(url, '.' + pathx)
    for x in common_general_folder:
        dirpart = "/" + main_folders[1] + "/" + common_folders[2]
        pathx = "/" + pathx_part + dirpart + "/" + x + '.' + file_extensions[1]
        url = base_url + base_folder + pathx
        if not os.path.isdir(pathx_part + dirpart):
            os.makedirs(pathx_part + dirpart)
        DownloadViaUrl(url, '.' + pathx)
    for x in common_objects_folder:
        dirpart = "/" + main_folders[1] + "/" + common_folders[3]
        pathx = "/" + pathx_part + dirpart + "/" + x + '.' + file_extensions[1]
        url = base_url + base_folder + pathx
        if not os.path.isdir(pathx_part + dirpart):
            os.makedirs(pathx_part + dirpart)
        DownloadViaUrl(url, '.' + pathx)
    for x in common_rooms_folder:
        dirpart = "/" + main_folders[1] + "/" + common_folders[4]
        pathx = "/" + pathx_part + dirpart + "/" + x + '.' + file_extensions[1]
        url = base_url + base_folder + pathx
        if not os.path.isdir(pathx_part + dirpart):
            os.makedirs(pathx_part + dirpart)
        DownloadViaUrl(url, '.' + pathx)
    for x in lang_main_folder:
        dirpart = "/" + main_folders[2]
        pathx = "/" + pathx_part +dirpart + "/" + x + '.' + file_extensions[0]
        url = base_url + base_folder + pathx
        if not os.path.isdir(pathx_part + dirpart):
            os.makedirs(pathx_part + dirpart)
        DownloadViaUrl(url, '.' + pathx)
    for x in social_vkontakte_folder:
        dirpart = "/" + main_folders[4] + "/" + social_folders[0]
        pathx = "/" + pathx_part + dirpart + "/" + x + '.' + file_extensions[1]
        url = base_url + base_folder + pathx
        if not os.path.isdir(pathx_part + dirpart):
            os.makedirs(pathx_part + dirpart)
        DownloadViaUrl(url, '.' + pathx)
    for x in social_vkontakte_lang_folder:
        dirpart = "/" + main_folders[4] + "/" + social_folders[0] + "/" + social_folders[1]
        pathx = "/" + pathx_part + dirpart + "/" + x + '.' + file_extensions[0]
        url = base_url + base_folder + pathx
        if not os.path.isdir(pathx_part + dirpart):
            os.makedirs(pathx_part + dirpart)
        DownloadViaUrl(url, '.' + pathx)
elif question == False:
    print("Download canceled by user")
else:
    print("Answer is unknown")
input("Press any key and enter to close window...")