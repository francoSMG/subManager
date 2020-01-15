import subdivx 
manager=subdivx.manager(username='yourUser',password='yourPassword')
manager.connect()
subsLinks=manager.search(query='Big Bang ',pageRange=range(1,2))
for link in subsLinks:
    manager.downloadSub(url=link,destinationFolder='./example')