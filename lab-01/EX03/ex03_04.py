def try_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]
    last_elemant = tuple_data[-1]
    return first_element, last_elemant
input_tuple = eval(input("nhap tuple, vi du(1, 2, 3):"))
first,last = try_cap_phan_tu(input_tuple)
print("phan tu dau tien:",first)
print("phan tu cuoi cung:",last)