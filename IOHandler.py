def write_player_array_array_to_file(filename, playerArrArr):
    f = open(filename, 'w')
    for playerArray in playerArrArr:
        out = ""
        for score in playerArray:
            out = out + str(score) + ","
        out = out[:-1]
        f.write(out + "\n")
    f.close()

def CSVToArray(inp):
    string = inp[:-1]
    nextComma = string.find(",")
    output = []
    while(nextComma != -1 and string != ""):
        output.append(int(string[0:nextComma]))
        string = string[nextComma + 1:]
        nextComma = string.find(",")
    output.append(int(string))
    return output # remove trailing newline

def read_file_to_player_array_array(filename):
    f = open(filename, 'r')
    line = f.readline()
    data_shape = []
    while line != "":
        data_shape.append(CSVToArray(line))
        line = f.readline()
    return data_shape