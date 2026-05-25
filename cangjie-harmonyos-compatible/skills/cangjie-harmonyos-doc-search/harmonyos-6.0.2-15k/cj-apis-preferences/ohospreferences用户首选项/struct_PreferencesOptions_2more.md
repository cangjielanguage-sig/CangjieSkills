## struct PreferencesOptions

```cangjie
public struct PreferencesOptions {
    public let name: String
    public let dataGroupId: String
    public init(name: String)
    public init(name: String, dataGroupId: String)
}
```

**功能：** Preferences实例配置选项。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 12

### let dataGroupId

```cangjie
public let dataGroupId: String
```

**功能：** 应用组ID，需要向应用市场获取。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let name

```cangjie
public let name: String
```

**功能：** Preferences实例的名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### init(String)

```cangjie
public init(name: String)
```

**功能：** 用于创建Options实例的构造函数。默认在本应用沙箱目录下创建Preferences实例。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|Preferences实例的名称。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

var options = PreferencesOptions("name")
```

### init(String, String)

```cangjie
public init(name: String, dataGroupId: String)
```

**功能：** 用于创建Options实例的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|Preferences实例的名称。|
|dataGroupId|String|是|-|应用组ID，需要向应用市场获取。指定在此dataGroupId对应的沙箱路径下创建Preferences实例。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkData.*

var options = PreferencesOptions("name", "dataGroupId")
```

## enum PreferencesValueType

```cangjie
public enum PreferencesValueType {
    | integer(Int64)
    | double(Float64)
    | string(String)
    | bool(Bool)
    | boolArray(Array<Bool>)
    | doubleArray(Array<Float64>)
    | stringArray(Array<String>)
    | ...
}
```

**功能：** 用于表示允许的数据字段的枚举类型。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 12

### bool(Bool)

```cangjie
bool(Bool)
```

**功能：** 表示值类型为布尔值。

**起始版本：** 12

### boolArray(Array\<Bool>)

```cangjie
boolArray(Array<Bool>)
```

**功能：** 表示值类型为布尔类型的数组。

**起始版本：** 12

### double(Float64)

```cangjie
double(Float64)
```

**功能：** 表示值类型为Float64浮点数。

**起始版本：** 12

### doubleArray(Array\<Float64>)

```cangjie
doubleArray(Array<Float64>)
```

**功能：** 表示值类型为Float64类型的数组。

**起始版本：** 12

### integer(Int64)

```cangjie
integer(Int64)
```

**功能：** 表示值类型为Int64数字。

**起始版本：** 12

### string(String)

```cangjie
string(String)
```

**功能：** 表示值类型为字符串。

**起始版本：** 12

### stringArray(Array\<String>)

```cangjie
stringArray(Array<String>)
```

**功能：** 表示值类型为字符串类型的数组。

**起始版本：** 12