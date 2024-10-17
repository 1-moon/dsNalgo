# what is has_loop in linked list ?

This method is to detect if there is a cycle or loop present in the linked list

## Method

In order to detect the loop in LL, you are required to use Floyd's cycle-finding algorithm.
(also known as the "tortoise and the hare" algorithm).

## Key

- This algorithm uses two pointers

1. a slow pointer, which moves one step at a time
2. a fast pointer, which moves two steps at a time

- If there is a loop in the LL, the two ptrs will eventually meet at some point.
- If there is no loop, the fast pointer will reach the end of the list.

### Consideration

If your LL contains a loop, it indicates a flaw in its implementation.
This situation can manifest in several ways.
![situation_1](https://github.com/user-attachments/assets/04d27a15-4e98-4ac2-bddc-415e651be1b1)
![situation_2](https://github.com/user-attachments/assets/2d750a04-9922-4c81-9b63-0224735c84eb)
![situation_3](https://github.com/user-attachments/assets/bd4d73bc-5d3c-4ad8-b19f-f9dcd5fd2a3e)
