from collections import deque

def is_palindrome(string):
    queue = deque()
    string = string.lower().replace(" ", "")

    for char in string:
        queue.append(char)

    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False

    return True

while True:
    input_string = input("Word input: ")
    if is_palindrome(input_string):
        print("It's palindrome")
    else:
        print("It's not palindrome")