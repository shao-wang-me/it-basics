node make_toc.js docs/ docs/index.md
# Modified from https://gist.github.com/bzerangue/2504041
find docs/ -name "*.md*" | while read -r i; do pandoc "$i" -o "${i%.*}.html" -B header.html; done

# Might need to clean HTML files if Markdown files are removed
