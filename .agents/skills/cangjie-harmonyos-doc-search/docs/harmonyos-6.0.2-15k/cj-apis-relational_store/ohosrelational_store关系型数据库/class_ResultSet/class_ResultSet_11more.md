## class ResultSet

```cangjie
public class ResultSet {}
```

**功能：** 提供通过查询数据库生成的数据库结果集的访问方法。结果集是指用户调用关系型数据库查询接口之后返回的结果集合，提供了多种灵活的数据访问方式，以便用户获取各项数据。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

### prop columnCount

```cangjie
public prop columnCount: Int32
```

**功能：** 获取结果集中的列数。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### prop columnNames

```cangjie
public prop columnNames: Array<String>
```

**功能：** 获取结果集中所有列的名称。

**类型：** Array\<String>

**读写能力：** 只读

**起始版本：** 12

### prop isAtFirstRow

```cangjie
public prop isAtFirstRow: Bool
```

**功能：** 检查结果集是否位于第一行。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### prop isAtLastRow

```cangjie
public prop isAtLastRow: Bool
```

**功能：** 检查结果集是否位于最后一行。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### prop isClosed

```cangjie
public prop isClosed: Bool
```

**功能：** 检查当前结果集是否关闭。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### prop isEnded

```cangjie
public prop isEnded: Bool
```

**功能：** 检查结果集是否位于最后一行之后。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### prop isStarted

```cangjie
public prop isStarted: Bool
```

**功能：** 检查指针是否移动过。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### prop rowCount

```cangjie
public prop rowCount: Int32
```

**功能：** 获取结果集中的行数。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### prop rowIndex

```cangjie
public prop rowIndex: Int32
```

**功能：** 获取结果集当前行的索引。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### func close()

```cangjie
public func close(): Unit
```

**功能：** 关闭结果集。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**异常：**

- BusinessException：对应错误码的详细介绍请参见[关系型数据库错误码](../../errorcodes/cj-errorcode-data-rdb.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |14800000|Inner error.|
  |14800012|Row out of bounds.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

var rdbStore: RdbStore = getRdbStore(Global.getStageContext(),
    StoreConfig("RdbTest.db", RelationalStoreSecurityLevel.S1)) // 需获取Context应用上下文，详见本文使用说明
let resultSet = rdbStore.querySql("SELECT * FROM EMPLOYEE WHERE NAME = 'Peter'")
resultSet.close()
```