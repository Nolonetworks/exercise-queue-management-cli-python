import json
from DataStructures import Queue
from sms import send

# there queue has to be declared globally (outside any other function)
# that way all methods have access to it
queue = Queue(mode="FIFO")
    
def print_queue():
    # you must print on the console the entire queue list
    print("Printing the entire list...")
    print(queue.get_queue())

def add(cliente):
    queue.enqueue(cliente)
    size=queue.size()-1
    print('Tienes ',size,'personas antes')
    mensaje='Bienvenido, tiene ' , str(size) ,' personas antes'
    send(mensaje)

def dequeue():
    turno1=queue.get_queue()[0]
    queue.dequeue()
    turno2=queue.get_queue()[0]
    mensaje='Gracias por venir ' + turno1 + ', por favor' + turno2 + 'pase adelante.'
    send(mensaje)

def save():
    queue.save_queue()

def load():
    queue.load_queue()
        
      
print("\nHello, this is the Command Line Interface for a Queue Managment application.")
stop = False
while stop == False:
    
    print('''
What would you like to do (type a number and press Enter)?
- Type 1: For adding someone to the Queue.
- Type 2: For removing someone from the Queue.
- Type 3: For printing the current Queue state.
- Type 4: To export the queue to the queue.json file.
- Type 5: To import the queue from the queue.json file.
- Type 6: To quit
    ''')


    option = int(input("Enter a number:"))
    # add your options here using conditionals (if)
    if option == 3:
        print_queue()
    elif option == 6:
        print("Bye bye!")
        stop = True
    elif option == 1:
        print('Hola, ingrese sun nombre: ')
        cliente=input()
        print(cliente)
        add(cliente)
    elif option == 2:
        dequeue()
    elif option == 4:
        save()
    elif option == 5:
        load()
    else:
        print("Invalid option "+str(option))
