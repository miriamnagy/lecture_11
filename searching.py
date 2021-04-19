import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """

    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, "r") as json_file:
        data = json.load(json_file)


    return data[field]



def linear_search(sequential_data, number):
    index = []
    count = 0
    idx = 0
    # iterations = 0
    # for i in sequential_data:
    #     iterations = iterations + 1
    #     if i == number:
    #         count = count + 1
    #         index.append(iterations-1)
    # dictionary = {"positions": index, "count":count}
    # print(dictionary)
    # return dictionary
    while idx < len(sequential_data):
        if sequential_data[idx] == number:
            count = count + 1
            index.append(idx)
        idx = idx + 1

    return{"positions": index, "count": count}


def pattern_search(dna_sequence, pattern):
    idx = 0
    index = set()
    while idx < len(dna_sequence) - len(pattern):
        my_index = 0
        while my_index < len(pattern):
            if dna_sequence[idx + my_index] == pattern[my_index]:
                my_index = my_index + 1
            else:
                break
        else:

            index.add(idx)
        idx = idx + 1
    return index





def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    my_number = 0
    print(sequential_data)
    result = linear_search(sequential_data, my_number)
    print(result)
    dna_sequence = read_data("sequential.json", "dna_sequence")
    dna_search = pattern_search(dna_sequence, "ATA")
    print(dna_search)




if __name__ == '__main__':
    main()