def large_number(large_list):
    # Base case where if there is only one item in the list, it should be the maximum.
    if len(large_list) == 1:
        return large_list[0]
    
    # ChatGPT was used to help with the code. The code was adapted to fit into my script

    # Creates a list for the remaining items excluding the first item.
    # The recursive function will call the large_number function until the base case is reached, removing the first item every time.
    # When the base case is reached, the function will return large_list[0] as in line 4.
    # This is now the remaining_max value that will be used in lines, 16-19.
    # The second last item will be compared to the remaining_max value with lines 16-19.
    # After this, the third last item will be compared to remaining_max.
    # This process will continue until the maximum value is found.
    remaining_max = large_number(large_list[1:])
    
    if large_list[0] > remaining_max:
        return large_list[0]
    else:
        return remaining_max
    
print(large_number([20,10,4,2,1]))
