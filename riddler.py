import re
from functools import reduce

class RiddleSolver():

    def __init__(self):
        self.asciiToTextRegEx = re.compile('32|44|[1][0-9][0-9]|[6789][0-9]')
        self.hexToTextRegex = re.compile('[0-9a-f]{2}')

    def asciiToText(self, value):
        matches = self.asciiToTextRegEx.findall(value)
        chars = list(map(lambda x: chr(int(x)), matches))
        return ''.join(chars)

    def hexToText(self, value):
        matches = self.hexToTextRegex.findall(value)
        chars = list(map(lambda x: chr(int(x, 16)), matches))
        return ''.join(chars)

    def total(self, value):
        return reduce((lambda x, y: int(x) + int(y)), list(value))

riddle = '86111105991011081011151153210511632991141051011154432871051101031081011151153210210811711611610111411544328411111111610410810111511532981051161011154432771111171161041081011151153210911711611610111411546'
hint = '5468652073756d2074686520746f74616c206f66207468652061736369692076616c7565732066726f6d2065616368206c657474657220696e2074686520616e7377657220746f2074686520726964646c652e'
answer = '507473543466548535531534555466536545548466531466546538545544535466549533548535535544467'

riddler = RiddleSolver()

print('Riddle:')
print(riddler.asciiToText(riddle))
print('')

print('Hint:')
print(riddler.hexToText(hint))
print('')

print('Answer:')
print('wind')
print('')

total = riddler.total(answer)

print('Notes:')
print('1. According to the hint the total from the answer code is {}.'.format(total))
print('2. However the total for the actual answer "wind" is 434')
print('3. The English for the hint text is incorrect English.  Is this intentional?')
print('4. Is the incorrect English in the hint indicative that the answer total is incorrect?')
