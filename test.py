import sys 
import os


id = sys.argv[1]
a  = os.popen('dir .').readlines()


print(a)