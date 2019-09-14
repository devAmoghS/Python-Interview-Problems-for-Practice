## 1. How to find the `middle element` of a linked list in one pass
Solution: Start with two pointer `p` and `q`. For every second iteration of `p`, iterate `q`. When `p` reaches the end of the linked list. `q` will be in the middle of the list.

## 2. How to find the `loop` or `cycle` in a linked list in one pass
Solution: Start with two pointer `p` and `q`. For every second iteration of `p`, iterate `q`. If `p` and `q` are pointing to the same node, there is a loop or cycle present.

## 3. How to find the `k th` element from the end of a linked list in one pass
Solution: Start with two pointer `p` and `q`. When the `p` pointer reahces upto the `k th` element, increment `q`.When `p` reaches the end of the list. `q` is ponting to the element 'k th' from the end.

## 4. List some real world applications of linked list
Solution:

*Image viewer* – Previous and next images are linked, hence can be accessed by next and previous button.

*Previous and next page in web browser* – We can access previous and next url searched in web browser by pressing back and next button since, they are linked as linked list.

*Music Player* – Songs in music player are linked to previous and next song. you can play songs either from starting or ending of the list.
