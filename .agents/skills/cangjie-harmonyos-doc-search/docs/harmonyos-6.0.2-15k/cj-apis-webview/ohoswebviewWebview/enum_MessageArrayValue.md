## enum MessageArrayValue

```cangjie
public enum MessageArrayValue <: Equatable<MessageArrayValue> & ToString {
    | ARRAYSTRING(Array<String>)
    | ARRAYI64(Array<Int64>)
    | ARRAYF64(Array<Float64>)
    | ARRAYBOOL(Array<Bool>)
    | ...
}
```

**功能：** 数组类型数据。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**父类型：**

- Equatable\<MessageArrayValue>
- ToString

### ARRAYBOOL(Array\<Bool>)

```cangjie
ARRAYBOOL(Array<Bool>)
```

**功能：** Bool数组类型数据。

**起始版本：** 19

### ARRAYF64(Array\<Float64>)

```cangjie
ARRAYF64(Array<Float64>)
```

**功能：** Float64数组类型数据。

**起始版本：** 19

### ARRAYI64(Array\<Int64>)

```cangjie
ARRAYI64(Array<Int64>)
```

**功能：** Int64数组类型数据。

**起始版本：** 19

### ARRAYSTRING(Array\<String>)

```cangjie
ARRAYSTRING(Array<String>)
```

**功能：** 字符串数组类型数据。

**起始版本：** 19

### func !=(MessageArrayValue)

```cangjie
public operator func !=(other: MessageArrayValue): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[MessageArrayValue](#enum-messagearrayvalue)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不等，返回true，否则返回false。|

### func ==(MessageArrayValue)

```cangjie
public operator func ==(other: MessageArrayValue): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[MessageArrayValue](#enum-messagearrayvalue)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的字符串表示。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的字符串表示。|