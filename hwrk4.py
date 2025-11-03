web_dev = ["Rahul", "Sneha", "Amit"]
data_science = ["Neha", "Vikram", "Kiran"]
uiux_design = ["Priya", "Arjun", "Meena"]

all_participants = [web_dev, data_science, uiux_design]

web_dev.append("Divya")

data_science.insert(1, "Ravi")

uiux_design.pop()

copied_data_science = data_science.copy()
data_science.clear()
print("First two Web Development participants:", web_dev[:2])

name_lengths = [len(name) for name in copied_data_science]
print("Lengths of names in copied Data Science list:", name_lengths)


is_asha_present = any("Asha" in workshop for workshop in all_participants)
print("Is 'Asha' in any workshop list?", is_asha_present)

first_participants = (web_dev[0], copied_data_science[0], uiux_design[0])
print("Tuple of first participants:", first_participants)

print("\nAll participants (nested list):", all_participants)
print("Copied Data Science list:", copied_data_science)
print("Cleared original Data Science list:", data_science)
