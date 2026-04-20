## class ResultSet

```cangjie
public class ResultSet {}
```

**功能：** 提供通过查询数据库生成的数据库结果集的访问方法。结果集是指用户调用关系型数据库查询接口之后返回的结果集合，提供了多种灵活的数据访问方式，以便用户获取各项数据。

ResultSet实例不会实时刷新。使用结果集后，如果数据库中的数据发生变化（如增删改操作），需要重新查询才能获取到最新的数据。

下列API示例中，都需先使用[query](#func-queryrdbpredicates-arraystring)、[querySql](#func-querysqlstring-arrayrelationalstorevaluetype)等query类方法中任一方法获取到ResultSet实例，再通过此实例调用对应方法。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### prop columnCount

```cangjie
public prop columnCount: Int32
```

**功能：** 获取结果集中列的数量。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### prop columnNames

```cangjie
public prop columnNames: Array<String>
```

**功能：** 获取结果集中所有列的名称。

**类型：** Array\<String>

**读写能力：** 只读

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### prop isAtFirstRow

```cangjie
public prop isAtFirstRow: Bool
```

**功能：** 检查结果集指针是否位于第一行（行索引为0），true表示位于第一行，false表示不位于第一行。

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### prop isAtLastRow

```cangjie
public prop isAtLastRow: Bool
```

**功能：** 检查结果集指针是否位于最后一行，true表示位于最后一行，false表示不位于最后一行。

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### prop isClosed

```cangjie
public prop isClosed: Bool
```

**功能：** 检查当前结果集是否关闭，true表示结果集已关闭，false表示结果集未关闭。

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### prop isEnded

```cangjie
public prop isEnded: Bool
```

**功能：** 检查结果集指针是否位于最后一行之后，true表示位于最后一行之后，false表示不位于最后一行之后。

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### prop isStarted

```cangjie
public prop isStarted: Bool
```

**功能：** 检查指针是否移动过，true表示指针已移动过，false表示指针未移动过。

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### prop rowCount

```cangjie
public prop rowCount: Int32
```

**功能：** 获取结果集中行的数量。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

### prop rowIndex

```cangjie
public prop rowIndex: Int32
```

**功能：** 获取结果集当前行的索引位置，默认值为-1。索引位置下标从0开始。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22