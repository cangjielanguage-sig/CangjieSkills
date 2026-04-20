### func toString()

```cangjie
public func toString(): String
```

**功能：** 转换为 String。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|转换后的 String 对象。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func convertToString(context: JSContext): JSValue {
    let utf16Str = Utf16String("Hello Utf16String")
    let stringResult = utf16Str.toString()

    Hilog.info(0, "test", "Converted to string: ${stringResult}")

    return context.string(stringResult).toJSValue()
}
```

### operator func !=(Utf16String)

```cangjie
public operator func !=(target: Utf16String): Bool
```

**功能：** 判断与目标字符串是否不相等。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|[Utf16String](#class-utf16string)|是|-|比较的目标字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个字符串不相等返回true，否则返回false。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |

### operator func +(Utf16String)

```cangjie
public operator func +(right: Utf16String): Utf16String
```

**功能：** 往后拼接一个字符串。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|right|[Utf16String](#class-utf16string)|是|-|拼接的目标字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|[Utf16String](#class-utf16string)|拼接后的字符串。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |

### operator func \<(Utf16String)

```cangjie
public operator func <(target: Utf16String): Bool
```

**功能：** 判断是否小于目标字符串（按字符 Unicode 的字典序）。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|[Utf16String](#class-utf16string)|是|-|比较的目标字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|小于目标字符串返回true，否则返回false。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |

### operator func \<=(Utf16String)

```cangjie
public operator func <=(target: Utf16String): Bool
```

**功能：** 判断是否小于或等于目标字符串（按字符 Unicode 的字典序）。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|[Utf16String](#class-utf16string)|是|-|比较的目标字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|小于或等于目标字符串返回true，否则返回false。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |