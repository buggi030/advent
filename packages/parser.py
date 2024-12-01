import os
import re

def readData(filename):
    data = []
    with open(os.getcwd() + f'/inputs/{filename}', 'r') as f:
        data = f.readlines()
    return data

def ints(input: str) -> list[int]:
  return [int(match) for match in re.findall(r"-?\d+", input)]

def digits(input: str) -> list[int]:
  return [int(match) for match in re.findall(r"\d", input)]
