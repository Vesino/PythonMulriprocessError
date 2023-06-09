import multiprocessing
import queue
import time


class CustomWorker(multiprocessing.Process):
    def __init__(self, model_queue, all_queued, stop_event):
        super().__init__(daemon=True)
        self.model_queue = model_queue
        self.all_queued = all_queued
        self.stop_event = stop_event
        self.processed_count = 0

    def run(self) -> None:
        while not self.all_queued.is_set() or not self.model_queue.empty():
            print("while waiting")
            while True:
                if self.stop_event.is_set():
                    return
                try:
                    if self.model_queue.empty():
                        break
                    print("Adding value 1 to worker")
                    self.processed_count += 1
                    return
                except queue.Empty:
                    break
                except Exception:
                    ...
            time.sleep(1)
