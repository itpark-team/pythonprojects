file_in = open("input.txt", "r")

sum = 0
for line in file_in:
    line_as_int = int(line)
    sum = sum + line_as_int

file_in.close()

file_out = open("output.txt", "w")

file_out.write(str(sum))

file_out.close()
