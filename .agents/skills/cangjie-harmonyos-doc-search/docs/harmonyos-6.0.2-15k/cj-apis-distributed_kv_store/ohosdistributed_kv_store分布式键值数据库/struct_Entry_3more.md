## struct Entry

```cangjie
public struct Entry <: ToString {
    public var key: String
    public var value: KVValueType
    public init (key: String, value: KVValueType)
}
```

**功能：** 存储在数据库中的键值对。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**父类型：**

- ToString

### var key

```cangjie
public var key: String
```

**功能：** 键值。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### var value

```cangjie
public var value: KVValueType
```

**功能：** 值对象。

**类型：** [KVValueType](#enum-kvvaluetype)

**读写能力：** 可读写

**起始版本：** 12

### init(String, KVValueType)

```cangjie
public init (key: String, value: KVValueType)
```

**功能：** 用于创建Entry实例的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|键值。|
|value|[KVValueType](#enum-kvvaluetype)|是|-|值对象。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 转成字符串格式。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回转换后的字符串。|

## struct FieldNode

```cangjie
public struct FieldNode {
    public var nullable: Bool = true
    public var default: String
    public var type_: Int32 = 0
    public init (name: String)
}
```

**功能：** 表示Schema实例的节点，提供定义存储在数据库中的值的方法。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**起始版本：** 12

### var default

```cangjie
public var default: String
```

**功能：** 表示Fieldnode的默认值。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### var nullable

```cangjie
public var nullable: Bool = true
```

**功能：** 表示数据库字段是否可以为空。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 12

### var type_

```cangjie
public var type_: Int32 = 0
```

**功能：** 表示指定节点对应数据类型的值。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 12

### init(String)

```cangjie
public init (name: String)
```

**功能：** 创建带有值的FieldNode实例。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|FieldNode的值。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

var fieldNode = FieldNode("root")
fieldNode.nullable = false
```

## struct KVManagerConfig

```cangjie
public struct KVManagerConfig {
    public init (context: StageContext, bundleName: String)
}
```

**功能：** 提供KVManager实例的配置信息，包括调用方的包名和应用的上下文。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

### init(StageContext, String)

```cangjie
public init (context: StageContext, bundleName: String)
```

**功能：** 用于创建KVManagerConfig的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[StageContext](../../arkinterop/cj-apis-ark_interop_helper.md#type-stagecontext)|是|-|应用的上下文。|
|bundleName|String|是|-|调用方的包名。|