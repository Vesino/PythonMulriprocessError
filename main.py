import multiprocessing

from analysis_worker import CustomWorker


def run_parallel():
    all_queue = multiprocessing.Event()
    all_processed = multiprocessing.Event()
    stop_event = multiprocessing.Event()
    model_queue = multiprocessing.Queue()

    workers = [CustomWorker(model_queue, all_queue, stop_event)]

    try:
        print("iniciando workers")
        for worker in workers:
            worker.start()

        for i in [0]:
            model_queue.put(i)
        print("queue completa")
        all_queue.set()

        for worker in workers:
            worker.join()

            """
            # this variable will never update
            is related to how multiprocessing works in Python. 
            Each process runs in its own memory space, and any 
            changes made to variables within a process do not 
            reflect in the parent process.
            """
            print(f'{worker.processed_count=}')

        all_processed.set()

    finally:
        stop_event.set()
        print("Finalizacion del programa")


if __name__ == '__main__':
    run_parallel()
