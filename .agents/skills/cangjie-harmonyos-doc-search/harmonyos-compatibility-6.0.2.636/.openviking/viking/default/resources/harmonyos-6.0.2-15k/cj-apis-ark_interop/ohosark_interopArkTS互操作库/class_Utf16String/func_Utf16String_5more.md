### func ==(Utf16String)

```cangjie
public operator func == (target: Utf16String): Bool
```

**功能：** 判断与目标字符串是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|[Utf16String](#class-utf16string)|是|-|比较的目标字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个字符串相等返回true，否则返回false。|

### func >(Utf16String)

```cangjie
public operator func > (target: Utf16String): Bool
```

**功能：** 判断是否大于目标字符串（按字符 Unicode 的字典序）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|[Utf16String](#class-utf16string)|是|-|比较的目标字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|大于目标字符串返回true，否则返回false。|

### func >=(Utf16String)

```cangjie
public operator func >= (target: Utf16String): Bool
```

**功能：** 判断是否大于或等于目标字符串（按字符 Unicode 的字典序）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|[Utf16String](#class-utf16string)|是|-|比较的目标字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|大于或等于目标字符串返回true，否则返回false。|

### func \[](Int64)

```cangjie
public operator func [](index: Int64): UInt16
```

**功能：** 根据元素索引获取字符。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|下标。|

**返回值：**

| 类型     |说明|
|:-------|:----|
| UInt16 |获取到的字符。|

### func \[](Range\<Int64>)

```cangjie
public operator func [](range: Range<Int64>): Utf16String
```

**功能：** 从字符串截取一段子串。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|range|[Range](../apis/IMEKit/cj-apis-inputmethod.md#class-range)\<Int64>|是|-|截取范围。|

**返回值：**

|类型|说明|
|:----|:----|
|[Utf16String](#class-utf16string)|截取后的 Utf16String 字串。|