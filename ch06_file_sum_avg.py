file = (open('numbers.txt', 'r'))

# Sum of numbers
def sum_numbers():
    global file
    sum = 0
    for line in file:
        sum += int(line)
    print("The sum of the numbers is", sum)

# Average of numbers
def avg_numbers():
    global file
    sum = 0
    count = 0
    for line in file:
        sum += int(line)
        count += 1
    avg = sum / count
    print("The average of the numbers is", avg)
    
# Main
def main():
    sum_numbers()
    file.seek(0)
    avg_numbers()
    file.close()

main()