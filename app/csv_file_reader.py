from csv import reader


def make_data_brands(file_names, type_report):
    data = []
    for file_name in file_names:
        with open(file_name, mode="r", encoding="utf-8", newline="") as file:
            read_file = reader(file)
            for line in read_file:
                if "average-price" in type_report:
                    data.append(line[1:3:])
                else:
                    data.append(line[1:4:2])
    return data
