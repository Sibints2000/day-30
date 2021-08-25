# File not found
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["sdfsdf"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:


# Key Error
# a_dictionary = {"key: "value"}
# value = a_dictionary["non_existent_key"]

# Index Error
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# type Error
# text = "abc"
# print(text + 5)
