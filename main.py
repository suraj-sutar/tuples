# in tuple you cannot append the data.using append keyword or function
# but you want to add some data in the tuple you use this example

friends = ("suraj","kashinath","prayag")
# friends.append("chetan")
# print(friends)

# its gave you error because  you cant append the data in tuple

friends = ("suraj","kashinath","prayag")

friends = friends + ("chetan",)
print(friends)