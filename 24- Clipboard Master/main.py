import clipboard
import keyboard
import time
from my_stack import CStack
from my_queue import CQueue

def greetings():
    print("Welcome to Clipboard Master ---> ver1.0")

def get_memory_type():
    while True:
        try:
            memory_type = input("What type of memory do you want to use?[stack\queue]: ")
            if memory_type.lower() == "stack" or memory_type.lower() == "queue":
                if memory_type.lower() == "stack":
                    print("Stacking...")
                    memory = CStack()
                    memory_label = "stack"
                else:
                    print("Queueing...")
                    memory = CQueue()
                    memory_label = "queue"
                break
            else:
                raise Exception("Wrong Input")
        except:
            print("WRONG INPUT: Please The instruction carefully and enter your input again.")
            print("If you want to exit the program press Ctrl+c")
            continue
    return memory, memory_label

def get_text():
    global memory
    global memory_label
    global pasting

    time.sleep(0.05)
    memory_handler(val=clipboard.paste())
    clipboard.copy(memory.atfront())
    pasting = False

def set_text():
    global memory
    global memory_label
    global pasting

    if len(memory) == 0:
        clipboard.copy("")
    else:
        if not pasting:
            memory_handler()
            pasting = True
        clipboard.copy(memory_handler())


def memory_handler(val=None):
    if val!=None:
        if memory_label=="stack":
            memory.push(val)
        else:
            memory.enqueue(val)
    else:
        if memory_label=="stack":
            return memory.pop()
        else:
            return memory.dequeue()

if __name__ == "__main__":

    greetings()
    memory, memory_label = get_memory_type()
    pasting = False
    

    keyboard.add_hotkey("ctrl+c", get_text)
    keyboard.add_hotkey("ctrl+v", set_text)

    input("")
    