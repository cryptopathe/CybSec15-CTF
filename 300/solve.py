# Copyright (c) 2015 Pascal Junod <pascal@junod.info>
# Licensed under the MIT license (copy available at https://opensource.org/licenses/MIT)

from Crypto.Cipher import AES
import hashlib


pi = [2, 63317, 63331, 63337, 63347, 63353, 63361, 63367, 63377, 63389, 63391, 63397, 63409, 63419, 63421, 63439, 63443,
    63463, 63467, 63473, 63487, 63493, 63499, 63521, 63527, 63533, 63541, 63559, 63577, 63587, 63589, 63599, 63601,
    63607, 63611, 63617, 63629, 63647, 63649, 63659, 63667, 63671, 63689, 63691, 63697, 63703, 63709, 63719, 63727,
    63737, 63743, 63761, 63773, 63781, 63793, 63799, 63803, 63809, 63823, 63839, 63841, 63853, 63857, 63863, 63901,
    63907, 63913, 63929, 63949, 63977, 63997, 64007, 64013, 64019, 64033, 64037, 64063, 64067, 64081, 64091, 64109,
    64123, 64151, 64153, 64157, 64171, 64187, 64189, 64217, 64223, 64231, 64237, 64271, 64279, 64283, 64301, 64303,
    64319, 64327, 64333, 64373, 64381, 64399, 64403, 64433, 64439, 64451, 64453, 64483, 64489, 64499, 64513, 64553,
    64567, 64577, 64579, 64591, 64601, 64609, 64613, 64621, 64627, 64633, 64661, 64663, 64667, 64679, 64693, 64709,
    64717]

g = 5

ga = 148269435073271505596500918203676478260050377054699645297627646124287928021068128874626703723566660218378940694783618009813282462112920447382373172050683959394286963250141692310143491739940296040206510436823896138834900947496798708585546476241568097202388442890614351527789438409260876642960155502421656218430757670276302451509421571533434790063793450615805051836759411127178893817056356576746760434468728709103297947999000188162761143567788765368787645749642475703230750980877550801515162102461542330403649762723475340218697442879386285010217320748650812005518633552322175308740923418721560349120796652666935465200139406

gb  = 109521608064614903921417413416690262413697172507979461475361252709002817072076337286402798222398082256611058127732826695856472177055450077619686030864060892749685895950667479668884035230090536293677249802901224949793707922367721430621345066840979594660800762777480036512763712033902555967666926184553571782023776597469398102655134708894003481084256457190426142457501124148202780225614796899892871599299804290263332780879919819863967664033533749515611667184384700129201590582800893763156098158021477833319005213651191262987237962346400542682580653773951951075311832525434271807071870606588331169695305420057216994177176314

def solve (g, h, p, pi):
    for i in range (pi):
        if pow (g, i, p) == h:
            return i

if __name__ == "__main__":

    p = 1
    for i in range (len (pi)):
        p *= pi[i]
    p += 1
    print ("p = " + str(p))

    gi = []
    gai = []
    xi = []

    # Computing logs mod p_i
    for i in range (len (pi)):
        gi.append (pow (g, (p-1)//pi[i], p))
        gai.append (pow (ga, (p-1)//pi[i], p))
        xi.append (solve (gi[i], gai[i], p, pi[i]))
        
    # Combining everything using Chinese remainders
    a = 0
    for i in range (len(pi)):
        a += xi[i]*pow((p-1)//pi[i], pi[i]-2, pi[i])*((p-1)//pi[i])

    print (a % (p-1))

    gab = pow (gb, a, p)

    print ("gab = " + str (gab))
    
    IV = '\x23\x43\x79\x62\x53\x65\x63\x31\x35\x20\x72\x75\x6c\x65\x7a\x7a'
    key = hashlib.sha256 (str(gab).encode('utf-8')).digest ()
    enc = AES.new (key, AES.MODE_CBC, IV=IV)
    c = b'\x9b@\x18$$\x8e\xe4\xb8,\xb4h\xfd\xb6\xec1\n\xd1D)~\x05\x8a\xdf\x01\x03\x93#(f\xb4\xff\xec'
    p = enc.decrypt (c)
    print (p)
