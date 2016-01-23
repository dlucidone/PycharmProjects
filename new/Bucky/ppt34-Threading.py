import threading


class BuckyMessenger(threading.Thread):
    def run(self):
        for _ in range(500):
            print(threading.current_thread().getName())

x = BuckyMessenger(name='Send Message')
y = BuckyMessenger(name='Receive Message')

x.start()
y.start()