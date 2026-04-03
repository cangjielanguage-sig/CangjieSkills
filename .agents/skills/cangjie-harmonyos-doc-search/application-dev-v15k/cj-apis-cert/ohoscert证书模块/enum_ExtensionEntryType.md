## enum ExtensionEntryType

```cangjie
public enum ExtensionEntryType <: Equatable<ExtensionEntryType> & ToString {
    | EXTENSION_ENTRY_TYPE_ENTRY
    | EXTENSION_ENTRY_TYPE_ENTRY_CRITICAL
    | EXTENSION_ENTRY_TYPE_ENTRY_VALUE
    | ...
}
```

**功能：** 表示获取扩展域中对象类型。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**父类型：**

- Equatable\<ExtensionEntryType>
- ToString

### EXTENSION_ENTRY_TYPE_ENTRY

```cangjie
EXTENSION_ENTRY_TYPE_ENTRY
```

**功能：** 表示获取整个对象。

**起始版本：** 19

### EXTENSION_ENTRY_TYPE_ENTRY_CRITICAL

```cangjie
EXTENSION_ENTRY_TYPE_ENTRY_CRITICAL
```

**功能：** 表示获取对象的critical属性。

**起始版本：** 19

### EXTENSION_ENTRY_TYPE_ENTRY_VALUE

```cangjie
EXTENSION_ENTRY_TYPE_ENTRY_VALUE
```

**功能：** 表示获取对象的数据。

**起始版本：** 19

### func !=(ExtensionEntryType)

```cangjie
public operator func !=(other: ExtensionEntryType): Bool
```

**功能：** 对扩展域中对象类型进行判不等。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[ExtensionEntryType](#enum-extensionentrytype)|是|扩展域中对象类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果扩展域中对象类型不同，返回true，否则返回false。|

### func ==(ExtensionEntryType)

```cangjie
public operator func ==(other: ExtensionEntryType): Bool
```

**功能：** 对扩展域中对象类型进行判等。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[ExtensionEntryType](#enum-extensionentrytype)|是|扩展域中对象类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果扩展域中对象类型相同，返回true，否则返回false。|

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取当前枚举的所表示的值。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|当前枚举所表示的值。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回扩展域中对象类型的字符串表示。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|扩展域中对象类型的字符串表示。|