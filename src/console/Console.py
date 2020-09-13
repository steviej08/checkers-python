import threading
import time


class Console:

    @staticmethod
    def _quit_symbols():
        return ["q", "quit", "exit"]

    def __init__(self):
        self.active = True

        print("")
        print("To Quit at any point in the console type one of the following")

        for symbol in self._quit_symbols():
            print(symbol)

        print("")

    def start(self):
        worker_thread = threading.Thread(target=self._work_wrapper)
        worker_thread.start()

        while True:
            should_stop = not self.active or not worker_thread.is_alive()
            if should_stop:
                break

        if worker_thread.is_alive():
            worker_thread.join()
        print("Exiting console...")
        time.sleep(10)
        print("Exited.")

    def _work_wrapper(self):
        try:
            self.work()
        except Exception as exc:
            self.stop()
            raise exc

    def work(self):
        pass

    def stop(self):
        self.active = False

    def interact(self, display):
        result = input(display)

        self.active = result not in self._quit_symbols()

        return result

    def __del__(self):
        self.stop()
