"""This code is a tes"""
# argv.py
import string
import sys 
def getBrandName ():
    argList = sys.argv

    if (len(argList) == 2 ):
        print("you have entered correct brand nums!")
        brandName = argList[1]
        return brandName  
    else: 
       print("you have entered the wrong arguments bestie")
       return  

brandName = getBrandName()

