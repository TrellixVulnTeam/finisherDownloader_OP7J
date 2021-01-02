# Gamesdrive Downloader
Script to download finisher site folders at once.\
Sites tested: [ddl2](https://ddl2.finisher.site)\
                 [scarlet2](https://scarlet2.finisher.site)\
                 vallhalla.dyro.me


**Note: You must have Chrome or Firefox (highly recommended) installed.**

## Chrome Users:
  * You'll need to use firefox.
  * Else, you need to update chrome and download the latest stable version of chromedriver.exe from [here](https://chromedriver.chromium.org/downloads) (The version should match with the version of Chrome browser)
  * Paste the chromedriver.exe file to a folder in PATH. I recommend C:\Windows\System32 folder as it is already added in your PATH variable

## Downloading and Installing
### On Windows:
  * Download the relased .zip file from [here](https://github.com/abhiraj2/finisherDownloader/releases/tag/v0.2)
  * Extract the file and launch the main.exe application.
### On Linux:
  * Download the source code and launch the main.py file from the terminal 

## Using the program
The process is the same on both Windows as well as Linux
  * After launching the program, you will be asked to enter the URL for the folder on the Finisher site.
  * Enter the URL and press Enter. 
  * Next the program will scrap the files and folders from the URL entered.
  * **The program will ask you, if you want to change the download location. The default location is your Downloads folder. Press Y/y to change it or N/n to download it in the default location.**
  * After scraping, it will ask for the download location for the files. The default location is the Downloads folder.\
 That should be it, the program should download all the files in that folder including the subfolders.
 It should look something like this\
 ![Image of cmd running main.exe](https://i.ibb.co/4T3FSmJ/Finisher-downloader-scrshot.png)
 
 ## Things to know about using the program.
  * Folders with a huge number of files and subfolders require a good chunk of time. 
  * Program skips some files, so it retries them a maximum of three times. If the file still hasn't been downloaded, you can check debug_files.txt to check them and downloaded them manually.
  * I downloaded a folder with 906 files and 901 files were successfully downloaded. Another time, out of 891 files 886 files were downloaded.
  * If you're getting a large number of skipped files there is a good probability that it is an issue on the servers end. Please check by downloading skipped files manually. 
  * There are no progress bars, so if the program looks stuck on downloading, it is not. Just wait a while.
  * I get upto 8 MB/s on browser when downloading files from the site direcly. I'm getting the same approx speed when downloading via the program.
  * If you get any unusual errors, feel free to contact me at the GamesDrive discord. Username: thundr_strike#4901
