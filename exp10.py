import re

# 1. Extract digits
s = input("Enter string: ")
print(re.findall(r'\d', s))

# 2. Words beginning with A or a
s = input("Enter sentence: ")
print(re.findall(r'\b[Aa]\w*\b', s))

# 3. Count vowels
s = input("Enter string: ")
print(len(re.findall(r'[aeiou]', s, re.I)))

# 4. Extract uppercase letters
s = input("Enter string: ")
print(re.findall(r'[A-Z]', s))

# 5. Identify spaces, tabs and newlines
s = input("Enter text: ")
print([repr(c) for c in re.findall(r'[ \t\n]', s)])

# 6. Replace multiple spaces
s = input("Enter sentence: ")
print(re.sub(r' {2,}', ' ', s))

# 7. Words of exactly five characters
s = input("Enter sentence: ")
print(re.findall(r'\b[A-Za-z]{5}\b', s))

# 8. Words ending with s
s = input("Enter sentence: ")
print(re.findall(r'\b\w+s\b', s, re.I))

# 9. Remove special characters
s = input("Enter string: ")
print(re.sub(r'[^A-Za-z0-9 ]', '', s))

# 10. Count words
s = input("Enter sentence: ")
print(len(re.findall(r'\b\w+\b', s)))

# 11. Validate mobile number
s = input("Enter mobile number: ")
print("Valid" if re.fullmatch(r'[6-9]\d{9}', s) else "Invalid")

# 12. Validate email
s = input("Enter email: ")
print("Valid" if re.fullmatch(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', s) else "Invalid")

# 13. Extract dates
s = input("Enter paragraph: ")
print(re.findall(r'\b(?:0[1-9]|[12]\d|3[01])-(?:0[1-9]|1[0-2])-\d{4}\b', s))

# 14. Extract URLs
s = input("Enter text: ")
print(re.findall(r'https?://[^\s]+', s))

# 15. Extract hashtags
s = input("Enter post: ")
print(re.findall(r'#[A-Za-z0-9_]+', s))

# 16. Validate password
s = input("Enter password: ")
p = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}'
print("Valid" if re.fullmatch(p, s) else "Invalid")

# 17. Find repeated consecutive words
s = input("Enter sentence: ")
print(re.findall(r'\b(\w+)\s+\1\b', s, re.I))

# 18. Extract PIN codes
s = input("Enter paragraph: ")
print(re.findall(r'\b[1-9]\d{5}\b', s))

# 19. Validate vehicle number
s = input("Enter vehicle number: ").upper()
print("Valid" if re.fullmatch(r'[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}', s) else "Invalid")

# 20. Extract file extensions
s = input("Enter filenames: ")
print(re.findall(r'\b[\w.-]+\.(\w+)\b', s))

# 21. Remove HTML tags, spaces and punctuation
s = input("Enter text: ")
s = re.sub(r'<[^>]*>', ' ', s)
s = re.sub(r'[^\w\s]', '', s)
print(re.sub(r'\s+', ' ', s).strip())

# 22. Extract invoice numbers, dates and amounts
s = input("Enter invoice text: ")
print("Invoice:", re.findall(r'Invoice\s*(?:No\.?|Number|#)\s*[:\-]?\s*([A-Z0-9/-]+)', s, re.I))
print("Dates:", re.findall(r'\b\d{2}-\d{2}-\d{4}\b', s))
print("Amounts:", re.findall(r'(?:₹|Rs\.?|INR)\s*[\d,]+(?:\.\d{2})?', s, re.I))

# 23. Identify single-line comments
s = input("Enter Python source code: ")
print(re.findall(r'(?m)#.*$', s))

# 24. Validate product code
s = input("Enter product code: ")
print("Valid" if re.fullmatch(r'[A-Z]{3}-\d{4}-[A-Z]{2}', s) else "Invalid")

# 25. Extract student records
s = input("Enter record (
