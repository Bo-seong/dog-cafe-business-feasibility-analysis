import operator
import insertDB
conDb = insertDB.connectDB('root','1234')
analysis_element =conDb.select_sql("""
        element_id AS '업체번호',
        category AS '종류',
        gu AS '애견구',
        element_name AS '업체명'
        """,'crawling.analysis_element')

dog_register = conDb.select_sql("""
        dog_register_id AS '애견번호',
        city AS '시',
        gu AS '마릿수구',
        dong AS '동',
        dog_number AS '애견수'
        """,'crawling.dog_register')

population = conDb.select_sql("""
        gu AS '인구수구',
        2006_pop AS '시작인구수',
        2021_pop AS '끝인구수'
        """,'crawling.population')

park = conDb.select_sql("""
        gu AS '공원구',
        park_num AS '공원수'
        """,'crawling.park_number')

total_count = conDb.select_sql("""
        *
        """,'crawling.total_count')

total_score = conDb.select_sql("""
        *
        """,'crawling.total_score')


#구 동물병원 카운트
donggu_hospital_count = 0
seogu_hospital_count = 0
namgu_hospital_count = 0
bukgu_hospital_count = 0
Gwangsangu_hospital_count = 0

#구 애견미용실 카운트
donggu_dog_salon_count = 0
seogu_dog_salon_count = 0
namgu_dog_salon_count = 0
bukgu_dog_salon_count = 0
Gwangsangu_dog_salon_count = 0

#관련업체 수
donggu_rival_count = 0
seogu_rival_count = 0
namgu_rival_count = 0
bukgu_rival_count = 0
Gwangsangu_rival_count = 0

#구 애견 등록 수
donggu_dog_registration_count = 0
seogu_dog_registration_count = 0
namgu_dog_registration_count = 0
bukgu_dog_registration_count = 0
Gwangsangu_dog_registration_count = 0

base_dic = {'동구':0,'서구':0,'남구':0,'북구':0,'광산구':0}
hospital_dic = {'동구':0,'서구':0,'남구':0,'북구':0,'광산구':0}
dog_salon_dic = {'동구':0,'서구':0,'남구':0,'북구':0,'광산구':0}
dog_registration_dic = {'동구':0,'서구':0,'남구':0,'북구':0,'광산구':0}
park_dic = {'동구':0,'서구':0,'남구':0,'북구':0,'광산구':0}
rival_dic = {'동구':0,'서구':0,'남구':0,'북구':0,'광산구':0}
population_start_dic = {'동구':0,'서구':0,'남구':0,'북구':0,'광산구':0}
population_end_dic = {'동구':0,'서구':0,'남구':0,'북구':0,'광산구':0}
population_dic = {'동구':0,'서구':0,'남구':0,'북구':0,'광산구':0}
population_score = {'동구':0,'서구':0,'남구':0,'북구':0,'광산구':0}


for idx in analysis_element:
  if idx['종류']=='병원':
    if idx['애견구']=='동구':
      donggu_hospital_count+=1
    elif idx['애견구']=='서구':
      seogu_hospital_count+=1
    elif idx['애견구']=='남구':
      namgu_hospital_count+=1
    elif idx['애견구']=='북구':
      bukgu_hospital_count+=1
    elif idx['애견구']=='광산구':
      Gwangsangu_hospital_count+=1
  if idx['종류']=='미용':
    if idx['애견구']=='동구':
      donggu_dog_salon_count+=1
    elif idx['애견구']=='서구':
      seogu_dog_salon_count+=1
    elif idx['애견구']=='남구':
      namgu_dog_salon_count+=1
    elif idx['애견구']=='북구':
      bukgu_dog_salon_count+=1
    elif idx['애견구']=='광산구':
      Gwangsangu_dog_salon_count+=1
  if idx['종류']=='애견카페':
    if idx['애견구']=='동구':
      donggu_rival_count+=1
    elif idx['애견구']=='서구':
      seogu_rival_count+=1
    elif idx['애견구']=='남구':
      namgu_rival_count+=1
    elif idx['애견구']=='북구':
      bukgu_rival_count+=1
    elif idx['애견구']=='광산구':
      Gwangsangu_rival_count+=1

