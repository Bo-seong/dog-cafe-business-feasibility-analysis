import pandas as pd

title=[]
address =[]

for i in range(1,14):
    vetname = pd.read_html("https://www.animal.go.kr/front/awtis/shop/hospitalList.do?totalCount=126&pageSize=10&bizKnCd=&boardId=shop&latitude=&longitude=&checkGeoloc=Y&menuNo=6000000002&searchUprCd=6290000&searchOrgCd=&searchCoNm=&searchPmsnNo=&&page=" + str(i))
    for i in range(len(vetname[0]["병원명"])):
        title.append(vetname[0]["병원명"][i])
        address.append(' '.join(vetname[0]["소재지"][i].split()[:2]))
print(title)
print(address)



list_name_addr = []
for i in range(len(title)):
    lis = []
    lis.append("병원")
    lis.append(address[i])
    lis.append(title[i])
    list_name_addr.append(lis)

print(list_name_addr)


import insertDB

conDB = insertDB.connectDB('root', '1234')
query = "INSERT INTO crawling.analysis_element (category, gu, element_name) VALUES (%s, %s, %s)"
conDB.insert_many_sql(query, list_name_addr)
conDB.close_db()
print("완료")