import argparse

from usecase.interface import load_call_data, find_similar_banks
from usecase.input_validation import (validate_idrssd, validate_directory, 
validate_call_data_object_list)

parser = argparse.ArgumentParser(description='Find banks similar to provided bank.')

parser.add_argument("--find_similar_banks", nargs=2,
help="finds banks similar to the one identified via bank idrssd\
    arg_1: bank_idrssd- idrssd of bank that will be used to find similar banks\
    arg_2: directory- directory where bank call data is stored")
# parser.add_argument("--plot", help="plots the distributions of all fields used to compare banks")

args = parser.parse_args()

if args.find_similar_banks:
    print(f"Arguments passed to find_similar_banks: {args.find_similar_banks}")
    call_data_object_list = load_call_data(validate_directory(args.find_similar_banks[1]))
    
    matching_agg_obj_list = find_similar_banks(
        validate_idrssd(int(args.find_similar_banks[0])), 
        validate_call_data_object_list(call_data_object_list)
    )

    print(f"number of matching banks: {len(matching_agg_obj_list)}")
    for obj in matching_agg_obj_list:
        print(obj.idrssd, obj.intersection_list)




