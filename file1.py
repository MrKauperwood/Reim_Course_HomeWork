from os.path import dirname, abspath
import sys
print(sys.path)
print(abspath(__file__))
print(dirname(dirname(abspath(__file__))))