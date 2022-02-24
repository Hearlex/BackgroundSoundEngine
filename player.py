import threading
import time
import random
import os
import sys
import simpleaudio as sa
from pydub import AudioSegment
from pydub.playback import play
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QFileDialog, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox
from PyQt6.QtGui import QIcon, QAction, QPixmap
from extras import addKeysToCombo, keyNames


picFormats = [".jpg", ".png"]
audFormats = [".wav", ".mp3"]

""" mserver = Server() DEPRECATED
mserver.boot() """

# List of Music
folder = ""
currentMusic = ""
contSongs = False
musicList = [os.path.abspath("hknotif.wav").replace('\\', '/')]
print(musicList[0])
pictureList = []
window = ""
keylist = []
keyConfig = dict()


# Audio Check
""" test = AudioSegment.empty()
test = AudioSegment.from_wav(musicList[0])
music = sa.play_buffer(test, 2, 1, 44100) """

music = sa.PlayObject(1)

# Creates the left and right players -- DEPRECATED
""" sfL = SfPlayer(musicList[0]).out()
sfR = SfPlayer(musicList[0]).out(1) """

def updateKeyConfig():
    list = keylist
    keyConfig.clear()
    for item in list:
        keyConfig[item['key'].currentText()]=item['path']

def playMusic():
    global contSongs
    contSongs = True
    newMusic()

def newMusic():
    if contSongs and len(musicList)>0:
        nextPic(window.screen.screenLabel)
        id = random.randint(0, len(musicList)-1)
        path = folder + musicList[id]
        print(path)
        song = AudioSegment.empty()
        if musicList[id].endswith('.wav'):
            song = AudioSegment.from_wav(path)
        elif musicList[id].endswith('.mp3'):
            song = AudioSegment.from_mp3(path)
        song.fade_in(2000).fade_out(3000)
        
        global music
        music = sa.play_buffer(song.raw_data, 2, 2, 44100)
        
        """ Deprecated
        sfL.path = path
        sfR.path = path
        sfL.out()
        sfR.out() """
    elif len(musicList) == 0:
        print("No Music!")

def newList(path):
    global folder
    folder = path+"/"
    musicList.clear()
    with os.scandir(path) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_file():
                if entry.name.endswith(tuple(audFormats)): musicList.append(entry.name)
                elif entry.name.endswith(tuple(picFormats)): pictureList.append(entry.name)
                print(entry.name)

def getList():
    print(musicList, pictureList)

def stopMusic():
    global contSongs
    global music
    contSongs = False
    music.stop()
    #sfL.stop()
    #sfR.stop()
    
""" DEPRECATED
tfL = TrigFunc(sfL["trig"], newMusic)
mserver.start() """
# Repeat Songs
def runningCheck():
    time.sleep(1)
    global contSongs
    global music
    while True:
        if contSongs and not music.is_playing():
            newMusic()


# Picture Slideshow
def nextPic(screen):
    w = screen.width()
    h = screen.height()
    if len(pictureList) > 0:
        id = random.randint(0, len(pictureList)-1)
        path = folder + pictureList[id]
        pixmap = QPixmap(path)
        screen.setPixmap(pixmap.scaled(w,h,Qt.AspectRatioMode.KeepAspectRatio))

class ScreenWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        #flags = Qt.WindowType.Window | Qt.WindowType.WindowTitleHint | Qt.WindowType.CustomizeWindowHint
        
        self.screenLabel = QLabel(self)
        self.setCentralWidget(self.screenLabel)
        self.screenLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setGeometry(100, 100, 200, 200)
        self.setWindowTitle('Player')
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.WindowTitleHint | Qt.WindowType.CustomizeWindowHint)
        self.setStyleSheet("background-color: black;")
        self.show()
        
    def keyPressEvent(self, e):
        if e.key() == Qt.Key.Key_F11:
            if self.isFullScreen():
                self.showNormal()
            else:
                self.showFullScreen()
                
        for keyName in keyNames:
            if e.key() == eval("Qt.Key.Key_{0}".format(keyName)):
                if keyName in keyConfig:
                    newList(keyConfig[keyName])
                    playMusic()



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.screen = ScreenWindow()


    def initUI(self):        
        # Widgets
        self.currentFolderLabel = QLabel(folder)
        
        self.playBtn = QPushButton("Play", self)
        self.playBtn.clicked.connect(playMusic)
        self.stopBtn = QPushButton("Stop", self)
        self.stopBtn.clicked.connect(stopMusic)
        
        # Layout
        layout = QVBoxLayout()
        layout.addSpacing(10)
        menulayout = QHBoxLayout()
        menulayout.addStretch(1)
        menulayout.addWidget(self.playBtn)
        menulayout.addWidget(self.stopBtn)
        self.shortkeyList = QVBoxLayout()
        layout.addLayout(self.shortkeyList)
        layout.addStretch(1)
        layout.addLayout(menulayout)
        layout.addWidget(self.currentFolderLabel)
        
        # Central
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(layout)
        self.setCentralWidget(self.mainWidget)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new Folder')
        openFile.triggered.connect(self.showDialog)
        
        addShortKey = QAction(QIcon('add.png'), 'Add Shortkey', self)
        addShortKey.setShortcut('Ctrl+N')
        addShortKey.setStatusTip('Add a new Shortkey for a folder')
        addShortKey.triggered.connect(self.addSK)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Folder')
        fileMenu.addAction(openFile)
        fileMenu.addAction(addShortKey)

        self.setGeometry(300, 300, 550, 450)
        self.setWindowTitle('Player')
        self.show()


    def showDialog(self):

        fname = ""
        home_dir = ""
        fname = QFileDialog.getExistingDirectory(self, "Select Directory")

        if fname:
           self.currentFolderLabel.setText(fname)
           newList(fname)
            
    def addSK(self):
        line = QHBoxLayout()
        folderLabel = QLabel()
        key = QComboBox()
        addKeysToCombo(key)
        fname = ""
        home_dir = ""
        fname = QFileDialog.getExistingDirectory(self, "Select Directory")
        
        key.activated.connect(updateKeyConfig)

        if fname:
           folderLabel.setText(fname)
           line.addWidget(key)
           line.addWidget(folderLabel)
           self.shortkeyList.addLayout(line)
           
           frame = dict()
           frame['key'] = key
           frame['path'] = fname
           keylist.append(frame)
        
        
           
    def closeEvent(self, event):
        self.screen.close()

def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    global window
    window = ex
    sys.exit(app.exec())

if __name__ == '__main__':
    t1 = threading.Thread(target=main)
    t2 = threading.Thread(target=runningCheck,daemon=True)
    
    t1.start()
    t2.start()
    
    t1.join()