def fillArray():
    return

def process(ratesUltimate, amount):
    valuesCurrent = [145, 234, 1267, 389, 190]

    sumCurrent = sum(valuesCurrent)
    print(sumCurrent)

    ratesCurrent = []

    for i in range(len(valuesCurrent)):
        currentRate = valuesCurrent[i]/sumCurrent
        ratesCurrent.append(currentRate)
        print(currentRate)

    if sum(ratesCurrent) != 1.0:
        exit()
    if len(valuesCurrent) != len(ratesCurrent):
        # fill the rest of short array with zeros
        fillArray()

    print(amount)



ratesUltimate = [0.2, 0.3, 0.1, 0.05, 0.35]

process(ratesUltimate, 1600)