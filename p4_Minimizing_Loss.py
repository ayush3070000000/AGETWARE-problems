def minimize_loss(prices):
    min_loss = float('inf')
    buy_year = sell_year = -1
    n = len(prices)
    
    for i in range(n):
        for j in range(i + 1, n):
            if prices[j] < prices[i]: 
                loss = prices[i] - prices[j]
                if loss < min_loss:
                    min_loss = loss
                    buy_year = i + 1
                    sell_year = j + 1
                    
    return buy_year, sell_year, min_loss


def main():
    n = int(input("Enter the number of years: "))
    print("Enter the prices for each year separated by spaces:")
    prices = list(map(int, input().split()))
    
    if len(prices) != n:
        print("Error: Number of prices entered does not match number of years.")
        return
    
    buy, sell, loss = minimize_loss(prices)
    
    if buy == -1:
        print("No loss is possible (you can't sell at a lower price in future).")
    else:
        print(f"Buy in Year {buy}, Sell in Year {sell}, Loss = {loss}")


# Run the program
if __name__ == "__main__":
    main()
