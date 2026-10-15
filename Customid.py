#Store customer account IDs in a list
ids = [101, 205, 310, 415, 520]
# Take customer ID from the user
key = int(input("Enter Customer ID: "))
# ---------- Linear Search ----------
# Check whether the ID exists in the list
if key in ids:
  print("Linear Search: ID Found")
else:
  print("Linear Search: ID Not Found")
# ---------- Binary Search ----------
# Set the starting position
low = 0
# Set the ending position
high = len(ids) - 1
# Initially, ID is not found
found = False
# Continue searching while the range is valid
while low <= high:
# Find the middle position
  mid = (low + high) // 2
# Check if middle ID is the required ID
   if ids[mid] == key:
    found = True
    break
# If key is greater, search the right half
   elif ids[mid] < key:
    low = mid + 1
# If key is smaller, search the left half
   else:
    high = mid - 1
# Display Binary Search result
    if found:
      print("Binary Search: ID Found")
    else:
      print("Binary Search: ID Not Found")