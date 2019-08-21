import bs4
import urllib.request as req
#import webbrowser
def movies(query):
    link='https://www.indiatoday.in/'+query
    httpresponse=req.urlopen(link)
    #webbrowser.open(link)
    page=bs4.BeautifulSoup(httpresponse,features="html.parser")
    #page
    data=page.find('div',class_='row itg-common-section')
    #print(data)
    j=1
    link=data.find_all('p')
    link=link[:5]
    for i in link:
        news=str(j)+'.'+i.text
        print(news)
        #movie_news=news
        j+=1
    #return movie_news
#link=data.find_all.('a')[3]['href']
#print(link)
def tech(query):
    link='https://www.indiatoday.in/'+query
    httpresponse=req.urlopen(link)
    #webbrowser.open(link)
    page=bs4.BeautifulSoup(httpresponse,features="html.parser")
    page
    data=page.find('div',class_='special-top-news')
    #print(data)
    info=data.find_all('li')
    j=1
    info=info[:5]
    for i in info:
        news=str(j)+'.'+i.text
        print(news)
        j+=1
    #return 0

def sports(query):
    link='https://www.indiatoday.in/'+query
    httpresponse=req.urlopen(link)
    #webbrowser.open(link)
    page=bs4.BeautifulSoup(httpresponse,features="html.parser")
    #print(page)
    data=page.find('div',class_='special-top-news')
    #print(data)
    info=data.find_all('li')
    j=1
    info=info[:5]
    for i in info:
        news=str(j)+'.'+i.text
        print(news)
        j+=1
    #return sports_news
        

def trending(query):
    link='https://www.indiatoday.in/'+query
    httpresponse=req.urlopen(link)
    #webbrowser.open(link)
    page=bs4.BeautifulSoup(httpresponse,features="html.parser")
    #print(page)
    data=page.find('div',class_='view-content')
    info=data.find_all('h2')
    j=1
    info=info[:5]
    for i in info:
        news=str(j)+'.'+i.text
        print(news)
        j+=1
    #return trending_news
# name=input("Enter the category of News - movies , sports , technology, trending ")
# def main():
#     if name == 'movies':
#         movies()
#     elif name == 'sports':
#         sports()
#     elif name == 'technology':
#         tech()
#     elif name == 'trending':
#         trending()
#     else:
#         print("Kindly Select From The Category ")
# main()
