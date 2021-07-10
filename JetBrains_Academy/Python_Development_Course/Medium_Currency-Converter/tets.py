# import requests
# r = requests.get("https://hyperskill.org/learn/step/8603")
# print(r)




# import requests
# url = 'https://docs.python.org/3/'
# r = requests.get(url)
# print(r.encoding)
# if r.encoding == 'ISO-8859-1':
#     print('Right encoding!')
# else:
#     print('You should change the encoding.')


# import requests
# def get_content_type(url):
#     r = requests.get(url)
# get_content_type('http://google.com')
# get_content_type('http://github.com')


# import requests
# def do_search(bookstore_url, params):
#     r = requests.get(bookstore_url, params = params)
#     return r, r.url
# print(do_search('http://bookstore.com/search', {'author': 'Austen', 'title': 'Emma'}))



# # write your code here
# for i in range(1,11):
#     file_name = f"file{i}.txt"
#     with open(file_name, 'w') as f:
#         f.write(str(i))


# with open(r"D:\LocalServer\learning_repo\JetBrains_Academy\Python_Development_Course\Medium_Currency-Converter\salary.txt", "r") as f1,\
#      open(r"D:\LocalServer\learning_repo\JetBrains_Academy\Python_Development_Course\Medium_Currency-Converter\salary_year.txt", "w") as f2:
#      lines = f1.readlines()
#      for line in lines:
#         m_income = int(line.rstrip())
#         y_income = m_income * 12
#         f2.write(str(y_income) + "\n")



# groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']
# number_of_groups = int(input())
# groups_dict = {groups[i]: None for i in range(len(groups))}
# for i in range(number_of_groups):
#     number_of_children_each_group = int(input())
#     if number_of_children_each_group:
#         groups_dict[groups[i]] = number_of_children_each_group
    # print(groups_dict)



import json
# Python dictionary 
movie_dict = {
  "movies": [
    {
      "title": "Inception",
      "director": "Christopher Nolan",
      "year": 2010
    },
    {
      "title": "The Lord of the Rings: The Fellowship of the Ring",
      "director": "Peter Jackson",
      "year": 2001
    },
    {
      "title": "Parasite",
      "director": "Bong Joon Ho",
      "year": 2019
    }
  ]
}
##Encoding to JSON
with open(r"D:\LocalServer\learning_repo\JetBrains_Academy\Python_Development_Course\Medium_Currency-Converter\movies.json", "w") as json_file:
    json.dump(movie_dict, json_file)
    json_str = json.dumps(movie_dict, indent=4)
    print(json_str)
##Decoding JSON
# from a file
with open(r"D:\LocalServer\learning_repo\JetBrains_Academy\Python_Development_Course\Medium_Currency-Converter\movies.json", "r") as json_file:
    movie_dict_from_json = json.load(json_file)
print(movie_dict_from_json == movie_dict)  # True
# from string
print(movie_dict == json.loads(json_str))  # True