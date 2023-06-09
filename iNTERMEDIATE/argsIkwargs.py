print('〰〰〰〰〰〰〰〰〰〰〰〰')
# ⚠ *args is used to send a non-keyworded arguments like method('lindi')
def test_var_args(f_arg, *args):
    print("first normal arg: ", f_arg)
    for arg in args:
        print("another arg through *args: ", arg)
test_var_args('faltind', 'python', 'test', 'django')


print('〰〰〰〰〰〰〰〰〰〰〰〰')
# ⚠ **kwargs is used to pass keyworded arguments like method(name='lindi')
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))
greet_me(name="fatlind")


print('〰〰〰〰〰〰〰〰〰〰〰〰')
def test_args_kwargs(arg1, arg2, arg3):
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    print("arg3: ", arg3)

args = ("two", 3, 5)
test_args_kwargs(*args)

print('〰〰〰〰〰〰〰〰〰〰〰〰')
kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)

# ◼◻◼◻|>   NOTES   <|◼◻◼◻
# Order of using *args **kwargs of these in functions then the order is
# some_func(args, *args, **kwargs)