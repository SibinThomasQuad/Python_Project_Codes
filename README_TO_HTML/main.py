import markdown
from markdown.extensions.tables import TableExtension

# Input and output file paths
input_md_file = 'readme.md'
output_html_file = 'readme.html'

# Read the content of the Markdown file
with open(input_md_file, 'r', encoding='utf-8') as md_file:
    md_content = md_file.read()

# Configure Markdown extensions
extensions = ['markdown.extensions.tables', 'markdown.extensions.fenced_code']

# Convert Markdown to HTML with GitHub-like styling
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="github-markdown.css">
</head>
<body class="markdown-body">
{markdown.markdown(md_content, extensions=extensions)}
</body>
</html>
"""

# Write the HTML content to the output file
with open(output_html_file, 'w', encoding='utf-8') as html_file:
    html_file.write(html_content)

print(f"Markdown file '{input_md_file}' has been converted to HTML with GitHub styling as '{output_html_file}'.")
