

def largest_elem_array(l : list()) -> int:
    print("Largest element in an array !")
    max = l[0]

    for i in l:
        if i > max:
            max = i
    return max




largest_element = largest_elem_array([1,2,3,40,5])
print(largest_element)