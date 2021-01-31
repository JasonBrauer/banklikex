import argparse
from matplotlib import pyplot

from usecase.interface import (load_call_data, find_similar_banks, idrssd_to_bank_name, 
load_overall_distributions)
from usecase.input_validation import (validate_idrssd, validate_directory, 
validate_call_data_object_list)

parser = argparse.ArgumentParser(description='Find banks similar to provided bank.',
    formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument("--find_similar_banks", nargs=2,
    help="finds banks similar to the one identified via bank idrssd\
    \narg_1: bank_idrssd - idrssd of bank that will be used to find similar banks\
    \narg_2: directory - directory where bank call data is stored")
parser.add_argument("--show_bank_names", action="store_true", 
    help="used with find similar banks to also list bank names")
parser.add_argument("--plot_distributions",
    help="plots the distributions of all fields used to compare banks\
    \narg_1: directory - directory where bank call data is stored"
    )

args = parser.parse_args()

if args.find_similar_banks:
    print(f"Arguments passed to find_similar_banks: {args.find_similar_banks}")
    call_data_object_list = load_call_data(validate_directory(args.find_similar_banks[1]))
    validated_call_data_object_list = validate_call_data_object_list(call_data_object_list)
    
    matching_agg_obj_list = find_similar_banks(
        validate_idrssd(int(args.find_similar_banks[0])), 
        validated_call_data_object_list
    )

    print(f"Number of matching banks: {len(matching_agg_obj_list)}")
    for obj in matching_agg_obj_list:
        if args.show_bank_names:
            print(obj.idrssd, idrssd_to_bank_name(validate_idrssd(obj.idrssd), 
            validated_call_data_object_list))
        else:
            print(obj.idrssd)

if args.plot_distributions:
    call_data_object_list = load_call_data(
        validate_directory(validate_directory(args.plot_distributions))
    )

    data_dict_list, ecdf_obj_dict = load_overall_distributions(
        validate_call_data_object_list(call_data_object_list)
    )
          
    for field in data_dict_list:
        fig, ax1 = pyplot.subplots()
        ax1.title.set_text(field)
        ax2 = ax1.twinx()

        ax1.hist(data_dict_list[field], bins=100, color='g')
        ax2.plot(ecdf_obj_dict[field].x, ecdf_obj_dict[field].y, 'b')

        ax1.set_xlabel(field)
        ax1.set_ylabel('Count', color='g')
        ax2.set_ylabel('Percentile', color='b')

    pyplot.show()




