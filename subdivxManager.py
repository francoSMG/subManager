class subdivxManager:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        import requests
        from lxml import html
        self.session_requests = requests.session()
    
    def connect(self):
        login_url = "http://www.subdivx.com/X50"
        result = self.session_requests.get(login_url)
        payload={
                "usuario":self.username,
                "clave":self.password,
                "accion":"50",
                "enviau":"1",
                "refer":"https://www.subdivx.com/index.php?abandon=1"
                }
        result = self.session_requests.post(
        	login_url, 
        	data = payload, 
        	headers = dict(referer=login_url)  
        )
        
    def search(self,query,pageRange=range(1,10)):      
        links=list()
        for page in pageRange:
            url = 'https://www.subdivx.com/index.php?accion=5&buscar='+query+'&masdesc=&idusuario=&nick=&oxfecha=&oxcd=&oxdown=&pg='+str(page)
            result = self.session_requests.get(
            	url, 
            	headers = dict(referer = url)
            )

            from bs4 import BeautifulSoup
            import urllib.parse as urlparse
            from urllib.parse import parse_qs
            soup = BeautifulSoup(result.content,features="lxml")
            allSubs=soup.find_all(id='buscador_detalle_sub_datos')
            print(allSubs)
            for subs in allSubs:
                htmlLink=subs.find_all(rel='nofollow',href=True,target='new')
                link=str(htmlLink[0]['href'])
                links.append(link)
            return links
        
    def downloadSub(self,url,destinationFolder):
        import urllib.request
        import time
        import random
        import os
        from zipfile import ZipFile
        print('\n downloading '+url)
        zipfile=destinationFolder+'/temp.zip'
        urllib.request.urlretrieve(url,zipfile)
        print('\n descomprimiendo')
        try: 
            with ZipFile(zipfile, 'r') as zipObj:
                zipObj.extractall(destinationFolder)
        except:
            os.system('unrar x '+zipfile+' '+destinationFolder)
        time.sleep(0.1+random.randrange(1,5,1)) #Para evitar negación de servicios DOS (mantener esta linea)!
        print('Done')
        
manager=subdivxManager(username='USER',password='PASS')
manager.connect()
subsLinks=manager.search(query='Big Bang ',pageRange=range(1,30))
for link in subsLinks:
    manager.downloadSub(url=link,destinationFolder='DIRECTORIO')