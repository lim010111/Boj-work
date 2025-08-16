def bnp(cash, price_flow):
    stocks = 0
    for price in price_flow:
        stocks += cash // price
        cash %= price
        if cash == 0:
            break

    cash = cash + price_flow[-1] * stocks
    return cash
    

def timing(cash, price_flow):
    stocks = 0
    lower, higher = 0, 0
    for i in range(1, 14):
        if price_flow[i] < price_flow[i - 1]:
            lower += 1
            higher = 0
            if lower >= 3:
                stocks += cash // price_flow[i]
                cash %= price_flow[i]
        elif price_flow[i] > price_flow[i - 1]:
            higher += 1
            lower = 0
            if higher >= 3:
                cash += stocks * price_flow[i]
                stocks = 0

    cash = cash + price_flow[-1] * stocks
    return cash
        

if __name__ == "__main__":
    cash = int(input())
    price_flow = list(map(int, input().split()))
    bnp_price = bnp(cash, price_flow)
    timing_price = timing(cash, price_flow)

    if bnp_price > timing_price:
        print("BNP")
    elif timing_price > bnp_price:
        print("TIMING")
    else:
        print("SAMESAME")