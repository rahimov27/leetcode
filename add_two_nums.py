# def adding_two_nums(number1, number2):
#     number1_list = []
#     number2_list = []
#     for i in str(number1):
#         number1_list.insert(-0, i)
#     for e in str(number2):
#         number2_list.insert(-0, e)
#     print(number1_list)
#     print(number2_list)
#     fullnum1 = "".join(number1_list)
#     fullnum2 = "".join(number2_list)
#     print(fullnum1)
#     print(fullnum2)
#     sol = int(fullnum1) + int(fullnum2)
#     print(sol)


# adding_two_nums(600, 1231)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def adding_two_nums(self, number1, number2):
        number1_list = []
        number2_list = []
        for i in str(number1):
            number1_list.insert(-0, i)
        for e in str(number2):
            number2_list.insert(-0, e)
        print(number1_list)
        print(number2_list)
        fullnum1 = "".join(number1_list)
        fullnum2 = "".join(number2_list)
        print(fullnum1)
        print(fullnum2)
        sol = int(fullnum1) + int(fullnum2)
        print(sol)


obj1 = Solution()
obj1.adding_two_nums(123, 224)
