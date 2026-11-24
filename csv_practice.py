import csv

# Exercise 2: Read and print raw rows
# Exercise 3: Skip the header
# Exercise 4: Compute totals
# Exercise 5: Filter and write
# Exercise 6: Use csv.DictReader

total_revenue = 0
original_count = 0
cleaned_count = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    with open("data/cleaned.csv", "w", newline="") as output_file:
        writer = csv.writer(output_file)

        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            original_count += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])

            total = price * quantity
            total_revenue += total

            print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

            if total > 100:
                writer.writerow([product, price, quantity, total])
                cleaned_count += 1

print(f"\nTotal revenue: ${total_revenue:.2f}")
print(f"Original rows: {original_count}")
print(f"Cleaned rows: {cleaned_count}")

# Exercise 6: Read using csv.DictReader

# csv.reader accesses columns using their positions.
# DictReader accesses columns using their header names.

dict_total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        dict_total_revenue += total

        print(row["product"], total)

print(f"\nDictReader total revenue: ${dict_total_revenue:.2f}")
# Exercise 8: Append mode log

from datetime import datetime

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("data/run_log.txt", "a") as log_file:
    log_file.write(f"{current_time} - Total Revenue: ${total_revenue:.2f}\n")

print("\nLog file updated successfully!")