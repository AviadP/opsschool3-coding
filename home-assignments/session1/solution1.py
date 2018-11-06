import json
import yaml


# TODO: add file as argument
# TODO: create function that print results into yaml file


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

    buckets.append(0)
    buckets = sorted(buckets)
    results = (ppl_ages, buckets)
    return results


def sort_data(data):
    buckets_list = data[1]
    pairs = []
    for i in range(0, len(buckets_list) - 1):
        pairs.append([buckets_list[i], buckets_list[i + 1]])

    results_string = ""
    for pair in pairs:
        results_string = results_string + "{0}-{1}: \n".format(pair[0], pair[1])
        for key, value in data[0].items():
            if (min(pair)) <= value < (max(pair)):
                results_string = results_string + "- {0} \n".format(key)

    print(results_string)
    return results_string


def write_to_ymal(results_dict):
    pass


def main():
    file_name = "input.json"
    sort_data(import_data_from_file(file_name))


if __name__ == "__main__":
    main()
