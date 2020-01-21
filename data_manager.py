file_nicknames = "data_nickname.txt"
file_results = "results.txt"


def read_file_nicknames(file):
    fil = open(file, "r")
    lines = fil.readlines()
    players_info = []
    for line in lines:
        item = line.strip("\n").split(",")
        players_info.append(item)
     
    return players_info 



def add_new_nicknames(data, file):
    with open(file_nicknames, 'a') as fil:
        record = []
        for key in data.keys():
            record.append(data[key])
        row = ",".join(map(str, record))
        fil.write(row + "\n")
