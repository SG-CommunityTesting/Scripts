from .rule_filename_matches_id import filename_matches_id
from .rule_sorted_keys import sorted_keys
from .rule_indentation import indentation_correct
from .rule_remove_BOM import remove_bom

VALIDATORS = [
    filename_matches_id,
    sorted_keys,
    indentation_correct,
    remove_bom
]
