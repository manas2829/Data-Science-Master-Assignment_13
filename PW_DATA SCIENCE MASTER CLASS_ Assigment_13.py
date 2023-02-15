#!/usr/bin/env python
# coding: utf-8

# # Assignment_14-02-2023

# ## 1. What is multithreading in python?why it is used?Name the module used to handle threads in python.
# 
# ### Ans:-
# 
#     Multithreading in Python refers to the ability to execute multiple threads (i.e.,sub-tasks or sub-processes)concurrently
#     within the same program. In other words, it allows a program to perform multiple tasks simultaneously, thereby improving 
#     performance and responsiveness.
#     
#     In Python, the threading module provides a way to create and manage threads. To create a new thread, you can define a 
#     new function and then create a Thread object, passing in the function as an argument. For example, the following code
#     creates a new thread that prints the numbers 0 through 10:

# In[1]:


import threading

def print_number():
    for i in range (10):
        print(i)
        
t= threading.Thread(target=print_number)
t.start()


# ### 
#     In this example, a new thread is created using the Thread constructor, passing the print_numbers function as the target 
#     argument. The start() method is then called on the thread object to start the new thread.
#   _________________________________________________________________________________________________________________________  
#     
#     Multithreading is used in Python for a variety of reasons, primarily to improve the performance and responsiveness of 
#     programs that perform multiple tasks simultaneously. 
#     
#     Here are some of the main reasons why multithreading is used in Python:
#     
#     1.Improved performance:-   By allowing a program to perform multiple tasks simultaneously, multithreading can 
#     help improve the overall performance of a program. 
#     
#     2.User interface responsiveness:-  Multithreading can be used to keep a program's user interface responsive even 
#     while long-running tasks are performed in the background. 
#     
#     3.Resource utilization:- Multithreading can also help improve resource utilization in a program. 
# 
#     Overall, multithreading is a powerful tool that can help improve the performance and responsiveness of Python programs
#     in many different situations. 
#     
#    _________________________________________________________________________________________________________________________
#    
#        The module used to handle threads in Python is called threading. The threading module provides a way to create and 
#        manage threads in Python. It allows you to create new threads, start and stop them, and also provides various 
#        synchronization primitives such as locks, events, semaphores, and conditions for coordinating the activities of
#        multiple threads.
#     
#     
#     
#     
#     
# 
# 
# 
# 
#     
#     

# ## 2. Why threading module used? Write the use of the following functions:
# 
# ### 1.activeacount()
# ### 2.currentThread()
# ### 3. enumerate()
# 
# 
# ### Ans:-
# 
#     The threading module is used in Python for creating and managing threads in a program. It provides a way to write
#     concurrent programs in a simpler and more structured way than using low-level thread APIs. The threading module
#     provides a number of functions and classes for working with threads, including the following:
#     
#     1.active_count():- This function returns the number of currently active threads in the program, including the main
#     thread. This can be useful for debugging and monitoring the behavior of a multi-threaded program.
# 
#     2.current_thread():- This function returns a reference to the current thread object. This can be useful for obtaining
#     information about the current thread, such as its name or identifier.
# 
#     3.enumerate():-This function returns a list of all currently active thread objects in the program, including the main 
#     thread. This can be useful for debugging and monitoring the behavior of a multi-threaded program, as well as for 
#     performing operations on all threads in the program, such as joining them.
#     
#     
#     

# ## 3. Explain the following Functions:-
# 
# ### 1.run()
# ### 2.start()
# ### 3.jion()
# ### 4.isAlive()
# 
# ### Ans:-
#     In Python's threading module, there are several functions and methods available for working with threads. Here are the
#     explanations for some of the commonly used methods:
#     
#     1.run():- This is the method that will be called when a thread starts running. You can define this method in your own
#     subclass of the Thread class to specify what the thread should do. The run() method is executed in a separate thread 
#     of control, so any code that you place in this method will run concurrently with the main thread.
# 
#     2.start():- This method starts the thread's activity. It is used to create a new thread and start its execution. 
#     The start() method starts a new thread of execution, and the run() method is called in that thread.
# 
#     3.join():- This method is used to wait for a thread to complete its work before continuing with the main program. 
#     The join() method blocks the calling thread until the thread on which it is called completes execution. This can
#     be useful for synchronizing the activities of multiple threads, or for ensuring that a thread has completed its work
#     before continuing with the main program.
#     
#     4.isAlive():- This method returns a boolean value indicating whether or not the thread is currently executing. 
#     The isAlive() method can be used to check whether a thread has finished executing or is still running. If the 
#     thread is still running, this method will return True, otherwise it will return False.
# 

