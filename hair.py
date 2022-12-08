import pandas as pd

title=[]
address =[]

for i in range(1,31):
    hair = pd.read_html("https://animal.go.kr/front/awtis/shop/salesList.do?totalCount=292&pageSize=10&bizKnCd=&boardId=shop&longitude=&latitude=&sWrkCd=F&menuNo=6000000130&searchUprCd=6290000&searchOrgCd=&busWrkNo=&searchCoNm=&searchPmsnNo=&&page="+ str(i))
    # print(hair)
    for i in range(len(hair[0]["업체명"])):
        title.append(hair[0]["업체명"][i])
        address.append(hair[0]["소재지"][i].split()[:2][1])
print(title)
print(address)


list_name_addr = []
for i in range(len(title)):
    lis = []
    lis.append("미용")
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