for idx in dog_register:
  if idx['마릿수구']=='동구':
    donggu_dog_registration_count+=idx['애견수']
  elif idx['마릿수구']=='서구':
    seogu_dog_registration_count +=idx['애견수']
  elif idx['마릿수구']=='남구':
    namgu_dog_registration_count +=idx['애견수']
  elif idx['마릿수구']=='북구':
    bukgu_dog_registration_count +=idx['애견수']
  elif idx['마릿수구']=='광산구':
    Gwangsangu_dog_registration_count +=idx['애견수']

# print(donggu_hospital_count)  
# print(seogu_hospital_count)  
# print(namgu_hospital_count)  
# print(bukgu_hospital_count)  
# print(Gwangsangu_hospital_count) 
# print()
# print(donggu_dog_salon_count)  
# print(seogu_dog_salon_count)  
# print(namgu_dog_salon_count)  
# print(bukgu_dog_salon_count)  
# print(Gwangsangu_dog_salon_count)  
# print()
# print(donggu_rival_count)  
# print(seogu_rival_count)  
# print(namgu_rival_count)  
# print(bukgu_rival_count)  
# print(Gwangsangu_rival_count)  
# print()
# print(donggu_dog_registration_count)
# print(seogu_dog_registration_count)
# print(namgu_dog_registration_count)
# print(bukgu_dog_registration_count)
# print(Gwangsangu_dog_registration_count)

gu_hospital_li = [donggu_hospital_count,seogu_hospital_count,namgu_hospital_count,bukgu_hospital_count,Gwangsangu_hospital_count]
gu_dog_salon_li = [donggu_dog_salon_count,seogu_dog_salon_count,namgu_dog_salon_count,bukgu_dog_salon_count,Gwangsangu_dog_salon_count]
gu_rival_li = [donggu_rival_count,seogu_rival_count,namgu_rival_count,bukgu_rival_count,Gwangsangu_rival_count]
gu_dog_registration_li = [donggu_dog_registration_count ,seogu_dog_registration_count ,namgu_dog_registration_count ,bukgu_dog_registration_count ,Gwangsangu_dog_registration_count ]



analysis_hospital_count_li=[]
analysis_dog_salon_count_li=[]
analysis_rival_count_li=[]
dog_registration_count_li=[]
park_count_li=[]
population_count_li=[]

for population_idx in population:
  population_count_li.append(population_idx['끝인구수'])

for park_idx in park:
  park_count_li.append(park_idx['공원수'])

for i in range(len(gu_hospital_li)):
  analysis_hospital_count_li.append(gu_hospital_li[i])
  analysis_dog_salon_count_li.append(gu_dog_salon_li[i])
  analysis_rival_count_li.append(gu_rival_li[i])
  dog_registration_count_li.append(gu_dog_registration_li[i])

for i,key in enumerate(hospital_dic.keys()):
  hospital_dic[key] = analysis_hospital_count_li[i]
for i,key in enumerate(dog_salon_dic.keys()):
  dog_salon_dic[key] = analysis_dog_salon_count_li[i]
for i,key in enumerate(rival_dic.keys()):
  rival_dic[key] = analysis_rival_count_li[i]
for i,key in enumerate(dog_registration_dic.keys()):
  dog_registration_dic[key] = dog_registration_count_li[i]
for i,key in enumerate(park_dic.keys()):
  park_dic[key] = park_count_li[i]
for i,key in enumerate(population_dic.keys()):
  population_dic[key] = population_count_li[i]


print("count")
print(hospital_dic)
print(dog_salon_dic)
print(dog_registration_dic)
print(park_dic)
print(population_dic)
print(rival_dic)

