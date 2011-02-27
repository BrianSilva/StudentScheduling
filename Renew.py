import os
import time
import pickle
import random
import string
import hashlib

# Character Sets
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation
letters = lowercase + uppercase
normal = lowercase + uppercase + digits
powerful = lowercase + uppercase + digits + "!@$%^&*()-_=+`~|:;<,>.?/"

def random_string_generator(n):
    output = ""
    for i in range(n):
        output += random.choice(powerful)
    return output
def generate_random_strings(n):
    full_hash = ""
    count = 1
    while count <= n:
        full_hash += random_string_generator(random.randint(6, 255)) + " "
        count += 1
    if Renew().License1(full_hash) == True:
        if Renew().License2(full_hash) == True:
            return True
        else:
            return False
    else:
        return False

class Renew:
    def License(self):
        if generate_random_strings(185) == True:
            return True
        else:
            return False
    def License1(self, full_hash):
        success = False
        directory = os.getcwd()
        file = "/Settings.ini"
        path = directory + file
        try:
            f = open(path, "wb")
            pickle.dump(full_hash, f)
            f.close()
            success = True
        except:
            success = False
        return success
    def License2(self, full_hash):
        success = False
        directory = os.getcwd()
        file = "/Do_Not_Modify.dat"
        path = directory + file
        try:
            f = open(path, "w")
            f.write(full_hash)
            f.close()
            sucess = True
        except:
            success = False
        return success

class Renew_License:
    def run(self, code):
        if code.lower() == "ssrf":
            renewed = False
            if Renew().License() == True:
                file = "Do_Not_Modify.dat"
                f = open(file, "r")
                o = f.readlines()
                f.close()
                os.remove(file)
                full_hash = ""
                for line in o:
                    md5_line = hashlib.md5()
                    md5_line.update(bytes(line, encoding = "utf8"))
                    full_hash += md5_line.hexdigest() + "\n"
                full_hash = str(full_hash)
                f = open(file, "w")
                f.write(full_hash)
                f.close()
                renewed = True
            else:
                renewed = False
            return renewed
        else:
            return False
