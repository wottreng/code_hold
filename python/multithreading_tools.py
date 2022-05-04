'''
multiprocessing tools module
written by Mark Wottreng
'''

import multiprocessing as mp
import time


def multithreading(target_function, target_function_args: list, verbose=False):
    # for tick toc timer:
    if verbose: start_time = time.time()
    #
    number_of_tasks = len(target_function_args)
    number_of_cores = mp.cpu_count() - 1  # leave one core for main thread
    # build tasking queue ---------
    job_queue = []
    for i in range(number_of_tasks):
        p = mp.Process(target=target_function, args=target_function_args[i])
        job_queue.append(p)
    # --- start multiprocessing --------
    active_thread_counter = 0
    while active_thread_counter < number_of_tasks:
        if active_thread_counter <= len(job_queue):
            if verbose: print(f"start thread {active_thread_counter}")
            job_queue[active_thread_counter].start()
            active_thread_counter += 1
        #
        while len(mp.active_children()) >= number_of_cores:
            if verbose: print("queue: waiting for threads to complete...")
            time.sleep(0.5)
    # ----------------------

    # wait for all threads to complete
    if verbose: print("wait for all threads to finish...")
    while len(mp.active_children()) > 0:  # !! this is blocking for main thread
        time.sleep(1)
        if verbose: print("waiting...")
    #
    if verbose:
        # calculate how long it took:
        stop_time = time.time()
        time_diff: float = int(stop_time - start_time)
        #
        time_hours = int(time_diff / 3600)
        time_min = int((time_diff - (time_hours * 3600)) / 60.0)
        time_sec = int(time_diff - (time_hours * 3600) - (time_min * 60))
        #
        print(f"process took: {time_hours} hours, {time_min} minutes, {time_sec} seconds")


if __name__ == '__main__':
    print("multitasking testing")

    # example cpu intensive testing function
    def test_function(num: int, string_var: str):
        a = 100000000
        x = num
        while x < a:
            x += 1
        print(f"thread finished, message: {string_var}")


    args: list = []
    for i in range(20):
        args.append((i, f"hello_#{i}"))  # append a tuple of function arguments
    multithreading(test_function, args, verbose=True)
