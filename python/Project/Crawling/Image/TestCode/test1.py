
result_1 = []
for number in range(30):
    result_1.append(number)

print(result_1)

result_2 = []
for number in range(30):
    if number < 10:
        result_2.append(format("00%d" % (number)))
    else :
        result_2.append(format("0%d" % (number)))

print(result_2)
