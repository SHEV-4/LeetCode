# Add Two Numbers
# 29.10.2025
# 6ms 36.65%
# 17.98mb 35.31%
# Solution 1
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result:Optional[ListNode] = None
        
        current = None
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            node = ListNode(total%10)
            carry = total // 10
            if result is None:
                result = node
                current = node
            else:
                current.next = node
                current = node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return result
# 29.10.2025
# 4ms 54.58%
# 17.58mb 99.77%
# Solution 2
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        text1,text2 = "",""
        num1,num2 = 0,0
        result:Optional[ListNode] = None
        current = None
        while l1:
            text1 += str(l1.val)
            l1 = l1.next

        while l2:
            text2 += str(l2.val)
            l2 = l2.next
        
        num1 = int(text1[::-1])
        num2 = int(text2[::-1])

        text_result = str(num1 + num2)


        for el in text_result[::-1]:
            node = ListNode(int(el))
            if result is None:
                result = node
                current = node
            else:
                current.next = node
                current = node

        return result
