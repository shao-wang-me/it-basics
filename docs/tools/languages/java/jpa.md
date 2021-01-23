# Java Persistence API (JPA)

1. What is JPA?

   JPA is a part of Jakarta EE (formerly Java EE, EE stands for Enterprise Edition). It provides ORM (object-relational mapping).

1. What ways of query does JPA have?

   1. JPQL (Java Persistence Querying Language): similar to SQL.
   1. Criteria API: no embedded language, similar to Django's model layer.
   1. Native SQL
 
   It supports many other ways of query.

1. Where is the API?

   The API is in package `javax.persistence`;

1. What are JPA providers?

   Just like JDBC, Java only provides a set of interface, the actual work is done by providers. In JDBC, the API is in `java.sql`, and the actual providers are JDBC drivers provided by database vendors or third-parties. Some notable JPA providers: EclipseLink, Hibernate and OpenJPA, etc.
