
def check_palindrome(string):
    if string == string[::-1]:
        return f"Given string is palindrome"
    return f"Given string is not palindrome"

s = "Subin"
print(check_palindrome(s))


lst = [1, 2, 3, 3, 4]
lst.append(5)
print(lst)

tpl = (1, 2, 3, 4)
print(tpl)

#unique element
set = {1, 2, 4, 4, 5}
set.add(6)
print(set)