# File not found
try:
    file = open("a_file.txt")
except:
    file = open("a_file.txt", "w")

# Key Error
# a_dictionary = {"key: "value"}
# value = a_dictionary["non_existent_key"]

# Index Error
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# type Error
# text = "abc"
# print(text + 5)
