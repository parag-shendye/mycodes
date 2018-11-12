import math


def forward_euler(time_step, n):
#time_step:= del t
# n:=no. of steps
    result = [0] * n
    result[0] = 1
    for i in range(1, n):
        result[i] = result[i - 1] - 3 * result[i - 1] * time_step#formula for forward euler upto first order  taylor exp.
    return result


def check(result,allowance, time_step):
    approx = True#initiate approx as true
    for i in range(len(result)):
        solution = math.exp(-3 * i * time_step)
        if abs(result[i] - solution) > allowance:
            print(result[i], solution)
            approx = False
    return approx


def main():
    time_step = 0.1
    n = 100
    allowance = 0.01

    result = forward_euler(time_step, n)
    approx = check(result, allowance, time_step)
    print("All values within limits") if approx else print("Values not in limits")
    
main()
