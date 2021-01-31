# 生成首页目录
node make_toc.js docs/ docs/index.md

# 自动删除HTML文件
find docs/ -name "*.html" -exec rm {} \;

# 改自https://gist.github.com/bzerangue/2504041
find docs/ -name "*.md*" | while read -r i; do pandoc "$i" -s -o "${i%.*}.html" -B header.html; done

# TODO 自定义CSS
