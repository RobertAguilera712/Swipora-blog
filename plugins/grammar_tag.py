# import re
# from markdown import Extension
# from markdown.preprocessors import Preprocessor
# from pelican import signals
# from plugins.utils import parse_grammar

# # Match {% uppercase %} ... {% enduppercase %} across multiple lines.
# GRAMMAR_REGEX = re.compile(
#     r'{%\s*grammar\s*%}(.*?){%\s*endgrammar\s*%}', 
#     re.DOTALL
# )

# class GrammarPreprocessor(Preprocessor):
#     def run(self, lines):
#         # Join lines to search across line breaks
#         text = '\n'.join(lines)
        
#         def replace_match(match):
#             # Convert the inner text to uppercase
#             content =  match.group(1)

#             question = True if content.strip().endswith("?") else False


#             return parse_grammar(content, question)
        
#         # Substitute the text before Markdown turns it into HTML paragraphs
#         new_text = GRAMMAR_REGEX.sub(replace_match, text)
#         return new_text.split('\n')

# class GrammarExtension(Extension):
#     def extendMarkdown(self, md):
#         # Insert our preprocessor at the very beginning of Markdown execution
#         md.preprocessors.register(GrammarPreprocessor(md), 'grammar_block', 5)

# def register_markdown_extension(pelican_obj):
#     """Registers the extension into Pelican's Markdown settings."""
#     if 'MARKDOWN' not in pelican_obj.settings:
#         pelican_obj.settings['MARKDOWN'] = {}
    
#     if 'extensions' not in pelican_obj.settings['MARKDOWN']:
#         pelican_obj.settings['MARKDOWN']['extensions'] = []
        
#     pelican_obj.settings['MARKDOWN']['extensions'].append(GrammarExtension())

# def register():
#     """Connect to Pelican's initialized signal."""
#     signals.initialized.connect(register_markdown_extension)

import re
from markdown import Extension
from markdown.preprocessors import Preprocessor
from pelican import signals
from plugins.utils import parse_grammar

# Match {% grammar %} ... {% endgrammar %} across multiple lines
GRAMMAR_REGEX = re.compile(
    r'{%\s*grammar\s*%}(.*?){%\s*endgrammar\s*%}', 
    re.DOTALL
)

class GrammarPreprocessor(Preprocessor):
    def run(self, lines):
        text = '\n'.join(lines)
        
        def replace_match(match):
            content = match.group(1)
            
            # Convert raw newlines inside the tag into spaces so it stays on one line.
            # (Since you are already manually typing <br> for line breaks)
            content = content.replace('\n', ' ')
            
            question = True if content.strip().endswith("?") else False
            
            # Run your custom grammar parser
            html_output = parse_grammar(content, question)
            
            # Surround with blank lines to force Markdown to treat it as an independent HTML block
            return f"\n\n{html_output}\n\n"
        
        new_text = GRAMMAR_REGEX.sub(replace_match, text)
        return new_text.split('\n')

class GrammarExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(GrammarPreprocessor(md), 'grammar_block', 5)

def register_markdown_extension(pelican_obj):
    if 'MARKDOWN' not in pelican_obj.settings:
        pelican_obj.settings['MARKDOWN'] = {}
    
    if 'extensions' not in pelican_obj.settings['MARKDOWN']:
        pelican_obj.settings['MARKDOWN']['extensions'] = []
        
    pelican_obj.settings['MARKDOWN']['extensions'].append(GrammarExtension())

def register():
    signals.initialized.connect(register_markdown_extension)
