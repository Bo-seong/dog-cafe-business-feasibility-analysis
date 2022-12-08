import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import insertDB
from server import chatServer
import webbrowser

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("2team/2team.ui")[0]


class ReceiveQThread(QThread):
    receive = pyqtSignal(str)

    def __init__(self, server : chatServer):
        super().__init__()
        self.server = server

    def run(self):
        while True:
            msg = self.server.receive()
            if not msg:
                break
            print(msg)
            self.receive.emit(msg)

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('SERVER_Window')
        con_db = insertDB.connectDB('root', '0000')

        lis_tot_sco = self.gu_score()

        #광산구
        self.gwang_label_park2_2.setText(str((con_db.select_sql("SELECT count(*) FROM crawling.analysis_element WHERE category = '미용' AND gu='광산구';"))[0][0]) + '개')
        self.gwang_label_dog2.setText(str((con_db.select_sql("SELECT sum(dog_number) FROM crawling.dog_register WHERE gu = '광산구';"))[0][0]) + '마리')
        self.gwang_label_hospi2.setText(str((con_db.select_sql("SELECT count(*) FROM crawling.analysis_element WHERE gu = '광산구' AND category = '병원';"))[0][0]) + '개')
        self.gwang_label_salon2.setText(str((con_db.select_sql("SELECT count(*) FROM crawling.analysis_element WHERE gu = '광산구' AND category = '미용';"))[0][0]) + '개')
        self.gwang_label_rival2.setText(str((con_db.select_sql("SELECT count(*) FROM crawling.analysis_element WHERE gu = '광산구' AND category = '애견카페';"))[0][0]) + '개')
        self.gwang_label_count2.setText(str(lis_tot_sco[0]) + '점')
        self.gwang_link_btn.clicked.connect(lambda: webbrowser.open("https://new.land.naver.com/offices?ms=35.1511,126.7279,13&a=TJ&e=RETAIL&h=330&ad=true"))
        
        #동구
        self.dong_label_park2.setText(str((con_db.select_sql("SELECT count(*) FROM crawling.analysis_element WHERE category = '미용' AND gu='동구';"))[0][0]) + '개')
        self.dong_label_dog2.setText(str((con_db.select_sql("SELECT sum(dog_number) FROM crawling.dog_register WHERE gu = '동구';"))[0][0]) + '마리')
        self.dong_label_hospi2.setText(str((con_db.select_sql("SELECT count(*) FROM crawling.analysis_element WHERE gu = '동구' AND category = '병원';"))[0][0]) + '개')
        self.dong_label_salon2.setText(str((con_db.select_sql("SELECT count(*) FROM crawling.analysis_element WHERE gu = '동구' AND category = '미용';"))[0][0]) + '개')
        self.dong_label_rival2.setText(str((con_db.select_sql("SELECT count(*) FROM crawling.analysis_element WHERE gu = '동구' AND category = '애견카페';"))[0][0]) + '개')
        self.dong_label_count2.setText(str(lis_tot_sco[2]) + '점')
        self.dong_link_btn.clicked.connect(lambda: webbrowser.open("https://new.land.naver.com/offices?ms=35.1259285,126.9380163,14&a=TJ&e=RETAIL&h=330&ad=true"))

        #서구
        self.seo_label_park2.setText(str((con_db.select_sql("SELECT count(*) FROM crawling.analysis_element WHERE category = '미용' AND gu='서구';"))[0][0]) + '개')
        self.seo_label_dog2.setText(str((con_db.select_sql("SELECT sum(dog_number) FROM crawling.dog_register WHERE gu = '서구';"))[0][0]) + '마리')
        self.seo_label_hospi2.setText(str((con_db.select_sql("SELECT count(*) FROM crawling.analysis_element WHERE gu = '서구' AND category = '병원';"))[0][0]) + '개')
        self.seo_label_salon2.setText(str((con_db.select_sql("SELECT count(*) FROM crawling.analysis_element WHERE gu = '서구' AND category = '미용';"))[0][0]) + '개')
        self.seo_label_rival2.setText(str((con_db.select_sql("SELECT count(*) FROM crawling.analysis_element WHERE gu = '서구' AND category = '애견카페';"))[0][0]) + '개')
        self.seo_label_count2.setText(str(lis_tot_sco[4]) + '점')
        self.seo_link_btn.clicked.connect(lambda: webbrowser.open("https://new.land.naver.com/offices?ms=35.1330184,126.8563914,14&a=TJ&e=RETAIL&h=330&ad=true"))
        
        #남구
        self.nam_label_park2.setText(str((con_db.select_sql("SELECT count(*) FROM crawling.analysis_element WHERE category = '미용' AND gu='남구';"))[0][0]) + '개')
        self.nam_label_dog2.setText(str((con_db.select_sql("SELECT sum(dog_number) FROM crawling.dog_register WHERE gu = '남구';"))[0][0]) + '마리')
        self.nam_label_hospi2.setText(str((con_db.select_sql("SELECT count(*) FROM crawling.analysis_element WHERE gu = '남구' AND category = '병원';"))[0][0]) + '개')
        self.nam_label_salon2.setText(str((con_db.select_sql("SELECT count(*) FROM crawling.analysis_element WHERE gu = '남구' AND category = '미용';"))[0][0]) + '개')
        self.nam_label_rival2.setText(str((con_db.select_sql("SELECT count(*) FROM crawling.analysis_element WHERE gu = '남구' AND category = '애견카페';"))[0][0]) + '개')
        self.nam_label_count2.setText(str(lis_tot_sco[1]) + '점')
        self.nam_link_btn.clicked.connect(lambda: webbrowser.open("https://new.land.naver.com/offices?ms=35.115468,126.8987059,14&a=TJ&e=RETAIL&h=330&ad=true"))
        
        # 북구
        self.buk_label_park2.setText(str((con_db.select_sql("SELECT count(*) FROM crawling.analysis_element WHERE category = '미용' AND gu='북구';"))[0][0]) + '개')
        self.buk_label_dog2.setText(str((con_db.select_sql("SELECT sum(dog_number) FROM crawling.dog_register WHERE gu = '북구';"))[0][0]) + '마리')
        self.buk_label_hospi2.setText(str((con_db.select_sql("SELECT count(*) FROM crawling.analysis_element WHERE gu = '북구' AND category = '병원';"))[0][0]) + '개')
        self.buk_label_salon2.setText(str((con_db.select_sql("SELECT count(*) FROM crawling.analysis_element WHERE gu = '북구' AND category = '미용';"))[0][0]) + '개')
        self.buk_label_rival2.setText(str((con_db.select_sql("SELECT count(*) FROM crawling.analysis_element WHERE gu = '북구' AND category = '애견카페';"))[0][0]) + '개')
        self.buk_label_count2.setText(str(lis_tot_sco[3]) + '점')
        self.buk_link_btn.clicked.connect(lambda: webbrowser.open("https://new.land.naver.com/offices?ms=35.1888735,126.932094,14&a=TJ&e=RETAIL&h=330&ad=true"))

        self.stackedWidget:QStackedWidget # class type 지정해주기
        self.stackedWidget.setCurrentIndex(0) # 시작 페이지 지정

        self.btn_start_1.clicked.connect(self.nextPage)
        self.btn_gwang_1.clicked.connect(self.gwangpage)
        self.btn_dong_1.clicked.connect(self.dongpage)
        self.btn_seo_1.clicked.connect(self.seopage)
        self.btn_nam_1.clicked.connect(self.nampage)
        self.btn_buk_1.clicked.connect(self.bukpage)

        self.btn_gwang_pre.clicked.connect(self.choicePage)
        self.btn_dong_pre.clicked.connect(self.choicePage)
        self.btn_seo_pre.clicked.connect(self.choicePage)
        self.btn_nam_pre.clicked.connect(self.choicePage)
        self.btn_buk_pre.clicked.connect(self.choicePage)
        self.btn_sangdam_pre.clicked.connect(self.choicePage)
        self.btn_talk.clicked.connect(self.talkpage)

        self.btn_SendMessage.clicked.connect(self.chat)
        self.inputChat.returnPressed.connect(self.chat)

        self.server = chatServer()
        self.server.setting()
        self.server.setupSock()
        # self.server.send("msg")
        self.sametime = ReceiveQThread(server=self.server)
        self.sametime.receive.connect(self.printChat)
        # self.sametime.receive.connect(self.receivechat)
        self.sametime.start()
    
        # DB 연결 종료
        con_db.close_db()


    def nextPage(self) :  #다음페이지 함수
        # btn :QPushButton = self.sender()
        page = self.stackedWidget.currentIndex() # 현재 페이지 넘버 가져오기
        self.stackedWidget.setCurrentIndex(page + 1) #현재 페이지에서  + 1

    def choicePage(self) :  #선택페이지로 돌아가는 함수
        self.stackedWidget.setCurrentIndex(1)

    def gwangpage(self):
        self.stackedWidget.setCurrentIndex(2)

    def dongpage(self):
        self.stackedWidget.setCurrentIndex(3)

    def seopage(self):
        self.stackedWidget.setCurrentIndex(4)

    def nampage(self):
        self.stackedWidget.setCurrentIndex(5)

    def bukpage(self):
        self.stackedWidget.setCurrentIndex(6)

    def talkpage(self):
        self.stackedWidget.setCurrentIndex(7)

    def gu_score(self):
        con_db = insertDB.connectDB('root', '0000')
         # 점수
        result = con_db.select_sql(
            """SELECT ani_hos_score, ani_salon_score, ani_reg_score, park_score, popul_score
            FROM crawling.total_score"""
            )

        rival_score = con_db.select_sql(
            """SELECT rival_score
            FROM crawling.total_score""")

        lis = []

        for i in range(5):
            res = 0
            for j in range(5):
                res += result[i][j]
            lis.append(res * 4 - rival_score[i][0] * 3)

        return lis

    def chat(self):
        msg = "상담사:" + self.inputChat.text()
        self.inputChat.clear()
        self.chatTextBrowser.append(msg)
        self.server.send(msg)

    # def receivechat(self):
    #     receiveDate = self.server.receive()
    #     self.chatTextBrowser.append(receiveDate)

    def printChat(self, msg):
        self.chatTextBrowser.append(msg)


if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_() 