if (len(total_count)==0):
  for key in base_dic:
    conDb.insert_many_sql("""insert into crawling.total_count (
                                              gu,
                                              ani_hos_count,
                                              ani_salon_count,
                                              ani_reg_count,
                                              park_count,
                                              popul_count,
                                              rival_count,
                                              time_data)
                                              values (%s,%s,%s,%s,%s,%s,%s,CURDATE())""",[(key,hospital_dic[key],dog_salon_dic[key],dog_registration_dic[key],park_dic[key],population_dic[key],rival_dic[key])])




def hospital_logic(gu_hospital,dog_count):
  dog_treat = 500 #병원이 한달에 맡을 수 있는 마릿수
  gu_dog_treat = gu_hospital * dog_treat # 구의 병원 수 * 병원이 한달에 맡을 수 있는 마릿수
  hos_percentage = gu_dog_treat / dog_count
  # print(gu_hospital,dog_count)
  return hos_percentage
 
def dog_salon_logic(gu_salon,dog_count):
  dog_treat = 200 #미용실이 한달에 맡을 수 있는 마릿수
  gu_dog_treat = gu_salon * dog_treat # 구의 미용실 수 * 미용실이 한달에 맡을 수 있는 마릿수
  hos_percentage = gu_dog_treat / dog_count
  # print(gu_hospital,dog_count)
  return hos_percentage

def population_logic(start,end):
  year_gap = 15
  ex1 = 1/year_gap
  pop_percentage = ((end/start*ex1))-(1*ex1)
  return pop_percentage
  # return 


for idx in population:
  population_start_dic[idx['인구수구']]=idx['시작인구수']
  population_end_dic[idx['인구수구']]=idx['끝인구수']




for i,key in enumerate(dog_registration_dic):
  hospital_dic[key] = hospital_logic(analysis_hospital_count_li[i],dog_registration_dic[key])
  dog_salon_dic[key] = dog_salon_logic(analysis_dog_salon_count_li [i],dog_registration_dic[key])
  population_score[key] = population_logic(population_start_dic[key],population_end_dic[key])



hospital_score =dict(sorted(hospital_dic.items(), key = operator.itemgetter(1)))
dog_salon_score =dict(sorted(dog_salon_dic.items(), key = operator.itemgetter(1)))
dog_registration_score =dict(sorted(dog_registration_dic.items(), key = operator.itemgetter(1)))
park_score =dict(sorted(park_dic.items(), key = operator.itemgetter(1)))
population_score_2 =dict(sorted(population_score.items(), key = operator.itemgetter(1)))

print("idx")
print(hospital_score)
print(dog_salon_score)
print(dog_registration_score)
print(park_score)
print(population_score_2)


for i,key in enumerate(hospital_score):
  hospital_score[key]=i+1

for i,key in enumerate(dog_salon_score):
  dog_salon_score[key]=i+1

for i,key in enumerate(dog_registration_score):
  dog_registration_score[key]=i+1

for i,key in enumerate(park_score):
  park_score[key]=i+1

for i,key in enumerate(population_score_2):
  population_score_2[key]=i+1


  
print("score")
print(hospital_score)
print(dog_salon_score)
print(dog_registration_score)
print(park_score)
print(population_score_2)
print(rival_dic)
dddd =0
for key in base_dic:
  print(key,(hospital_score[key]+dog_salon_score[key]+dog_registration_score[key]+park_score[key]+population_score_2[key])*4-(rival_dic[key]*3))
  dddd+=(hospital_score[key]+dog_salon_score[key]+dog_registration_score[key]+park_score[key]+population_score_2[key])*4-(rival_dic[key]*3)

print('평균',dddd/5)

if len(total_score)==0:
  for key in base_dic:
    conDb.insert_many_sql("""insert into crawling.total_score (
                                              gu,
                                              ani_hos_score,
                                              ani_salon_score,
                                              ani_reg_score,
                                              park_score,
                                              popul_score,
                                              rival_score)
                                              values (%s,%s,%s,%s,%s,%s,%s)""",[(key,hospital_score[key],dog_salon_score[key],dog_registration_score[key],park_score[key],population_score_2[key],rival_dic[key])])




