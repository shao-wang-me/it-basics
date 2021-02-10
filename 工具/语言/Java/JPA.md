# Java Persistence API (JPA)

## API

[jahe/jpa-cheatsheet.java](https://gist.github.com/jahe/18a4efe614fc73cf184d8ceef8cdc996)

JPA的API都在`javax.persistence`这个package中，当然还需要配合实际的JPA provider使用。

### EntityManager

1. find
1. persist
1. merge
1. contains
1. detach
1. flush
1. remove
1. refresh

## 什么是JPA?

JPA is a part of Jakarta EE (formerly Java EE, EE stands for Enterprise Edition). It provides ORM (object-relational mapping).

## What ways of query does JPA have?

1. JPQL (Java Persistence Querying Language): similar to SQL.
1. Criteria API: no embedded language, similar to Django's model layer.
1. Native SQL

It supports many other ways of query.

## 什么是JPA provider?

Just like JDBC, Java only provides a set of interface, the actual work is done by providers. In JDBC, the API is in `java.sql`, and the actual providers are JDBC drivers provided by database vendors or third-parties. Some notable JPA providers: EclipseLink, Hibernate and OpenJPA, etc.

## JPA支持哪些关系?

The basic ones:

1. OneToOne: A - B
1. ManyToOne: A \*- B
1. OneToMany: A -\* B
1. ManyToMany: A \*-\* B, realised by A -* A_B *- B where A_B is a JoinTable

## 怎么映射ManyToMany关系?

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
