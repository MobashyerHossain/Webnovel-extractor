from bs4 import BeautifulSoup as soup
from docx import Document
import regex as re
import requests
import os

########################################     Helpers Start     ########################################

def clear():
    os.system('cls')

def get_page_html(link):
    page = requests.get(link)
    page_html = soup(page.content, "html.parser")
    page.close()
    return page_html

#########################################     Helpers End     #########################################

########################################   Wuxia World Start   ########################################

def wuxia_world():
    clear()

    site_link = "https://m.wuxiaworld.co"

    print('Welcome to Wuxia World!')
    print('1. Choose from Faveourites')
    print('2. Search by Novel name')
    print('3. Go Back')

    option = -1
    while(option < 1 or option > 3):
        option = int(input('choice: '))

    if option == 1:
        wuxia_faveourites(site_link)
    elif option == 2:
        wuxia_search(site_link)
    else:
        main()

def wuxia_faveourites(site_link):
    clear()
    print("Favourites!\n")

    try:
        f = open("wuxia_favourites_list.txt", 'r')
        favs = f.readlines()
    except:
        f = open("wuxia_favourites_list.txt", 'a+')
        favs = []
    
    if (len(favs) != 0):
        for i, line in enumerate(favs, 1):
            print("{}. {}".format(i, line.replace('\n', '')))
        print('{}. Go Back'.format(len(favs)+1))
    else:
        print('No Favourites Added yet')
        print('1. Go Back')
        backop = -1
        while backop != 1:
            backop = int(input('choice: '))
        
        if backop == 1:
            wuxia_world()

    f.close()

    print('\n')
    option = -1
    while(option < 1 or option > len(favs)+1):
        option = int(input('choice: '))

    

    if option == len(favs)+1:
        wuxia_world()
    else:
        novel_name = favs[option-1]
        novel = novel_name.lower().replace(' ', '-')
        novel_page_link = site_link + '/' +  novel.replace("'", '-') + '/'
        wuxia_novel(novel_name, novel_page_link)

def wuxia_search(novel_link):
    clear()
    print("Search Page!\n")
    return 1

def wuxia_novel(novel_name, novel_page_link):
    clear()
    print("Chapter List of\n{}".format(novel_name))
    # print(novel_page_link)
    novel_page_html = get_page_html(novel_page_link)
    chapter_list = novel_page_html.find_all("a", class_="chapter-item")

    for chapter in chapter_list:
        print(chapter)
    return 1

########################################    Wuxia World End    ########################################

########################################    Novel Full Start   ########################################

def novel_full():
    clear()
    return 1

########################################     Novel Full End    ########################################

###########################################    Main Start   ###########################################

def main():
    clear()

    print("Choose your preferred Website?")
    print("1. Wuxiaworld")
    print("2. Novelfull")

    site_choice = -1
    while(site_choice < 1 or site_choice > 2):
        site_choice = int(input('choice: '))

    if site_choice == 1:
        wuxia_world()
    else:
        novel_full()

if __name__=="__main__":
    main()

###########################################     Main End    ###########################################