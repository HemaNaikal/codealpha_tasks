# ============================================
# TASK 2: Stock Portfolio Tracker
# Author: Hema
# Description: Calculates total investment based
#              on manually defined stock prices.
# ============================================

import csv
import os

# Hardcoded stock price dictionary (price per share in USD)
STOCK_PRICES = {
    "APPLE": 180,
    "TESLA": 250,
    "GOOGLE": 140,
    "AMAZON": 185,
    "MICROSOFT": 420,
    "INFOSYS": 18,
    "TCS": 45,
    "RELIANCE": 30
}

def display_available_stocks():
    """Display all available stocks and their prices."""
    print("\n" + "=" * 40)
    print("   AVAILABLE STOCKS & PRICES")
    print("=" * 40)
    print(f"{'Stock':<12} {'Price (USD)':>12}")
    print("-" * 40)
    for stock, price in STOCK_PRICES.items():
        print(f"{stock:<12} ${price:>11}")
    print("=" * 40)

def get_portfolio_input():
    """Get stock names and quantities from the user."""
    portfolio = {}
    print("\nEnter your stock holdings (type 'done' to finish):")

    while True:
        stock = input("\nEnter stock name (e.g., AAPL): ").strip().upper()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print(f"  ❌ '{stock}' not found. Available: {', '.join(STOCK_PRICES.keys())}")
            continue

        try:
            qty = int(input(f"  Enter quantity for {stock}: ").strip())
            if qty <= 0:
                print("  ❌ Quantity must be a positive number.")
                continue
            portfolio[stock] = portfolio.get(stock, 0) + qty
            print(f"  ✅ Added {qty} shares of {stock}")
        except ValueError:
            print("  ❌ Invalid quantity. Please enter a whole number.")

    return portfolio

def calculate_investment(portfolio):
    """Calculate individual and total investment values."""
    results = []
    total = 0

    for stock, qty in portfolio.items():
        price = STOCK_PRICES[stock]
        value = price * qty
        total += value
        results.append({
            "Stock": stock,
            "Quantity": qty,
            "Price (USD)": price,
            "Value (USD)": value
        })

    return results, total

def display_results(results, total):
    """Display the portfolio summary on screen."""
    print("\n" + "=" * 55)
    print("          📊 PORTFOLIO SUMMARY")
    print("=" * 55)
    print(f"{'Stock':<10} {'Qty':>6} {'Price':>10} {'Value':>14}")
    print("-" * 55)
    for row in results:
        print(f"{row['Stock']:<10} {row['Quantity']:>6} ${row['Price (USD)']:>9} ${row['Value (USD)']:>13,}")
    print("=" * 55)
    print(f"{'TOTAL INVESTMENT':>40}  ${total:>13,}")
    print("=" * 55)

def save_results(results, total):
    """Ask user if they want to save results as .txt or .csv."""
    print("\nWould you like to save the results?")
    print("  1. Save as .txt")
    print("  2. Save as .csv")
    print("  3. No, skip saving")
    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "1":
        filename = "portfolio_result.txt"
        with open(filename, "w") as f:
            f.write("STOCK PORTFOLIO TRACKER - RESULTS\n")
            f.write("=" * 50 + "\n")
            f.write(f"{'Stock':<10} {'Qty':>6} {'Price':>10} {'Value':>14}\n")
            f.write("-" * 50 + "\n")
            for row in results:
                f.write(f"{row['Stock']:<10} {row['Quantity']:>6} ${row['Price (USD)']:>9} ${row['Value (USD)']:>13,}\n")
            f.write("=" * 50 + "\n")
            f.write(f"TOTAL INVESTMENT: ${total:,}\n")
        print(f"  ✅ Results saved to '{filename}'")

    elif choice == "2":
        filename = "portfolio_result.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["Stock", "Quantity", "Price (USD)", "Value (USD)"])
            writer.writeheader()
            writer.writerows(results)
            writer.writerow({"Stock": "TOTAL", "Quantity": "", "Price (USD)": "", "Value (USD)": total})
        print(f"  ✅ Results saved to '{filename}'")

    else:
        print("  Skipped saving.")

def main():
    print("\n" + "=" * 40)
    print("   💹 STOCK PORTFOLIO TRACKER")
    print("=" * 40)

    display_available_stocks()

    portfolio = get_portfolio_input()

    if not portfolio:
        print("\n⚠️  No stocks entered. Exiting.")
        return

    results, total = calculate_investment(portfolio)
    display_results(results, total)
    save_results(results, total)

    print("\n👋 Thank you for using Stock Portfolio Tracker!\n")

if __name__ == "__main__":
    main()
