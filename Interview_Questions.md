## 1. How to find the `middle element` of a linked list in one pass ?
Solution: Start with two pointer `p` and `q`. For every second iteration of `p`, iterate `q`. When `p` reaches the end of the linked list. `q` will be in the middle of the list.

## 2. How to find the `loop` or `cycle` in a linked list in one pass ?
Solution: Start with two pointer `p` and `q`. For every second iteration of `p`, iterate `q`. If `p` and `q` are pointing to the same node, there is a loop or cycle present.

## 3. How to find the `k th` element from the end of a linked list in one pass ?
Solution: Start with two pointer `p` and `q`. When the `p` pointer reahces upto the `k th` element, increment `q`.When `p` reaches the end of the list. `q` is ponting to the element 'k th' from the end.

## 4. List some real world applications of linked list ?
Solution:

*Image viewer* – Previous and next images are linked, hence can be accessed by next and previous button.

*Previous and next page in web browser* – We can access previous and next url searched in web browser by pressing back and next button since, they are linked as linked list.

*Music Player* – Songs in music player are linked to previous and next song. you can play songs either from starting or ending of the list.

## 5. What is a data structure ?

Solution: Data structure refers to the way data is organized and manipulated. It seeks to find ways to make data access more efficient. When dealing with the data structure, we not only focus on one piece of data but the different set of data and how they can relate to one another in an organized manner.

## 6. Explain the `LIFO` scheme.

Solution: LIFO is a short form of Last In First Out. It refers how data is accessed, stored and retrieved. Using this scheme, data that was stored last should be the one to be extracted first. This also means that in order to gain access to the first data, all the other data that was stored before this first data must first be retrieved and extracted.

## 7. What is merge sort ?

Solution: Merge sort, is a  divide-and-conquer approach for sorting the data. In a sequence of data, adjacent ones are merged and sorted to create bigger sorted lists. These sorted lists are then merged again to form an even bigger sorted list, which continues until you have one single sorted list.

## 8. What are the minimum number of queues to implement a prioriy queue ?

Solution: The minimum number of queues needed in this case is two. One queue is intended for sorting priorities while the other queue is used for actual storage of data.
