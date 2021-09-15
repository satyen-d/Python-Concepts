# Stack Data Structure
'''
Stack Operations:-
1. Push()
2. Pop()
3. isEmpty()

'''

stack = []

def push(stack, a):
    stack.append(a)

def pop(stack):
    if isEmpty():
        print("Stack is empty")
    else:
        stack.pop()

def isEmpty():
    if stack:
        return False
    else:
        return True


push(stack,2)
print(stack)
push(stack,3)
print(stack)
push(stack,4)
print(stack)
push(stack,5)
print(stack)
push(stack,6)

pop(stack)
print(stack)
pop(stack)
print(stack)
pop(stack)
print(stack)
pop(stack)
print(stack)
pop(stack)
print(stack)
pop(stack)
print(stack)
pop(stack)
print(stack)
pop(stack)
print(stack)
pop(stack)
