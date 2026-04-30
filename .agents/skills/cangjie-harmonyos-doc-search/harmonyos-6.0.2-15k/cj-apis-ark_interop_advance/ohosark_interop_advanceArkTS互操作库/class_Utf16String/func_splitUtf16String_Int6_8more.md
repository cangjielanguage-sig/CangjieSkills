### func split(Utf16String, Int64, Bool)

```cangjie
public func split(seperator: Utf16String, maxSplit: Int64, remoteEmpty!: Bool = false): Array<Utf16String>
```

**功能：** 分割字符串。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|seperator|[Utf16String](#class-utf16string)|是|-|分隔符。当分隔符为空字符串时，每个字符都是单独的元素。|
|maxSplit|Int64|是|-|分割最大数量。为 0 时无上限。|
|remoteEmpty|Bool|否|false|是否删除空白元素。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[Utf16String](#class-utf16string)>|分割后的元素数组。|

### func startsWith(Utf16String)

```cangjie
public func startsWith(target: Utf16String): Bool
```

**功能：** 字符串是否以目标字符串开头。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|[Utf16String](#class-utf16string)|是|-|目标字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|是否以目标字符串开头。|

### func toJSValue(JSContext)

```cangjie
public func toJSValue(context: JSContext): JSValue
```

**功能：** 将 Utf16String 对象转换成 JSValue。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|ArkTS 统一类型。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 转换为 String。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|String|转换后的 String 对象。|

### func !=(Utf16String)

```cangjie
public operator func != (target: Utf16String): Bool
```

**功能：** 判断与目标字符串是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|[Utf16String](#class-utf16string)|是|-|比较的目标字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个字符串不相等返回true，否则返回false。|

### func +(Utf16String)

```cangjie
public operator func + (right: Utf16String): Utf16String
```

**功能：** 往后拼接一个字符串。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|right|[Utf16String](#class-utf16string)|是|-|拼接的目标字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|[Utf16String](#class-utf16string)|拼接后的字符串。|

### func \<(Utf16String)

```cangjie
public operator func < (target: Utf16String): Bool
```

**功能：** 判断是否小于目标字符串（按字符 Unicode 的字典序）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|[Utf16String](#class-utf16string)|是|-|比较的目标字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|小于目标字符串返回true，否则返回false。|

### func \<=(Utf16String)

```cangjie
public operator func <= (target: Utf16String): Bool
```

**功能：** 判断是否小于或等于目标字符串（按字符 Unicode 的字典序）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|[Utf16String](#class-utf16string)|是|-|比较的目标字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|小于或等于目标字符串返回true，否则返回false。|