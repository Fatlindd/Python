import dbm
import pickle

random_str = 'This is a random string.'
words = {'why': 'pse', 'okay': 'ani'}

# 1 -> c | if not created, create a database with name database
db = dbm.open('database', 'c')
db['random_str'] = random_str

# module pickle is used to serialize python object into a binary format
# so it convert python object into a byte stream represenation that can
# be stored in a file.
words = pickle.dumps(words)
db['words'] = words
db.close()

# After database was created clear code 
# And update with this below
import dbm
import pickle

random_str = 'This is a random string.'
words = {'why': 'pse', 'okay': 'ani'}

db = dbm.open('database')
random_str = db['random_str']
words = db['words']

# is used to deserialize a Python object from a binary string representation.
# It takes a binary string produced by dumps() and returns the original Python object.
words = pickle.loads(words)

print(random_str)
print(words) 