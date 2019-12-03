import numpy as np

print("welcom to the to-do list")

tasks = int(input("give the no. of tasks you want: "))
count = 0

task = []

while count != tasks:
    intask = input("input your task: ")
    task = task.append([intask])
    count = count + 1
    if(count == tasks):
        break

print(task)