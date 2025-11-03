paragraph = """
    Python is a popular programming language. 
    This Python course helps beginners learn coding concepts easily.
"""

length = len(paragraph)
print("Length of paragraph:", length)

print("First character:", paragraph[0])
print("Last character:", paragraph[-1])

preview = paragraph[:50]
print("Preview (first 50 chars):", preview)

updated_paragraph = paragraph.replace("Python", "PYTHON")
print("\nAfter replacement:\n", updated_paragraph)

lower_paragraph = updated_paragraph.lower()
print("\nIn lowercase:\n", lower_paragraph)

clean_paragraph = lower_paragraph.strip()
print("\nAfter stripping whitespaces:\n", clean_paragraph)

words = clean_paragraph.split()
print("\nList of words:", words)

if "course" in words:
    print("\nThe word 'course' is found in the paragraph.")
else:
    print("\nThe word 'course' is NOT found in the paragraph.")
final_message = "The course description is {} characters long and has {} words.".format(len(clean_paragraph), len(words))
print("\n" + final_message)
