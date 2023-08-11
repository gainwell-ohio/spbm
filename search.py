import logging

from mkdocs.commands.build import DuplicateFilter
from mkdocs.contrib.search import SearchPlugin as BasePlugin
from mkdocs.contrib.search.search_index import SearchIndex as BaseIndex

# -----------------------------------------------------------------------------
# Class
# -----------------------------------------------------------------------------

# Search plugin with custom search index
class SearchPlugin(BasePlugin):

    # Override to use a custom search index
    def on_pre_build(self, config):
        super().on_pre_build(config)
        self.search_index = SearchIndex(**self.config)

# -----------------------------------------------------------------------------

# Search index with support for additional fields
class SearchIndex(BaseIndex):

    # Override to add additional fields for each page
    def add_entry_from_context(self, page):
        index = len(self._entries)
        super().add_entry_from_context(page)

        # Add document tags, if any
        if page.meta.get("tags"):
            if type(page.meta["tags"]) is list:
                entry = self._entries[index]
                entry["tags"] = [
                    str(tag) for tag in page.meta["tags"]
                ]
            else:
                log.warning(
                    "Skipping 'tags' due to invalid syntax [%s]: %s",
                    page.file.src_uri,
                    page.meta["tags"]
                )

        # Add document boost for search
        if "search" in page.meta:
            search = page.meta["search"]
            if "boost" in search:
                for entry in self._entries[index:]:
                    entry["boost"] = search["boost"]

# -----------------------------------------------------------------------------
# Data
# -----------------------------------------------------------------------------

# Set up logging
log = logging.getLogger("mkdocs")
log.addFilter(DuplicateFilter())
