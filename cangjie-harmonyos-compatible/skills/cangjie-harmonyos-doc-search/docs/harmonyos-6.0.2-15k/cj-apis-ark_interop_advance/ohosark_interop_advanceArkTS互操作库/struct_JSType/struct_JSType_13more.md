## struct JSType

```cangjie
public struct JSType {
    public static let UNDEFINED: JSType = JSType(0)
    public static let NULL: JSType = JSType(1)
    public static let NUMBER: JSType = JSType(2)
    public static let BOOLEAN: JSType = JSType(3)
    public static let BIGINT: JSType = JSType(4)
    public static let STRING: JSType = JSType(5)
    public static let SYMBOL: JSType = JSType(6)
    public static let OBJECT: JSType = JSType(7)
    public static let FUNCTION: JSType = JSType(8)
    public static let EXTERNAL: JSType = JSType(9)
}
```

**功能：** ArkTS 数据类型枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

在 ArkTS 里，通过 typeof 操作符可枚举出某个数据的大致类型，JSType 罗列出这些类型并且加入 EXTERNAL 类型。

### static let BIGINT

```cangjie
public static let BIGINT: JSType = JSType(4)
```

**功能：** bigint 类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**类型：** [JSType](#struct-jstype)

### static let BOOLEAN

```cangjie
public static let BOOLEAN: JSType = JSType(3)
```

**功能：** bool 类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**类型：** [JSType](#struct-jstype)

### static let EXTERNAL

```cangjie
public static let EXTERNAL: JSType = JSType(9)
```

**功能：** external 类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**类型：** [JSType](#struct-jstype)

### static let FUNCTION

```cangjie
public static let FUNCTION: JSType = JSType(8)
```

**功能：** function 类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**类型：** [JSType](#struct-jstype)

### static let NULL

```cangjie
public static let NULL: JSType = JSType(1)
```

**功能：** null 类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**类型：** [JSType](#struct-jstype)

### static let NUMBER

```cangjie
public static let NUMBER: JSType = JSType(2)
```

**功能：** number 类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**类型：** [JSType](#struct-jstype)

### static let OBJECT

```cangjie
public static let OBJECT: JSType = JSType(7)
```

**功能：** object 类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**类型：** [JSType](#struct-jstype)

### static let STRING

```cangjie
public static let STRING: JSType = JSType(5)
```

**功能：** string 类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**类型：** [JSType](#struct-jstype)

### static let SYMBOL

```cangjie
public static let SYMBOL: JSType = JSType(6)
```

**功能：** symbol 类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**类型：** [JSType](#struct-jstype)

### static let UNDEFINED

```cangjie
public static let UNDEFINED: JSType = JSType(0)
```

**功能：** undefined 类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**类型：** [JSType](#struct-jstype)

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取 JSType 的字符串描述。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|String|字符串描述。|

### func !=(JSType)

```cangjie
public operator func !=(target: JSType): Bool
```

**功能：** 对两个 JSType 进行不等判断。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|[JSType](#struct-jstype)|是|-|对比的目标类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表两个类型不等。|