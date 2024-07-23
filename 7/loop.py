value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# while loop

while value <= 10:
    value += 1
    if value == 6:
        continue
    print(value)
else:
    print("Value is now equal to " + str(value))

# for loop
names = ['dave', 'sarah', 'john']
# for x in names:
#     print(x)

# for x in "Mississippi":
#     print (x)
for x in names:
    if x == "sarah":
        # break
        continue
    print(x)

# for x in range(4):
#     print()

for x in range(2,4):
    print(x)