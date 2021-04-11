import requests
import threading
import time
import os
def main():
    print('''

   _____       _       ______ _           _
  / ____|     | |     |  ____(_)         | |
 | (___  _   _| |__   | |__   _ _ __   __| | ___ _ __
  \___ \| | | | '_ \  |  __| | | '_ \ / _` |/ _ \ '__|
  ____) | |_| | |_) | | |    | | | | | (_| |  __/ |
 |_____/ \__,_|_.__/  |_|    |_|_| |_|\__,_|\___|_|




                    Code By it4min
                    SubDomain Finder
                    Telegram Channel: t.me/LinuxArmy

                [1] Use your word list
                [2] Use ready word list

    ''')

def yscan():
    def domain_scanner(domain_name,sub_domnames):
        for subdomain in sub_domnames:
            url = f"https://{subdomain}.{domain_name}"
            try:
                requests.get(url)
                print(f'[+] {url}')
            except requests.ConnectionError:
                pass
        print('***** Scanning Finished *****')
    if __name__ == '__main__':
        print('''

   _____       _       ______ _           _             __
  / ____|     | |     |  ____(_)         | |           /_ |
 | (___  _   _| |__   | |__   _ _ __   __| | ___ _ __   | |
  \___ \| | | | '_ \  |  __| | | '_ \ / _` |/ _ \ '__|  | |
  ____) | |_| | |_) | | |    | | | | | (_| |  __/ |     | |
 |_____/ \__,_|_.__/  |_|    |_|_| |_|\__,_|\___|_|     |_|




                ''')
        dom_name = input("Enter The Domain Name>>> ")
        wordlist= input("Enter The WordList Name>>> ")
        with open(wordlist,'r') as file:
            name = file.read()
            sub_dom = name.splitlines()
        domain_scanner(dom_name,sub_dom)



def rscan():
    def start():
        print ('''

   _____       _       ______ _           _             ___
  / ____|     | |     |  ____(_)         | |           |__ \
 | (___  _   _| |__   | |__   _ _ __   __| | ___ _ __     ) |
  \___ \| | | | '_ \  |  __| | | '_ \ / _` |/ _ \ '__|   / /
  ____) | |_| | |_) | | |    | | | | | (_| |  __/ |     / /_
 |_____/ \__,_|_.__/  |_|    |_|_| |_|\__,_|\___|_|    |____|





        ''')
    def Desc():
    	time.sleep(1)
    	global url
    	url = str(input("Enter The Domain Name>>> "))
    def find():
    	payload = 'https://api.hackertarget.com/hostsearch/?q=%s' % (url,)
    	print (" [*] Please Wait...\n")
    	result = requests.get(payload)
    	print (" --------------------------------")
    	print (result.text)
    	print (" --------------------------------")
    if __name__ == '__main__':
    	start()
    	Desc()
    	print ("\n*************** [ Subdomains ] ***************\n")
    	find()
if __name__ == '__main__':
    os.system('clear')
    main()
    x=input('Enter your number>>> ')
    if x == '1':
        os.system('clear')
        yscan()
    if x == '2':
        os.system('clear')
        rscan()
