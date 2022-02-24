from pyo import *
import random
import os
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QFileDialog, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox
from PyQt6.QtGui import QIcon, QAction, QPixmap

picFormats = [".jpg", ".png"]

mserver = Server()
mserver.boot()

# List of Music
folder = ""
currentMusic = ""
contSongs = False
musicList = ["hknotif.wav"]
pictureList = []
window = ""
keylist = []
keyConfig = dict()

# Creates the left and right players
sfL = SfPlayer(musicList[0]).out()
sfR = SfPlayer(musicList[0]).out(1)

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
    if contSongs:
        nextPic(window.screen.screenLabel)
        id = random.randint(0, len(musicList)-1)
        path = folder + musicList[id]
        print(path)
        sfL.path = path
        sfR.path = path
        sfL.out()
        sfR.out()

def newList(path):
    global folder
    folder = path+"/"
    musicList.clear()
    with os.scandir(path) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_file():
                if entry.name.endswith(".wav"): musicList.append(entry.name)
                elif entry.name.endswith(tuple(picFormats)): pictureList.append(entry.name)
                print(entry.name)

def getList():
    print(musicList, pictureList)

def stopMusic():
    global constSongs
    contSongs = False
    sfL.stop()
    sfR.stop()

tfL = TrigFunc(sfL["trig"], newMusic)
mserver.start()

# Add all shortcuts
def addKeysToCombo(combo):
    combo.addItem('Escape')
    combo.addItem('Tab')
    combo.addItem('Backtab')
    combo.addItem('Backspace')
    combo.addItem('Return')
    combo.addItem('Enter')
    combo.addItem('Insert')
    combo.addItem('Delete')
    combo.addItem('Pause')
    combo.addItem('Print')
    combo.addItem('SysReq')
    combo.addItem('Clear')
    combo.addItem('Home')
    combo.addItem('End')
    combo.addItem('Left')
    combo.addItem('Up')
    combo.addItem('Right')
    combo.addItem('Down')
    combo.addItem('PageUp')
    combo.addItem('PageDown')
    combo.addItem('Shift')
    combo.addItem('Control')
    combo.addItem('Meta')
    combo.addItem('Alt')
    combo.addItem('AltGr')
    combo.addItem('CapsLock')
    combo.addItem('NumLock')
    combo.addItem('ScrollLock')
    combo.addItem('F1')
    combo.addItem('F2')
    combo.addItem('F3')
    combo.addItem('F4')
    combo.addItem('F5')
    combo.addItem('F6')
    combo.addItem('F7')
    combo.addItem('F8')
    combo.addItem('F9')
    combo.addItem('F10')
    #combo.addItem('F11')
    combo.addItem('F12')
    combo.addItem('F13')
    combo.addItem('F14')
    combo.addItem('F15')
    combo.addItem('F16')
    combo.addItem('F17')
    combo.addItem('F18')
    combo.addItem('F19')
    combo.addItem('F20')
    combo.addItem('F21')
    combo.addItem('F22')
    combo.addItem('F23')
    combo.addItem('F24')
    combo.addItem('F25')
    combo.addItem('F26')
    combo.addItem('F27')
    combo.addItem('F28')
    combo.addItem('F29')
    combo.addItem('F30')
    combo.addItem('F31')
    combo.addItem('F32')
    combo.addItem('F33')
    combo.addItem('F34')
    combo.addItem('F35')
    combo.addItem('Super_L')
    combo.addItem('Super_R')
    combo.addItem('Menu')
    combo.addItem('Hyper_L')
    combo.addItem('Hyper_R')
    combo.addItem('Help')
    combo.addItem('Direction_L')
    combo.addItem('Direction_R')
    combo.addItem('Space')
    combo.addItem('Any')
    combo.addItem('Exclam')
    combo.addItem('QuoteDbl')
    combo.addItem('NumberSign')
    combo.addItem('Dollar')
    combo.addItem('Percent')
    combo.addItem('Ampersand')
    combo.addItem('Apostrophe')
    combo.addItem('ParenLeft')
    combo.addItem('ParenRight')
    combo.addItem('Asterisk')
    combo.addItem('Plus')
    combo.addItem('Comma')
    combo.addItem('Minus')
    combo.addItem('Period')
    combo.addItem('Slash')
    combo.addItem('0')
    combo.addItem('1')
    combo.addItem('2')
    combo.addItem('3')
    combo.addItem('4')
    combo.addItem('5')
    combo.addItem('6')
    combo.addItem('7')
    combo.addItem('8')
    combo.addItem('9')
    combo.addItem('Colon')
    combo.addItem('Semicolon')
    combo.addItem('Less')
    combo.addItem('Equal')
    combo.addItem('Greater')
    combo.addItem('Question')
    combo.addItem('At')
    combo.addItem('A')
    combo.addItem('B')
    combo.addItem('C')
    combo.addItem('D')
    combo.addItem('E')
    combo.addItem('F')
    combo.addItem('G')
    combo.addItem('H')
    combo.addItem('I')
    combo.addItem('J')
    combo.addItem('K')
    combo.addItem('L')
    combo.addItem('M')
    combo.addItem('N')
    combo.addItem('O')
    combo.addItem('P')
    combo.addItem('Q')
    combo.addItem('R')
    combo.addItem('S')
    combo.addItem('T')
    combo.addItem('U')
    combo.addItem('V')
    combo.addItem('W')
    combo.addItem('X')
    combo.addItem('Y')
    combo.addItem('Z')
    combo.addItem('BracketLeft')
    combo.addItem('Backslash')
    combo.addItem('BracketRight')
    combo.addItem('AsciiCircum')
    combo.addItem('Underscore')
    combo.addItem('QuoteLeft')
    combo.addItem('BraceLeft')
    combo.addItem('Bar')
    combo.addItem('BraceRight')
    combo.addItem('AsciiTilde')
    combo.addItem('nobreakspace')
    combo.addItem('exclamdown')
    combo.addItem('cent')
    combo.addItem('sterling')
    combo.addItem('currency')
    combo.addItem('yen')
    combo.addItem('brokenbar')
    combo.addItem('section')
    combo.addItem('diaeresis')
    combo.addItem('copyright')
    combo.addItem('ordfeminine')
    combo.addItem('guillemotleft')
    combo.addItem('notsign')
    combo.addItem('hyphen')
    combo.addItem('registered')
    combo.addItem('macron')
    combo.addItem('degree')
    combo.addItem('plusminus')
    combo.addItem('twosuperior')
    combo.addItem('threesuperior')
    combo.addItem('acute')
    combo.addItem('mu')
    combo.addItem('paragraph')
    combo.addItem('periodcentered')
    combo.addItem('cedilla')
    combo.addItem('onesuperior')
    combo.addItem('masculine')
    combo.addItem('guillemotright')
    combo.addItem('onequarter')
    combo.addItem('onehalf')
    combo.addItem('threequarters')
    combo.addItem('questiondown')
    combo.addItem('Agrave')
    combo.addItem('Aacute')
    combo.addItem('Acircumflex')
    combo.addItem('Atilde')
    combo.addItem('Adiaeresis')
    combo.addItem('Aring')
    combo.addItem('AE')
    combo.addItem('Ccedilla')
    combo.addItem('Egrave')
    combo.addItem('Eacute')
    combo.addItem('Ecircumflex')
    combo.addItem('Ediaeresis')
    combo.addItem('Igrave')
    combo.addItem('Iacute')
    combo.addItem('Icircumflex')
    combo.addItem('Idiaeresis')
    combo.addItem('ETH')
    combo.addItem('Ntilde')
    combo.addItem('Ograve')
    combo.addItem('Oacute')
    combo.addItem('Ocircumflex')
    combo.addItem('Otilde')
    combo.addItem('Odiaeresis')
    combo.addItem('multiply')
    combo.addItem('Ooblique')
    combo.addItem('Ugrave')
    combo.addItem('Uacute')
    combo.addItem('Ucircumflex')
    combo.addItem('Udiaeresis')
    combo.addItem('Yacute')
    combo.addItem('THORN')
    combo.addItem('ssharp')
    combo.addItem('division')
    combo.addItem('ydiaeresis')
    combo.addItem('Multi_key')
    combo.addItem('Codeinput')
    combo.addItem('SingleCandidate')
    combo.addItem('MultipleCandidate')
    combo.addItem('PreviousCandidate')
    combo.addItem('Mode_switch')
    combo.addItem('Kanji')
    combo.addItem('Muhenkan')
    combo.addItem('Henkan')
    combo.addItem('Romaji')
    combo.addItem('Hiragana')
    combo.addItem('Katakana')
    combo.addItem('Hiragana_Katakana')
    combo.addItem('Zenkaku')
    combo.addItem('Hankaku')
    combo.addItem('Zenkaku_Hankaku')
    combo.addItem('Touroku')
    combo.addItem('Massyo')
    combo.addItem('Kana_Lock')
    combo.addItem('Kana_Shift')
    combo.addItem('Eisu_Shift')
    combo.addItem('Eisu_toggle')
    combo.addItem('Hangul')
    combo.addItem('Hangul_Start')
    combo.addItem('Hangul_End')
    combo.addItem('Hangul_Hanja')
    combo.addItem('Hangul_Jamo')
    combo.addItem('Hangul_Romaja')
    combo.addItem('Hangul_Jeonja')
    combo.addItem('Hangul_Banja')
    combo.addItem('Hangul_PreHanja')
    combo.addItem('Hangul_PostHanja')
    combo.addItem('Hangul_Special')
    combo.addItem('Dead_Grave')
    combo.addItem('Dead_Acute')
    combo.addItem('Dead_Circumflex')
    combo.addItem('Dead_Tilde')
    combo.addItem('Dead_Macron')
    combo.addItem('Dead_Breve')
    combo.addItem('Dead_Abovedot')
    combo.addItem('Dead_Diaeresis')
    combo.addItem('Dead_Abovering')
    combo.addItem('Dead_Doubleacute')
    combo.addItem('Dead_Caron')
    combo.addItem('Dead_Cedilla')
    combo.addItem('Dead_Ogonek')
    combo.addItem('Dead_Iota')
    combo.addItem('Dead_Voiced_Sound')
    combo.addItem('Dead_Semivoiced_Sound')
    combo.addItem('Dead_Belowdot')
    combo.addItem('Dead_Hook')
    combo.addItem('Dead_Horn')
    combo.addItem('Dead_Stroke')
    combo.addItem('Dead_Abovecomma')
    combo.addItem('Dead_Abovereversedcomma')
    combo.addItem('Dead_Doublegrave')
    combo.addItem('Dead_Belowring')
    combo.addItem('Dead_Belowmacron')
    combo.addItem('Dead_Belowcircumflex')
    combo.addItem('Dead_Belowtilde')
    combo.addItem('Dead_Belowbreve')
    combo.addItem('Dead_Belowdiaeresis')
    combo.addItem('Dead_Invertedbreve')
    combo.addItem('Dead_Belowcomma')
    combo.addItem('Dead_Currency')
    combo.addItem('Dead_a')
    combo.addItem('Dead_A')
    combo.addItem('Dead_e')
    combo.addItem('Dead_E')
    combo.addItem('Dead_i')
    combo.addItem('Dead_I')
    combo.addItem('Dead_o')
    combo.addItem('Dead_O')
    combo.addItem('Dead_u')
    combo.addItem('Dead_U')
    combo.addItem('Dead_Small_Schwa')
    combo.addItem('Dead_Capital_Schwa')
    combo.addItem('Dead_Greek')
    combo.addItem('Dead_Lowline')
    combo.addItem('Dead_Aboveverticalline')
    combo.addItem('Dead_Belowverticalline')
    combo.addItem('Dead_Longsolidusoverlay')
    combo.addItem('Back')
    combo.addItem('Forward')
    combo.addItem('Stop')
    combo.addItem('Refresh')
    combo.addItem('VolumeDown')
    combo.addItem('VolumeMute')
    combo.addItem('VolumeUp')
    combo.addItem('BassBoost')
    combo.addItem('BassUp')
    combo.addItem('BassDown')
    combo.addItem('TrebleUp')
    combo.addItem('TrebleDown')
    combo.addItem('MediaPlay')
    combo.addItem('MediaStop')
    combo.addItem('MediaPrevious')
    combo.addItem('MediaNext')
    combo.addItem('MediaRecord')
    combo.addItem('MediaPause')
    combo.addItem('MediaTogglePlayPause')
    combo.addItem('HomePage')
    combo.addItem('Favorites')
    combo.addItem('Search')
    combo.addItem('Standby')
    combo.addItem('OpenUrl')
    combo.addItem('LaunchMail')
    combo.addItem('LaunchMedia')
    combo.addItem('Launch0')
    combo.addItem('Launch1')
    combo.addItem('Launch2')
    combo.addItem('Launch3')
    combo.addItem('Launch4')
    combo.addItem('Launch5')
    combo.addItem('Launch6')
    combo.addItem('Launch7')
    combo.addItem('Launch8')
    combo.addItem('Launch9')
    combo.addItem('LaunchA')
    combo.addItem('LaunchB')
    combo.addItem('LaunchC')
    combo.addItem('LaunchD')
    combo.addItem('LaunchE')
    combo.addItem('LaunchF')
    combo.addItem('LaunchG')
    combo.addItem('LaunchH')
    combo.addItem('MonBrightnessUp')
    combo.addItem('MonBrightnessDown')
    combo.addItem('KeyboardLightOnOff')
    combo.addItem('KeyboardBrightnessUp')
    combo.addItem('KeyboardBrightnessDown')
    combo.addItem('PowerOff')
    combo.addItem('WakeUp')
    combo.addItem('Eject')
    combo.addItem('ScreenSaver')
    combo.addItem('WWW')
    combo.addItem('Memo')
    combo.addItem('LightBulb')
    combo.addItem('Shop')
    combo.addItem('History')
    combo.addItem('AddFavorite')
    combo.addItem('HotLinks')
    combo.addItem('BrightnessAdjust')
    combo.addItem('Finance')
    combo.addItem('Community')
    combo.addItem('AudioRewind')
    combo.addItem('BackForward')
    combo.addItem('ApplicationLeft')
    combo.addItem('ApplicationRight')
    combo.addItem('Book')
    combo.addItem('CD')
    combo.addItem('Calculator')
    combo.addItem('ToDoList')
    combo.addItem('ClearGrab')
    combo.addItem('Close')
    combo.addItem('Copy')
    combo.addItem('Cut')
    combo.addItem('Display')
    combo.addItem('DOS')
    combo.addItem('Documents')
    combo.addItem('Excel')
    combo.addItem('Explorer')
    combo.addItem('Game')
    combo.addItem('Go')
    combo.addItem('iTouch')
    combo.addItem('LogOff')
    combo.addItem('Market')
    combo.addItem('Meeting')
    combo.addItem('MenuKB')
    combo.addItem('MenuPB')
    combo.addItem('MySites')
    combo.addItem('News')
    combo.addItem('OfficeHome')
    combo.addItem('Option')
    combo.addItem('Paste')
    combo.addItem('Phone')
    combo.addItem('Calendar')
    combo.addItem('Reply')
    combo.addItem('Reload')
    combo.addItem('RotateWindows')
    combo.addItem('RotationPB')
    combo.addItem('RotationKB')
    combo.addItem('Save')
    combo.addItem('Send')
    combo.addItem('Spell')
    combo.addItem('SplitScreen')
    combo.addItem('Support')
    combo.addItem('TaskPane')
    combo.addItem('Terminal')
    combo.addItem('Tools')
    combo.addItem('Travel')
    combo.addItem('Video')
    combo.addItem('Word')
    combo.addItem('Xfer')
    combo.addItem('ZoomIn')
    combo.addItem('ZoomOut')
    combo.addItem('Away')
    combo.addItem('Messenger')
    combo.addItem('WebCam')
    combo.addItem('MailForward')
    combo.addItem('Pictures')
    combo.addItem('Music')
    combo.addItem('Battery')
    combo.addItem('Bluetooth')
    combo.addItem('WLAN')
    combo.addItem('UWB')
    combo.addItem('AudioForward')
    combo.addItem('AudioRepeat')
    combo.addItem('AudioRandomPlay')
    combo.addItem('Subtitle')
    combo.addItem('AudioCycleTrack')
    combo.addItem('Time')
    combo.addItem('Hibernate')
    combo.addItem('View')
    combo.addItem('TopMenu')
    combo.addItem('PowerDown')
    combo.addItem('Suspend')
    combo.addItem('ContrastAdjust')
    combo.addItem('TouchpadToggle')
    combo.addItem('TouchpadOn')
    combo.addItem('TouchpadOff')
    combo.addItem('MicMute')
    combo.addItem('Red')
    combo.addItem('Green')
    combo.addItem('Yellow')
    combo.addItem('Blue')
    combo.addItem('ChannelUp')
    combo.addItem('ChannelDown')
    combo.addItem('Guide')
    combo.addItem('Info')
    combo.addItem('Settings')
    combo.addItem('MicVolumeUp')
    combo.addItem('MicVolumeDown')
    combo.addItem('New')
    combo.addItem('Open')
    combo.addItem('Find')
    combo.addItem('Undo')
    combo.addItem('Redo')
    combo.addItem('MediaLast')
    combo.addItem('unknown')
    combo.addItem('Call')
    combo.addItem('Camera')
    combo.addItem('CameraFocus')
    combo.addItem('Context1')
    combo.addItem('Context2')
    combo.addItem('Context3')
    combo.addItem('Context4')
    combo.addItem('Flip')
    combo.addItem('Hangup')
    combo.addItem('No')
    combo.addItem('Select')
    combo.addItem('Yes')
    combo.addItem('ToggleCallHangup')
    combo.addItem('VoiceDial')
    combo.addItem('LastNumberRedial')
    combo.addItem('Execute')
    combo.addItem('Printer')
    combo.addItem('Play')
    combo.addItem('Sleep')
    combo.addItem('Zoom')
    combo.addItem('Exit')
    combo.addItem('Cancel')


