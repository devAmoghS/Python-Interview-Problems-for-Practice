## 1. How to find the middle element of a linked list
Solution: Start with two pointer `p` and `q`. For every second iteration of `p`, iterate `q`. When `p` reaches the end of the linked list. `q` will be in the middle of the list.

## 2. How to find the loop or cycle in a linked list
Solution: Start with two pointer `p` and `q`. For every second iteration of `p`, iterate `q`. If `p` and `q` are pointing to the same node, there is a loop or cycle present.
