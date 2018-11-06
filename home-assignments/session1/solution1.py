import json
import yaml
import argparse


# TODO: fix encoding issue


def import_data_from_file(file_name):
    j_file = file_name
    with open(j_file, encoding="utf-8") as jfile:
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


def sort_output_data(data):
    buckets_list = data[1]
    pairs = []
    for i in range(0, len(buckets_list) - 1):
        pairs.append([buckets_list[i], buckets_list[i + 1]])

    result_dict = {}
    for pair in pairs:
        ages = "{0} - {1}".format(pair[0], pair[1])
        result_dict[ages] = []
        for key, value in data[0].items():
            if (min(pair)) <= value < (max(pair)):
                result_dict[ages].append(key)

    return result_dict


def write_to_yaml(sorted_dict):
    with open("ex1_results.yaml", "w") as yaml_file:
        yaml.dump(sorted_dict, yaml_file, default_flow_style=False)


def main(input_file: str):
    sorted_data = import_data_from_file(input_file)
    data_output = sort_output_data(sorted_data)
    write_to_yaml(data_output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="JSON file path")
    args = parser.parse_args()
    input_file = args.input
    main(input_file=input_file)
