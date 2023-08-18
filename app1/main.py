# with open("hello.txt", 'r') as lines:
#     lines = lines.readlines()
#
# for line in lines:
#     if line.lower().__contains__("amila"):
#         print("incorrect person")
#     else:
#         print("all good")

try:
    file = open("yo.txt", 'r')
except:
    print("error")
