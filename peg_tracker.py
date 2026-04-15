def get_coin_id(symbol):
    mapping = {
        "USDC": "usd-coin",
        "USDT": "tether",
        "DAI": "dai"
    }
    return mapping.get(symbol)


def calculate_peg_deviation(price, peg=1.0):
    return ((price - peg) / peg) * 100


def classify_peg_status(deviation):
    if deviation > 0.5:
        return "Above peg"
    elif deviation < -0.5:
        return "Below peg"
    else:
        return "On peg"

import requests


def fetch_coin_data(coin_id):
    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": coin_id,
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }

    response = requests.get(url, params=params)
    data = response.json()

    price = data[coin_id]["usd"]
    change_24h = data[coin_id]["usd_24h_change"]

    return price, change_24h


def format_output(symbol, price, change_24h, deviation, status):
    return (
        f"{symbol} | Price: ${price:.4f} | "
        f"24h: {change_24h:.2f}% | "
        f"Deviation: {deviation:.2f}% | "
        f"Status: {status}"
    )


def main():
    symbols = ["USDC", "USDT", "DAI"]

    for symbol in symbols:
        coin_id = get_coin_id(symbol)
        price, change_24h = fetch_coin_data(coin_id)
        deviation = calculate_peg_deviation(price)
        status = classify_peg_status(deviation)

        output = format_output(symbol, price, change_24h, deviation, status)
        print(output)


if __name__ == "__main__":
    main()
