#######################
# Basic Math          #
#######################

def get_greatest(number_list):
    greatest_number = number_list[0]
    list_modified = number_list[1:]
    for number in list_modified:
        if number > greatest_number:
            greatest_number = number
    return greatest_number


def get_smallest(number_list):
    smallest_number = number_list[0]
    list_modified = number_list[1:]
    for n in list_modified:
        if n < smallest_number:
            smallest_number = n
    return smallest_number


def get_mean(number_list):
    mean = None
    sum = 0
    for i in range(len(number_list)):
        sum += number_list[i]
    mean = sum / len(number_list)
    return mean


def get_median(number_list):
    median = None
    asc_sorted = sorted(number_list)
    median = asc_sorted[(len(number_list)-1)//2] if (len(number_list)-1)%2 == 0 else (asc_sorted[(len(number_list)-1)//2] + asc_sorted[(len(number_list)-1)//2+1])/2
    return median
