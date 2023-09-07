x = list(l.rstrip("\n") for l in open("assets/numbers.txt", "r", encoding="utf-8"))[
    7:14
]


for ex in range(5):
    print(ex)

lineLen = len(open("assets/numbers.txt", "r", encoding="utf-8").readlines())
print(lineLen)
print(x)
