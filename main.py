expenses = [
    {"category": "Food", "amount": 25.50},
    {"category": "Transport", "amount": 12.00},
    {"category": "Food", "amount": 40.00},
    {"category": "Entertainment", "amount": 15.00},
    {"category": "Utilities", "amount": 60.00},
]


def calculate_total(expenses_list):
    return sum(item["amount"] for item in expenses_list)


def category_breakdown(expenses_list):
    breakdown = {}
    for item in expenses_list:
        cat = item["category"]
        breakdown[cat] = breakdown.get(cat, 0) + item["amount"]
    return breakdown


def main():
    print("--- Personal Finance Summary ---")
    total = calculate_total(expenses)
    print(f"Total Spent: ${total:.2f}\n")

    print("Breakdown by Category:")
    breakdown = category_breakdown(expenses)
    for category, amount in breakdown.items():
        print(f"  - {category}: ${amount:.2f}")


if __name__ == "__main__":
    main()