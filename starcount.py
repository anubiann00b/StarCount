from BeautifulSoup import BeautifulSoup
import requests
import operator

def main():
    numPages = 40
    users = {}

    for pageNum in range(1, numPages+1):
        page = requests.get('http://chat.stackexchange.com/rooms/info/16/the-frying-pan/?tab=stars&page=' + str(pageNum))
        soup = BeautifulSoup(page.content)
        addPage(soup, users)
        print 'Page ' + str(pageNum)
        printDict(users)

def addPage(soup, users):
    for div in soup.findAll('div', attrs={'class': 'username'}):
        if div.find('a') is None:
            usernameContainer = div
        else:
            usernameContainer = div.find('a')
        name = usernameContainer.text.encode('utf-8')
        if name in users.keys():
            users[name] += 1
        else:
            users[name] = 1

def printDict(dict):
    for key in sorted(dict, key=dict.get, reverse=True):
        print str(dict[key]) + ': ' + key
    print

if __name__=="__main__":
   main()