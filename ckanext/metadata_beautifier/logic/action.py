import ckan.plugins.toolkit as tk
import ckanext.metadata_beautifier.logic.schema as schema


@tk.side_effect_free
def metadata_beautifier_get_sum(context, data_dict):
    tk.check_access(
        "metadata_beautifier_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.metadata_beautifier_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'metadata_beautifier_get_sum': metadata_beautifier_get_sum,
    }
