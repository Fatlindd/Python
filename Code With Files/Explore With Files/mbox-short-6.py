
filename = input('> Enter a filename: ')
lines = [line.strip('\n') for line in open(filename, 'rt') if line.startswith('From ')]
domain_dict = {}

for line in lines:
    line = line.split()
    email = line[1]
    domain = email.split('@')[1]
    domain_dict[domain] = domain_dict.get(domain, 0) + 1
print(domain_dict)

