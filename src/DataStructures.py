import json

class Queue:

    def __init__(self, mode, current_queue=[]):
        self._queue = current_queue
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        if mode is None:
            raise "Please specify a queue mode FIFO or LIFO"
        else:
            self._mode = mode
    
    def enqueue(self, item):
        if self._mode=='FIFO':
            self._queue.append(item)
        else:
            self._queue.insert(0,item)
    def dequeue(self):
        self._queue.pop(0)

    def get_queue(self):
        return self._queue

    def size(self):
        return len(self._queue)

    def save_queue(self):
        if "FIFO" in self._mode:
                with open('clientesFIFO.json', 'w') as file:
                    json.dump(self._queue, file)
                print('\n Archivo creado ---> '+'clientesFIFO.json')

    def load_queue(self):
        if "FIFO" in self._mode:
            self._queue=[]
            with open('clientesFIFO.json') as file:
                self._queue = json.load(file)
                print(self._queue)
                print('\n Archivo CARGADO FIFO---> '+'clientesFIFO.json')