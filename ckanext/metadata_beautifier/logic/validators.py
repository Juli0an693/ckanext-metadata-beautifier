import ckan.plugins.toolkit as tk


def metadata-beautifier_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "metadata-beautifier_required": metadata-beautifier_required,
    }
