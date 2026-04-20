## enum PRIKeyType

```cangjie
public enum PRIKeyType <: Hashable & Equatable<PRIKeyType> {
    | Integer(Int64)
    | Double(Float64)
    | Str(String)
    | ...
}
```

**功能：** 用于表示数据库表某一行主键的数据类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 19

**父类型：**

- Hashable
- Equatable\<PRIKeyType>

### Double(Float64)

```cangjie
Double(Float64)
```

**功能：** 表示值类型为浮点型数字。

**起始版本：** 19

### Integer(Int64)

```cangjie
Integer(Int64)
```

**功能：** 表示值类型为整型数字。

**起始版本：** 19

### Str(String)

```cangjie
Str(String)
```

**功能：** 表示值类型为字符串。

**起始版本：** 19

### func hashCode()

```cangjie
public func hashCode(): Int64
```

**功能：** 返回哈希值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int64|返回哈希值。|

### func !=(PRIKeyType)

```cangjie
public operator func !=(rhs: PRIKeyType): Bool
```

**功能：** 判断两个PRIKeyType是否不等。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rhs|[PRIKeyType](#enum-prikeytype)|是|-|待判不等的PRIKeyType。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回两个PRIKeyType是否不等。|

### func ==(PRIKeyType)

```cangjie
public operator func ==(rhs: PRIKeyType): Bool
```

**功能：** 判断两个PRIKeyType是否相等。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rhs|[PRIKeyType](#enum-prikeytype)|是|-|待判等的PRIKeyType。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回两个PRIKeyType是否相等。|

## enum Progress

```cangjie
public enum Progress {
    | SYNC_BEGIN
    | SYNC_IN_PROGRESS
    | SYNC_FINISH
    | ...
}
```

**功能：** 描述端云同步过程。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

### SYNC_BEGIN

```cangjie
SYNC_BEGIN
```

**功能：** 表示端云同步过程开始。

**起始版本：** 12

### SYNC_FINISH

```cangjie
SYNC_FINISH
```

**功能：** 表示端云同步过程已完成。

**起始版本：** 12

### SYNC_IN_PROGRESS

```cangjie
SYNC_IN_PROGRESS
```

**功能：** 表示正在端云同步过程中。

**起始版本：** 12

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取该Progress实例的值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回该Progress实例的值。|