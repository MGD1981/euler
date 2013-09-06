

def get_change(amount, denominations, coins_used=[]):
    combos = []
    if amount == 0:
        return [sorted(coins_used)]
    elif len(denominations) == 0:
        return []
    denominations = sorted(denominations)
    coin = denominations[-1]
    times_into_amount = int(amount/coin)
    for i in range (0, times_into_amount + 1):
        combos.extend(get_change(
            amount - (coin * i), denominations[:-1], coins_used + ([coin] * i)))
    return combos


if __name__ == '__main__':

    amount = float(raw_input("\nFor what amount do you need change?\n\n>>"))
    print "\nIn cents, what denominations of coins are available,",
    denominations = eval('['+str(raw_input("separated by commas?\n\n>> "))+']')
    for x in denominations:
        x = int(x)
    combos = get_change(int(amount), denominations)
    print "\nThere are %d combinations of coins.\n" % len(combos)
        
