# Java Persistence API (JPA)

[JPA规范网站](https://jakarta.ee/specifications/persistence/3.0/)

最权威的资料是[JPA 3.0规范文件，2020年9月8日]，写得很清楚，质量很高，啃下来不算太难。或者看[JPA 3.0规范PDF版本]。

## 实体 Entity

> An entity is a lightweight persistent domain object.

Entity类：

1. 标记为`@Entity`或在XML中标记为Entity
1. 有一个无参的constructor，public或protected
1. 不能是nested class，不能是enum或interface
1. 不能是final，方法和要存储的变量都不能是final
1. 如果一个entity实例要传输为detached对象，就必须实现Serializable interface
1. 支持inheritance、polymorphic associations和polymorphic queries
1. 可以是抽象类，可以继承非entity类，也可以继承entity类；非entity类也可以继承entity类
1. entity的persistence state由instance变量表示（可以是JavaBeans属性）。对客户来说，必须由access methods（getter和setter）访问
1. entity类可以有business方法

```java
@Entity
public class Customer implements Serializable {
    private Long id;
    private String name;
    private Address address;
    private Collection<Order> orders = new HashSet();
    private Set<PhoneNumber> phones = new HashSet();

    // No-arg constructor
    public Customer() {}

    @Id // property access is used
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Address getAddress() {
        return address;
    }

    public void setAddress(Address address) {
        this.address = address;
    }

    @OneToMany
    public Collection<Order> getOrders() {
        return orders;
    }

    public void setOrders(Collection<Order> orders) {
        this.orders = orders;
    }

    @ManyToMany
    public Set<PhoneNumber> getPhones() {
        return phones;
    }

    public void setPhones(Set<PhoneNumber> phones) {
        this.phones = phones;
    }

    // Business method to add a phone number to the customer
    public void addPhone(PhoneNumber phone) {
        this.getPhones().add(phone);

        // Update the phone entity instance to refer to this customer
        phone.addCustomer(this);
    }
}
```

这里是可以有一些商业逻辑的。

> 注：这里的讨论全都忽略了@Embeddable和复合主键，太麻烦，需要的话再看文档。继承也不在此详述。

### 访问类型

这里的访问类型指的是JPA provider是直接访问field还是property。除非标为`@Transient`，所有field或者property都会被persist。

### 主键、ID

简单主键是最容易的，直接加`@Id`即可。复合主键很麻烦，尽量不要用。

### 属性 Attributes

Field或者property，[不标注的话默认是`@Basic`][Attribute的默认标注]，如果是

### 集合 Collections

一个attribute可以是一个集合，这个集合要么是普通元素，如果不是别的entity的话，就得mark为@ElementCollection，数据存在某个表里。如果是entity的话，则用@OneToMany或@ManyToMany。

#### Map

无论是普通元素还是entity，我们都可以把这样的集合看成是一个map，在本entity中的我们只有map的key，实际的value是在另外一个table中或者是另外一个entity。Entity的话，key就是外键。 这样子的map只能在这一侧使用。

##### Key

如果map的key是基础类型，可以用@MapKeyColumn标注哪一列是该key。如果key是个entity，则用@MapKeyJoinColumn或@MapKeyJoinColumn。如果不是用generics的话，要用@MapKeyClass标注数据类型。

##### Value

如果value是基础类型，要用一个@CollectionTable来map，如果没用泛型，要在@ElementCollection中用targetClass说明数据类型。

如果value是entity，则对于@ManyToMany使用一个join表，对unidirectional的@OneToMany默认也使用一个join表。如果@ManyToOne或@OneToMany是bidirectional的，则默认不需要join表。和上述类似，如果不用泛型，则在@OneToMany或@ManyToMany标注中用targetClass说明类型。

### 实体关系 Entity Relationships

实体间关系是polymorphic的。TODO：什么意思？

实体间关系类型：

1. @OneToOne
1. @OneToMany
1. @ManyToOne
1. @ManyToMany

关系可以是bidirectional或unidirectional的。双向关系是一方own的，另一方并不own这个关系。另一方虽然也标注关系类型，但是只用mappedBy标注对应的own这个关系的entity的attribute。拥有的一方总是多的那一方，比如@ManyToOne，而不能是@OneToMany。单向关系，另一方不用标注。

| Owning Side | Inverse Side (w/ mappedBy)，没有的话是单向关系 | 备注 |
| --- | --- | --- |
| @OneToOne | @OneToOne |
| @ManyToOne | @OneToMany |
| @ManyToMany | @ManyToMany | 要有join表 |
| @OneToOne |
| @OneToMany | | 要有join表 |
| @ManyToOne |
| @ManyToMany | | 要有join表 |

> 只有保存拥有关系的一方时，改变才会被cascade到另一方。
> 
> It is particularly important to ensure that changes to the inverse side of a relationship result in appropriate updates on the owning side, so as to ensure the changes are not lost when they are synchronized to the database.

#### 例子：@OneToOne、@ManyToOne（@OneToMany w/ mappedBy）

```java
@Entity
public class Employee { // 默认表是EMPLOYEE
    private Cubicle assignedCubicle; // 默认外键叫ASSIGNEDCUBICLE_<PK_CUBICLE>，且是unique的

    @OneToOne
    public Cubicle getAssignedCubicle() {
        return assignedCubicle;
    }

    public void setAssignedCubicle(Cubicle cubicle) {
        this.assignedCubicle = cubicle;
    }

    // ...
}

@Entity
public class Cubicle { // 默认表是CUBICLE
    private Employee residentEmployee;

    @OneToOne(mappedBy="assignedCubicle")
    public Employee getResidentEmployee() {
        return residentEmployee;
    }

    public void setResidentEmployee(Employee employee) {
        this.residentEmployee = employee;
    }

    // ...
}
```

#### 例子：@ManyToMany

```java
@Entity
public class Project { // 默认表是PROJECT
    private Collection<Employee> employees; // 默认外键是EMPLOYEES_<PK_EMPLOYEE>

    @ManyToMany
    public Collection<Employee> getEmployees() { // 默认join表是PROJECT_EMPLOYEE
        return employees;
    }

    public void setEmployees(Collection<Employee> employees) {
        this.employees = employees;
    }

    // ...
}

@Entity
public class Employee { // 默认表是EMPLOYEE
    private Collection<Project> projects; // 默认外键是PROJECTS_<PK_PROJECT>

    @ManyToMany(mappedBy="employees")
    public Collection<Project> getProjects() {
        return projects;
    }

    public void setProjects(Collection<Project> projects) {
        this.projects = projects;
    }

    // ...
}
```

## 实体操作 Entity Operations

### EntityManager

一个EntityManager是关联一个persistence context的。

使用样例：

```java
@Stateless
public class OrderEntryBean implements OrderEntry {
    @PersistenceContext
    EntityManager em;

    public void enterOrder(int custID, Order newOrder) {
        Customer cust = em.find(Customer.class, custID);
        cust.getOrders().add(newOrder);
        newOrder.setCustomer(cust);
        em.persist(newOrder);
    }
}
```

### 实体实例生命周期 Entity Instance's Life Cycle

任何一个entity实例都属于以下四种状态之一。

1. 新建的 new
1. 被管理的 managed
1. 脱离的 detached
1. 已移除的 removed

| 生命周期 | Persistence Identity | Persistence Context | 备注 |
| --- | --- | --- | --- |
| New | 无 | 无 | 新建的 |
| Manged | 有 | 有 |
| Detached | 有 | 无 |
| Removed | 有 | 有 | Transaction提交时将移除 |

![JPA实体生命周期图](https://www.objectdb.com/files/images/manual/jpa-states.png)


```puml
@startuml
digraph {
a -> b
b -> c
}
@enduml
```








## API

[jahe/jpa-cheatsheet.java](https://gist.github.com/jahe/18a4efe614fc73cf184d8ceef8cdc996)

JPA的API都在`javax.persistence`这个package中，当然还需要配合实际的JPA provider使用。

### EntityManager

注意，在保存的时候，@OneToMany的关系是不会被保存的，因为这个关系是属于有@ManyToOne的那个Entity的，必须要单独保存那个Entity。参见[Why merging is not cascaded on a one to many relationship - Stack Overflow](https://stackoverflow.com/questions/13153237/why-merging-is-not-cascaded-on-a-one-to-many-relationship)。似乎可以标记cascade type，不过手动的话就是这样。

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


<!-- 链接 -->
[Attribute的默认标注]: https://jakarta.ee/specifications/persistence/3.0/jakarta-persistence-spec-3.0.html#a511
[JPA 3.0规范文件，2020年9月8日]: https://jakarta.ee/specifications/persistence/3.0/jakarta-persistence-spec-3.0.html
[JPA 3.0规范PDF版本]: https://jakarta.ee/specifications/persistence/3.0/jakarta-persistence-spec-3.0.pdf
