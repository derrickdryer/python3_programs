def main():
    # Open text file
    outfile = open("test.txt", "w")
    
    # Write data to the file
    outfile.write("John T Smith\n")
    outfile.write("Jane E Jones\n")
    outfile.write("Willard J Smith\n")
    
    # Close the file
    outfile.close()
    
main()