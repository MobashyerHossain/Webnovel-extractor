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
    site_link = "https://m.wuxiaworld.co/"
    print('Welcome to Wuxia World!')
    print('1. Browse by Genre')
    print('2. Search by Novel name')
    print('3. Go Back')
    option = int(input('choice: '))

    if option == 1:
        wuxia_genre(site_link)
    elif option == 2:
        wuxia_search(site_link)
    else:
        main()

def wuxia_genre(site_link, genre_link = 'category/0/1.html'):
    clear()
    pg_html = get_page_html(site_link + genre_link)
    
    genre_list = pg_html.find_all(class_=re.compile("cate-list-item"))
    
    print('Choose a Genre?')
    for i, genre in enumerate(genre_list, 1):
        genre = genre.get_text().replace(' ', '')
        print("{}. {}".format(i, genre))
    print("{}. {}".format(len(genre_list)+1, 'Go Back'))
    
    genre_option = -1
    while(genre_option < 1 or genre_option > len(genre_list)):
        genre_option = int(input('choice: '))

    print(genre_list[genre_option-1])

def wuxia_search(site_link):
    clear()
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
    site_choice = int(input("Choice: "))

    if site_choice == 1:
        wuxia_world()
    else:
        novel_full()

if __name__=="__main__":
    main()

###########################################     Main End    ###########################################