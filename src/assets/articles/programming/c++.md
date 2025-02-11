## node constructor

```cpp
struct Node {
    int value;
    Node* next;
    Node(int value) : value(value), next(nullptr) {}
};
```
interpretation:
- `Node` is a struct with a constructor that takes an int value and sets the next pointer to nullptr
- `value` is an int
- `next` is a pointer to a Node(and * is used to indicate that it is a pointer(meaning it stores an address))

Leetcode Linked List problems:
- 142. Linked List Cycle II

code:
```cpp
First construct has a constructor that takes an int value and sets the next pointer to nullptr:
struct Node {
    int value;
    Node* next;
    Node(int value) : value(value), next(nullptr) {}};

ListNode* detectCycle(ListNode* head) {

}
```
we use floyd's cycle detection algorithm to detect the cycle in the linked list.(the basic idea is to have two pointers, one that moves one step at a time and the other that moves two steps at a time. If there is a cycle, the two pointers will meet at some point.)
the intuition to construct the algorithm:
- if there is a cycle, the fast pointer will eventually meet the slow pointer again.
- if there is no cycle, the fast pointer will reach the end of the list.

proof：图论考虑距离等价


尝试考虑等价的东西，很多东西换一种等价方式就可以更容易解决