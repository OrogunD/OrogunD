

with open('input.txt', 'r') as textfile:
    data = textfile.read()

def marker_detector (data, size):
    ts = len(data) #ts: text size
    for i in range(ts - size + 1): 
        s = set(data[i:i + size])
        if len(s) == size:
            return i + size

print ('Amount of marker :' + str(marker_detector(data,4)))

print ('Amount of marker :' + str(marker_detector(data,14)))