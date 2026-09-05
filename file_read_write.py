# Without Any Libraries (Pure Python)
# my_file = open("C:\\Users\\shand\\Desktop\\myfile.txt", "r")
# print(my_file)
# file_cnt = my_file.read()
# my_file.close()
# print(file_cnt)
# a,r,w

with open("C:\\Users\\MTS\\Downloads\\myfile.txt", "w", encoding="utf-8") as my_file:
    my_file.write("\nPROD-1001,ElectroniWireless Noise-Canceling Headphones,cs,149.99,45,ELEC-WH-01,In Stock.")

# with open("C:\\Users\\shand\\Desktop\\myfile.txt", "a", encoding="utf-8") as my_file:
#     my_file.write("\nLine 3: This line is safely added to the bottom!")

# Let's read it back to confirm
with open("C:\\Users\\MTS\\Downloads\\myfile.txt", "r", encoding="utf-8") as my_file:
    a=my_file.read()
    print(a)
    split_data = a.split(",")
    print(split_data)
    for i in split_data:
        print(i)
    # for i in a:
    #     print(i)