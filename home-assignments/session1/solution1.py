import json
import yaml
import argparse


# TODO: fix encoding issue


def import_data_from_file(file_name):
    j_file = file_name
    try:
        with open(j_file, encoding="utf-8") as jfile:
            output = json.load(jfile)
    except Exception as e:
        print(e)
        exit(1)

    ppl_ages = output['ppl_ages']
    buckets = output['buckets']
    all_ages = []
    for name, age in ppl_ages.items():
        all_ages.append(age)

    max_age = max(all_ages)
    max_partition = max(buckets)
    if max_age > max_partition:
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
    try:
        with open("ex1_results.yaml", "w") as yaml_file:
            yaml.dump(sorted_dict, yaml_file, default_flow_style=False)
    except Exception as e:
        print(e)
        exit()


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
