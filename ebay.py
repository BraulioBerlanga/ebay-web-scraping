from bs4 import BeautifulSoup
import requests
import lxml
import doc_handler

print("program is running...")

#will take the first index-1 pages
index=3

for x in range(index):
    result = requests.get("https://www.ebay.com/sch/i.html?_from=R40&_nkw=phone+case&_sacat=0&LH_TitleDesc=0&_dmd=1&rt=nc&_pgn="+str(x+1))
    src=result.content
    soup=BeautifulSoup(src,'lxml')

    tags_li=soup.find_all('li')
    record=1
    for li in tags_li:
        try:
            if li.attrs['class'][0]=='s-item':
                tags_a=li.find_all('a')
                tags_h3=li.find_all('h3')
                tags_spans=li.find_all('span')
                for a in tags_a:
                    try:
                        if a.attrs['class'][0]=='s-item__link':
                            link=a.attrs['href']
                    except:
                        link='NOTFOUND'
                        pass
                for h3 in tags_h3:
                    try:
                        if h3.attrs['class'][0]=='s-item__title':
                            title=h3.text.replace(",","")
                    except:
                        title='NOTFOUND'
                        pass
                for span in tags_spans:
                    try:
                        if span.attrs['class'][0]=='s-item__price':
                            price=span.text
                    except:
                        price='NOTFOUND'
                        pass
                for span in tags_spans:
                    try:
                        if span.attrs['class'][0]=='s-item__location':
                            location=span.text
                    except:
                        location='NOTFOUND'
                        pass
                for span in tags_spans:
                    try:
                        if span.attrs['class'][0]=='s-item__hotness':
                            sales=span.text
                    except:
                        sales='NOTFOUND'
                        pass
                for span in tags_spans:
                    try:
                        if span.attrs['class'][0]=='s-item__shipping':
                            delivery=span.text
                    except:
                        delivery='NOTFOUND'
                        pass
                try:
                    dict_item={'page':x+1,'record':record,'li':li.attrs['data-view'],'title':title,'price':price,'location':location,'sales':sales,'delivery':delivery,'link':link}
                    doc_handler.Doc_handler(dict_item)
                    record=record+1        
                except:
                    pass
        except:
            pass

print('program have ended')

