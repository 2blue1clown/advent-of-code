def extractCalibration(s):
    out = ''
    for i in range(len(s)):
        num = getNumber(i,s)
        if num:
            out = out+str(num)
            break;
    for j in range(len(s)):
        num = getNumber(len(s)-1 - j,s)
        if num:
            out += str(num)
            break; 
    print(f"Extracted {out} from {s}")
    return out

numbers = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"zero":0}

def getNumber(i,s):
    possibleNumbers = ["one","two","three","four","five","six","seven","eight","nine","zero"]
    if s[i].isnumeric():
        return int(s[i])
    else:
        word = ''
        while len(possibleNumbers) > 0 and i < len(s):
            word += s[i]
            i+= 1
            if word in possibleNumbers:
                return numbers[word]
            else:
                possibleNumbers = list(filter(lambda x: x.startswith(word),possibleNumbers))
        return None
        
calibrationValues = []    


with open('./day1/input.txt', 'r',encoding='utf-8') as f:
    for line in f:
        calibrationValues.append(int(extractCalibration(line)))

print(calibrationValues)
print(sum(calibrationValues))


