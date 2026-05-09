## enum PreferencesEvent

```cangjie
public enum PreferencesEvent {
    | PreferencesChange
    | PreferencesMultiProcessChange
    | ...
}
```

**功能：** Preferences的事件类型枚举。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

### PreferencesChange

```cangjie
PreferencesChange
```

**功能：** 表示数据变更。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

### PreferencesMultiProcessChange

```cangjie
PreferencesMultiProcessChange
```

**功能：** 表示多进程间的数据变更。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

## enum StorageType

```cangjie
public enum StorageType {
    | Xml
    | Gskv
    | ...
}
```

**功能：** Preferences的存储模式枚举。

> **说明：**
>
> - 在选择存储模式前，建议调用isStorageTypeSupported检查当前平台是否支持对应存储模式。
>
> - 当选择某一模式通过getPreferences接口获取实例后，不允许中途切换模式。
>
> - 首选项不支持不同模式间数据的迁移，若需将数据从一种模式切换至另一种模式，需通过读写首选项的形式进行数据迁移。
>
> - 若需要变更首选项的存储路径，不能通过移动或覆盖文件的方式进行，需通过读写首选项的形式进行数据迁移。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

### Gskv

```cangjie
Gskv
```

**功能：** 表示GSKV存储模式。

**特点：** 数据以GSKV数据库模式进行存储。对数据的操作实时落盘，无需调用flush接口对数据进行落盘。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

### Xml

```cangjie
Xml
```

**功能：** 表示XML存储模式，这是Preferences的默认存储模式。

**特点：** 数据XML格式进行存储。对数据的操作发生在内存中，需要调用flush接口进行落盘。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

## enum PreferencesValueType

```cangjie
public enum PreferencesValueType {
    | Integer(Int64)
    | Double(Float64)
    | StringData(String)
    | BoolData(Bool)
    | BoolArray(Array<Bool>)
    | DoubleArray(Array<Float64>)
    | StringArray(Array<String>)
    | ...
}
```

**功能：** 表示支持的值类型。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

### BoolArray(Array\<Bool>)

```cangjie
BoolArray(Array<Bool>)
```

**功能：** 表示值类型为布尔类型的数组。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

### BoolData(Bool)

```cangjie
BoolData(Bool)
```

**功能：** 表示值类型为布尔值。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

### Double(Float64)

```cangjie
Double(Float64)
```

**功能：** 表示值类型为双精度浮点数类型。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

### DoubleArray(Array\<Float64>)

```cangjie
DoubleArray(Array<Float64>)
```

**功能：** 表示值类型为双精度浮点数类型的数组。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

### Integer(Int64)

```cangjie
Integer(Int64)
```

**功能：** 表示值类型为64位有符号整型类型。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

### StringArray(Array\<String>)

```cangjie
StringArray(Array<String>)
```

**功能：** 表示值类型为字符串类型的数组。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22

### StringData(String)

```cangjie
StringData(String)
```

**功能：** 表示值类型为字符串。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 22