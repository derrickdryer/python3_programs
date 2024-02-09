def main():
    # Open text file
    infile = open("test.txt", "r")
    
    # Read the file's contents
    file_contents = infile.read()
    
    # Close the file
    infile.close()
    
    # Print the data that was read
    print(file_contents)
    
main()