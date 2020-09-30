from bs4 import BeautifulSoup as soup
from docx import Document
import regex as re

wuxia_world():
    print('Welcome to Wuxia World!')
    print('1. List of Light Novel')
    print('2. List of Genre')
    print('3. Search by name')
    novel = input('Name of Novel: ')


novel_full():
    return 1

def main():
    print("Choose your preferred site?")
    print("1. Wuxiaworld")
    print("2. Novelfull")
    site_choice = int(input("Choice: "))

    if site_choice == 1:
        wuxia_world()
    else:
        novel_full()

if __name__=="__main__":
    main()