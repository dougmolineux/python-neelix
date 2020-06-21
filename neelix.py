import logging
import os
import json
from pathlib import Path

def getFiles(path):
  return os.listdir(path)

def readFile(file_path):
  return Path(file_path).read_text()

def parse(text, path):
    try:
      parsedJson = json.loads(text)
      return True
    except ValueError as e:
      print('FAIL \n\t', e)
      return False

def main(path):
  files = getFiles(path)
  invalidJsons = 0

  for idx, file in enumerate(files, start=1):
    filename, file_extension = os.path.splitext(file)

    if file_extension == '.json':
      fullFilePath = path + '/' + file
      print('Checking: ', fullFilePath, end ="... ")
      json = readFile(fullFilePath)
      if not parse(json, fullFilePath):
        invalidJsons += 1
      else:
        print("SUCCESS")

    if idx == len(files):
      print(idx, "files checked.")
      if invalidJsons > 0:
        print(invalidJsons, "Invalid Jsons found.")
      else:
        print("Success! No invalid JSONs found.")

main('tests')
