import os

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class MetadataBeautifierPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITranslation)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "metadata-beautifier")

    # ITranslation
    def i18n_directory(self):
        """Return the path to the i18n directory."""
        return os.path.join(os.path.dirname(__file__), "i18n")

    def i18n_locales(self):
        """Return the list of locales this plugin supports."""
        i18n_path = self.i18n_directory()
        if os.path.isdir(i18n_path):
            return [
                d
                for d in os.listdir(i18n_path)
                if os.path.isdir(os.path.join(i18n_path, d))
            ]
        return []

    def i18n_domain(self):
        """Return the i18n domain for this plugin."""
        return "ckanext-metadata-beautifier"

    # ITemplateHelpers
    def get_helpers(self):
        """Return a dictionary of helper functions."""
        return {
            'get_tooltip_text': self._get_tooltip_text,
        }

    def _get_tooltip_text(self, field):
        """Return tooltip text for a given field."""
        if not field:
            return toolkit._('No field specified.')
            
        tooltip_texts = {
            'dataset_url': toolkit._('The permanent URL to access this dataset. Use this link to share or reference the dataset.'),
            'version': toolkit._('The version number of this dataset. Useful for tracking changes and updates.'),
            'source': toolkit._('The original source or origin of this dataset data.'),
            'size': toolkit._('The total size of all files in this dataset.'),
            'num_resources': toolkit._('The number of individual files or resources contained in this dataset.'),
            'author': toolkit._('The person or organization that created this dataset.'),
            'maintainer': toolkit._('The person or organization responsible for maintaining this dataset.'),
            'license': toolkit._('The license under which this dataset is available for use and redistribution.'),
            'created': toolkit._('The date and time when this dataset was first created.'),
            'last_updated': toolkit._('The date and time when this dataset was last modified or updated.'),
            'package_id': toolkit._('The unique identifier for this dataset in the system.'),
            'package_name': toolkit._('The unique name identifier used in URLs for this dataset.'),
            'organization_id': toolkit._('The unique identifier of the organization that owns this dataset.'),
            'private': toolkit._('Whether this dataset is private (only visible to organization members) or public.'),
            'creator_user_id': toolkit._('The unique identifier of the user who created this dataset.'),
            'revision_id': toolkit._('The unique identifier of this specific version/revision of the dataset.'),
            'state': toolkit._('The current state of this dataset (active, deleted, etc.).'),
            'metadata_rdf': toolkit._('Download dataset metadata in RDF format for semantic web applications.'),
            'metadata_jsonld': toolkit._('Download dataset metadata in JSON-LD format for linked data applications.'),
            'metadata_json': toolkit._('Download dataset metadata in JSON format for programmatic access.'),
            'api_package_show': toolkit._('API endpoint to retrieve complete dataset information in JSON format.'),
            'api_resource_show': toolkit._('API endpoint to retrieve specific resource information in JSON format.'),
        }
        
        # Try to get the tooltip text, with fallback
        result = tooltip_texts.get(field.lower().replace('-', '_').replace(' ', '_'))
        if result:
            return result
            
        # Try with original field name
        result = tooltip_texts.get(field)
        if result:
            return result
            
        return toolkit._('No additional information available for this field.')
