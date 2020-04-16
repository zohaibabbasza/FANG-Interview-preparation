s = "anviaj"

# d = dict()
# p = []
# n = []
# i = 0

# while i != len(s):
#     print(d)
#     if s[i] in d:
#         d[s[i]] += 1
#         if len(p) > len(n) :
#             n = p
#             p = []
#             del d[s[i]]
#     else:
#         d[s[i]] = 1
#         p.append(s[i])
#     i+=1
# print(n)
# print(p)
# if len(n) <= len(p):
#     n = n + p
# print(len(set(n)))

#p = [a,n,v,i]

s = 'dvdf'
d = dict()
p = 0
n = 0
i = 0

while i != len(s):
    if s[i] in d:
        d[s[i]] += 1
        if p > n :
            n = p
        p = 0
        d = {}
    d[s[i]] = 1
    p += 1
    i+=1
    print(d)
    print('P:',p)

print(n)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode: 
        while l1 is not None:
            s = l1.val + l2.val
            if s < 10:
                l1.val = s
            else:
                l1.val = s % 10
                l1.next.val = l1.next.val + s / 10
            l1  = l1.next
            l2 = l2.next
        return l1



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode: 
        new_list = l1
        if l1.val == 0 and l1.next is None:
            return l2
        elif l2.val == 0 and l2.next is None:
            return l1
        while l1 is not None or l2 is not None:
            if l1 and l2:
                s = l1.val + l2.val
            elif l1:
                s = l1.val
            else:
                s = l2.val
            if s < 10:
                if l1:
                    l1.val = s
                else:
                    l1 = ListNode(s)
            else:
                if l1:
                    l1.val = s % 10
                else:
                    l1 = ListNode(s % 10)
                if l1.next:
                    l1.next.val = l1.next.val + s // 10
                else:
                    l1.next = ListNode(s // 10)
            if l1:
                l1  = l1.next
            if l2:
                l2 = l2.next

        return new_list

[9]
[1,9,9,9,9,9,8,9,9,9]
[0,0,0,0,0,0,9]