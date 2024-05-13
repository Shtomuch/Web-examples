import multiprocessing
import time


def factorize(*number):
    result = []
    for i in number:
        divisors = []
        for j in range(1, i + 1):
            if i % j == 0:
                divisors.append(j)
        result.append(divisors)
    return result

def main():
    input_staff = input("Enter the choise 1 or 2 of the file: ")

    match input_staff:
        case "1":
            start_time = time.perf_counter()
            factorize(128, 255, 99999, 10651060, 21312321, 123324)
            end_time = time.perf_counter()
            print(f"Час виконання: {end_time - start_time} секунд")
        case "2":
            with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
                start_time = time.perf_counter()
                pool.map(factorize, [128, 255, 99999, 10651060, 21312321, 123324])
                end_time = time.perf_counter()
                print(f"Час виконання: {end_time - start_time} секунд")
        case _:
            print("Unknown choise")

if __name__ == "__main__":
    main()