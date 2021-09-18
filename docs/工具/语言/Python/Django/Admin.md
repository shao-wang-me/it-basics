# 管理界面（Admin）

很简单，只需要在 `admin.py` 中注册一下模型：

```python
from django.contrib import admin
import models

admin.site.register(models.Article)
```
