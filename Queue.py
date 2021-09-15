# Queue Data Structure
'''
Que Operations:-
1. Enqueue()
2. Dequeue()
3. isEmpty()
'''

Queue = []

def enqueue(queue, num, a):
    Queue.append(num)

def dequeue(queue):
    if isempty():
        print("Queue is empty")
    else:
        Queue.pop(0)

def isempty():
    if Queue:
        return False
    else:
        return True


enqueue(Queue,1)
print(Queue)
enqueue(Queue,2)
print(Queue)
enqueue(Queue,3)
print(Queue)
enqueue(Queue,4)
print(Queue)


dequeue(Queue)
print(Queue)
dequeue(Queue)
print(Queue)
dequeue(Queue)
print(Queue)
dequeue(Queue)
print(Queue)
dequeue(Queue)
print(Queue)
dequeue(Queue)
print(Queue)
dequeue(Queue)



print("Hello")