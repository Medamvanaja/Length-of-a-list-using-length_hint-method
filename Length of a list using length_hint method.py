from operator import length_hint
test_list = [1, 4, 5, 7, 8]
print("The list is : " + str(test_list))
list_len = len(test_list)
list_len_hint = length_hint(test_list)
print("Length of list using len() is : " + str(list_len))
print("Length of list using length_hint() is : " + str(list_len_hint))
