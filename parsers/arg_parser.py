import argparse

parser = argparse.ArgumentParser(description="Example argparse script")

parser.add_argument("--input-file", "-i", type=str, help="The input file to process")
parser.add_argument("--output-file", "-o", type=str, help="The output file to write")
parser.add_argument("--verbose", "-v", action="store_true", help="Print verbose output")

args = parser.parse_args()

print("Input file:", args.input_file)
print("Output file:", args.output_file)
print("Verbose:", args.verbose)

# In this example, the 'argparse.ArgumentParser' class is used to create
# a parser object. The 'add_argument' method is used to specify the arguments
# to be parsed. The 'input-file' and 'output-file' arguments are
# specified as 'str' types, while the 'verbose' argument is specified
# as a 'store_true' action, meaning that it takes no value and is set to 'True'
# if it is present on the command line. Finally, the 'parse_args' method
# is called to parse the command-line arguments,
# and the resulting 'args' object is used to access the values of the arguments
