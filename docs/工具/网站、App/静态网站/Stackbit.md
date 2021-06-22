# Stackbit

Stackbit 是一个在线平台，为静态网站生成器（Gatsby、Next.js、Eleventy、Gridsome、Hexo、Hugo、Jekyll、Next.js、Nuxt、Sapper 和 Vuepress）提供类似 Wix 的可视化编辑能力。只需要符合一定项目结构规范，再添加一个 stackbit.yaml 配置文件，把代码上传到 GitHub 上，就可以直接在 Stackbit 上进行可视化编辑。支持直接把 Git 当作 CMS，或者一些流行的国外的在线 CMS 平台（Contentful、Sanity、Forestry 和 NetlifyCMS）。

具体而言，Stackbit 会在 GitHub 中创建一个 preview 分支用于预览编辑，发布时则把 preview 合并到主分支。

```shell
npm install -g @stackbit/cli
stackbit init
stackbit validate  # 验证配置是否正确
```
