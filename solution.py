import os
import threading
import time


def Union(lst1, lst2):
    final_list = sorted(list(set(lst1) | set(lst2)))
    return final_list  


def readEntries(fileNumber):
    file = open(folderPath + "\\" + (filesNames[fileNumber]), encoding = 'utf8')
    read = file.read()
    file.seek(0)
    byte_array = bytearray(read, 'utf-8')
    mvs.append(byte_array)

def mergingEntries(fileNumber): 
    termWithIds = (bytes(mvs[fileNumber])).splitlines()
    #To ignore the title line(term, docsId) 
    index = 1
    for index in range(len(termWithIds)):
        term = termWithIds[index].decode("utf-8").split(',')[0]
        mapVal = map(int, list(termWithIds[index].decode("utf-8").split(',')[1::]))
        docsList = list(mapVal)  

        if term not in dictionary:
            dictionary[term] = docsList
        else: 
            sortedDocsList = Union(dictionary[term], docsList)
            dictionary[term] = sortedDocsList

folderPath = input("Please inter the full path of the folder as the following format \n C:\\Users\\hp\\Desktop\\rama_hasiba_1st_HW\n") 
#folderPath = "C:\\Users\\hp\\Desktop\\rama_hasiba_1st_HW\\newDocs"
fullPath = "r'" + folderPath + "'"
filesNames = os.listdir(r'C:\\Users\\hp\\Desktop\\rama_hasiba_1st_HW\\newDocs')

dictionary = {}
fileIndex = 0
mvs = []
while fileIndex < len(filesNames): 
    firstThread = threading.Thread(target = readEntries, args = (fileIndex, ))
    firstThread.start()
    firstThread.join()

    secondThread = threading.Thread(target = mergingEntries, args = (fileIndex, ))
    secondThread.start()
    secondThread.join()
    dictionary = dict(sorted(dictionary.items()))

    if fileIndex == (len(filesNames) - 1):
        invertedIndexFile = open('invertedIndexFile.csv', 'w')
        for item in dictionary:
            print(item, ",", dictionary[item], file = invertedIndexFile)         
        fileIndex = fileIndex + 1
    else:
        fileIndex = fileIndex + 1 
 