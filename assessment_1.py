import queue

queue = queue.Queue()
counter = 0

def generate_request():
    global counter
    
    new_request = f"Request {counter}"
    queue.put(new_request)
    counter += 1

def process_request():
    if not queue.empty():
        request = queue.get()
        print("Request processed:", request)
    else:
        print("Empty queue")

while True:
    user_input = input("Type 'add' to add request to queue or type 'quit' to quit: ")
    
    if user_input == "add":
        generate_request()
    elif user_input == "quit":
        break

    process_request()