import sys
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QDialog,QApplication,QFileDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
import pandas as pd
import matplotlib.pyplot as plt
import random
import os


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("final.ui",self)
        self.path=os.getcwd()
        self.valuelist=[]
        self.index=0
        self.data=[]
        self.filename=''
        self.Browse.clicked.connect(self.browsefiles)
        self.DataChart.clicked.connect(self.visualization)

    def browsefiles(self):
        self.filename=QFileDialog.getOpenFileName(self,'Open File','D:','CSV files(*.csv)')
        self.Input.setText(self.filename[0])

    def visualization(self):
        try:
            f=self.filename[0]
            df=pd.read_csv(f)
            #print(df)
            #df = pd.read_csv('D:/python lec ss lab/covid.csv')
            del df['WHOR']
            self.index=random.randint(0,50)
            labels= ['Confirmed','Deaths','Recovered','Active','New cases','Confirmed last week']
            self.valuelist=[]
            for i in labels:
                self.valuelist.append(df[i][self.index])
            #print(valuelist)
            columns=df.columns
            self.data=[]
            for i in range(0,5):
                self.data.append( labels[i] + " - " + str(self.valuelist[i]))
            plt.pie(self.valuelist,labels=None)
            plt.title("COVID-19 Data Analysis" + '\n' + 'Country: ' + df['Country'][self.index])
            plt.legend(self.data, bbox_to_anchor=(0.67,0.997), loc="upper left")
            #plt.show()
            plt.savefig('idea.png')
            #print(f)
            Display_Image=QPixmap(self.path+"\\idea.png")
            self.Image1.setPixmap(Display_Image)
        except:
            f=''


app=QApplication(sys.argv)
m = MainWindow()
widget=QtWidgets.QStackedWidget()
widget.addWidget(m)
widget.setFixedWidth(900)
widget.setFixedHeight(800)
widget.show()
app.exec_()
if os.path.exists("idea.png") or os.path.exists(".png"):
  os.remove("idea.png")
  os.remove(".png")
sys.exit()  


