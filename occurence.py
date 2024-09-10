# def occurence(lst):
#     new_lst = []
#     for i in range(len(lst)):
#         for j in range(i+1, len(lst)):
#             if lst[i] == lst[j]:
#                 new_lst.append(lst[j])
#     return new_lst
        
    

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4,7]
# print(occurence(lst))

# def my_function(lst):
#     new_lst = []
#     for i in range(len(lst)):
#         for j in range(i+1, len(lst)):
#             if lst[i] == lst[j]:
#                 new_lst.append(lst[j])
                
#     return new_lst
    
# lst = [1, 3, 4, 5, 6, 1, 3]
# print(my_function(lst))

# def word_count(word):
#     count = 0
#     for i in range(len(word)):
#         for j in range(i+1, len(word)):
#             if word[i] == word[j]:
#                 count += 1
#             else:
#                 count = 1
                
        
#     return f'{word[i]}: {count}'

        
# word = "Hello world"
# print(word_count(word))