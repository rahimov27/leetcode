# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000


# def my_function(text):
#     symbols = []
#     number = []
#     for i in text:
#         symbols.append(i)
#     print(symbols)
#     for symbol in symbols:
#         if symbol == "I":
#             number.append(1)
#         elif symbol == "V":
#             number.append(5)
#         elif symbol == "X":
#             number.append(10)
#         elif symbol == "L":
#             number.append(50)
#         elif symbol == "C":
#             number.append(100)
#         elif symbol == "D":
#             number.append(500)
#         elif symbol == "M":
#             number.append(1000)
#     print(sum(number))


# my_function("IIIXV")


# def romanToInt(text: str) -> int:
# def switch(number):
#     if number == 1:
#         return "I"
#     elif number == 5:
#         return "V"
#     elif number == 10:
#         return "X"
#     elif number == 50:
#         return "L"
#     elif number == 100:
#         return "C"
#     elif number == 500:
#         return "D"
#     elif number == 1000:
#         return "M"


# print(switch(500))


# class Solution:
#     def romanToInt(self, text: str) -> int:
#         symbols = []
#         number = []
#         for i in text:
#             symbols.append(i)
#         print(symbols)
#         for symbol in symbols:
#             if symbol == "I":
#                 number.append(1)
#             elif symbol == "V":
#                 number.append(5)
#             elif symbol == "X":
#                 number.append(10)
#             elif symbol == "L":
#                 number.append(50)
#             elif symbol == "C":
#                 number.append(100)
#             elif symbol == "D":
#                 number.append(500)
#             elif symbol == "M":
#                 number.append(1000)
#         print(sum(number))


# obj1 = Solution()
# obj1.romanToInt("IIIXV")


# def solution(roman: str) -> int:
#     symbols = []
#     sorted_symbols = []
#     number = []
#     for i in roman:
#         symbols.append(i)
#     print(symbols)
#     for symbol in symbols:
#         if symbol == "I":
#             number.append(1)
#         elif symbol == "V":
#             number.append(5)
#         elif symbol == "X":
#             number.append(10)
#         elif symbol == "L":
#             number.append(50)
#         elif symbol == "C":
#             number.append(100)
#         elif symbol == "D":
#             number.append(500)
#         elif symbol == "M":
#             number.append(1000)
#     print(sum(number))


# solution("MMMCMXCIX")


# def sorting_symbols(text):
#     clear_symbols = []
#     for symbol in text:
#         if symbol == "M":
#             clear_symbols.insert(0, "M")
#         if symbol == "D":
#             clear_symbols.insert(1, "D")
#         if symbol == "C":
#             clear_symbols.insert(2, "C")
#         if symbol == "L":
#             clear_symbols.insert(3, "L")
#         if symbol == "X":
#             clear_symbols.insert(4, "X")
#         if symbol == "V":
#             clear_symbols.insert(5, "V")
#         if symbol == "I":
#             clear_symbols.insert(6, "I")
#     print(clear_symbols)


# sorting_symbols("MMMCMXCIX")

# Join function
# text = ["S", "A", "G", "D", "I", "I"]
# fullname = "".join(text)
# print(fullname)


# def sorting_symbols(text):
#     clear_symbols = []
#     for symbol in text:
#         if symbol == "M":
#             clear_symbols.append("M")
#         if symbol == "D":
#             clear_symbols.append("D")
#         if symbol == "C":
#             clear_symbols.append("C")
#         if symbol == "L":
#             clear_symbols.append("L")
#         if symbol == "X":
#             clear_symbols.append("X")
#         if symbol == "V":
#             clear_symbols.append("V")
#         if symbol == "I":
#             clear_symbols.append("I")
#     print("".join(clear_symbols))


# sorting_symbols("MMMCMXCIX")
