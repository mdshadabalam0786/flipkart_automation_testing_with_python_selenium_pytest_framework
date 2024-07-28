def check(pack_of):
    list_of_brand_name = ['Pack of 2 Men Solid Crew Neck Cotton Blend Dark Green T-Shirt', 'Pack of 2 Men Colorblock Polo Neck Cotton Blend Red, Black T-Shirt',
                          'Pack of 2 TQH Men Sleeveless Men Solid Round Neck Polyester Black, Grey T-Shirt',
                          'Pack of 2 Men Solid Polo Neck Cotton Blend White, Black T-Shirt',
                          'Pack of 2 Men Printed Round Neck Polyester Pink, Blue T-Shirt',
                          'Pack of 2 Men Printed Round Neck Polyester Black, Grey T-Shirt',
                          'Pack of 2 Men Solid Polo Neck Cotton Blend Multicolor T-Shirt',
                          'Pack of 2 Men Solid Polo Neck Cotton Blend Multicolor T-Shirt',
                          'Pack of 2 Men Printed Round Neck Cotton Blend Multicolor T-Shirt',
                          'Pack of 2 Men Solid Polo Neck Cotton Blend Multicolor T-Shirt',
                          'Pack of 2 Men Typography Round Neck Cotton Blend Pink, ''Light Green T-Shirt',
                          'Pack of 2 Men Solid Round Neck Polyester Black T-Shirt',
                          'Pack of 2 Men Solid Polo Neck Cotton Blend Multicolor T-Shirt',
                          'Pack of 2 Men Graphic Print Round Neck Cotton Blend Navy Blue, Beige T-Shirt',
                          'Pack of 2 Men Printed Round Neck Cotton Blend Multicolor T-Shirt',
                          'Pack of 2 Men Printed Round Neck Polyester Grey, Dark Green T-Shirt',
                          'Pack of 2 Men Printed Round Neck Cotton Blend Multicolor T-Shirt',
                          'Pack of 2 Men Printed Round Neck Cotton Blend Multicolor T-Shirt',
                          'Pack of 2 Men Printed Round Neck Polyester Multicolor T-Shirt',
                          'Pack of 2 Men Colorblock Round Neck Cotton Blend White, Maroon, Black T-Shirt',
                          'Pack of 2 Men Printed Round Neck Cotton Blend Multicolor T-Shirt',
                          'Pack of 2 Men Colorblock Round Neck Cotton Blend Multicolor T-Shirt',
                          'Pack of 2 Men Printed Round Neck Polyester Light Green, Dark Green T-Shirt',
                          'Pack of 2 Men Solid Round Neck Polyester Dark Blue, Black T-Shirt',
                          'Pack of 2 Men Solid Polo Neck Cotton Blend Multicolor T-Shirt',
                          'Pack of 2 Men Solid Polo Neck Cotton Blend Black, Grey T-Shirt',
                          'Pack of 2 Men Colorblock Polo Neck Cotton Blend Grey T-Shirt',
                          'Pack of 2 Men Solid Crew Neck Pure Cotton Multicolor T-Shirt',
                          'Pack of 2 Men Typography Round Neck Cotton Blend Grey T-Shirt',
                          'Pack of 2 Men Abstract Round Neck Poly Cotton Multicolor T-Shirt',
                          'Pack of 2 Men Typography Round Neck Polyester Multicolor T-Shirt',
                          'Pack of 2 Men Striped Round Neck Cotton Blend Multicolor T-Shirt',
                          'Pack of 2 Men Striped Round Neck Cotton Blend Multicolor T-Shirt',
                          'Pack of 2 Men Striped Round Neck Cotton Blend Black T-Shirt',
                          'Pack of 2 Men Striped Round Neck Polyester Green, Black T-Shirt',
                          'Pack of 2 Men Solid Polo Neck Cotton Blend Maroon, Red T-Shirt',
                          'Pack of 2 Men Striped Round Neck Cotton Blend Multicolor T-Shirt',
                          'Pack of 2 Men Solid Polo Neck Cotton Blend Multicolor T-Shirt',
                          'Pack of 2 Men Printed Round Neck Polyester Green, Yellow T-Shirt',
                          'Pack of 2 Men Colorblock Round Neck Cotton Blend Multicolor T-Shirt']



    for item in list_of_brand_name:
        # Extract the number of packs from the string
        num_packs = int(item.split(' ')[2])

        # Check the range and if the number of packs matches
        if pack_of == "3 - 6" and num_packs not in range(3, 7):
            print(list_of_brand_name)
            print(f"Pattern filter is not working as expected for {pack_of}")
            break
        elif pack_of == "7 - 10" and num_packs not in range(7, 11):
            print(list_of_brand_name)
            print(f"Pack of filter is not working as expected for {pack_of}")
            break
        elif (pack_of == "Pack of 2" or pack_of=="Pack of 1") and num_packs==2:

            print(list_of_brand_name)
            print(len(list_of_brand_name))
            print(f"Pack of filter is not working as expected for {pack_of}")
            break
    else:
        print(list_of_brand_name)

        print(f"All items match the filter for {pack_of}")


