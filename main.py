import time


def tnpo_algorithm(list_result):
    
    current_number = list_result[-1]
    time.sleep(0.025)
    print(current_number) #for checking the result
    
    if not(current_number == 1):
        if (current_number % 2 == 1 ): 
            list_result.append(current_number*3+1)
        elif (current_number % 2 == 0):
            list_result.append(current_number/2)
        tnpo_algorithm(list_result)

    return(list_result)

starting_number = input("Input starting number:")
list_result = []
list_result.append(int(starting_number))
list_result = tnpo_algorithm(list_result)

print("n: ", (len(list_result)))

# print("result: ")
# print(list_result)