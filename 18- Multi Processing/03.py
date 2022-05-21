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


    processes = []
    for i in range(10):
        p = multiprocessing.Process(target=abgosht, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    
    end = time.time()
    
    print(f"Took: {round(end - start, 2)} second(s).")