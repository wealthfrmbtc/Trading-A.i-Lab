def calculate_pnl(entry, exit, shares, leverage=1):
    price_change = exit - entry
    raw_pl = price_change * shares
    leveraged_pl = raw_pl * leverage
    
    invested_capital = entry * shares
    pct_return = (leveraged_pl / invested_capital) * 100

    return {
        'price_change': price_change,
        'raw_pl': raw_pl,
        'leveraged_pl': leveraged_pl,
        'pct_return': pct_return
    }


if __name__ == '__main__':
    result = calculate_pnl(50120, 49960, 0.05, 3)
print(result)    