import time
from concurrent.futures import ProcessPoolExecutor, as_completed


# Декоратор для измерения времени выполнения функции
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения {func.__name__}: {end_time - start_time:.5f} секунд")
        return result

    return wrapper


# Пример IO-bound задачи: имитация задержки (например, запрос к серверу)
def io_bound_task():
    time.sleep(2)  # Имитируем задержку 2 секунды
    return "IO-bound task completed"


# Пример CPU-bound задачи: вычисления с использованием математических операций
def cpu_bound_task():
    result = 0
    for i in range(1, 100_000_000):
        result += 1
    return


@measure_time
def run_multiple_io_tasks():
    with ProcessPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(io_bound_task) for _ in range(5)]
        for future in as_completed(futures):
            future.result()  # Ожидаем завершения задачи


@measure_time
def run_multiple_cpu_tasks():
    with ProcessPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(cpu_bound_task) for _ in range(5)]
        for future in as_completed(futures):
            future.result()  # Ожидаем завершения задачи


if __name__ == "__main__":
    # Измеряем время для 5 CPU-bound задач
    run_multiple_cpu_tasks()

    # Измеряем время для 5 IO-bound задач
    run_multiple_io_tasks()
