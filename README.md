ckanext-metadata-beautifier
========================

This CKAN extension extends and improves the metadata display in CKAN.

## Requirements

CKAN 2.11.2 or higher

## Installation

### Installation from source

1. Clone the repository:

   ```bash
   cd $CKAN_SRC
   git clone https://bitbucket.org/ondics/ckanext-metadata-beautifier.git
   ```

2. Install the extension:

   ```bash
   cd ckanext-metadata-beautifier
   pip install .
   ```

3. Add `metadata-beautifier` to the `ckan.plugins` setting in your CKAN configuration file:

   ```ini
   ckan.plugins = ... metadata_beautifier
   ```

4. Restart CKAN.

### Installation with Docker

Add this to your Dockerfile:

```dockerfile
COPY src/ $SRC_DIR
RUN cd $SRC_DIR/ckanext-metadata-beautifier && \
    python3 setup.py develop
```

Add `metadata_beautifier` to the `CKAN__PLUGINS` environment variable:

```bash
CKAN__PLUGINS="... metadata_beautifier"
```

## Development Installation

For development installation:

```bash
cd ckanext-metadata-beautifier
pip install -e .
```

## Running Tests

To run the tests:

```bash
pytest
```

## Tested with CKAN

| CKAN Version | Python Version | Status |
|-------------|----------------|---------|
| 2.11.4      | 3.8+           | ✅ Tested|

## Copyright

(C) 2026 Ondics GmbH

## License

This extension is licensed under the AGPL v3.
