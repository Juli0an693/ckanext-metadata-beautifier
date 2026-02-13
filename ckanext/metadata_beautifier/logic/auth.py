import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def metadata_beautifier_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "metadata_beautifier_get_sum": metadata_beautifier_get_sum,
    }
