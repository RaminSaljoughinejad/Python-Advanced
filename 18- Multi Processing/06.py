import time
import concurrent.futures
 
def abgosht(seconds):
    print(f"Abgosht #{seconds} Making Abgosht")
    print(f"Abgosht #{seconds} Getting the Ingredients ready.")
    print(f"Abgosht #{seconds} Leaving it to boil...")
    time.sleep(seconds)
    return f"Abgosht #{seconds} Abgosht is ready!"

if __name__ == "__main__":
    start = time.time()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        rsults = [executor.submit(abgosht, 2) for i in range(10)]
        
        for result in concurrent.futures.as_completed(rsults):
            print(result.result())

    end = time.time()
    print(f"Took: {round(end - start, 2)} second(s).")