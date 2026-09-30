"""Generate discovery files from the canonical URLs of the rendered site."""
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree as ET

from pelican import signals


class PageMetadata(HTMLParser):
    def __init__(self):
        super().__init__()
        self.canonical = None
        self.noindex = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href")
        if tag == "meta" and attrs.get("name") == "robots":
            self.noindex = "noindex" in attrs.get("content", "").lower()


def write_discovery_files(pelican):
    output = Path(pelican.settings["OUTPUT_PATH"])
    site_url = pelican.settings["SITEURL"].rstrip("/")
    if not site_url.startswith(("https://", "http://")):
        return
    urls = set()
    for path in output.rglob("*.html"):
        metadata = PageMetadata()
        metadata.feed(path.read_text(encoding="utf-8"))
        if metadata.canonical and not metadata.noindex:
            urls.add(metadata.canonical)
    sitemap = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for url in sorted(urls):
        ET.SubElement(ET.SubElement(sitemap, "url"), "loc").text = url
    ET.ElementTree(sitemap).write(output / "sitemap.xml", encoding="utf-8", xml_declaration=True)
    (output / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {site_url}/sitemap.xml\n", encoding="utf-8"
    )


def register():
    signals.finalized.connect(write_discovery_files)
