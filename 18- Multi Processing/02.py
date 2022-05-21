import time
import multiprocessing

def abgosht(num):
    print(f"Abgosht #{num} Making Abgosht")
    print(f"Abgosht #{num} Getting the Ingredients ready.")
    print(f"Abgosht #{num} Leaving it to boil...")
    time.sleep(1)
    print(f"Abgosht #{num} Abgosht is ready!")


if __name__ == "__main__":

    start = time.time()

    p1 = multiprocessing.Process(target=abgosht, args=(1,))
    p2 = multiprocessing.Process(target=abgosht, args=(2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    
    end = time.time()
    
    print(f"Took: {round(end - start, 2)} second(s).")