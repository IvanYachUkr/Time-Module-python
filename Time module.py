import time
import matplotlib.pyplot as plt


def check_execution_time(function, arg_of_func):
    start_from_epoch = time.time()  # This method returns the time as a floating point
    # expressed in seconds since the epoch, in UTC.

    start_from_epoch_ns = time.time_ns()  # -||- in nanoseconds

    start = time.process_time()  # Return the value (in fractional seconds) of the sum of the system
    # and user CPU time of the current process. It does not include time elapsed during sleep.
    start_ns = time.process_time_ns()

    function(arg_of_func)

    end = time.process_time()
    end_ns = time.process_time_ns()

    end_from_epoch = time.time()
    end_from_epoch_ns = time.time_ns()
    print(f'The execution time of the programme was approximately {end - start} seconds '
          f'or {end_ns - start_ns} nanoseconds')

    print(f"You had been using this programme for "
          f"{end_from_epoch - start_from_epoch} seconds")

    print(f"You had been using this programme for "
          f""f"{end_from_epoch_ns - start_from_epoch_ns} nanoseconds")

    return end - start


def match_command(command):
    match command:
        case 'y' | 'Y':
            print(f'Local time is {time.ctime()}')

        # time.ctime() method converts a time in seconds since
        # the epoch to a string in local time. This is equivalent to
        # asctime(localtime(seconds)).
        # Current time is returned by localtime()
        # is used when the time tuple is not present.

        # Parameter:
        #
        # sec: number
        # of
        # seconds
        # to
        # be
        # converted
        # into
        # string
        # representation.
        case 'n' | 'N':
            print('Thank you for using this programme!')
        case 'greenwich time':
            print(f'Greenwich time is {time.asctime(time.gmtime())}')
        case 'wait':
            time.sleep(2)
        case _:
            print("Wrong input")


def generate_full_set(n):
    A = set()
    for i in range(n):
        for j in range(n):
            A.add((i, j))
    print(f"full set on {n}-1")
    return A


check_execution_time(match_command, 'y')
print('\n\n')
time.sleep(2)

# suspends execution of the current thread for a given number of seconds.
check_execution_time(match_command, 'n')
time.sleep(2)
print('\n\n')
check_execution_time(match_command, 'greenwich time')
time.sleep(2)
print('\n\n')
check_execution_time(match_command, 'wait')
time.sleep(2)
print('\n\n')
check_execution_time(match_command, 'y')
time.sleep(2)
print('\n\n')

x = [10, 25, 50, 75, 100, 250, 500, 750, 1000, 1500, 2500, 5000, 10000]
y = []

for el in x:
    y_0 = check_execution_time(generate_full_set, el)
    y.append(y_0)
    time.sleep(5)
    print('\n\n')

plt.plot(x, y)
# naming the x-axis
plt.xlabel('n - axis')
# naming the y-axis
plt.ylabel('time - axis')

plt.show()
