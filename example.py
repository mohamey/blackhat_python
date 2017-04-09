def sum(num_one, num_two):
    num_one_int = convert_integer(num_one)
    num_two_int = convert_integer(num_two)
    
    result = num_one_int + num_two_int
    
    return result

def convert_integer(num_string):
    converted_int = int(num_string)
    return converted_int

answer = sum("1", "2")