## class DataExchangeOperation

```cangjie
public class DataExchangeOperation <: DataOperation {
    public DataExchangeOperation(public let start!: Int32, public let end!: Int32, public let key!: ExchangeKey = ExchangeKey())
}
```

**功能：** 交换数据操作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [DataOperation](#interface-dataoperation)

### let end

```cangjie
public let end: Int32
```

**功能：** 第二个交换位置。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let key

```cangjie
public let key: ExchangeKey = ExchangeKey()
```

**功能：** 分配新的键值，默认使用原键值。

**类型：** [ExchangeKey](#class-exchangekey)

**读写能力：** 只读

**起始版本：** 12

### let start

```cangjie
public let start: Int32
```

**功能：** 第一个交换位置。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### DataExchangeOperation(Int32, Int32, ExchangeKey)

```cangjie
public DataExchangeOperation(public let start!: Int32, public let end!: Int32, public let key!: ExchangeKey = ExchangeKey())
```

**功能：** 创建一个DataExchangeOperation类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|start|Int32|是|-| **命名参数。** 第一个交换位置。|
|end|Int32|是|-| **命名参数。** 第二个交换位置。|
|key|[ExchangeKey](#class-exchangekey)|否|ExchangeKey()| **命名参数。** 分配新的键值，默认使用原键值。|

## class DataMoveOperation

```cangjie
public class DataMoveOperation <: DataOperation {
    public DataMoveOperation(public let from!: Int32, public let to!: Int32, public let key!: ?String = "")
}
```

**功能：** 移动数据操作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [DataOperation](#interface-dataoperation)

### let from

```cangjie
public let from: Int32
```

**功能：** 起始移动位置。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let key

```cangjie
public let key: ?String = ""
```

**功能：** 为被移动的数据分配新的键值，默认使用原键值。

**类型：** ?String

**读写能力：** 只读

**起始版本：** 12

### let to

```cangjie
public let to: Int32
```

**功能：** 目的移动位置。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### DataMoveOperation(Int32, Int32, ?String)

```cangjie
public DataMoveOperation(public let from!: Int32, public let to!: Int32, public let key!: ?String = "")
```

**功能：** 创建一个DataMoveOperation类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|from|Int32|是|-| **命名参数。** 起始移动位置。|
|to|Int32|是|-| **命名参数。** 目的移动位置。|
|key|?String|否|""| **命名参数。** 为被移动的数据分配新的键值，默认使用原键值。|

## class DataReloadOperation

```cangjie
public class DataReloadOperation <: DataOperation {
    public DataReloadOperation()
}
```

**功能：** 重载所有数据操作。当onDatasetChange含有DataReloadOperation操作时，其余操作全部失效，框架会自己调用keygenerator进行键值比对。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [DataOperation](#interface-dataoperation)

### DataReloadOperation()

```cangjie
public DataReloadOperation()
```

**功能：** 创建一个DataReloadOperation类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19