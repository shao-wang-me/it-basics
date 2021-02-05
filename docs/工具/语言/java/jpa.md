# Java Persistence API (JPA)

1. 什么是JPA?

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

1. What relationships does JPA have?

   The basic ones:

   1. OneToOne: A - B
   1. ManyToOne: A \*- B
   1. OneToMany: A -\* B
   1. ManyToMany: A \*-\* B, realised by A -* A_B *- B where A_B is a JoinTable

1. How to map ManyToMany relationships?

   For example, if you have table A, B and A_B where A_B is a JoinTable of A and B. You can define A in JPA as:

   ```java
   @Entity
   public class A {
       @ManyToMany
       @JoinTable(name = "A_B",
               joinColumns = @JoinColumn(name = "A_ID", referencedColumnName = "ID"),
               inverseJoinColumns = @JoinColumn(name = "B_ID", referencedColumnName = "ID"))
       private List<B> bs;
   }
   ```
   
   B as:

   ```java
   @Entity
   public class B {
       @ManyToMany(mappedBy="bs")
       private List<A> as;
   }
   ```
   
   If the JoinTable has more columns other than A and B's ids, you can fallback and use ManyToOne on the JoinTable.
