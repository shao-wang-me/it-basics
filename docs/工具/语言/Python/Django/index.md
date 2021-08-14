# Django

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
