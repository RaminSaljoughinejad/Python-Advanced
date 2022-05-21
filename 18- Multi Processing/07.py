import time
import concurrent.futures
from unittest import result
 
def abgosht(seconds):
    print(f"Abgosht #{seconds} Making Abgosht")
    print(f"Abgosht #{seconds} Getting the Ingredients ready.")
    print(f"Abgosht #{seconds} Leaving it to boil...")
    time.sleep(seconds)
    return f"Abgosht #{seconds} Abgosht is ready!"

if __name__ == "__main__":
    start = time.time()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(abgosht, range(1,5))
        for result in results:
            print(result)

    end = time.time()
    print(f"Took: {round(end - start, 2)} second(s).")


#increase it by one!