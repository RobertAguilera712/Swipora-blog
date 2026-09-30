"""Render unlisted WebView alternatives without changing public article URLs."""
from pelican import signals


def write_app_articles(generator, writer):
    template = generator.get_template("app_article")
    for article in [*generator.articles, *generator.translations]:
        writer.write_file(
            "app/" + article.save_as,
            template,
            generator.context,
            article=article,
            category=article.category,
            url="app/" + article.url,
            relative_urls=generator.settings["RELATIVE_URLS"],
        )


def register():
    signals.article_writer_finalized.connect(write_app_articles)
