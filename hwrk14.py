import random
import math

names_input = input("Enter the names of customers who placed orders today (comma-separated): ")
names_list = [name.strip() for name in names_input.split(",")]
unique_names = list(set(names_list))
random.shuffle(unique_names)

if len(unique_names) < 2:
    print("\nNot enough participants for 2 winners!")
else:
    winner1, winner2 = random.sample(unique_names, 2)
    rev_winner1 = winner1[::-1]
    rev_winner2 = winner2[::-1]

    total = len(unique_names)
    sqrt_round = round(math.sqrt(total))
    print("\n--- Lucky Draw Results ---")
    print(f"Unique Participants: {unique_names}")
    print(f"Total number of unique participants: {total}")
    print(f"Rounded square root of participants: {sqrt_round}")
    print(f"Winner 1: {winner1} → Reversed: {rev_winner1}")
    print(f"Winner 2: {winner2} → Reversed: {rev_winner2}")
