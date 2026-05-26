## enum ExtensionOidType

```cangjie
public enum ExtensionOidType <: Equatable<ExtensionOidType> & ToString {
    | EXTENSION_OID_TYPE_ALL
    | EXTENSION_OID_TYPE_CRITICAL
    | EXTENSION_OID_TYPE_UNCRITICAL
    | ...
}
```

**功能：** 表示获取扩展域中对象标识符类型。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**父类型：**

- Equatable\<ExtensionOidType>
- ToString

### EXTENSION_OID_TYPE_ALL

```cangjie
EXTENSION_OID_TYPE_ALL
```

**功能：** 表示获取扩展域中所有的对象标识符。

**起始版本：** 19

### EXTENSION_OID_TYPE_CRITICAL

```cangjie
EXTENSION_OID_TYPE_CRITICAL
```

**功能：** 表示获取扩展域中critical为true的对象标识符。

**起始版本：** 19

### EXTENSION_OID_TYPE_UNCRITICAL

```cangjie
EXTENSION_OID_TYPE_UNCRITICAL
```

**功能：** 表示获取扩展域中critical为false的对象标识符。

**起始版本：** 19

### func !=(ExtensionOidType)

```cangjie
public operator func !=(other: ExtensionOidType): Bool
```

**功能：** 对扩展域中对象标识符类型进行判不等。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[ExtensionOidType](#enum-extensionoidtype)|是|扩展域中对象标识符类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果扩展域中对象标识符类型不同，返回true，否则返回false。|

### func ==(ExtensionOidType)

```cangjie
public operator func ==(other: ExtensionOidType): Bool
```

**功能：** 对扩展域中对象标识符类型进行判等。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[ExtensionOidType](#enum-extensionoidtype)|是|扩展域中对象标识符类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果扩展域中对象标识符类型相同，返回true，否则返回false。|

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

**功能：** 返回扩展域中对象标识符类型的字符串表示。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|扩展域中对象标识符类型的字符串表示。|