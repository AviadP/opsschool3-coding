import json
import yaml


# TODO: create function that sort returned list and divide it into sub-lists for each partition
# TODO: create function that run over the dict and split its items into proper sublist
# TODO: for debug purpose only (remove when it works) - add print for results
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
    temp_list = []
    for key, value in ppl_ages.items():
        temp_list.append(value)

    max_age = max(temp_list)
    max_part = max(buckets)
    if max_age > max_part:
        buckets.append(max_age)

    buckets = sorted(buckets)
    results = (ppl_ages, buckets)
    return results


def sort_data(data):
    buckets_list = data[1]
    pairs = []
    for i in range(0, len(buckets_list)-1):
        pairs.append([buckets_list[i], buckets_list[i+1]])

    results_dict = {}
    for key in data[0].items():
        pass


def write_to_ymal(data):
    pass


if __name__ == "__main__":
    file_name = "input.json"
    #print(import_data_from_file(file_name), "\n")
    #print((import_data_from_file(file_name)[1]))
    sort_data(import_data_from_file(file_name))
