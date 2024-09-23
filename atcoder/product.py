def product(s: str) -> str:
    a, b = map(int, s.split())
    c = a * b
    if c % 2 == 0:
        return "Even"
    else:
        return "Odd"


assert product("3 4") == "Even"
assert product("1 21") == "Odd"


# # 提出用
# a, b = map(int, input().split())
# if (a * b) % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

