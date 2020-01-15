import subdivx 
manager=subdivx.manager(username='fm2020',password='qweasd')
manager.connect()
subsLinks=manager.search(query='Big Bang ',pageRange=range(1,2))
for link in subsLinks:
    manager.downloadSub(url=link,destinationFolder='./example')