# ## 4. Write a phyton program to create two threads. Thread one must be print the list of squares and thread two must print the list of cubes.
# 
# ### Ans:-
# 

# In[2]:


import threading

def print_squares():
    squares=[i**2 for i in range (1,11)]
    print ("List of squares",squares)
    
def peint_cubes():
    cubes = [1**3 for i in range (1,11)]
    print("List of cubes",cubes)
   
 # Create two threads
t1 = threading.Thread(target=print_squares)
t2 = threading.Thread(target=print_cubes)
 # Start the threads
t1.start()
t2.start()

t1.join()
t2.join()

print("DONE!!")


# ## 5.State advantage and disadvantage of multithreading.
# 
# ### Ans:-
#     Multithreading has several advantages and disadvantages:
#     
#     Advantages:
#     
#     1.Improved performance: Multithreading can improve the performance of an application by allowing multiple tasks to run
#     concurrently on a multicore processor. This can result in faster response times and better overall system performance.
#     
#     2.Resource sharing: Threads can share resources, such as memory and data, with each other more efficiently than separate
#     processes, which can reduce the overall resource requirements of an application.
#     
#     3.Simplified program structure: Multithreading can simplify the structure of a program by allowing it to be broken down
#     into smaller, more manageable pieces that can be executed independently.
#     
#     4.Improved user experience: Multithreading can improve the user experience of an application by allowing it to remain 
#     responsive to user input while performing background tasks.
#     _______________________________________________________________________________________________________________________
#     
#     Disadvantages:
#     
#     1.Complexity: Multithreaded programming can be more complex than single-threaded programming due to the need to manage
#     shared resources and coordinate the execution of multiple threads.
#     
#     2.Synchronization issues: When multiple threads access the same shared resources, synchronization issues can arise that 
#     can lead to data corruption or other problems. Proper synchronization mechanisms such as locks, semaphores, and monitors
#     must be used to avoid these issues.
#     
#     3.Debugging and testing: Multithreaded programs can be more difficult to debug and test than single-threaded programs 
#     due to the increased complexity and the possibility of race conditions and other synchronization issues.
#     
#     4.Overhead: Creating and managing threads incurs additional overhead compared to running a single thread, which can 
#     result in decreased performance if not implemented properly.
#     
#     
# 

# ## 6. Explain deadlock and race conditions.
# 
# ### Ans:-
#         Deadlock and race conditions are two common types of issues that can occur in concurrent programming.
#         
#         Deadlock occurs when two or more threads or processes are blocked and waiting for each other to release a resource,
#         such as a lock or a shared piece of data. In other words, each thread or process is waiting for the other to finish
#         using a resource, but neither is able to proceed until the other releases it. This can result in a situation where 
#         all the threads or processes involved are unable to make progress, effectively freezing the program.
#         
#         A simple example of a deadlock could involve two threads trying to access two resources in different orders. 
#         Suppose Thread A has acquired Resource 1 and is waiting to acquire Resource 2, while Thread B has acquired 
#         Resource 2 and is waiting to acquire Resource 1. In this scenario, neither thread can proceed because they 
#         are each waiting for the other to release a resource.
#         __________________________________________________________________________________________________________________
#         
#         A race condition, on the other hand, occurs when the behavior of a program depends on the timing or order in which 
#         threads or processes execute. Specifically, a race condition occurs when two or more threads or processes access a 
#         shared resource concurrently, and the final outcome depends on the order in which the threads execute. If the 
#         threads access the shared resource in a different order, the program's behavior may be different.
#         
#         A classic example of a race condition involves a bank account that multiple threads can access to withdraw or 
#         deposit money. If two threads try to withdraw money from the account at the same time, the final account balance 
#         will depend on the order in which the withdrawals are processed. If one thread's withdrawal is processed first, the
#         other thread may end up withdrawing more money than is actually available in the account.
#         
#                                           Both deadlocks and race conditions can be difficult to debug and resolve, and 
#          can lead to unpredictable and undesirable behavior in concurrent programs. Programmers need to be aware of these
#          issues and use appropriate synchronization techniques, such as locks or semaphores, to avoid them.
