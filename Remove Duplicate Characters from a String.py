# Remove duplicate characters from a string

def remove_duplicates(s):
    result = ""
    
    for ch in s:
        if ch not in result:
            result += ch
    
    return result


# Input
string = "programming"

# Function call
output = remove_duplicates(string)

# Print result
print("String after removing duplicates:", output)
