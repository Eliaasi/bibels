import time

class Timer:
    def __init__(self):
        self._aika = None
        
    def start(self):
        self._aika = time.perf_counter()
            
    def stop(self):
        loppuaika = time.perf_counter() - self._aika
        self._aika = None
        print(f'Aikaa kului: {loppuaika:0.4f} sekuntia')