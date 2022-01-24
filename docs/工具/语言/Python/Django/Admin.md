# 管理界面（Admin）

很简单，只需要在 `admin.py` 中注册一下模型：

```python
from django.contrib import admin
import models

admin.site.register(models.Article)
```

## `ModelAdmin`

```python
from django.contrib import admin
import models

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):

    # 选项

    actions
    actions_on_top
    actions_on_button
    actions_selection_counter

    date_hierarchy = 'publish_date'
    empty_value_display

    exclude  # 不要显示某些字段
    fields  # 选择要显示的字段，并且排序
    fieldsets  # 类似 fields，只是可以 grouping fields

    filter_horizontal
    filter_vertical

    form
    formfield_overrides

    inlines

    list_display  # 哪些在列表中显示
    list_display_links
    list_editable
    list_filter
    list_max_show_all
    list_per_page
    list_select_related
    ordering
    paginator
    search_fields
    search_help_text
    show_full_result_count
    sortable_by

    prepopulated_fields
    preserve_fielters
    radio_fields
    autocomplete_fields
    raw_id_fields
    readonly_fields

    save_as  # True, False
    save_as_continue  # True, False
    save_on_top

    view_on_site = 'https://book.com/辞海/  # 在页面上显示个 view on site 的按钮，该按钮的 URL 就是这个

    # 方法

    def save_model()  # 覆盖模型保存逻辑
    def delete_model()
    def delete_queryset()
    def save_formset()
    def save_related()
    def get_queryset()
    def response_add()
    def response_change()
    def response_delete()
    def get_deleted_objects()

    def get_list_display()
    def get_list_display_links()
    def get_list_filter()
    def get_list_select_related()
    def get_ordering()
    def get_sortable_by()
    def get_search_fields()
    def get_search_results()
    def get_paginator()

    def get_changelist()
    def get_changelist_form()
    def get_changelist_formset()
    def lookup_allowed()

    def has_view_permission()
    def has_add_permission()
    def has_change_permission()
    def has_delete_permission()
    def has_module_permission()

    def get_fields()
    def get_fieldsets()
    def get_exclude()
    def get_autocomplete_fields()
    def get_readonly_fields()
    def get_prepopulated_fields()

    def get_inlines()
    def get_inline_instances()

    def get_urls()

    def get_form()
    def get_formsets_with_inlines()
    def formfield_for_foreignkey()
    def formfield_for_manytomany()
    def formfield_for_choice_field()
    def get_formset_kwargs()
    def get_changeform_initial_data()

    def message_user()

    # 这些一般是用来提供额外的参数的（extra_context）
    def add_view()
    def change_view(self, request, object_id, form_url='', extra_context=None):
        return super().change_view(request, object_id, form_url, extra_context={**extra_context, name='Shao'})
    def changelist_view()
    def delete_view()
    def history_view()

    class Media:
        css = {}
        js = {}
```