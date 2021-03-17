import numpy as np
import math
data = [5,3,7]

data[0] = -5
data.extend([10])
data.insert(1, 16)
print(data)
data.remove(data[0])
print(sorted(data))
data = sorted(data)
negdata= []
for number in data:
    if number % 2 == 0:
        num = np.negative(number)
        negdata.append(num)


    else:
         negdata.append(number)

print(negdata)
print(sorted(negdata))
negativedata = np.negative(data.copy())
print(negativedata)
for number in data:
    length = len(data)
    dates = [ sum(data[0:x:1]) for x in range(1, length +1)]


print(dates)