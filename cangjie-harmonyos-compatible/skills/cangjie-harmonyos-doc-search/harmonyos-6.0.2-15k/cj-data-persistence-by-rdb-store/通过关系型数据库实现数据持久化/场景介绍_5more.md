## 场景介绍

关系型数据库基于SQLite组件，适用于存储包含复杂关系数据的场景，比如一个班级的学生信息，需要包括姓名、学号、各科成绩等，又或者公司的雇员信息，需要包括姓名、工号、职位等。由于数据之间有较强的对应关系，复杂程度比键值型数据更高，此时需要使用关系型数据库来持久化保存数据。

大数据量场景下查询数据可能会导致耗时长甚至应用无响应，对于此类情况建议如下：

- 单次查询数据量不超过5000条。
- 拼接SQL语句尽量简洁。
- 合理地分批次查询。

## 基本概念

- **谓词：** 数据库中用来代表数据实体的性质、特征或者数据实体之间关系的词项，主要用来定义数据库的操作条件。
- **结果集：** 指用户查询之后的结果集合，可以对数据进行访问。结果集提供了灵活的数据访问方式，可以更方便地拿到用户想要的数据。

## 运作机制

关系型数据库对应用提供通用的操作接口，底层使用SQLite作为持久化存储引擎，支持SQLite具有的数据库特性，包括但不限于事务、索引、视图、触发器、外键、参数化查询和预编译SQL语句。

**图1** 关系型数据库运作机制

![relationStore_local](figures/relationStore_local.png)

## 约束限制

- 系统默认日志方式是WAL（Write Ahead Log）模式，系统默认落盘方式是FULL模式。
- 数据库中有4个读连接和1个写连接，线程获取到空闲读连接时，即可进行读取操作。当没有空闲读连接且有空闲写连接时，会将写连接当做读连接来使用。
- 为保证数据的准确性，数据库同一时间只能支持一个写操作。
- 当应用被卸载完成后，设备上的相关数据库文件及临时文件会被自动清除。
- 仓颉侧支持的基本数据类型：Int64、Float64、String、二进制类型数据、Bool。
- 为保证插入并读取数据成功，建议一条数据不要超过2M。超出该大小，插入成功，读取失败。

## 接口说明

以下是关系型数据库持久化功能的相关接口，更多接口及使用方式请参见[关系型数据库](../../API_Reference/source_zh_cn/apis/ArkData/cj-apis-relational_store.md)。

| 接口名称 | 描述 |
| -------- | -------- |
| getRdbStore(context: StageContext, config: StoreConfig): RdbStore | 获得一个RdbStore，操作关系型数据库，开发者可以根据自己的需求配置RdbStore的参数，然后通过RdbStore调用相关接口可以执行相关的数据操作。 |
| executeSql(sql: String, bindArgs: Array\<RelationalStoreValueType>): Unit | 执行包含指定参数但不返回值的SQL语句。 |
| insert(table: String, values: Map\<String, RelationalStoreValueType>): Int64 | 向目标表中插入一行数据。 |
| update(values: Map\<String, RelationalStoreValueType>, predicates: RdbPredicates): Int64 | 根据predicates的指定实例对象更新数据库中的数据。 |
| delete(predicates: RdbPredicates): Int64 | 根据predicates的指定实例对象从数据库中删除数据。 |
| query(predicates: RdbPredicates, columns: Array\<String>): ResultSet| 根据指定条件查询数据库中的数据。 |
| deleteRdbStore(context: StageContext, name: String): Unit | 删除数据库。 |