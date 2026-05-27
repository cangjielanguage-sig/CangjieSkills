## struct Schema

```cangjie
public struct Schema {
    public var root: FieldNode = FieldNode("undefined")
    public var indexes: Array<String> = []
    public var mode: Int32 = 0
    public var skip: Int32 = 0
}
```

**功能：** 表示数据库模式，可以在创建或打开数据库时创建Schema对象并将它们放入[KVOptions](#class-kvoptions)中。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**起始版本：** 12

### var indexes

```cangjie
public var indexes: Array<String> = []
```

**功能：** 表示json类型的字符串数组。

**类型：** Array\<String>

**读写能力：** 可读写

**起始版本：** 12

### var mode

```cangjie
public var mode: Int32 = 0
```

**功能：** 表示Schema的模式。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 12

### var root

```cangjie
public var root: FieldNode = FieldNode("undefined")
```

**功能：** 表示json根对象。

**类型：** [FieldNode](#struct-fieldnode)

**读写能力：** 可读写

**起始版本：** 12

### var skip

```cangjie
public var skip: Int32 = 0
```

**功能：** Schema的跳跃大小。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 12

## enum KVSecurityLevel

```cangjie
public enum KVSecurityLevel {
    | S1
    | S2
    | S3
    | S4
    | ...
}
```

**功能：** 数据库的安全级别枚举。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 12

### S1

```cangjie
S1
```

**功能：** 表示数据库的安全级别为低级别，数据的泄露、篡改、破坏、销毁可能会给个人或组织导致有限的不利影响。例如，性别、国籍，用户申请记录等。

**起始版本：** 12

### S2

```cangjie
S2
```

**功能：** 表示数据库的安全级别为中级别，数据的泄露、篡改、破坏、销毁可能会给个人或组织导致严重的不利影响。例如，个人详细通信地址，姓名昵称等。

**起始版本：** 12

### S3

```cangjie
S3
```

**功能：** 表示数据库的安全级别为高级别，数据的泄露、篡改、破坏、销毁可能会给个人或组织导致严重的不利影响。例如，个人实时精确定位信息、运动轨迹等。

**起始版本：** 12

### S4

```cangjie
S4
```

**功能：** 表示数据库的安全级别为关键级别，业界法律法规中定义的特殊数据类型，涉及个人的最私密领域的信息，一旦泄露、篡改、破坏、销毁可能会给个人或组织造成重大不利影响的数据。例如，政治观点、宗教、和哲学信仰、工会成员资格、基因数据、生物信息、健康和性生活状况、性取向、设备认证鉴权、个人的信用卡等财务信息。

**起始版本：** 12

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 转成Int32格式。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回转换后的Int32。|

## enum SubscribeType

```cangjie
public enum SubscribeType {
    | SUBSCRIBE_TYPE_LOCAL
    | SUBSCRIBE_TYPE_REMOTE
    | SUBSCRIBE_TYPE_ALL
    | ...
}
```

**功能：** 订阅类型枚举。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 19

### SUBSCRIBE_TYPE_ALL

```cangjie
SUBSCRIBE_TYPE_ALL
```

**功能：** 表示订阅远端和本地数据变更。

**起始版本：** 19

### SUBSCRIBE_TYPE_LOCAL

```cangjie
SUBSCRIBE_TYPE_LOCAL
```

**功能：** 表示订阅本地数据变更。

**起始版本：** 19

### SUBSCRIBE_TYPE_REMOTE

```cangjie
SUBSCRIBE_TYPE_REMOTE
```

**功能：** 表示订阅远端数据变更。

**起始版本：** 19