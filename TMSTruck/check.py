import os

path = "C:\\temp\myFolder\example\\"

newPath = path.replace(os.sep, '/')

print (newPath)