check("Pack of 2")

# def check(pack_of):
#     list_of_brand_name = ['Pack of 3 Men Solid Round Neck Pure Cotton Multicolor T-Shirt',
#          'Pack of 3 Men Printed Round Neck Cotton Blend Multicolor T-Shirt',
#          'Pack of 4 Men Solid Round Neck Polyester Silver, Blue, Black, Grey T-Shirt',
#          'Pack of 4 Men Solid Round Neck Polyester Multicolor T-Shirt',
#          'Pack of 4 Men Solid Round Neck Polyester Multicolor T-Shirt',
#          'Pack of 4 Men Solid Round Neck Polyester Multicolor T-Shirt',
#          'Pack of 3 Men Graphic Print Round Neck Pure Cotton Multicolor T-Shirt',
#          'Pack of 4 Men Solid, Self Design, Colorblock Round Neck Reversible Polyester Multicolor T-Shirt',
#          'Pack of 4 Men Printed Round Neck Polyester Multicolor T-Shirt', 'Pack of 4 Men Solid Round Neck Polyester Multicolor T-Shirt',
#          'Pack of 4 Men Solid, Self Design Round Neck Reversible Polyester Multicolor T-Shirt',
#          'Pack of 4 Men Solid, Self Design Round Neck Reversible Polyester Multicolor T-Shirt',
#          'Pack of 5 Men Solid Round Neck Polyester Multicolor T-Shirt', 'Pack of 4 Men Solid Round Neck Polyester Black, Blue, Grey T-Shirt',
#          'Pack of 3 Men Solid Round Neck Polyester Multicolor T-Shirt', 'Pack of 4 Men Solid Round Neck Polyester Multicolor T-Shirt',
#          'Pack of 4 Men Solid Round Neck Polyester Light Blue, Blue, Black, Grey T-Shirt',
#          'Pack of 3 Men Printed Round Neck Cotton Blend Multicolor T-Shirt',
#          'Pack of 5 Men Solid Round Neck Polyester Multicolor T-Shirt',
#          'Pack of 4 Men Printed Round Neck Polyester Black, Green, White, Navy Blue T-Shirt',
#          'Pack of3 Men Solid Round Neck Cotton Blend Multicolor T-Shirt',
#          'Pack of 3 Men Solid Round Neck Polyester Dark Blue, White, Light Blue T-Shirt',
#          'Pack of 5 Round_5_05_S Men Solid Round Neck Polyester Multicolor T-Shirt',
#          'Pack of 4 Men Solid Round Neck Polyester Multicolor T-Shirt', 'Pack of 4 Men Solid Round Neck Polyester Multicolor T-Shirt',
#          'Pack of 5 Men Solid Round Neck Polyester Multicolor T-Shirt', 'Pack of 3 Men Solid Round Neck Polyester Multicolor T-Shirt',
#          'Pack of 3 Men Solid Round Neck Pure Cotton Light Blue, Red, Maroon T-Shirt', 'Pack of 4 Men Solid Round Neck Polyester Multicolor T-Shirt',
#          'Pack of 3 Men Printed Round Neck Polyester Black, White, Navy Blue T-Shirt',
#          'Pack of 3 Men Solid Round Neck Pure Cotton Red, White, Dark Blue T-Shirt',
#          'Pack of 3 Men Solid Round Neck Cotton Blend Multicolor T-Shirt',
#          'Pack of 4 Men Solid Round Neck Polyester Multicolor T-Shirt',
#          'Pack of 4 Men Solid Round Neck Polyester Multicolor T-Shirt',
#          'Pack of 3 Men Solid Round Neck Poly Cotton Black, Grey, Maroon T-Shirt',
#          'Pack of 4 Men Solid Round Neck Polyester MulticolorT-Shirt',
#          'Pack of 3 Men Solid Hooded Neck Cotton Blend Multicolor T-Shirt',
#          'Pack of 3 Oversized Men Solid Round Neck Pure Cotton Multicolor T-Shirt',
#          'Pack of 3 Men Solid Round Neck Cotton Blend Multicolor T-Shirt',
#          'Pack of 4 Men Solid Round Neck Polyester Multicolor T-Shirt']
#     for item in list_of_brand_name:
#         # Extract the number of packs from the string
#         num_packs = int(item.split(' ')[2])
#
#         # Check the range and if the number of packs matches
#         if pack_of == "3 - 6" and num_packs not in range(3, 7):
#             print(f"Pattern filter is not working as expected for {pack_of}")
#             break
#         elif pack_of == "7 - 10" and num_packs not in range(7, 11):
#             print(f"Pack of filter is not working as expected for {pack_of}")
#             break
#     else:
#         print(f"All items match the filter for {pack_of}")
#
# check("3 - 6")