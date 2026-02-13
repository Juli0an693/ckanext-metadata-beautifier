from flask import Blueprint


metadata_beautifier = Blueprint(
    "metadata-beautifier", __name__)


def page():
    return "Hello, metadata-beautifier!"


metadata_beautifier.add_url_rule(
    "/metadata-beautifier/page", view_func=page)


def get_blueprints():
    return [metadata_beautifier]
