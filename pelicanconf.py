from pymdownx import emoji
import re

MARKDOWN = {
    "extensions": [
        "pymdownx.mark",
        "pymdownx.smartsymbols",
        "pymdownx.tilde",
        "pymdownx.saneheaders",
        "pymdownx.keys",
        "pymdownx.inlinehilite",
        "pymdownx.emoji",
        "pymdownx.snippets",
        "pymdownx.extra",
        "pymdownx.arithmatex",
        "attr_list",
    ],
    "extension_configs": {
        "pymdownx.emoji": {
            "emoji_index": emoji.gemoji,
            "emoji_generator": emoji.to_svg,
        },
        "pymdownx.extra": {"markdown.extensions.attr_list": {}},
        "pymdownx.arithmatex": {"generic": True},
    },
}

AUTHOR = "Roberto Aguilera"
SITENAME = "Swipora"
SITESUBTITLE = "Aprende inglés de forma inteligente"
SITEURL = ""
THEME = "./themes/swipora_theme"

PATH = "content"

TIMEZONE = "America/Mexico_City"

DEFAULT_LANG = "es"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

AUTHOR_ABOUT = "Soy un ingeniero de software apasionado por compartir conocimiento y crear soluciones digitales. Cuento con amplia experiencia en el desarrollo de aplicaciones móviles, web y de escritorio, diseñando todo tipo de software que impulse y se adapte a tu negocio."


# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

DISPLAY_PAGES_ON_MENU = True

SUMMARY_MAX_PARAGRAPHS = 1

# Enable Pygments for syntax highlighting
PYGMENTS_RST_OPTIONS = {"class": "highlight"}
# Optional: Use CSS classes instead of inline styles
PYGMENTS_USE_CLASSES = True

LIQUID_TAGS = ["img", "literal", "video", "youtube", "vimeo", "include_code"]

STATIC_PATHS = [
    "images",
]

ARTICLE_URL = "blog/{slug}.html"
ARTICLE_SAVE_AS = "blog/{slug}.html"

INDEX_SAVE_AS = "blog/index.html"

SITEURL = "https://code.robertoaguilera.dev/proxy/8000"
RELATIVE_URLS = False

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["grammar_tag"]

LOCALE = ('es_ES.UTF-8', 'es')