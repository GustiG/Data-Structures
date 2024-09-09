"""
Practice - Josephus Problem from codechef.com
You need to solve the famous Josephus problem using circular linked list in this section.

There are N people standing in a circle like 1->2->3...->N->1 and there is a knife. Whoever has the knife kills the person next to them and hands over the knife, i.e., if 2 has the knife in 1->2->3->1 then 2 kills 3 and hands over the knife to 1. This process continues until there is only one person left, i.e., there is no one left to kill. This last person is deemed as the winner. Initially the knife is with person 1.

For a given N, you need to determine the winner.

Note - You are given a circular linked list containing elements from 1 to N with head initially at 1. In the solution function, you need to output a single integer denoting the winner.
Do not make changes anywhere except the solveJosephus() function.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases. The description of the test cases follows.
The first and only line of each test case contains a single integer 
N
N, denoting the number of people
Output Format
For each test case, output on a new line the winner of that game.


Explanation:
For n=5, the moves are as followed (the person in bracket holds the knife):
(1)->2->3->4->5->1 = (1 kills 2 and hands knife to 3)
1->(3)->4->5->1 = (3 kills 4 and hands knife to 5)
1->3->(5)->1 = (5 kills 1 and hands knife to 3)
(3)->5 = (3 kills 5 and is the only person left)

Therefore, 3 is the winner.
"""
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtEnd(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self.tail.next = self.head

    def solveJosephus(self):
        # Complete this function
        current = self.head
        
        while current.next != current:
            knife_pass = current.next.next
            if current.next == self.head:
                self.head = knife_pass
            
            current.next = knife_pass
            current = current.next
        return current.value

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())

        ll = LinkedList()
        for i in range(1, n + 1):
            ll.insertAtEnd(i)
        print(ll.solveJosephus())

