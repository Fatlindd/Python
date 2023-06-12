
with open('data_file.txt', 'rt') as file:
    content = file.readlines()

# generates \n in every single row
print(content)

# remove \n with strip() method
content = [line.strip() for line in content]
print(content)