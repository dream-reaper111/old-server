"""
PROGRAM: SOCKET_PROGRAM.py
PROGRAMMER: Taipan.py, NullByte.py
PROJECT_DATE_STARTED: 04/11/17
PROJECT_DATE_END:

"""

import os, sys, time, errno, socket, base64, random, string
from threading import Thread
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from pyfiglet import figlet_format
from Crypto import Random
from Crypto.Cipher import AES
from hashlib import sha512
# Create an INET, STREAMing socket



#NullByte Addendum: We'll use this to keep track of people connected, and to use it to pass communications.
global nullmem, hasher
nullmem = []
hasher = sha512(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))).hexdigest()[:16]
#---------------------------------------------------------------------------------------------------------

#NullByte Addendum: Made the class threaded, that way we can have multiple instances of it running.
class mySocket(Thread):
        # class for the socket

    #Impor
    def __init__(self, sock=None):
        super(mySocket, self).__init__()
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
        self.messagestosend = []
        self.name = ''
        self.address = ''
        self.hashnum = 1
        self.wait = False
        self.key = sha512('nullchatter').hexdigest()[:16]
    #NullByte Addnendum: I don't think this is needed. The server should simply accept connections from clients.
    #I don't see why it would need to do the connecting if the client does the connecting/
    #def connect(self, host, port):
    #    self.sock.connect((host, port))

    # NullByte Addendum:
    # Added exception handling to the code, that way it doesn't completely crash the server
    # if something goes wrong. Also, made mySend simpler, and more fool-proof

    def mySend(self, msg):
        try:
            self.sock.send(msg)
        except IOError, e:
            if e.errno == errno.EPIPE:
                self.closeThread()
        except socket.error:
            self.closeThread()
        except:
            pass

    def closeThread(self):
        print 'Connection Closed: '+self.name
        self.sock.close()
        for count, i in enumerate(nullmem):
            if self.name.lower() in i.name.lower():
                nullmem.pop(count)
                break
        sys.exit(0)

    def dead(self):
        while True:
            response = os.system("ping -c 1 -w2 " + str(self.address) + " > /dev/null 2>&1")
            if response == 1:
                self.closeThread()
            time.sleep(120)

    def intialize(self):
        initdata = self.decrypt(self.key, self.myReceive())
        print initdata
        self.enchashnum()
        if initdata != sha512('IGVKMFMR9O3CYZ6HFVPD7LGN14OEV59K6NXKPTFYPELPL5YB9Y121UO178FKHJF20Q133IDH0N3H0SJA9LZCCYONNI2QSIYPLWE5MMZJ347L55MMYUSIE7RWOLYR8AIIPV2AGV9NRE7950FLTAOLLDBO4UNQI0ZIXVHU2VP0TH6B0UEXK19UMRIL6J38L1B1OJNR1EVF75J6LV4QQHEYT2577WXV1O9XZ4VC3QL72666HU877L3H3QUA3XM64NITIYEUBJ7OXCIQ4YOIDMRKWDBBMHM9W9J23MCRDDNMM85KI5E7ANR3YVGV2GCCCD4O6L2O7OYNOND6L8X5XA6FKA2Q3EYL508OPUITRQ25XM19DDJX7F6MMSHI2UWU8T1UJDMNKP9EXHW64OS8SFX810KD6OA4U9W7FXOTNZCNXQ9RPZQH9HE0BLDY05F4LMFQJT0SFG8UELNEY42WVMZH84KSDPBMPXUCM3GPRN55YBVD9G5H9JPZFSPDQEPRG4ES3FD5U9607TRTLGFR9QM9DE50IC9YXNZWMHSEA2C1BYPLZTRT3TOA6OA72ELAZMOYSXZ1487KSYNB6JTM2XF3TGPXJ53A96HZW9GX39W0137NE57Q02BPSESBESMPGDVT8R9FJGB1MPTLDOS2YH1SI1T8UAM83F2UJBJ8RUYOO64W2FM359NMG81INDAGVD66FXD782BFPEEXMN641CY5VSLSWCC0ID0J4R51PVYJDMT7XJQVDYBC7YU927SOJ5JQO4UCO9SCJFQ7ETZWDY7IFWHBYBKGRDIQM6I7U9QPABHZTJPZQ8WRJWTCLK53SB5KDXLVIHNDZYF3TLMW6BAEMGEHLA6DWU66TRNBGF4T4D4CZ8YY91FV7VI0P6RUBUQWQMBFAC8TGM84LS68L6Z0ZM0Z9PWO9E2HY57PBAT6X7G3UENPQRJ56KUNI57FT719YI8PLQ35PS32UCRQ1AME85Y0VLPL5YP70HDUBAN6MR3Y7ALVFCL98UX62AY59B2IZMVA3Q6NPBN9JEP2JSM0I6CWWRW5QQU0PBH6YT51QQZ3TM4MPR8Y34EPCTDGPBPISH9QTK55UF9XKFCUFH8HA5AUP30V85P8TM8OEQQHD2S7EIHX1HOHKFZLS103RPXIBXFOVQI5JBJW6EPNTE4HVYMI0EI4WXGQZDCC7EYMRBREI8C6N896OZEHBSIYRKSLTX6B684QSRSHMS7SK5NU3CX3Z3NMF263HSG0NVRV6WI1ZZISNS25CQR42FS4YPEDBRR2PGZ5H5F3O9K2NPOXUDPSAVZLRRAU4OZ2RQ4RB2BOZWCQ0R2KTTQ7QQW7C8G6CCD9U56CJS3MSO45ZQL8JDAL50AQWGYV51M598LDLEG1WLRJZMHSXSSA8OA7V9G0P0KAYEV5HCS52YICO81VIC1VOAJ4IA9HRLW7T1P8Y5UVGCILNYBJUFQNEKH63WBO18ZG25WWM2MGSQ7LCWYM0GJT9819E7ZIZ7544I2VBX8OLID65OFD0BU0S28R8WU86U3Y8ZXIFR23DKKW1FI6L2T1XOPNKKTGOWZM4IF8CW4IL79YHEZKDNC08QAPX7I5Y8WDVFOAWCLWVN0EWY2SQU189V8QFQ4TD1V9HTS6WG63LGU192XT4M8SDSIWRN77TR0TE346H9BP803ZVN37F5SYNCWPZSUI01KIZY9ND2AAYAPSHSW5XTG2MZJ3HGIOYL67IT0DF2Z42INNDM8V7KY580NUJEJB6D1UNFRNIUV0F7O10AZLVJ18DK7TW4K580Z0L3LC1Z1NG51QZWYV6XUF4ZYNEZSEUXPF91208R8ADEN0BUGS16IU0MRGJO196WXF4KF3QC5AHU5U74UBH2MAI0C7ZQA1IL5YOFLLYB9EC86F13XJAMQ3C80R9RZKZM2083O2NRYHB372C77FA8TBB5PGKB40BOYCHTEJOI66D7QRNC9SVE0AWULDQLRYY4CWD9YKCPW9Z8G0ZV9WBAL9DMZT2E1MQPGXCPV6KY7YKRHYCSS46X9M6K34ZCIO').hexdigest()[:2048]:
            self.closeThread()
        print 'LOGIN SUCCESS'
        self.mySend(self.encrypt(self.key, 'Initialize'))
        self.enchashnum()
        while True:
            data = self.myReceive()
            if data:
                data = self.decrypt(self.key, data)
                self.enchashnum()
                if data != None and data != '':
                    self.name = data
                    print 'Name is now: '+self.name
                    break
        self.banner()

    def banner(self):
        ban = '-'*50+'\n'
        ban += figlet_format('NULLSEC', font='doom')
        ban += '-'*50+'\n'
        self.mySend(self.encrypt(self.key, ban))
        self.enchashnum()

    def addMessage(self, msg):
        self.wait = True
        tub = msg[:msg.index(':') + 1]
        lis = self.decrypt(hasher, msg[msg.index(':') + 1:])
        messagies = tub + ' '+ lis
        self.mySend(self.encrypt(self.key, messagies))
        self.enchashnum()
        self.wait = False

    def listUsers(self):
        global nullmem
        usrs = ''
        for i in nullmem:
            usrs += i.name+'\n'
        return self.stylemesssage(usrs)

    def _pad(self, s, bs=32):
        return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

    def _unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]

    def encrypt(self, key, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, key, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    #NullByte Addendum:
    #Added exception handling to the code, that way it doesn't completely crash the server
    #if something goes wrong. Also re-wrote receiver to be fool-proof.

    def myReceive(self, timeout=.25):
        mess = ''
        self.sock.settimeout(timeout)
        try:
            while 1:
                data = self.sock.recv(4096)
                if not data: break
                else: mess += data
        except socket.error as e:
            if e.errno != errno.EPIPE: 
                pass
            else:
                pass
            #    self.closeThread()
        except:
            pass
        return mess
    #NullByte Addendum: What's a message without a little style? ;)
    def stylemesssage(self, msg):
        content = ''
        content += '----------------------------------------------------------------------\n'
        content += msg+'\n'
        content += '----------------------------------------------------------------------\n'
        return content

    def enchashnum(self):
        if self.hashnum != 20:
            self.hashnum += 1
            self.key = sha512(self.key).hexdigest()[:16]
        else:
            self.hashnum = 1
            self.key = sha512('nullchatter').hexdigest()[:16]
    
    def handleinf(self, data):
        global hasher, nullmem
        success = 0
        if data:
            try:
                data = self.decrypt(self.key, data)
                self.enchashnum()
                success = 1
            except:
                self.mySend(self.encrypt(self.key, '<Unable To Decode Message>'))
                self.enchashnum()
                self.enchashnum()
                success = 0
            
            if success == 1:    
                if data == '0x90exit0x90':
                    self.closeThread()
                else:
                    for user in nullmem:
                        while user.wait == True: 
                            print 'waiting' 
                        Thread(target=user.addMessage, args=[self.name + ': ' + self.encrypt(hasher, data) ,]).start()
                        
    def runtimehandler(self):
        while True:
            try:
                data = self.myReceive()
                Thread(target=self.handleinf, args=[data,]).start()
            except socket.error:
                self.closeThread()
            except:
                print 'Handled Exception...'
    #NullByte Addendum:
    #I've made this function as the main thread handler for our server. This function controls everything for each user.
    def run(self):
        Thread(target=self.dead).start()
        self.intialize()
        Thread(target=self.runtimehandler).start()
        Thread(target=self.runtimehandler).start()

s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
# Now connect to the web server on port 1337
# - the normal http port

#NullByte Addendum: Added exception handling, multi-threading, as well as keeping track of users.
s.bind(('127.0.0.1', 4445))
s.listen(5)
while 1:
    try:
        # accecpt connections from outside
        clientsocket, address = s.accept()
        # now do something with the clientsocket
        # in this case, we'll pretend this is a treaded server
        ct = mySocket(clientsocket)
        ct.daemon = True
        nullmem.append(ct)
        ct.start()
    except KeyboardInterrupt:
        for i in nullmem:
            i.closeThread()
        s.close()
        sys.exit(0)
    except:
        for i in nullmem:
            i.closeThread()
        s.close()
        sys.exit(0)

