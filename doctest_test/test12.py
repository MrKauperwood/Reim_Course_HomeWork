import os
import doctest
import unittest

root_path = '.'
massive = []


for root, dirs, files in os.walk(root_path):
   for name in filter(lambda x: x[-3:]==".py", files):
      path = os.path.join(root, name)
      with open(path, "r") as file:
          text = file.readlines()[:10]
          if "#DOCTEST" in str(text):
              massive.append(path[2:-3].replace("\\", "."))

print(massive)

for file in massive:
    print(file)
    pm = __import__(file)
    doctest.testmod(pm)
    print()




