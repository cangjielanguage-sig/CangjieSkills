## class DataAddOperation

```cangjie
public class DataAddOperation <: DataOperation {
    public DataAddOperation(index: Int32, count!: Int32 = 1, key!: ?String = None, keys!: ?Array<String> = None)
}
```

**功能：** 添加数据操作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [DataOperation](#interface-dataoperation)

### DataAddOperation(Int32, Int32, ?String, ?Array\<String>)

```cangjie
public DataAddOperation(index: Int32, count!: Int32 = 1, key!: ?String = None, keys!: ?Array<String> = None)
```

**功能：** 创建一个DataAddOperation类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-|插入数据索引值。|
|count|Int32|否|1| **命名参数。** 插入数量。初始值：1.|
|key|?String|否|None| **命名参数。** 为插入的数据分配键值。|
|keys|?Array\<String>|否|None| **命名参数。** 为插入的数据分配键值。|

## class DataChangeOperation

```cangjie
public class DataChangeOperation <: DataOperation {
    public DataChangeOperation(public let index: Int32, public let key!: ?String = "")
}
```

**功能：** 改变数据操作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [DataOperation](#interface-dataoperation)

### let index

```cangjie
public let index: Int32
```

**功能：** 改变的数据的索引值。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let key

```cangjie
public let key: ?String = ""
```

**功能：** 为改变的数据分配新的键值，默认使用原键值。

**类型：** ?String

**读写能力：** 只读

**起始版本：** 12

### DataChangeOperation(Int32, ?String)

```cangjie
public DataChangeOperation(public let index: Int32, public let key!: ?String = "")
```

**功能：** 创建一个DataChangeOperation类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-|改变的数据的索引值。|
|key|?String|否|""| **命名参数。** 为改变的数据分配新的键值，默认使用原键值。|

## class DataDeleteOperation

```cangjie
public class DataDeleteOperation <: DataOperation {
    public DataDeleteOperation(public let index: Int32, public let count!: Int32 = 1)
}
```

**功能：** 删除数据操作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [DataOperation](#interface-dataoperation)

### let count

```cangjie
public let count: Int32 = 1
```

**功能：** 删除数据数量。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let index

```cangjie
public let index: Int32
```

**功能：** 起始删除位置索引值。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### DataDeleteOperation(Int32, Int32)

```cangjie
public DataDeleteOperation(public let index: Int32, public let count!: Int32 = 1)
```

**功能：** 创建一个DataDeleteOperation类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-|起始删除位置索引值。|
|count|Int32|否|1| **命名参数。** 删除数据数量。|