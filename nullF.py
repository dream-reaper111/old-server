# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nullchat.ui'
#
# Created: Mon Apr 24 20:21:18 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore
from PyQt4 import QtGui
import sys, socket, re
from threading import Thread
import time, errno, base64
from Crypto import Random
from Crypto.Cipher import AES
from hashlib import sha512
from pyfiglet import figlet_format
global key, hasnumm, sock


key = sha512('nullchatter').hexdigest()[:16]
hashnum = 1
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def update_list(self, data): 
    self.listWidget.addItem(data)

def ench():
   global hashnum, key
   if hashnum != 20: 
		hashnum += 1
		key = sha512(key).hexdigest()[:16]
   else:
		hashnum = 1
		key = sha512('nullchatter').hexdigest()[:16]
	
def mySend(mssg):
        totalSent = 0
        try:
            sock.send(mssg)
        except IOError, e:
            if e.errno == errno.EPIPE:
                closeThread()
        except socket.error:
            closeThread()
        except:
            pass

def myReceive(timeout=.5):
        global sock
        mess = ''
        sock.settimeout(timeout)
        try:
            while 1: 
                data = sock.recv(1024)
                if not data: break
                else:
                    mess += data
        except:
            pass
        return mess
        
def mainListener(self):
    global key
    while True: 
        try:
            data = myReceive()
        except KeyboardInterrupt, SystemExit:
            pass
        if data != None and data != '':
            try:
                data = decrypt(key, data)
            except: 
                data = 'Couln\'t Decode Message'
            data = re.sub("(.{50})", "\\1\n", data, 0, re.DOTALL)
            update_list(self, data)
            self.listWidget.setCurrentRow(self.listWidget.currentRow())
            ench()
            
            
def _pad(s, bs=32):
    return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
    
def _unpad(s):
    return s[:-ord(s[len(s) - 1:])]

def encrypt(keys, raw):
    raw = _pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(keys, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))

def decrypt(keys, enc):
    enc = base64.b64decode(enc)
    iv = enc[:AES.block_size]
    cipher = AES.new(keys, AES.MODE_CBC, iv)
    return _unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

