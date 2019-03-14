'''
Steven Gardiner
CS 100 2018S Section 004
HW 09, March 14, 2018
'''

# Problem 1g


def file_copy(in_file, out_file):
    # Open the in file
    file = open(in_file, 'r')
    # Read the in file
    content = file.read()
    # Close the in file
    file.close()
    # Open the outfile
    written = open(out_file, 'w')
    # Write the infiles content to the outfile
    written.write(content)
    # Close the outfile
    written.close()
    return

