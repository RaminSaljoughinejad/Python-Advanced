import time
import multiprocessing

def abgosht(seconds):
    print(f"Abgosht #{seconds} Making Abgosht")
    print(f"Abgosht #{seconds} Getting the Ingredients ready.")
    print(f"Abgosht #{seconds} Leaving it to boil...")
    time.sleep(seconds)
    print(f"Abgosht #{seconds} Abgosht is ready!")


if __name__ == "__main__":

    start = time.time()


    processes = []
    for i in range(10):
        p = multiprocessing.Process(target=abgosht, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    
    end = time.time()
    
    print(f"Took: {round(end - start, 2)} second(s).")