# JSF (Jakarta Server Faces)

JSF是Jakarta EE（原Java EE）的一部分，是构建组件式的Web UI的specification，也是一个MVC的web框架。

1. Where can I find references of JSF tags/components?

   For example, given this:

   ```xml
   <ui:composition xmlns="http://www.w3.org/1999/xhtml"
                   xmlns:ui="http://java.sun.com/jsf/facelets"
                   xmlns:h="http://java.sun.com/jsf/html"
                   xmlns:p="http://primefaces.org/ui"
                   xmlns:f="http://java.sun.com/jsf/core">
   </ui:composition>
   ```

   `p` is from PrimeFaces (<https://www.primefaces.org/documentation/>), `f`, `ui` and `h` are from JSF (<https://jakarta.ee/specifications/faces/3.0/vdldoc/>).

   You can find PrimeFaces demo here: <https://www.primefaces.org/showcase/index.xhtml>.

## PrimeFaces数据表格惰性加载（DataTable Lazy Loading）

文档：<https://primefaces.github.io/primefaces/10_0_0/#/components/datatable?id=lazy-loading>\
示例：<https://www.primefaces.org/showcase/ui/data/datatable/lazy.xhtml>

在服务器端惰性加载数据（比如从数据库），适合大数据集。绑定的数据得是一个LazyDataModel。用这个的话，排序、过滤、分页等都要自己在LazyDataModel中实现了。每当分页、排序、过滤发生的时候，都会调用LazyDataModel的load方法。

需要实现选择的话，还要覆盖（override）SelectableDataModel的`public T getRowData(String)`和`public Object getRowKey(T)`。相当于根据rowKey字符串找rowData和根据rowData得到rowKey字符串。关于选择，参见文档：<https://primefaces.github.io/primefaces/10_0_0/#/components/datatable?id=row-selection>。

这里加`lazy="true"`。
```xhtml
<p:dataTable var="car" value="#{carBean.model}" paginator="true" rows="10" lazy="true">
   //columns
</p:dataTable>
```

![org.primefaces.model.LazyDataModel](PrimeFaces%20LazyDataModel.png)

这里要用LazyDataModel。
```java
public class CarBean {
    // 这个model是dataTable的value绑定的值
    private LazyDataModel model;
    // 也可以是更精确的LazyDataModel<Car>

    public CarBean() {
        model = new LazyDataModel() {
            // 每当有分页、排序、过滤发生的时候都会调用load
            @Override
            public List<Car> load(int first, int pageSize, String sortField,
                             SortOrder sortOrder, Map<String, Object> filters) {
                // 加载数据
                List<Car> data = new ArrayList<>();
                // ...
                // 设置总行数
                model.setRowCount(data.size());
                return data;
            }
            @Override
            public Car getRowData(String rowKey) {
                // ...
            }
            @Override
            // 这个返回的Object当然可以直接是String，否则PrimeFaces可能会用toString等方法得到一个String
            public Object getRowKey(Car rowData) {
                // ...
            }
        };
    }
}
```

TODO ?faces-redirect=true是什么？
