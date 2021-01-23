# Extensible Markup Language (XML)

1. What is `xmlns`?

   It defines an XML namespace.

   > XML namespaces provide a simple method for qualifying element and attribute names used in Extensible Markup Language documents by associating them with namespaces identified by URI references. (<https://www.w3.org/TR/REC-xml-names/>)

   It provides a way to distinguish tags from different origin with the same name. It is often a URL which may or may not point to a real web page.

   Sometimes people use the schema's URL. This is only a convention.

   Example:

   ```xml
   <person xmlns="http://www.your.example.com/xml/person">
        <name>Rob</name>
        <age>37</age>
        <homecity xmlns="http://www.my.example.com/xml/cities">
            <name>London</name>
            <lat>123.000</lat>
            <long>0.00</long>
        </homecity>
    </person>
   ```
