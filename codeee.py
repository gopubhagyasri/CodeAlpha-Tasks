import re

# Read input file
with open("input.txt", "r") as file:
    text = file.read()

# Extract emails using regex
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

# Save emails to output file
with open("emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Emails extracted successfully!")

print("\nExtracted Emails:")
for email in emails:
    print(email)