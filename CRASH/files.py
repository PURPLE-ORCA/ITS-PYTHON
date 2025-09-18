# import os 

# file_path = r"C:\Users\purple Orca\Pictures\WALLPAPERS\wallhaven-qzkpg7_1920x1080.png"

# if os.path.exists(file_path):
#     print(f"{file_path} exists")

#     if os.path.isfile(file_path):
#         print(f"{file_path} is a file")
#     else:
#         print(f"{file_path} is a directory")
# else:
#     print(f"{file_path} does not exist")



# txt_data = "33AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaaaaaa"

# file_path = "output.txt"

# # with open(file_path, "x") as file: 
# # with open(file_path, "a") as file: // TO APPEND DATA
# with open(file_path, "w") as file:
#     file.write(txt_data)
#     print(f"the file {file_path} wa created succesfully")




# import csv

# employees = [["Name", "Age", "Job"],
#              ["Spongebob", 30, "Cook"],
#              ["Patrick", 37, "Unemployed"],
#              ["Sandy", 27, "Scientist"]]

# file_path = "output.csv"

# try:
#     with open(file_path, "w", newline="") as file:
#         writer = csv.writer(file)
#         for row in employees:
#             writer.writerow(row)
#         print(f"csv file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")


