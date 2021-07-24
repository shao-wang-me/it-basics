# Django

## 数据 Model

### 定义

在 `models.py` 中定义模型：

```python
from django.db import models

class Reporter(models.Model):
    # 定义字段类型和参数
    full_name = models.CharField(max_length=70)

    # 定义字符表示
    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    # 外键，Article 和 Reporter 是多对一关系，且规定删除 Reporter 时 删除对应的 Article
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
```

### 使用

```python
# 代码高亮不太对，不要在意

# 导入模型
>>> from news.models import Article, Reporter

# 全部 Reporter
>>> Reporter.objects.all()
<QuerySet []>

# 创建 Reporter 并保存
>>> r = Reporter(full_name='John Smith')
>>> r.save()

>>> Reporter.objects.all()
<QuerySet [<Reporter: John Smith>]>

>>> r.id
1
>>> r.full_name
'John Smith'

# 根据字段查询
>>> Reporter.objects.get(id=1)
<Reporter: John Smith>
>>> Reporter.objects.get(full_name__startswith='John')
<Reporter: John Smith>
>>> Reporter.objects.get(full_name__contains='mith')
<Reporter: John Smith>
>>> Reporter.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Reporter matching query does not exist.

# 创建 Article 并保存，注意 reporter 是之前的 r
>>> from datetime import date
>>> a = Article(pub_date=date.today(), headline='Django is cool',
...     content='Yeah.', reporter=r)
>>> a.save()

>>> Article.objects.all()
<QuerySet [<Article: Django is cool>]>

# 从 a 得到 reporter r
>>> r = a.reporter
>>> r.full_name
'John Smith'

# 查询 r 的所有 Article 得到 article a
>>> r.article_set.all()
<QuerySet [<Article: Django is cool>]>

# 查询所有 reporter 的全名以 John 开始的 Article
>>> Article.objects.filter(reporter__full_name__startswith='John')
<QuerySet [<Article: Django is cool>]>

# 更改 r 的全名
>>> r.full_name = 'Billy Goat'
>>> r.save()

# 删除 r
>>> r.delete()
```

### Migration 相关命令

```shell
python manage.py makemigrations
python manage.py migrate
```

### 管理界面（Admin）

很简单，只需要在 `admin.py` 中注册一下模型：

```python
from django.contrib import admin

from . import models

admin.site.register(models.Article)
```

## URL 映射

在 `urls.py` 里，映射 URL 和视图（view）：

```python
from django.urls import path

from . import views

urlpatterns = [
    # int 是数据类型，year 是 URL 参数名称，views.year_archive 是视图
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
]
```

所以 `/articles/2005/05/39323/` 会调用 `news.views.article_detail(request, year=2005, month=5, pk=39323)`。
