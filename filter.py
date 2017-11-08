import sys

infile = sys.argv[1]
outfile = 'u' + infile[1:]

infile = open(infile, "r")
outfile = open(outfile, "w")

for line in infile:
	outfile.write(line.replace("::", "\t"))

infile.close()
outfile.close()