# Picture Slideshow
def nextPic(screen):
    w = screen.width()
    h = screen.height()
    
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
        elif e.key() == Qt.Key.Key_Escape:
            if 'Escape' in keyConfig:
                newList(keyConfig['Escape'])
                playMusic()
        elif e.key() == Qt.Key.Key_Tab:
            if 'Tab' in keyConfig:
                newList(keyConfig['Tab'])
                playMusic()
        elif e.key() == Qt.Key.Key_Backtab:
            if 'Backtab' in keyConfig:
                newList(keyConfig['Backtab'])
                playMusic()
        elif e.key() == Qt.Key.Key_Backspace:
            if 'Backspace' in keyConfig:
                newList(keyConfig['Backspace'])
                playMusic()
        elif e.key() == Qt.Key.Key_Return:
            if 'Return' in keyConfig:
                newList(keyConfig['Return'])
                playMusic()
        elif e.key() == Qt.Key.Key_Enter:
            if 'Enter' in keyConfig:
                newList(keyConfig['Enter'])
                playMusic()
        elif e.key() == Qt.Key.Key_Insert:
            if 'Insert' in keyConfig:
                newList(keyConfig['Insert'])
                playMusic()
        elif e.key() == Qt.Key.Key_Delete:
            if 'Delete' in keyConfig:
                newList(keyConfig['Delete'])
                playMusic()
        elif e.key() == Qt.Key.Key_Pause:
            if 'Pause' in keyConfig:
                newList(keyConfig['Pause'])
                playMusic()
        elif e.key() == Qt.Key.Key_Print:
            if 'Print' in keyConfig:
                newList(keyConfig['Print'])
                playMusic()
        elif e.key() == Qt.Key.Key_SysReq:
            if 'SysReq' in keyConfig:
                newList(keyConfig['SysReq'])
                playMusic()
        elif e.key() == Qt.Key.Key_Clear:
            if 'Clear' in keyConfig:
                newList(keyConfig['Clear'])
                playMusic()
        elif e.key() == Qt.Key.Key_Home:
            if 'Home' in keyConfig:
                newList(keyConfig['Home'])
                playMusic()
        elif e.key() == Qt.Key.Key_End:
            if 'End' in keyConfig:
                newList(keyConfig['End'])
                playMusic()
        elif e.key() == Qt.Key.Key_Left:
            if 'Left' in keyConfig:
                newList(keyConfig['Left'])
                playMusic()
        elif e.key() == Qt.Key.Key_Up:
            if 'Up' in keyConfig:
                newList(keyConfig['Up'])
                playMusic()
        elif e.key() == Qt.Key.Key_Right:
            if 'Right' in keyConfig:
                newList(keyConfig['Right'])
                playMusic()
        elif e.key() == Qt.Key.Key_Down:
            if 'Down' in keyConfig:
                newList(keyConfig['Down'])
                playMusic()
        elif e.key() == Qt.Key.Key_PageUp:
            if 'PageUp' in keyConfig:
                newList(keyConfig['PageUp'])
                playMusic()
        elif e.key() == Qt.Key.Key_PageDown:
            if 'PageDown' in keyConfig:
                newList(keyConfig['PageDown'])
                playMusic()
        elif e.key() == Qt.Key.Key_Shift:
            if 'Shift' in keyConfig:
                newList(keyConfig['Shift'])
                playMusic()
        elif e.key() == Qt.Key.Key_Control:
            if 'Control' in keyConfig:
                newList(keyConfig['Control'])
                playMusic()
        elif e.key() == Qt.Key.Key_Meta:
            if 'Meta' in keyConfig:
                newList(keyConfig['Meta'])
                playMusic()
        elif e.key() == Qt.Key.Key_Alt:
            if 'Alt' in keyConfig:
                newList(keyConfig['Alt'])
                playMusic()
        elif e.key() == Qt.Key.Key_AltGr:
            if 'AltGr' in keyConfig:
                newList(keyConfig['AltGr'])
                playMusic()
        elif e.key() == Qt.Key.Key_CapsLock:
            if 'CapsLock' in keyConfig:
                newList(keyConfig['CapsLock'])
                playMusic()
        elif e.key() == Qt.Key.Key_NumLock:
            if 'NumLock' in keyConfig:
                newList(keyConfig['NumLock'])
                playMusic()
        elif e.key() == Qt.Key.Key_ScrollLock:
            if 'ScrollLock' in keyConfig:
                newList(keyConfig['ScrollLock'])
                playMusic()
        elif e.key() == Qt.Key.Key_F1:
            if 'F1' in keyConfig:
                newList(keyConfig['F1'])
                playMusic()
        elif e.key() == Qt.Key.Key_F2:
            if 'F2' in keyConfig:
                newList(keyConfig['F2'])
                playMusic()
        elif e.key() == Qt.Key.Key_F3:
            if 'F3' in keyConfig:
                newList(keyConfig['F3'])
                playMusic()
        elif e.key() == Qt.Key.Key_F4:
            if 'F4' in keyConfig:
                newList(keyConfig['F4'])
                playMusic()
        elif e.key() == Qt.Key.Key_F5:
            if 'F5' in keyConfig:
                newList(keyConfig['F5'])
                playMusic()
        elif e.key() == Qt.Key.Key_F6:
            if 'F6' in keyConfig:
                newList(keyConfig['F6'])
                playMusic()
        elif e.key() == Qt.Key.Key_F7:
            if 'F7' in keyConfig:
                newList(keyConfig['F7'])
                playMusic()
        elif e.key() == Qt.Key.Key_F8:
            if 'F8' in keyConfig:
                newList(keyConfig['F8'])
                playMusic()
        elif e.key() == Qt.Key.Key_F9:
            if 'F9' in keyConfig:
                newList(keyConfig['F9'])
                playMusic()
        elif e.key() == Qt.Key.Key_F10:
            if 'F10' in keyConfig:
                newList(keyConfig['F10'])
                playMusic()
        elif e.key() == Qt.Key.Key_F11:
            if 'F11' in keyConfig:
                newList(keyConfig['F11'])
                playMusic()
        elif e.key() == Qt.Key.Key_F12:
            if 'F12' in keyConfig:
                newList(keyConfig['F12'])
                playMusic()
        elif e.key() == Qt.Key.Key_F13:
            if 'F13' in keyConfig:
                newList(keyConfig['F13'])
                playMusic()
        elif e.key() == Qt.Key.Key_F14:
            if 'F14' in keyConfig:
                newList(keyConfig['F14'])
                playMusic()
        elif e.key() == Qt.Key.Key_F15:
            if 'F15' in keyConfig:
                newList(keyConfig['F15'])
                playMusic()
        elif e.key() == Qt.Key.Key_F16:
            if 'F16' in keyConfig:
                newList(keyConfig['F16'])
                playMusic()
        elif e.key() == Qt.Key.Key_F17:
            if 'F17' in keyConfig:
                newList(keyConfig['F17'])
                playMusic()
        elif e.key() == Qt.Key.Key_F18:
            if 'F18' in keyConfig:
                newList(keyConfig['F18'])
                playMusic()
        elif e.key() == Qt.Key.Key_F19:
            if 'F19' in keyConfig:
                newList(keyConfig['F19'])
                playMusic()
        elif e.key() == Qt.Key.Key_F20:
            if 'F20' in keyConfig:
                newList(keyConfig['F20'])
                playMusic()
        elif e.key() == Qt.Key.Key_F21:
            if 'F21' in keyConfig:
                newList(keyConfig['F21'])
                playMusic()
        elif e.key() == Qt.Key.Key_F22:
            if 'F22' in keyConfig:
                newList(keyConfig['F22'])
                playMusic()
        elif e.key() == Qt.Key.Key_F23:
            if 'F23' in keyConfig:
                newList(keyConfig['F23'])
                playMusic()
        elif e.key() == Qt.Key.Key_F24:
            if 'F24' in keyConfig:
                newList(keyConfig['F24'])
                playMusic()
        elif e.key() == Qt.Key.Key_F25:
            if 'F25' in keyConfig:
                newList(keyConfig['F25'])
                playMusic()
        elif e.key() == Qt.Key.Key_F26:
            if 'F26' in keyConfig:
                newList(keyConfig['F26'])
                playMusic()
        elif e.key() == Qt.Key.Key_F27:
            if 'F27' in keyConfig:
                newList(keyConfig['F27'])
                playMusic()
        elif e.key() == Qt.Key.Key_F28:
            if 'F28' in keyConfig:
                newList(keyConfig['F28'])
                playMusic()
        elif e.key() == Qt.Key.Key_F29:
            if 'F29' in keyConfig:
                newList(keyConfig['F29'])
                playMusic()
        elif e.key() == Qt.Key.Key_F30:
            if 'F30' in keyConfig:
                newList(keyConfig['F30'])
                playMusic()
        elif e.key() == Qt.Key.Key_F31:
            if 'F31' in keyConfig:
                newList(keyConfig['F31'])
                playMusic()
        elif e.key() == Qt.Key.Key_F32:
            if 'F32' in keyConfig:
                newList(keyConfig['F32'])
                playMusic()
        elif e.key() == Qt.Key.Key_F33:
            if 'F33' in keyConfig:
                newList(keyConfig['F33'])
                playMusic()
        elif e.key() == Qt.Key.Key_F34:
            if 'F34' in keyConfig:
                newList(keyConfig['F34'])
                playMusic()
        elif e.key() == Qt.Key.Key_F35:
            if 'F35' in keyConfig:
                newList(keyConfig['F35'])
                playMusic()
        elif e.key() == Qt.Key.Key_Super_L:
            if 'Super_L' in keyConfig:
                newList(keyConfig['Super_L'])
                playMusic()
        elif e.key() == Qt.Key.Key_Super_R:
            if 'Super_R' in keyConfig:
                newList(keyConfig['Super_R'])
                playMusic()
        elif e.key() == Qt.Key.Key_Menu:
            if 'Menu' in keyConfig:
                newList(keyConfig['Menu'])
                playMusic()
        elif e.key() == Qt.Key.Key_Hyper_L:
            if 'Hyper_L' in keyConfig:
                newList(keyConfig['Hyper_L'])
                playMusic()
        elif e.key() == Qt.Key.Key_Hyper_R:
            if 'Hyper_R' in keyConfig:
                newList(keyConfig['Hyper_R'])
                playMusic()
        elif e.key() == Qt.Key.Key_Help:
            if 'Help' in keyConfig:
                newList(keyConfig['Help'])
                playMusic()
        elif e.key() == Qt.Key.Key_Direction_L:
            if 'Direction_L' in keyConfig:
                newList(keyConfig['Direction_L'])
                playMusic()
        elif e.key() == Qt.Key.Key_Direction_R:
            if 'Direction_R' in keyConfig:
                newList(keyConfig['Direction_R'])
                playMusic()
        elif e.key() == Qt.Key.Key_Space:
            if 'Space' in keyConfig:
                newList(keyConfig['Space'])
                playMusic()
        elif e.key() == Qt.Key.Key_Any:
            if 'Any' in keyConfig:
                newList(keyConfig['Any'])
                playMusic()
        elif e.key() == Qt.Key.Key_Exclam:
            if 'Exclam' in keyConfig:
                newList(keyConfig['Exclam'])
                playMusic()
        elif e.key() == Qt.Key.Key_QuoteDbl:
            if 'QuoteDbl' in keyConfig:
                newList(keyConfig['QuoteDbl'])
                playMusic()
        elif e.key() == Qt.Key.Key_NumberSign:
            if 'NumberSign' in keyConfig:
                newList(keyConfig['NumberSign'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dollar:
            if 'Dollar' in keyConfig:
                newList(keyConfig['Dollar'])
                playMusic()
        elif e.key() == Qt.Key.Key_Percent:
            if 'Percent' in keyConfig:
                newList(keyConfig['Percent'])
                playMusic()
        elif e.key() == Qt.Key.Key_Ampersand:
            if 'Ampersand' in keyConfig:
                newList(keyConfig['Ampersand'])
                playMusic()
        elif e.key() == Qt.Key.Key_Apostrophe:
            if 'Apostrophe' in keyConfig:
                newList(keyConfig['Apostrophe'])
                playMusic()
        elif e.key() == Qt.Key.Key_ParenLeft:
            if 'ParenLeft' in keyConfig:
                newList(keyConfig['ParenLeft'])
                playMusic()
        elif e.key() == Qt.Key.Key_ParenRight:
            if 'ParenRight' in keyConfig:
                newList(keyConfig['ParenRight'])
                playMusic()
        elif e.key() == Qt.Key.Key_Asterisk:
            if 'Asterisk' in keyConfig:
                newList(keyConfig['Asterisk'])
                playMusic()
        elif e.key() == Qt.Key.Key_Plus:
            if 'Plus' in keyConfig:
                newList(keyConfig['Plus'])
                playMusic()
        elif e.key() == Qt.Key.Key_Comma:
            if 'Comma' in keyConfig:
                newList(keyConfig['Comma'])
                playMusic()
        elif e.key() == Qt.Key.Key_Minus:
            if 'Minus' in keyConfig:
                newList(keyConfig['Minus'])
                playMusic()
        elif e.key() == Qt.Key.Key_Period:
            if 'Period' in keyConfig:
                newList(keyConfig['Period'])
                playMusic()
        elif e.key() == Qt.Key.Key_Slash:
            if 'Slash' in keyConfig:
                newList(keyConfig['Slash'])
                playMusic()
        elif e.key() == Qt.Key.Key_0:
            if '0' in keyConfig:
                newList(keyConfig['0'])
                playMusic()
        elif e.key() == Qt.Key.Key_1:
            if '1' in keyConfig:
                newList(keyConfig['1'])
                playMusic()
        elif e.key() == Qt.Key.Key_2:
            if '2' in keyConfig:
                newList(keyConfig['2'])
                playMusic()
        elif e.key() == Qt.Key.Key_3:
            if '3' in keyConfig:
                newList(keyConfig['3'])
                playMusic()
        elif e.key() == Qt.Key.Key_4:
            if '4' in keyConfig:
                newList(keyConfig['4'])
                playMusic()
        elif e.key() == Qt.Key.Key_5:
            if '5' in keyConfig:
                newList(keyConfig['5'])
                playMusic()
        elif e.key() == Qt.Key.Key_6:
            if '6' in keyConfig:
                newList(keyConfig['6'])
                playMusic()
        elif e.key() == Qt.Key.Key_7:
            if '7' in keyConfig:
                newList(keyConfig['7'])
                playMusic()
        elif e.key() == Qt.Key.Key_8:
            if '8' in keyConfig:
                newList(keyConfig['8'])
                playMusic()
        elif e.key() == Qt.Key.Key_9:
            if '9' in keyConfig:
                newList(keyConfig['9'])
                playMusic()
        elif e.key() == Qt.Key.Key_Colon:
            if 'Colon' in keyConfig:
                newList(keyConfig['Colon'])
                playMusic()
        elif e.key() == Qt.Key.Key_Semicolon:
            if 'Semicolon' in keyConfig:
                newList(keyConfig['Semicolon'])
                playMusic()
        elif e.key() == Qt.Key.Key_Less:
            if 'Less' in keyConfig:
                newList(keyConfig['Less'])
                playMusic()
        elif e.key() == Qt.Key.Key_Equal:
            if 'Equal' in keyConfig:
                newList(keyConfig['Equal'])
                playMusic()
        elif e.key() == Qt.Key.Key_Greater:
            if 'Greater' in keyConfig:
                newList(keyConfig['Greater'])
                playMusic()
        elif e.key() == Qt.Key.Key_Question:
            if 'Question' in keyConfig:
                newList(keyConfig['Question'])
                playMusic()
        elif e.key() == Qt.Key.Key_At:
            if 'At' in keyConfig:
                newList(keyConfig['At'])
                playMusic()
        elif e.key() == Qt.Key.Key_A:
            if 'A' in keyConfig:
                newList(keyConfig['A'])
                playMusic()
        elif e.key() == Qt.Key.Key_B:
            if 'B' in keyConfig:
                newList(keyConfig['B'])
                playMusic()
        elif e.key() == Qt.Key.Key_C:
            if 'C' in keyConfig:
                newList(keyConfig['C'])
                playMusic()
        elif e.key() == Qt.Key.Key_D:
            if 'D' in keyConfig:
                newList(keyConfig['D'])
                playMusic()
        elif e.key() == Qt.Key.Key_E:
            if 'E' in keyConfig:
                newList(keyConfig['E'])
                playMusic()
        elif e.key() == Qt.Key.Key_F:
            if 'F' in keyConfig:
                newList(keyConfig['F'])
                playMusic()
        elif e.key() == Qt.Key.Key_G:
            if 'G' in keyConfig:
                newList(keyConfig['G'])
                playMusic()
        elif e.key() == Qt.Key.Key_H:
            if 'H' in keyConfig:
                newList(keyConfig['H'])
                playMusic()
        elif e.key() == Qt.Key.Key_I:
            if 'I' in keyConfig:
                newList(keyConfig['I'])
                playMusic()
        elif e.key() == Qt.Key.Key_J:
            if 'J' in keyConfig:
                newList(keyConfig['J'])
                playMusic()
        elif e.key() == Qt.Key.Key_K:
            if 'K' in keyConfig:
                newList(keyConfig['K'])
                playMusic()
        elif e.key() == Qt.Key.Key_L:
            if 'L' in keyConfig:
                newList(keyConfig['L'])
                playMusic()
        elif e.key() == Qt.Key.Key_M:
            if 'M' in keyConfig:
                newList(keyConfig['M'])
                playMusic()
        elif e.key() == Qt.Key.Key_N:
            if 'N' in keyConfig:
                newList(keyConfig['N'])
                playMusic()
        elif e.key() == Qt.Key.Key_O:
            if 'O' in keyConfig:
                newList(keyConfig['O'])
                playMusic()
        elif e.key() == Qt.Key.Key_P:
            if 'P' in keyConfig:
                newList(keyConfig['P'])
                playMusic()
        elif e.key() == Qt.Key.Key_Q:
            if 'Q' in keyConfig:
                newList(keyConfig['Q'])
                playMusic()
        elif e.key() == Qt.Key.Key_R:
            if 'R' in keyConfig:
                newList(keyConfig['R'])
                playMusic()
        elif e.key() == Qt.Key.Key_S:
            if 'S' in keyConfig:
                newList(keyConfig['S'])
                playMusic()
        elif e.key() == Qt.Key.Key_T:
            if 'T' in keyConfig:
                newList(keyConfig['T'])
                playMusic()
        elif e.key() == Qt.Key.Key_U:
            if 'U' in keyConfig:
                newList(keyConfig['U'])
                playMusic()
        elif e.key() == Qt.Key.Key_V:
            if 'V' in keyConfig:
                newList(keyConfig['V'])
                playMusic()
        elif e.key() == Qt.Key.Key_W:
            if 'W' in keyConfig:
                newList(keyConfig['W'])
                playMusic()
        elif e.key() == Qt.Key.Key_X:
            if 'X' in keyConfig:
                newList(keyConfig['X'])
                playMusic()
        elif e.key() == Qt.Key.Key_Y:
            if 'Y' in keyConfig:
                newList(keyConfig['Y'])
                playMusic()
        elif e.key() == Qt.Key.Key_Z:
            if 'Z' in keyConfig:
                newList(keyConfig['Z'])
                playMusic()
        elif e.key() == Qt.Key.Key_BracketLeft:
            if 'BracketLeft' in keyConfig:
                newList(keyConfig['BracketLeft'])
                playMusic()
        elif e.key() == Qt.Key.Key_Backslash:
            if 'Backslash' in keyConfig:
                newList(keyConfig['Backslash'])
                playMusic()
        elif e.key() == Qt.Key.Key_BracketRight:
            if 'BracketRight' in keyConfig:
                newList(keyConfig['BracketRight'])
                playMusic()
        elif e.key() == Qt.Key.Key_AsciiCircum:
            if 'AsciiCircum' in keyConfig:
                newList(keyConfig['AsciiCircum'])
                playMusic()
        elif e.key() == Qt.Key.Key_Underscore:
            if 'Underscore' in keyConfig:
                newList(keyConfig['Underscore'])
                playMusic()
        elif e.key() == Qt.Key.Key_QuoteLeft:
            if 'QuoteLeft' in keyConfig:
                newList(keyConfig['QuoteLeft'])
                playMusic()
        elif e.key() == Qt.Key.Key_BraceLeft:
            if 'BraceLeft' in keyConfig:
                newList(keyConfig['BraceLeft'])
                playMusic()
        elif e.key() == Qt.Key.Key_Bar:
            if 'Bar' in keyConfig:
                newList(keyConfig['Bar'])
                playMusic()
        elif e.key() == Qt.Key.Key_BraceRight:
            if 'BraceRight' in keyConfig:
                newList(keyConfig['BraceRight'])
                playMusic()
        elif e.key() == Qt.Key.Key_AsciiTilde:
            if 'AsciiTilde' in keyConfig:
                newList(keyConfig['AsciiTilde'])
                playMusic()
        elif e.key() == Qt.Key.Key_nobreakspace:
            if 'nobreakspace' in keyConfig:
                newList(keyConfig['nobreakspace'])
                playMusic()
        elif e.key() == Qt.Key.Key_exclamdown:
            if 'exclamdown' in keyConfig:
                newList(keyConfig['exclamdown'])
                playMusic()
        elif e.key() == Qt.Key.Key_cent:
            if 'cent' in keyConfig:
                newList(keyConfig['cent'])
                playMusic()
        elif e.key() == Qt.Key.Key_sterling:
            if 'sterling' in keyConfig:
                newList(keyConfig['sterling'])
                playMusic()
        elif e.key() == Qt.Key.Key_currency:
            if 'currency' in keyConfig:
                newList(keyConfig['currency'])
                playMusic()
        elif e.key() == Qt.Key.Key_yen:
            if 'yen' in keyConfig:
                newList(keyConfig['yen'])
                playMusic()
        elif e.key() == Qt.Key.Key_brokenbar:
            if 'brokenbar' in keyConfig:
                newList(keyConfig['brokenbar'])
                playMusic()
        elif e.key() == Qt.Key.Key_section:
            if 'section' in keyConfig:
                newList(keyConfig['section'])
                playMusic()
        elif e.key() == Qt.Key.Key_diaeresis:
            if 'diaeresis' in keyConfig:
                newList(keyConfig['diaeresis'])
                playMusic()
        elif e.key() == Qt.Key.Key_copyright:
            if 'copyright' in keyConfig:
                newList(keyConfig['copyright'])
                playMusic()
        elif e.key() == Qt.Key.Key_ordfeminine:
            if 'ordfeminine' in keyConfig:
                newList(keyConfig['ordfeminine'])
                playMusic()
        elif e.key() == Qt.Key.Key_guillemotleft:
            if 'guillemotleft' in keyConfig:
                newList(keyConfig['guillemotleft'])
                playMusic()
        elif e.key() == Qt.Key.Key_notsign:
            if 'notsign' in keyConfig:
                newList(keyConfig['notsign'])
                playMusic()
        elif e.key() == Qt.Key.Key_hyphen:
            if 'hyphen' in keyConfig:
                newList(keyConfig['hyphen'])
                playMusic()
        elif e.key() == Qt.Key.Key_registered:
            if 'registered' in keyConfig:
                newList(keyConfig['registered'])
                playMusic()
        elif e.key() == Qt.Key.Key_macron:
            if 'macron' in keyConfig:
                newList(keyConfig['macron'])
                playMusic()
        elif e.key() == Qt.Key.Key_degree:
            if 'degree' in keyConfig:
                newList(keyConfig['degree'])
                playMusic()
        elif e.key() == Qt.Key.Key_plusminus:
            if 'plusminus' in keyConfig:
                newList(keyConfig['plusminus'])
                playMusic()
        elif e.key() == Qt.Key.Key_twosuperior:
            if 'twosuperior' in keyConfig:
                newList(keyConfig['twosuperior'])
                playMusic()
        elif e.key() == Qt.Key.Key_threesuperior:
            if 'threesuperior' in keyConfig:
                newList(keyConfig['threesuperior'])
                playMusic()
        elif e.key() == Qt.Key.Key_acute:
            if 'acute' in keyConfig:
                newList(keyConfig['acute'])
                playMusic()
        elif e.key() == Qt.Key.Key_mu:
            if 'mu' in keyConfig:
                newList(keyConfig['mu'])
                playMusic()
        elif e.key() == Qt.Key.Key_paragraph:
            if 'paragraph' in keyConfig:
                newList(keyConfig['paragraph'])
                playMusic()
        elif e.key() == Qt.Key.Key_periodcentered:
            if 'periodcentered' in keyConfig:
                newList(keyConfig['periodcentered'])
                playMusic()
        elif e.key() == Qt.Key.Key_cedilla:
            if 'cedilla' in keyConfig:
                newList(keyConfig['cedilla'])
                playMusic()
        elif e.key() == Qt.Key.Key_onesuperior:
            if 'onesuperior' in keyConfig:
                newList(keyConfig['onesuperior'])
                playMusic()
        elif e.key() == Qt.Key.Key_masculine:
            if 'masculine' in keyConfig:
                newList(keyConfig['masculine'])
                playMusic()
        elif e.key() == Qt.Key.Key_guillemotright:
            if 'guillemotright' in keyConfig:
                newList(keyConfig['guillemotright'])
                playMusic()
        elif e.key() == Qt.Key.Key_onequarter:
            if 'onequarter' in keyConfig:
                newList(keyConfig['onequarter'])
                playMusic()
        elif e.key() == Qt.Key.Key_onehalf:
            if 'onehalf' in keyConfig:
                newList(keyConfig['onehalf'])
                playMusic()
        elif e.key() == Qt.Key.Key_threequarters:
            if 'threequarters' in keyConfig:
                newList(keyConfig['threequarters'])
                playMusic()
        elif e.key() == Qt.Key.Key_questiondown:
            if 'questiondown' in keyConfig:
                newList(keyConfig['questiondown'])
                playMusic()
        elif e.key() == Qt.Key.Key_Agrave:
            if 'Agrave' in keyConfig:
                newList(keyConfig['Agrave'])
                playMusic()
        elif e.key() == Qt.Key.Key_Aacute:
            if 'Aacute' in keyConfig:
                newList(keyConfig['Aacute'])
                playMusic()
        elif e.key() == Qt.Key.Key_Acircumflex:
            if 'Acircumflex' in keyConfig:
                newList(keyConfig['Acircumflex'])
                playMusic()
        elif e.key() == Qt.Key.Key_Atilde:
            if 'Atilde' in keyConfig:
                newList(keyConfig['Atilde'])
                playMusic()
        elif e.key() == Qt.Key.Key_Adiaeresis:
            if 'Adiaeresis' in keyConfig:
                newList(keyConfig['Adiaeresis'])
                playMusic()
        elif e.key() == Qt.Key.Key_Aring:
            if 'Aring' in keyConfig:
                newList(keyConfig['Aring'])
                playMusic()
        elif e.key() == Qt.Key.Key_AE:
            if 'AE' in keyConfig:
                newList(keyConfig['AE'])
                playMusic()
        elif e.key() == Qt.Key.Key_Ccedilla:
            if 'Ccedilla' in keyConfig:
                newList(keyConfig['Ccedilla'])
                playMusic()
        elif e.key() == Qt.Key.Key_Egrave:
            if 'Egrave' in keyConfig:
                newList(keyConfig['Egrave'])
                playMusic()
        elif e.key() == Qt.Key.Key_Eacute:
            if 'Eacute' in keyConfig:
                newList(keyConfig['Eacute'])
                playMusic()
        elif e.key() == Qt.Key.Key_Ecircumflex:
            if 'Ecircumflex' in keyConfig:
                newList(keyConfig['Ecircumflex'])
                playMusic()
        elif e.key() == Qt.Key.Key_Ediaeresis:
            if 'Ediaeresis' in keyConfig:
                newList(keyConfig['Ediaeresis'])
                playMusic()
        elif e.key() == Qt.Key.Key_Igrave:
            if 'Igrave' in keyConfig:
                newList(keyConfig['Igrave'])
                playMusic()
        elif e.key() == Qt.Key.Key_Iacute:
            if 'Iacute' in keyConfig:
                newList(keyConfig['Iacute'])
                playMusic()
        elif e.key() == Qt.Key.Key_Icircumflex:
            if 'Icircumflex' in keyConfig:
                newList(keyConfig['Icircumflex'])
                playMusic()
        elif e.key() == Qt.Key.Key_Idiaeresis:
            if 'Idiaeresis' in keyConfig:
                newList(keyConfig['Idiaeresis'])
                playMusic()
        elif e.key() == Qt.Key.Key_ETH:
            if 'ETH' in keyConfig:
                newList(keyConfig['ETH'])
                playMusic()
        elif e.key() == Qt.Key.Key_Ntilde:
            if 'Ntilde' in keyConfig:
                newList(keyConfig['Ntilde'])
                playMusic()
        elif e.key() == Qt.Key.Key_Ograve:
            if 'Ograve' in keyConfig:
                newList(keyConfig['Ograve'])
                playMusic()
        elif e.key() == Qt.Key.Key_Oacute:
            if 'Oacute' in keyConfig:
                newList(keyConfig['Oacute'])
                playMusic()
        elif e.key() == Qt.Key.Key_Ocircumflex:
            if 'Ocircumflex' in keyConfig:
                newList(keyConfig['Ocircumflex'])
                playMusic()
        elif e.key() == Qt.Key.Key_Otilde:
            if 'Otilde' in keyConfig:
                newList(keyConfig['Otilde'])
                playMusic()
        elif e.key() == Qt.Key.Key_Odiaeresis:
            if 'Odiaeresis' in keyConfig:
                newList(keyConfig['Odiaeresis'])
                playMusic()
        elif e.key() == Qt.Key.Key_multiply:
            if 'multiply' in keyConfig:
                newList(keyConfig['multiply'])
                playMusic()
        elif e.key() == Qt.Key.Key_Ooblique:
            if 'Ooblique' in keyConfig:
                newList(keyConfig['Ooblique'])
                playMusic()
        elif e.key() == Qt.Key.Key_Ugrave:
            if 'Ugrave' in keyConfig:
                newList(keyConfig['Ugrave'])
                playMusic()
        elif e.key() == Qt.Key.Key_Uacute:
            if 'Uacute' in keyConfig:
                newList(keyConfig['Uacute'])
                playMusic()
        elif e.key() == Qt.Key.Key_Ucircumflex:
            if 'Ucircumflex' in keyConfig:
                newList(keyConfig['Ucircumflex'])
                playMusic()
        elif e.key() == Qt.Key.Key_Udiaeresis:
            if 'Udiaeresis' in keyConfig:
                newList(keyConfig['Udiaeresis'])
                playMusic()
        elif e.key() == Qt.Key.Key_Yacute:
            if 'Yacute' in keyConfig:
                newList(keyConfig['Yacute'])
                playMusic()
        elif e.key() == Qt.Key.Key_THORN:
            if 'THORN' in keyConfig:
                newList(keyConfig['THORN'])
                playMusic()
        elif e.key() == Qt.Key.Key_ssharp:
            if 'ssharp' in keyConfig:
                newList(keyConfig['ssharp'])
                playMusic()
        elif e.key() == Qt.Key.Key_division:
            if 'division' in keyConfig:
                newList(keyConfig['division'])
                playMusic()
        elif e.key() == Qt.Key.Key_ydiaeresis:
            if 'ydiaeresis' in keyConfig:
                newList(keyConfig['ydiaeresis'])
                playMusic()
        elif e.key() == Qt.Key.Key_Multi_key:
            if 'Multi_key' in keyConfig:
                newList(keyConfig['Multi_key'])
                playMusic()
        elif e.key() == Qt.Key.Key_Codeinput:
            if 'Codeinput' in keyConfig:
                newList(keyConfig['Codeinput'])
                playMusic()
        elif e.key() == Qt.Key.Key_SingleCandidate:
            if 'SingleCandidate' in keyConfig:
                newList(keyConfig['SingleCandidate'])
                playMusic()
        elif e.key() == Qt.Key.Key_MultipleCandidate:
            if 'MultipleCandidate' in keyConfig:
                newList(keyConfig['MultipleCandidate'])
                playMusic()
        elif e.key() == Qt.Key.Key_PreviousCandidate:
            if 'PreviousCandidate' in keyConfig:
                newList(keyConfig['PreviousCandidate'])
                playMusic()
        elif e.key() == Qt.Key.Key_Mode_switch:
            if 'Mode_switch' in keyConfig:
                newList(keyConfig['Mode_switch'])
                playMusic()
        elif e.key() == Qt.Key.Key_Kanji:
            if 'Kanji' in keyConfig:
                newList(keyConfig['Kanji'])
                playMusic()
        elif e.key() == Qt.Key.Key_Muhenkan:
            if 'Muhenkan' in keyConfig:
                newList(keyConfig['Muhenkan'])
                playMusic()
        elif e.key() == Qt.Key.Key_Henkan:
            if 'Henkan' in keyConfig:
                newList(keyConfig['Henkan'])
                playMusic()
        elif e.key() == Qt.Key.Key_Romaji:
            if 'Romaji' in keyConfig:
                newList(keyConfig['Romaji'])
                playMusic()
        elif e.key() == Qt.Key.Key_Hiragana:
            if 'Hiragana' in keyConfig:
                newList(keyConfig['Hiragana'])
                playMusic()
        elif e.key() == Qt.Key.Key_Katakana:
            if 'Katakana' in keyConfig:
                newList(keyConfig['Katakana'])
                playMusic()
        elif e.key() == Qt.Key.Key_Hiragana_Katakana:
            if 'Hiragana_Katakana' in keyConfig:
                newList(keyConfig['Hiragana_Katakana'])
                playMusic()
        elif e.key() == Qt.Key.Key_Zenkaku:
            if 'Zenkaku' in keyConfig:
                newList(keyConfig['Zenkaku'])
                playMusic()
        elif e.key() == Qt.Key.Key_Hankaku:
            if 'Hankaku' in keyConfig:
                newList(keyConfig['Hankaku'])
                playMusic()
        elif e.key() == Qt.Key.Key_Zenkaku_Hankaku:
            if 'Zenkaku_Hankaku' in keyConfig:
                newList(keyConfig['Zenkaku_Hankaku'])
                playMusic()
        elif e.key() == Qt.Key.Key_Touroku:
            if 'Touroku' in keyConfig:
                newList(keyConfig['Touroku'])
                playMusic()
        elif e.key() == Qt.Key.Key_Massyo:
            if 'Massyo' in keyConfig:
                newList(keyConfig['Massyo'])
                playMusic()
        elif e.key() == Qt.Key.Key_Kana_Lock:
            if 'Kana_Lock' in keyConfig:
                newList(keyConfig['Kana_Lock'])
                playMusic()
        elif e.key() == Qt.Key.Key_Kana_Shift:
            if 'Kana_Shift' in keyConfig:
                newList(keyConfig['Kana_Shift'])
                playMusic()
        elif e.key() == Qt.Key.Key_Eisu_Shift:
            if 'Eisu_Shift' in keyConfig:
                newList(keyConfig['Eisu_Shift'])
                playMusic()
        elif e.key() == Qt.Key.Key_Eisu_toggle:
            if 'Eisu_toggle' in keyConfig:
                newList(keyConfig['Eisu_toggle'])
                playMusic()
        elif e.key() == Qt.Key.Key_Hangul:
            if 'Hangul' in keyConfig:
                newList(keyConfig['Hangul'])
                playMusic()
        elif e.key() == Qt.Key.Key_Hangul_Start:
            if 'Hangul_Start' in keyConfig:
                newList(keyConfig['Hangul_Start'])
                playMusic()
        elif e.key() == Qt.Key.Key_Hangul_End:
            if 'Hangul_End' in keyConfig:
                newList(keyConfig['Hangul_End'])
                playMusic()
        elif e.key() == Qt.Key.Key_Hangul_Hanja:
            if 'Hangul_Hanja' in keyConfig:
                newList(keyConfig['Hangul_Hanja'])
                playMusic()
        elif e.key() == Qt.Key.Key_Hangul_Jamo:
            if 'Hangul_Jamo' in keyConfig:
                newList(keyConfig['Hangul_Jamo'])
                playMusic()
        elif e.key() == Qt.Key.Key_Hangul_Romaja:
            if 'Hangul_Romaja' in keyConfig:
                newList(keyConfig['Hangul_Romaja'])
                playMusic()
        elif e.key() == Qt.Key.Key_Hangul_Jeonja:
            if 'Hangul_Jeonja' in keyConfig:
                newList(keyConfig['Hangul_Jeonja'])
                playMusic()
        elif e.key() == Qt.Key.Key_Hangul_Banja:
            if 'Hangul_Banja' in keyConfig:
                newList(keyConfig['Hangul_Banja'])
                playMusic()
        elif e.key() == Qt.Key.Key_Hangul_PreHanja:
            if 'Hangul_PreHanja' in keyConfig:
                newList(keyConfig['Hangul_PreHanja'])
                playMusic()
        elif e.key() == Qt.Key.Key_Hangul_PostHanja:
            if 'Hangul_PostHanja' in keyConfig:
                newList(keyConfig['Hangul_PostHanja'])
                playMusic()
        elif e.key() == Qt.Key.Key_Hangul_Special:
            if 'Hangul_Special' in keyConfig:
                newList(keyConfig['Hangul_Special'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Grave:
            if 'Dead_Grave' in keyConfig:
                newList(keyConfig['Dead_Grave'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Acute:
            if 'Dead_Acute' in keyConfig:
                newList(keyConfig['Dead_Acute'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Circumflex:
            if 'Dead_Circumflex' in keyConfig:
                newList(keyConfig['Dead_Circumflex'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Tilde:
            if 'Dead_Tilde' in keyConfig:
                newList(keyConfig['Dead_Tilde'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Macron:
            if 'Dead_Macron' in keyConfig:
                newList(keyConfig['Dead_Macron'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Breve:
            if 'Dead_Breve' in keyConfig:
                newList(keyConfig['Dead_Breve'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Abovedot:
            if 'Dead_Abovedot' in keyConfig:
                newList(keyConfig['Dead_Abovedot'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Diaeresis:
            if 'Dead_Diaeresis' in keyConfig:
                newList(keyConfig['Dead_Diaeresis'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Abovering:
            if 'Dead_Abovering' in keyConfig:
                newList(keyConfig['Dead_Abovering'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Doubleacute:
            if 'Dead_Doubleacute' in keyConfig:
                newList(keyConfig['Dead_Doubleacute'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Caron:
            if 'Dead_Caron' in keyConfig:
                newList(keyConfig['Dead_Caron'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Cedilla:
            if 'Dead_Cedilla' in keyConfig:
                newList(keyConfig['Dead_Cedilla'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Ogonek:
            if 'Dead_Ogonek' in keyConfig:
                newList(keyConfig['Dead_Ogonek'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Iota:
            if 'Dead_Iota' in keyConfig:
                newList(keyConfig['Dead_Iota'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Voiced_Sound:
            if 'Dead_Voiced_Sound' in keyConfig:
                newList(keyConfig['Dead_Voiced_Sound'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Semivoiced_Sound:
            if 'Dead_Semivoiced_Sound' in keyConfig:
                newList(keyConfig['Dead_Semivoiced_Sound'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Belowdot:
            if 'Dead_Belowdot' in keyConfig:
                newList(keyConfig['Dead_Belowdot'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Hook:
            if 'Dead_Hook' in keyConfig:
                newList(keyConfig['Dead_Hook'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Horn:
            if 'Dead_Horn' in keyConfig:
                newList(keyConfig['Dead_Horn'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Stroke:
            if 'Dead_Stroke' in keyConfig:
                newList(keyConfig['Dead_Stroke'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Abovecomma:
            if 'Dead_Abovecomma' in keyConfig:
                newList(keyConfig['Dead_Abovecomma'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Abovereversedcomma:
            if 'Dead_Abovereversedcomma' in keyConfig:
                newList(keyConfig['Dead_Abovereversedcomma'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Doublegrave:
            if 'Dead_Doublegrave' in keyConfig:
                newList(keyConfig['Dead_Doublegrave'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Belowring:
            if 'Dead_Belowring' in keyConfig:
                newList(keyConfig['Dead_Belowring'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Belowmacron:
            if 'Dead_Belowmacron' in keyConfig:
                newList(keyConfig['Dead_Belowmacron'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Belowcircumflex:
            if 'Dead_Belowcircumflex' in keyConfig:
                newList(keyConfig['Dead_Belowcircumflex'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Belowtilde:
            if 'Dead_Belowtilde' in keyConfig:
                newList(keyConfig['Dead_Belowtilde'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Belowbreve:
            if 'Dead_Belowbreve' in keyConfig:
                newList(keyConfig['Dead_Belowbreve'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Belowdiaeresis:
            if 'Dead_Belowdiaeresis' in keyConfig:
                newList(keyConfig['Dead_Belowdiaeresis'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Invertedbreve:
            if 'Dead_Invertedbreve' in keyConfig:
                newList(keyConfig['Dead_Invertedbreve'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Belowcomma:
            if 'Dead_Belowcomma' in keyConfig:
                newList(keyConfig['Dead_Belowcomma'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Currency:
            if 'Dead_Currency' in keyConfig:
                newList(keyConfig['Dead_Currency'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_a:
            if 'Dead_a' in keyConfig:
                newList(keyConfig['Dead_a'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_A:
            if 'Dead_A' in keyConfig:
                newList(keyConfig['Dead_A'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_e:
            if 'Dead_e' in keyConfig:
                newList(keyConfig['Dead_e'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_E:
            if 'Dead_E' in keyConfig:
                newList(keyConfig['Dead_E'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_i:
            if 'Dead_i' in keyConfig:
                newList(keyConfig['Dead_i'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_I:
            if 'Dead_I' in keyConfig:
                newList(keyConfig['Dead_I'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_o:
            if 'Dead_o' in keyConfig:
                newList(keyConfig['Dead_o'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_O:
            if 'Dead_O' in keyConfig:
                newList(keyConfig['Dead_O'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_u:
            if 'Dead_u' in keyConfig:
                newList(keyConfig['Dead_u'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_U:
            if 'Dead_U' in keyConfig:
                newList(keyConfig['Dead_U'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Small_Schwa:
            if 'Dead_Small_Schwa' in keyConfig:
                newList(keyConfig['Dead_Small_Schwa'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Capital_Schwa:
            if 'Dead_Capital_Schwa' in keyConfig:
                newList(keyConfig['Dead_Capital_Schwa'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Greek:
            if 'Dead_Greek' in keyConfig:
                newList(keyConfig['Dead_Greek'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Lowline:
            if 'Dead_Lowline' in keyConfig:
                newList(keyConfig['Dead_Lowline'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Aboveverticalline:
            if 'Dead_Aboveverticalline' in keyConfig:
                newList(keyConfig['Dead_Aboveverticalline'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Belowverticalline:
            if 'Dead_Belowverticalline' in keyConfig:
                newList(keyConfig['Dead_Belowverticalline'])
                playMusic()
        elif e.key() == Qt.Key.Key_Dead_Longsolidusoverlay:
            if 'Dead_Longsolidusoverlay' in keyConfig:
                newList(keyConfig['Dead_Longsolidusoverlay'])
                playMusic()
        elif e.key() == Qt.Key.Key_Back:
            if 'Back' in keyConfig:
                newList(keyConfig['Back'])
                playMusic()
        elif e.key() == Qt.Key.Key_Forward:
            if 'Forward' in keyConfig:
                newList(keyConfig['Forward'])
                playMusic()
        elif e.key() == Qt.Key.Key_Stop:
            if 'Stop' in keyConfig:
                newList(keyConfig['Stop'])
                playMusic()
        elif e.key() == Qt.Key.Key_Refresh:
            if 'Refresh' in keyConfig:
                newList(keyConfig['Refresh'])
                playMusic()
        elif e.key() == Qt.Key.Key_VolumeDown:
            if 'VolumeDown' in keyConfig:
                newList(keyConfig['VolumeDown'])
                playMusic()
        elif e.key() == Qt.Key.Key_VolumeMute:
            if 'VolumeMute' in keyConfig:
                newList(keyConfig['VolumeMute'])
                playMusic()
        elif e.key() == Qt.Key.Key_VolumeUp:
            if 'VolumeUp' in keyConfig:
                newList(keyConfig['VolumeUp'])
                playMusic()
        elif e.key() == Qt.Key.Key_BassBoost:
            if 'BassBoost' in keyConfig:
                newList(keyConfig['BassBoost'])
                playMusic()
        elif e.key() == Qt.Key.Key_BassUp:
            if 'BassUp' in keyConfig:
                newList(keyConfig['BassUp'])
                playMusic()
        elif e.key() == Qt.Key.Key_BassDown:
            if 'BassDown' in keyConfig:
                newList(keyConfig['BassDown'])
                playMusic()
        elif e.key() == Qt.Key.Key_TrebleUp:
            if 'TrebleUp' in keyConfig:
                newList(keyConfig['TrebleUp'])
                playMusic()
        elif e.key() == Qt.Key.Key_TrebleDown:
            if 'TrebleDown' in keyConfig:
                newList(keyConfig['TrebleDown'])
                playMusic()
        elif e.key() == Qt.Key.Key_MediaPlay:
            if 'MediaPlay' in keyConfig:
                newList(keyConfig['MediaPlay'])
                playMusic()
        elif e.key() == Qt.Key.Key_MediaStop:
            if 'MediaStop' in keyConfig:
                newList(keyConfig['MediaStop'])
                playMusic()
        elif e.key() == Qt.Key.Key_MediaPrevious:
            if 'MediaPrevious' in keyConfig:
                newList(keyConfig['MediaPrevious'])
                playMusic()
        elif e.key() == Qt.Key.Key_MediaNext:
            if 'MediaNext' in keyConfig:
                newList(keyConfig['MediaNext'])
                playMusic()
        elif e.key() == Qt.Key.Key_MediaRecord:
            if 'MediaRecord' in keyConfig:
                newList(keyConfig['MediaRecord'])
                playMusic()
        elif e.key() == Qt.Key.Key_MediaPause:
            if 'MediaPause' in keyConfig:
                newList(keyConfig['MediaPause'])
                playMusic()
        elif e.key() == Qt.Key.Key_MediaTogglePlayPause:
            if 'MediaTogglePlayPause' in keyConfig:
                newList(keyConfig['MediaTogglePlayPause'])
                playMusic()
        elif e.key() == Qt.Key.Key_HomePage:
            if 'HomePage' in keyConfig:
                newList(keyConfig['HomePage'])
                playMusic()
        elif e.key() == Qt.Key.Key_Favorites:
            if 'Favorites' in keyConfig:
                newList(keyConfig['Favorites'])
                playMusic()
        elif e.key() == Qt.Key.Key_Search:
            if 'Search' in keyConfig:
                newList(keyConfig['Search'])
                playMusic()
        elif e.key() == Qt.Key.Key_Standby:
            if 'Standby' in keyConfig:
                newList(keyConfig['Standby'])
                playMusic()
        elif e.key() == Qt.Key.Key_OpenUrl:
            if 'OpenUrl' in keyConfig:
                newList(keyConfig['OpenUrl'])
                playMusic()
        elif e.key() == Qt.Key.Key_LaunchMail:
            if 'LaunchMail' in keyConfig:
                newList(keyConfig['LaunchMail'])
                playMusic()
        elif e.key() == Qt.Key.Key_LaunchMedia:
            if 'LaunchMedia' in keyConfig:
                newList(keyConfig['LaunchMedia'])
                playMusic()
        elif e.key() == Qt.Key.Key_Launch0:
            if 'Launch0' in keyConfig:
                newList(keyConfig['Launch0'])
                playMusic()
        elif e.key() == Qt.Key.Key_Launch1:
            if 'Launch1' in keyConfig:
                newList(keyConfig['Launch1'])
                playMusic()
        elif e.key() == Qt.Key.Key_Launch2:
            if 'Launch2' in keyConfig:
                newList(keyConfig['Launch2'])
                playMusic()
        elif e.key() == Qt.Key.Key_Launch3:
            if 'Launch3' in keyConfig:
                newList(keyConfig['Launch3'])
                playMusic()
        elif e.key() == Qt.Key.Key_Launch4:
            if 'Launch4' in keyConfig:
                newList(keyConfig['Launch4'])
                playMusic()
        elif e.key() == Qt.Key.Key_Launch5:
            if 'Launch5' in keyConfig:
                newList(keyConfig['Launch5'])
                playMusic()
        elif e.key() == Qt.Key.Key_Launch6:
            if 'Launch6' in keyConfig:
                newList(keyConfig['Launch6'])
                playMusic()
        elif e.key() == Qt.Key.Key_Launch7:
            if 'Launch7' in keyConfig:
                newList(keyConfig['Launch7'])
                playMusic()
        elif e.key() == Qt.Key.Key_Launch8:
            if 'Launch8' in keyConfig:
                newList(keyConfig['Launch8'])
                playMusic()
        elif e.key() == Qt.Key.Key_Launch9:
            if 'Launch9' in keyConfig:
                newList(keyConfig['Launch9'])
                playMusic()
        elif e.key() == Qt.Key.Key_LaunchA:
            if 'LaunchA' in keyConfig:
                newList(keyConfig['LaunchA'])
                playMusic()
        elif e.key() == Qt.Key.Key_LaunchB:
            if 'LaunchB' in keyConfig:
                newList(keyConfig['LaunchB'])
                playMusic()
        elif e.key() == Qt.Key.Key_LaunchC:
            if 'LaunchC' in keyConfig:
                newList(keyConfig['LaunchC'])
                playMusic()
        elif e.key() == Qt.Key.Key_LaunchD:
            if 'LaunchD' in keyConfig:
                newList(keyConfig['LaunchD'])
                playMusic()
        elif e.key() == Qt.Key.Key_LaunchE:
            if 'LaunchE' in keyConfig:
                newList(keyConfig['LaunchE'])
                playMusic()
        elif e.key() == Qt.Key.Key_LaunchF:
            if 'LaunchF' in keyConfig:
                newList(keyConfig['LaunchF'])
                playMusic()
        elif e.key() == Qt.Key.Key_LaunchG:
            if 'LaunchG' in keyConfig:
                newList(keyConfig['LaunchG'])
                playMusic()
        elif e.key() == Qt.Key.Key_LaunchH:
            if 'LaunchH' in keyConfig:
                newList(keyConfig['LaunchH'])
                playMusic()
        elif e.key() == Qt.Key.Key_MonBrightnessUp:
            if 'MonBrightnessUp' in keyConfig:
                newList(keyConfig['MonBrightnessUp'])
                playMusic()
        elif e.key() == Qt.Key.Key_MonBrightnessDown:
            if 'MonBrightnessDown' in keyConfig:
                newList(keyConfig['MonBrightnessDown'])
                playMusic()
        elif e.key() == Qt.Key.Key_KeyboardLightOnOff:
            if 'KeyboardLightOnOff' in keyConfig:
                newList(keyConfig['KeyboardLightOnOff'])
                playMusic()
        elif e.key() == Qt.Key.Key_KeyboardBrightnessUp:
            if 'KeyboardBrightnessUp' in keyConfig:
                newList(keyConfig['KeyboardBrightnessUp'])
                playMusic()
        elif e.key() == Qt.Key.Key_KeyboardBrightnessDown:
            if 'KeyboardBrightnessDown' in keyConfig:
                newList(keyConfig['KeyboardBrightnessDown'])
                playMusic()
        elif e.key() == Qt.Key.Key_PowerOff:
            if 'PowerOff' in keyConfig:
                newList(keyConfig['PowerOff'])
                playMusic()
        elif e.key() == Qt.Key.Key_WakeUp:
            if 'WakeUp' in keyConfig:
                newList(keyConfig['WakeUp'])
                playMusic()
        elif e.key() == Qt.Key.Key_Eject:
            if 'Eject' in keyConfig:
                newList(keyConfig['Eject'])
                playMusic()
        elif e.key() == Qt.Key.Key_ScreenSaver:
            if 'ScreenSaver' in keyConfig:
                newList(keyConfig['ScreenSaver'])
                playMusic()
        elif e.key() == Qt.Key.Key_WWW:
            if 'WWW' in keyConfig:
                newList(keyConfig['WWW'])
                playMusic()
        elif e.key() == Qt.Key.Key_Memo:
            if 'Memo' in keyConfig:
                newList(keyConfig['Memo'])
                playMusic()
        elif e.key() == Qt.Key.Key_LightBulb:
            if 'LightBulb' in keyConfig:
                newList(keyConfig['LightBulb'])
                playMusic()
        elif e.key() == Qt.Key.Key_Shop:
            if 'Shop' in keyConfig:
                newList(keyConfig['Shop'])
                playMusic()
        elif e.key() == Qt.Key.Key_History:
            if 'History' in keyConfig:
                newList(keyConfig['History'])
                playMusic()
        elif e.key() == Qt.Key.Key_AddFavorite:
            if 'AddFavorite' in keyConfig:
                newList(keyConfig['AddFavorite'])
                playMusic()
        elif e.key() == Qt.Key.Key_HotLinks:
            if 'HotLinks' in keyConfig:
                newList(keyConfig['HotLinks'])
                playMusic()
        elif e.key() == Qt.Key.Key_BrightnessAdjust:
            if 'BrightnessAdjust' in keyConfig:
                newList(keyConfig['BrightnessAdjust'])
                playMusic()
        elif e.key() == Qt.Key.Key_Finance:
            if 'Finance' in keyConfig:
                newList(keyConfig['Finance'])
                playMusic()
        elif e.key() == Qt.Key.Key_Community:
            if 'Community' in keyConfig:
                newList(keyConfig['Community'])
                playMusic()
        elif e.key() == Qt.Key.Key_AudioRewind:
            if 'AudioRewind' in keyConfig:
                newList(keyConfig['AudioRewind'])
                playMusic()
        elif e.key() == Qt.Key.Key_BackForward:
            if 'BackForward' in keyConfig:
                newList(keyConfig['BackForward'])
                playMusic()
        elif e.key() == Qt.Key.Key_ApplicationLeft:
            if 'ApplicationLeft' in keyConfig:
                newList(keyConfig['ApplicationLeft'])
                playMusic()
        elif e.key() == Qt.Key.Key_ApplicationRight:
            if 'ApplicationRight' in keyConfig:
                newList(keyConfig['ApplicationRight'])
                playMusic()
        elif e.key() == Qt.Key.Key_Book:
            if 'Book' in keyConfig:
                newList(keyConfig['Book'])
                playMusic()
        elif e.key() == Qt.Key.Key_CD:
            if 'CD' in keyConfig:
                newList(keyConfig['CD'])
                playMusic()
        elif e.key() == Qt.Key.Key_Calculator:
            if 'Calculator' in keyConfig:
                newList(keyConfig['Calculator'])
                playMusic()
        elif e.key() == Qt.Key.Key_ToDoList:
            if 'ToDoList' in keyConfig:
                newList(keyConfig['ToDoList'])
                playMusic()
        elif e.key() == Qt.Key.Key_ClearGrab:
            if 'ClearGrab' in keyConfig:
                newList(keyConfig['ClearGrab'])
                playMusic()
        elif e.key() == Qt.Key.Key_Close:
            if 'Close' in keyConfig:
                newList(keyConfig['Close'])
                playMusic()
        elif e.key() == Qt.Key.Key_Copy:
            if 'Copy' in keyConfig:
                newList(keyConfig['Copy'])
                playMusic()
        elif e.key() == Qt.Key.Key_Cut:
            if 'Cut' in keyConfig:
                newList(keyConfig['Cut'])
                playMusic()
        elif e.key() == Qt.Key.Key_Display:
            if 'Display' in keyConfig:
                newList(keyConfig['Display'])
                playMusic()
        elif e.key() == Qt.Key.Key_DOS:
            if 'DOS' in keyConfig:
                newList(keyConfig['DOS'])
                playMusic()
        elif e.key() == Qt.Key.Key_Documents:
            if 'Documents' in keyConfig:
                newList(keyConfig['Documents'])
                playMusic()
        elif e.key() == Qt.Key.Key_Excel:
            if 'Excel' in keyConfig:
                newList(keyConfig['Excel'])
                playMusic()
        elif e.key() == Qt.Key.Key_Explorer:
            if 'Explorer' in keyConfig:
                newList(keyConfig['Explorer'])
                playMusic()
        elif e.key() == Qt.Key.Key_Game:
            if 'Game' in keyConfig:
                newList(keyConfig['Game'])
                playMusic()
        elif e.key() == Qt.Key.Key_Go:
            if 'Go' in keyConfig:
                newList(keyConfig['Go'])
                playMusic()
        elif e.key() == Qt.Key.Key_iTouch:
            if 'iTouch' in keyConfig:
                newList(keyConfig['iTouch'])
                playMusic()
        elif e.key() == Qt.Key.Key_LogOff:
            if 'LogOff' in keyConfig:
                newList(keyConfig['LogOff'])
                playMusic()
        elif e.key() == Qt.Key.Key_Market:
            if 'Market' in keyConfig:
                newList(keyConfig['Market'])
                playMusic()
        elif e.key() == Qt.Key.Key_Meeting:
            if 'Meeting' in keyConfig:
                newList(keyConfig['Meeting'])
                playMusic()
        elif e.key() == Qt.Key.Key_MenuKB:
            if 'MenuKB' in keyConfig:
                newList(keyConfig['MenuKB'])
                playMusic()
        elif e.key() == Qt.Key.Key_MenuPB:
            if 'MenuPB' in keyConfig:
                newList(keyConfig['MenuPB'])
                playMusic()
        elif e.key() == Qt.Key.Key_MySites:
            if 'MySites' in keyConfig:
                newList(keyConfig['MySites'])
                playMusic()
        elif e.key() == Qt.Key.Key_News:
            if 'News' in keyConfig:
                newList(keyConfig['News'])
                playMusic()
        elif e.key() == Qt.Key.Key_OfficeHome:
            if 'OfficeHome' in keyConfig:
                newList(keyConfig['OfficeHome'])
                playMusic()
        elif e.key() == Qt.Key.Key_Option:
            if 'Option' in keyConfig:
                newList(keyConfig['Option'])
                playMusic()
        elif e.key() == Qt.Key.Key_Paste:
            if 'Paste' in keyConfig:
                newList(keyConfig['Paste'])
                playMusic()
        elif e.key() == Qt.Key.Key_Phone:
            if 'Phone' in keyConfig:
                newList(keyConfig['Phone'])
                playMusic()
        elif e.key() == Qt.Key.Key_Calendar:
            if 'Calendar' in keyConfig:
                newList(keyConfig['Calendar'])
                playMusic()
        elif e.key() == Qt.Key.Key_Reply:
            if 'Reply' in keyConfig:
                newList(keyConfig['Reply'])
                playMusic()
        elif e.key() == Qt.Key.Key_Reload:
            if 'Reload' in keyConfig:
                newList(keyConfig['Reload'])
                playMusic()
        elif e.key() == Qt.Key.Key_RotateWindows:
            if 'RotateWindows' in keyConfig:
                newList(keyConfig['RotateWindows'])
                playMusic()
        elif e.key() == Qt.Key.Key_RotationPB:
            if 'RotationPB' in keyConfig:
                newList(keyConfig['RotationPB'])
                playMusic()
        elif e.key() == Qt.Key.Key_RotationKB:
            if 'RotationKB' in keyConfig:
                newList(keyConfig['RotationKB'])
                playMusic()
        elif e.key() == Qt.Key.Key_Save:
            if 'Save' in keyConfig:
                newList(keyConfig['Save'])
                playMusic()
        elif e.key() == Qt.Key.Key_Send:
            if 'Send' in keyConfig:
                newList(keyConfig['Send'])
                playMusic()
        elif e.key() == Qt.Key.Key_Spell:
            if 'Spell' in keyConfig:
                newList(keyConfig['Spell'])
                playMusic()
        elif e.key() == Qt.Key.Key_SplitScreen:
            if 'SplitScreen' in keyConfig:
                newList(keyConfig['SplitScreen'])
                playMusic()
        elif e.key() == Qt.Key.Key_Support:
            if 'Support' in keyConfig:
                newList(keyConfig['Support'])
                playMusic()
        elif e.key() == Qt.Key.Key_TaskPane:
            if 'TaskPane' in keyConfig:
                newList(keyConfig['TaskPane'])
                playMusic()
        elif e.key() == Qt.Key.Key_Terminal:
            if 'Terminal' in keyConfig:
                newList(keyConfig['Terminal'])
                playMusic()
        elif e.key() == Qt.Key.Key_Tools:
            if 'Tools' in keyConfig:
                newList(keyConfig['Tools'])
                playMusic()
        elif e.key() == Qt.Key.Key_Travel:
            if 'Travel' in keyConfig:
                newList(keyConfig['Travel'])
                playMusic()
        elif e.key() == Qt.Key.Key_Video:
            if 'Video' in keyConfig:
                newList(keyConfig['Video'])
                playMusic()
        elif e.key() == Qt.Key.Key_Word:
            if 'Word' in keyConfig:
                newList(keyConfig['Word'])
                playMusic()
        elif e.key() == Qt.Key.Key_Xfer:
            if 'Xfer' in keyConfig:
                newList(keyConfig['Xfer'])
                playMusic()
        elif e.key() == Qt.Key.Key_ZoomIn:
            if 'ZoomIn' in keyConfig:
                newList(keyConfig['ZoomIn'])
                playMusic()
        elif e.key() == Qt.Key.Key_ZoomOut:
            if 'ZoomOut' in keyConfig:
                newList(keyConfig['ZoomOut'])
                playMusic()
        elif e.key() == Qt.Key.Key_Away:
            if 'Away' in keyConfig:
                newList(keyConfig['Away'])
                playMusic()
        elif e.key() == Qt.Key.Key_Messenger:
            if 'Messenger' in keyConfig:
                newList(keyConfig['Messenger'])
                playMusic()
        elif e.key() == Qt.Key.Key_WebCam:
            if 'WebCam' in keyConfig:
                newList(keyConfig['WebCam'])
                playMusic()
        elif e.key() == Qt.Key.Key_MailForward:
            if 'MailForward' in keyConfig:
                newList(keyConfig['MailForward'])
                playMusic()
        elif e.key() == Qt.Key.Key_Pictures:
            if 'Pictures' in keyConfig:
                newList(keyConfig['Pictures'])
                playMusic()
        elif e.key() == Qt.Key.Key_Music:
            if 'Music' in keyConfig:
                newList(keyConfig['Music'])
                playMusic()
        elif e.key() == Qt.Key.Key_Battery:
            if 'Battery' in keyConfig:
                newList(keyConfig['Battery'])
                playMusic()
        elif e.key() == Qt.Key.Key_Bluetooth:
            if 'Bluetooth' in keyConfig:
                newList(keyConfig['Bluetooth'])
                playMusic()
        elif e.key() == Qt.Key.Key_WLAN:
            if 'WLAN' in keyConfig:
                newList(keyConfig['WLAN'])
                playMusic()
        elif e.key() == Qt.Key.Key_UWB:
            if 'UWB' in keyConfig:
                newList(keyConfig['UWB'])
                playMusic()
        elif e.key() == Qt.Key.Key_AudioForward:
            if 'AudioForward' in keyConfig:
                newList(keyConfig['AudioForward'])
                playMusic()
        elif e.key() == Qt.Key.Key_AudioRepeat:
            if 'AudioRepeat' in keyConfig:
                newList(keyConfig['AudioRepeat'])
                playMusic()
        elif e.key() == Qt.Key.Key_AudioRandomPlay:
            if 'AudioRandomPlay' in keyConfig:
                newList(keyConfig['AudioRandomPlay'])
                playMusic()
        elif e.key() == Qt.Key.Key_Subtitle:
            if 'Subtitle' in keyConfig:
                newList(keyConfig['Subtitle'])
                playMusic()
        elif e.key() == Qt.Key.Key_AudioCycleTrack:
            if 'AudioCycleTrack' in keyConfig:
                newList(keyConfig['AudioCycleTrack'])
                playMusic()
        elif e.key() == Qt.Key.Key_Time:
            if 'Time' in keyConfig:
                newList(keyConfig['Time'])
                playMusic()
        elif e.key() == Qt.Key.Key_Hibernate:
            if 'Hibernate' in keyConfig:
                newList(keyConfig['Hibernate'])
                playMusic()
        elif e.key() == Qt.Key.Key_View:
            if 'View' in keyConfig:
                newList(keyConfig['View'])
                playMusic()
        elif e.key() == Qt.Key.Key_TopMenu:
            if 'TopMenu' in keyConfig:
                newList(keyConfig['TopMenu'])
                playMusic()
        elif e.key() == Qt.Key.Key_PowerDown:
            if 'PowerDown' in keyConfig:
                newList(keyConfig['PowerDown'])
                playMusic()
        elif e.key() == Qt.Key.Key_Suspend:
            if 'Suspend' in keyConfig:
                newList(keyConfig['Suspend'])
                playMusic()
        elif e.key() == Qt.Key.Key_ContrastAdjust:
            if 'ContrastAdjust' in keyConfig:
                newList(keyConfig['ContrastAdjust'])
                playMusic()
        elif e.key() == Qt.Key.Key_TouchpadToggle:
            if 'TouchpadToggle' in keyConfig:
                newList(keyConfig['TouchpadToggle'])
                playMusic()
        elif e.key() == Qt.Key.Key_TouchpadOn:
            if 'TouchpadOn' in keyConfig:
                newList(keyConfig['TouchpadOn'])
                playMusic()
        elif e.key() == Qt.Key.Key_TouchpadOff:
            if 'TouchpadOff' in keyConfig:
                newList(keyConfig['TouchpadOff'])
                playMusic()
        elif e.key() == Qt.Key.Key_MicMute:
            if 'MicMute' in keyConfig:
                newList(keyConfig['MicMute'])
                playMusic()
        elif e.key() == Qt.Key.Key_Red:
            if 'Red' in keyConfig:
                newList(keyConfig['Red'])
                playMusic()
        elif e.key() == Qt.Key.Key_Green:
            if 'Green' in keyConfig:
                newList(keyConfig['Green'])
                playMusic()
        elif e.key() == Qt.Key.Key_Yellow:
            if 'Yellow' in keyConfig:
                newList(keyConfig['Yellow'])
                playMusic()
        elif e.key() == Qt.Key.Key_Blue:
            if 'Blue' in keyConfig:
                newList(keyConfig['Blue'])
                playMusic()
        elif e.key() == Qt.Key.Key_ChannelUp:
            if 'ChannelUp' in keyConfig:
                newList(keyConfig['ChannelUp'])
                playMusic()
        elif e.key() == Qt.Key.Key_ChannelDown:
            if 'ChannelDown' in keyConfig:
                newList(keyConfig['ChannelDown'])
                playMusic()
        elif e.key() == Qt.Key.Key_Guide:
            if 'Guide' in keyConfig:
                newList(keyConfig['Guide'])
                playMusic()
        elif e.key() == Qt.Key.Key_Info:
            if 'Info' in keyConfig:
                newList(keyConfig['Info'])
                playMusic()
        elif e.key() == Qt.Key.Key_Settings:
            if 'Settings' in keyConfig:
                newList(keyConfig['Settings'])
                playMusic()
        elif e.key() == Qt.Key.Key_MicVolumeUp:
            if 'MicVolumeUp' in keyConfig:
                newList(keyConfig['MicVolumeUp'])
                playMusic()
        elif e.key() == Qt.Key.Key_MicVolumeDown:
            if 'MicVolumeDown' in keyConfig:
                newList(keyConfig['MicVolumeDown'])
                playMusic()
        elif e.key() == Qt.Key.Key_New:
            if 'New' in keyConfig:
                newList(keyConfig['New'])
                playMusic()
        elif e.key() == Qt.Key.Key_Open:
            if 'Open' in keyConfig:
                newList(keyConfig['Open'])
                playMusic()
        elif e.key() == Qt.Key.Key_Find:
            if 'Find' in keyConfig:
                newList(keyConfig['Find'])
                playMusic()
        elif e.key() == Qt.Key.Key_Undo:
            if 'Undo' in keyConfig:
                newList(keyConfig['Undo'])
                playMusic()
        elif e.key() == Qt.Key.Key_Redo:
            if 'Redo' in keyConfig:
                newList(keyConfig['Redo'])
                playMusic()
        elif e.key() == Qt.Key.Key_MediaLast:
            if 'MediaLast' in keyConfig:
                newList(keyConfig['MediaLast'])
                playMusic()
        elif e.key() == Qt.Key.Key_unknown:
            if 'unknown' in keyConfig:
                newList(keyConfig['unknown'])
                playMusic()
        elif e.key() == Qt.Key.Key_Call:
            if 'Call' in keyConfig:
                newList(keyConfig['Call'])
                playMusic()
        elif e.key() == Qt.Key.Key_Camera:
            if 'Camera' in keyConfig:
                newList(keyConfig['Camera'])
                playMusic()
        elif e.key() == Qt.Key.Key_CameraFocus:
            if 'CameraFocus' in keyConfig:
                newList(keyConfig['CameraFocus'])
                playMusic()
        elif e.key() == Qt.Key.Key_Context1:
            if 'Context1' in keyConfig:
                newList(keyConfig['Context1'])
                playMusic()
        elif e.key() == Qt.Key.Key_Context2:
            if 'Context2' in keyConfig:
                newList(keyConfig['Context2'])
                playMusic()
        elif e.key() == Qt.Key.Key_Context3:
            if 'Context3' in keyConfig:
                newList(keyConfig['Context3'])
                playMusic()
        elif e.key() == Qt.Key.Key_Context4:
            if 'Context4' in keyConfig:
                newList(keyConfig['Context4'])
                playMusic()
        elif e.key() == Qt.Key.Key_Flip:
            if 'Flip' in keyConfig:
                newList(keyConfig['Flip'])
                playMusic()
        elif e.key() == Qt.Key.Key_Hangup:
            if 'Hangup' in keyConfig:
                newList(keyConfig['Hangup'])
                playMusic()
        elif e.key() == Qt.Key.Key_No:
            if 'No' in keyConfig:
                newList(keyConfig['No'])
                playMusic()
        elif e.key() == Qt.Key.Key_Select:
            if 'Select' in keyConfig:
                newList(keyConfig['Select'])
                playMusic()
        elif e.key() == Qt.Key.Key_Yes:
            if 'Yes' in keyConfig:
                newList(keyConfig['Yes'])
                playMusic()
        elif e.key() == Qt.Key.Key_ToggleCallHangup:
            if 'ToggleCallHangup' in keyConfig:
                newList(keyConfig['ToggleCallHangup'])
                playMusic()
        elif e.key() == Qt.Key.Key_VoiceDial:
            if 'VoiceDial' in keyConfig:
                newList(keyConfig['VoiceDial'])
                playMusic()
        elif e.key() == Qt.Key.Key_LastNumberRedial:
            if 'LastNumberRedial' in keyConfig:
                newList(keyConfig['LastNumberRedial'])
                playMusic()
        elif e.key() == Qt.Key.Key_Execute:
            if 'Execute' in keyConfig:
                newList(keyConfig['Execute'])
                playMusic()
        elif e.key() == Qt.Key.Key_Printer:
            if 'Printer' in keyConfig:
                newList(keyConfig['Printer'])
                playMusic()
        elif e.key() == Qt.Key.Key_Play:
            if 'Play' in keyConfig:
                newList(keyConfig['Play'])
                playMusic()
        elif e.key() == Qt.Key.Key_Sleep:
            if 'Sleep' in keyConfig:
                newList(keyConfig['Sleep'])
                playMusic()
        elif e.key() == Qt.Key.Key_Zoom:
            if 'Zoom' in keyConfig:
                newList(keyConfig['Zoom'])
                playMusic()
        elif e.key() == Qt.Key.Key_Exit:
            if 'Exit' in keyConfig:
                newList(keyConfig['Exit'])
                playMusic()
        elif e.key() == Qt.Key.Key_Cancel:
            if 'Cancel' in keyConfig:
                newList(keyConfig['Cancel'])
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
        mserver.stop()
        self.screen.close()

def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    global window
    window = ex
    sys.exit(app.exec())


if __name__ == '__main__':
    main()