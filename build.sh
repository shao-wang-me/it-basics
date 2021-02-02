# 生成首页目录
node make_toc.js docs/ docs/index.md 'IT 基础'

# 自动删除HTML文件
echo Deleting HTML files.
find docs/ -name "*.html" -exec rm {} \;

# 改自https://gist.github.com/bzerangue/2504041
echo Generating HTML files.
find docs/ -name "*.md*" | while read -r i; do pandoc "$i" -s -o "${i%.*}.html" -B header.html -M lang=zh --shift-heading-level-by=-1 -N; done

echo Done.
