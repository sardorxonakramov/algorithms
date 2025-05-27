from program import Stack

data = ["salom", 1, 3,"4", "Alik",6.7]
salom = Stack()
salom.data =data

print(salom.IsEmpty())
salom.sorted()
print(salom.data)
salom.pop()

print(salom.pop())
salom.push("O'tirganimga kichkina ko'rineppanmi?")
print(salom.data)