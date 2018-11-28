import sys
import re

for userInput in sys.stdin:
  print("Entered: " + userInput)

  userInput = re.sub('[\r\n]', '', userInput)

  print("Reversed: " + userInput[::-1] + '\n')
