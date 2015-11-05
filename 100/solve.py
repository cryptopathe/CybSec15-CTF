# Copyright (c) 2015 Pascal Junod <pascal@junod.info>
# Licensed under the MIT license (copy available at https://opensource.org/licenses/MIT)

import base64

filename = "g-b-bellaso.txt"

if __name__ == "__main__":

    try:
        f = open (filename, "r")
        c = f.read ()

        c = base64.b64decode(c.split ("\n")[3])
        for i in range(17):
            c = base64.b64decode(c.split (" ")[3])
        print (c)

        key = "CyberSec15"

        p = ''
        for i in range(len (c)):
            p += chr(ord(c[i]) ^ ord(key[i % len (key)]))
        print (p)

    except:
            print ("Cannot open %s" % filename)
    finally:
        f.close ()

