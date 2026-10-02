def my_count(stop, start = 0, step = 1):

    if step == 0:
        raise ValueError("step must not be zero")

    if stop < start:
        raise ValueError("stop must be greater than or equal to start")

    if not isinstance(stop, (int, float)):
        raise ValueError("stop must be a number")

    if not isinstance(start, (int, float)):
        raise ValueError("start must be a number")

    if not isinstance(step, (int, float)):
        raise ValueError("step must be a number")   

    for i in range(start, stop, step):
        print(i)

my_count(100, -100, 42)
my_count(-100, 100, -42)