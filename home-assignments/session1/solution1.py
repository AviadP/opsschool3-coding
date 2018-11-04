import json


# TODO: create function that import data from json file - dict and list.
# TODO: create function that sort returned list and divide it into sub-lists for each partition
# TODO: create function that run over the dict and split its items into proper sublist
# TODO: for debug porpuse only (remove when it works) - add print for results
# TODO: create function that print results into yaml file
# TODO: create 'run' function


def draft():
    j = "input.json"

    with open("input.json") as jfile:
        output = json.load(jfile)

    ppl_ages = output['ppl_ages']
    buckets = output['buckets']
    print(ppl_ages, "\n", buckets)

    for key, value in ppl_ages.items():
        print(key)


def import_data_from_file(file_name):
    j_file = file_name
    with open(j_file) as jfile:
        output = json.load(jfile)

    ppl_ages = output['ppl_ages']
    buckets = output['buckets']
    results = (ppl_ages, buckets)
    return results


def sort_partitions(unsorted_list):
    unsorted_list.sort()

    pass

if __name__ == "__main__":
    file_name = "input.json"
    print(import_data_from_file(file_name), "\n")
    print((import_data_from_file(file_name)[1]))

