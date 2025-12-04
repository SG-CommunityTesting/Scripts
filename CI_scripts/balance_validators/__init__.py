from .rule_filename_matches_id import filename_matches_id
from .rule_sorted_keys import keys_sorted
from .rule_indentation import indentation_correct

VALIDATORS = [
    filename_matches_id,
    keys_sorted,
    indentation_correct
]
