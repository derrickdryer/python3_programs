print("===== RECTANGLE 1 AREA =====")
print("Enter the length and width of the rectangle")
length1 = int(input("Length: "))
width1 = int(input("Width: "))
area1 = length1 * width1
print("===== RECTANGLE 2 AREA =====")
print("Enter the length and width of the rectangle")
length2 = int(input("Length: "))
width2 = int(input("Width: "))
area2 = length2 * width2

if area1 > area2:
    print("Rectangle 1 has a greater area")
elif area1 < area2:
    print("Rectangle 2 has a greater area")
else:
    print("Both rectangles have the same area")