def initialization(self):
        global sock, key
        sock.connect(('127.0.0.1', 4445))
        mySend(encrypt(key, sha512('IGVKMFMR9O3CYZ6HFVPD7LGN14OEV59K6NXKPTFYPELPL5YB9Y121UO178FKHJF20Q133IDH0N3H0SJA9LZCCYONNI2QSIYPLWE5MMZJ347L55MMYUSIE7RWOLYR8AIIPV2AGV9NRE7950FLTAOLLDBO4UNQI0ZIXVHU2VP0TH6B0UEXK19UMRIL6J38L1B1OJNR1EVF75J6LV4QQHEYT2577WXV1O9XZ4VC3QL72666HU877L3H3QUA3XM64NITIYEUBJ7OXCIQ4YOIDMRKWDBBMHM9W9J23MCRDDNMM85KI5E7ANR3YVGV2GCCCD4O6L2O7OYNOND6L8X5XA6FKA2Q3EYL508OPUITRQ25XM19DDJX7F6MMSHI2UWU8T1UJDMNKP9EXHW64OS8SFX810KD6OA4U9W7FXOTNZCNXQ9RPZQH9HE0BLDY05F4LMFQJT0SFG8UELNEY42WVMZH84KSDPBMPXUCM3GPRN55YBVD9G5H9JPZFSPDQEPRG4ES3FD5U9607TRTLGFR9QM9DE50IC9YXNZWMHSEA2C1BYPLZTRT3TOA6OA72ELAZMOYSXZ1487KSYNB6JTM2XF3TGPXJ53A96HZW9GX39W0137NE57Q02BPSESBESMPGDVT8R9FJGB1MPTLDOS2YH1SI1T8UAM83F2UJBJ8RUYOO64W2FM359NMG81INDAGVD66FXD782BFPEEXMN641CY5VSLSWCC0ID0J4R51PVYJDMT7XJQVDYBC7YU927SOJ5JQO4UCO9SCJFQ7ETZWDY7IFWHBYBKGRDIQM6I7U9QPABHZTJPZQ8WRJWTCLK53SB5KDXLVIHNDZYF3TLMW6BAEMGEHLA6DWU66TRNBGF4T4D4CZ8YY91FV7VI0P6RUBUQWQMBFAC8TGM84LS68L6Z0ZM0Z9PWO9E2HY57PBAT6X7G3UENPQRJ56KUNI57FT719YI8PLQ35PS32UCRQ1AME85Y0VLPL5YP70HDUBAN6MR3Y7ALVFCL98UX62AY59B2IZMVA3Q6NPBN9JEP2JSM0I6CWWRW5QQU0PBH6YT51QQZ3TM4MPR8Y34EPCTDGPBPISH9QTK55UF9XKFCUFH8HA5AUP30V85P8TM8OEQQHD2S7EIHX1HOHKFZLS103RPXIBXFOVQI5JBJW6EPNTE4HVYMI0EI4WXGQZDCC7EYMRBREI8C6N896OZEHBSIYRKSLTX6B684QSRSHMS7SK5NU3CX3Z3NMF263HSG0NVRV6WI1ZZISNS25CQR42FS4YPEDBRR2PGZ5H5F3O9K2NPOXUDPSAVZLRRAU4OZ2RQ4RB2BOZWCQ0R2KTTQ7QQW7C8G6CCD9U56CJS3MSO45ZQL8JDAL50AQWGYV51M598LDLEG1WLRJZMHSXSSA8OA7V9G0P0KAYEV5HCS52YICO81VIC1VOAJ4IA9HRLW7T1P8Y5UVGCILNYBJUFQNEKH63WBO18ZG25WWM2MGSQ7LCWYM0GJT9819E7ZIZ7544I2VBX8OLID65OFD0BU0S28R8WU86U3Y8ZXIFR23DKKW1FI6L2T1XOPNKKTGOWZM4IF8CW4IL79YHEZKDNC08QAPX7I5Y8WDVFOAWCLWVN0EWY2SQU189V8QFQ4TD1V9HTS6WG63LGU192XT4M8SDSIWRN77TR0TE346H9BP803ZVN37F5SYNCWPZSUI01KIZY9ND2AAYAPSHSW5XTG2MZJ3HGIOYL67IT0DF2Z42INNDM8V7KY580NUJEJB6D1UNFRNIUV0F7O10AZLVJ18DK7TW4K580Z0L3LC1Z1NG51QZWYV6XUF4ZYNEZSEUXPF91208R8ADEN0BUGS16IU0MRGJO196WXF4KF3QC5AHU5U74UBH2MAI0C7ZQA1IL5YOFLLYB9EC86F13XJAMQ3C80R9RZKZM2083O2NRYHB372C77FA8TBB5PGKB40BOYCHTEJOI66D7QRNC9SVE0AWULDQLRYY4CWD9YKCPW9Z8G0ZV9WBAL9DMZT2E1MQPGXCPV6KY7YKRHYCSS46X9M6K34ZCIO').hexdigest()[:2048]))
        ench()
        decrypt(key, sock.recv(4096))
        ench()
        mySend(encrypt(key, 'Fr1ee'))
        ench()
        decrypt(key, sock.recv(4096))
        update_list(self, 'CONNECTION ESTABLISHED')
        ench()
             
def getmessages(self):
        try:
            mySend(self.encrypt(self.key, 'messages'))
            ench()
        except KeyboardInterrupt:
            pass
        except:
            print 'ERROR GETTING MESSAGES'

def starter(selfie):
	initialization(selfie)
	Thread(target=mainListener, args=[selfie,]).start()
	
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_null1(object):
    def setupUi(self, null1):
        self.startchat()
        null1.setObjectName(_fromUtf8("null1"))
        null1.resize(729, 304)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.textEdit = QtGui.QTextEdit(self.dockWidgetContents)
        self.textEdit.setGeometry(QtCore.QRect(10, 190, 481, 75))
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(500, 190, 71, 71))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.BroadcastMessage)
        self.listWidget = QtGui.QListWidget(self.dockWidgetContents)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 691, 171))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.pushButton_2 = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 190, 121, 71))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.closeEvent)
        null1.setWidget(self.dockWidgetContents)

        self.retranslateUi(null1)
        QtCore.QMetaObject.connectSlotsByName(null1)

    def retranslateUi(self, null1):
        null1.setWindowTitle(_translate("null1", "NULLSEC CHAT", None))
        self.pushButton.setText(_translate("null1", "SEND", None))
        self.pushButton_2.setText(_translate("null1", "DISCONNECT", None))
    
    def closeEvent(self):
        global sock, key 
        mySend(encrypt(key, '0x90exit0x90'))
        sock.close()
        sys.exit(0)
        
    def startchat(self): 
		temper = Thread(target=starter, args=[self,])
		temper.start()
        
    def BroadcastMessage(self):
        global key, sock
        msg = self.textEdit.toPlainText()
        crazy = msg
        try:
            #encrypt(key, msg)
            crazy = msg
            sock.send(encrypt(key, str(msg)))
            ench()
        except KeyboardInterrupt: 
            pass
        except:
            print 'ERROR SENDING MESSAGE'
        self.textEdit.clear()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    null1 = QtGui.QDockWidget()
    ui = Ui_null1()
    ui.setupUi(null1)
    null1.show()
    sys.exit(app.exec_())

