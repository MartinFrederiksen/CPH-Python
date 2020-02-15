import os

def allFileNamesInFolder(folderPath, outputFile):
    with open(outputFile, 'w') as File:
        for f in os.listdir(folderPath):
            File.write(folderPath + f + "\n")

def filesOfAllSubfolders(folderPath, outputFile):
    with open(outputFile, 'w') as File:
        for path,dirs,files in os.walk(folderPath):
            for filename in files:
                File.write(os.path.join(path,filename) + "\n")

def firstLineOfFile(filenames):
    for f in filenames:
        if os.path.isfile(f):
            with open(f, 'r') as File:
                print(File.readline())

def emailOfFiles(filenames):
    for f in filenames:
        if os.path.isfile(f):
            with open(f, 'r') as File:
                for line in File:
                    if '@' in line:
                        print(line)

def printMDHeader(filenames):
    for f in filenames:
        if os.path.isfile(f):
            with open(f, 'r') as File:
                for line in File:
                    if line.startswith("#") and line[1] == " ":
                        print(line)