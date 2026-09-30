"""Run with: python -m unittest discover -s tests."""
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from unittest import TestCase
from xml.etree import ElementTree as ET

from plugins.seo_sitemap import write_discovery_files


class SitemapTests(TestCase):
    def test_canonical_urls_are_deduplicated_escaped_and_drafts_excluded(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            pages = {
                'index.html': '<link rel="canonical" href="https://example.com/">',
                'alias.html': '<link rel="canonical" href="https://example.com/">',
                'article.html': '<link href="https://example.com/a?x=1&amp;y=2" rel="canonical">',
                'draft.html': '<link rel="canonical" href="https://example.com/draft"><meta name="robots" content="noindex, follow">',
                'unrelated.html': '<html>No canonical URL</html>',
            }
            for name, html in pages.items():
                (root / name).write_text(html)
            write_discovery_files(SimpleNamespace(settings={
                'OUTPUT_PATH': directory, 'SITEURL': 'https://example.com/',
            }))
            urls = [node.text for node in ET.parse(root / 'sitemap.xml').iter(
                '{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
            self.assertEqual(urls, ['https://example.com/', 'https://example.com/a?x=1&y=2'])
            self.assertIn('Sitemap: https://example.com/sitemap.xml\n', (root / 'robots.txt').read_text())

    def test_relative_development_build_does_not_emit_invalid_sitemap(self):
        with TemporaryDirectory() as directory:
            write_discovery_files(SimpleNamespace(settings={
                'OUTPUT_PATH': directory, 'SITEURL': '',
            }))
            self.assertFalse((Path(directory) / 'sitemap.xml').exists())
