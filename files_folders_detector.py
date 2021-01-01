import requests, time, os
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.firefox import options as fir_options
import re


def ensure_page_loaded(browser, page):
    page_loaded_method = []
    while not page_loaded_method:
        browser.get(page)
        time.sleep(2)
        sub_bruh_folder_method = browser.find_elements_by_class_name('folder')
        sub_bruh_files_method = browser.find_elements_by_class_name('file')
        folder_i_method = 0
        file_i_method = 0
        while True:
            if folder_i_method < len(sub_bruh_folder_method) and sub_bruh_folder_method[folder_i_method].find_elements_by_tag_name('div'):
                page_loaded_method.append(sub_bruh_folder_method[folder_i_method])
            if file_i_method < len(sub_bruh_files_method) and sub_bruh_files_method[file_i_method].find_elements_by_tag_name('div'):
                page_loaded_method.append(sub_bruh_files_method[file_i_method])
            if file_i_method >= len(sub_bruh_files_method) and folder_i_method >= len(sub_bruh_folder_method):
                break
            file_i_method = file_i_method + 1
            folder_i_method = folder_i_method + 1


def scraping_files_and_folders():
    browser = None
    url = input("Enter the URL for the Finisher to download: ")

    try:
        chrome_options = options.Options()
        chrome_options.add_argument("--headless")
        browser = webdriver.Chrome(options=chrome_options)
        print("Chrome Found.")
        browser.maximize_window()
    except(IOError, Exception):
        print("Chrome not Found. Moving to Firefox.")
        pass
    if not browser:
        try:
            firefox_options = fir_options.Options()
            firefox_options.add_argument("--headless")
            browser = webdriver.Firefox(options=firefox_options)
            print("Firefox Found.")
            browser.maximize_window()
        except(IOError, Exception):
            print("Firefox not found. Get one of these")
            pass

    folder_url = open('tempFolder.txt', 'w+')
    file_url = open('tempFile.txt', 'w+')
    folder_url_list = []
    file_url_list = []

    # Ensure that the page is loaded correctly
    ensure_page_loaded(browser, url)
    file = browser.find_elements_by_xpath("//a[@class='file']")
    file_view = browser.find_elements_by_xpath("//a[@class='file view']")
    for i in file:
        file_url_list.append(i.get_attribute('href'))
    for i in file_view:
        file_url_list.append(i.get_attribute('href'))

    index = 1
    folder_url_list.append(browser.find_elements_by_xpath("//a[@class='folder']")[0].get_attribute('href'))
    while True:
        time.sleep(3)
        folder = browser.find_elements_by_class_name("folder")
        real_folders = []
        for i in folder:
            if i.find_elements_by_tag_name("div"):
                real_folders.append(i)
                folder_url_list.append(i.get_attribute('href'))

        if index < len(folder_url_list):
            # Ensure that the page is loaded correctly
            print(f'Scraping Folder...')
            ensure_page_loaded(browser, folder_url_list[index])
            file = browser.find_elements_by_xpath("//a[@class='file']")
            file_view = browser.find_elements_by_xpath("//a[@class='file view']")
            for i in file:
                file_url_list.append(i.get_attribute('href'))
            for i in file_view:
                file_url_list.append(i.get_attribute('href'))
        else:
            break
        index = index + 1

    for i in folder_url_list:
        folder_url.write(str(i) + '\n')
    for i in file_url_list:
        file_url.write(str(i) + '\n')

    f = open('debug_file.txt', 'w+')
    for i in folder_url_list:
        f.write(str(i) + '\n')

    folder_url.close()
    file_url.close()
    time.sleep(3)
    browser.close()
