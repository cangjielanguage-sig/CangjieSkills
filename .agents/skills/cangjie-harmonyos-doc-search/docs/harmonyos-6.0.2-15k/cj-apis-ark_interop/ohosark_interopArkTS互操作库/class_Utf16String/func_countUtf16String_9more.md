### func count(Utf16String)

```cangjie
public func count(src: Utf16String): Int64
```

**功能：** 包含字符串次数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|[Utf16String](#class-utf16string)|是|-|目标字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|包含目标字符串的次数。|

### func dispose()

```cangjie
public func dispose(): Unit
```

**功能：** 释放保存字符串内容的内存。在首次 dispose 之后继续访问该字符串的内容将导致异常。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

### func endsWith(Utf16String)

```cangjie
public func endsWith(target: Utf16String): Bool
```

**功能：** 字符串是否以目标字符串结束。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|[Utf16String](#class-utf16string)|是|-|目标字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|是否以目标字符串结束。|

### func hashCode()

```cangjie
public func hashCode(): Int64
```

**功能：** 字符串 hash 值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|Int64|字符串 hash 值。<br>**注意：** 不保证该 hash 值与相同内容的 String 的 hash 一致。 不保证该 hash 值与相同内容的 ArkTS string 的 hash 一致。|

### func indexOf(Utf16String)

```cangjie
public func indexOf(target: Utf16String): ?Int64
```

**功能：** 向后查找字符串所在的位置（字符索引）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|[Utf16String](#class-utf16string)|是|-|目标字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|?Int64|首次找到目标字符串时返回位置索引，未找到时返回 None。|

### func indexOf(Utf16String, Int64)

```cangjie
public func indexOf(target: Utf16String, fromIndex: Int64): ?Int64
```

**功能：** 向后查找字符串所在的位置（编码单元索引）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|[Utf16String](#class-utf16string)|是|-|目标字符串。|
|fromIndex|Int64|是|-|当前字符串的查找起始位置，不填是 0。|

**返回值：**

|类型|说明|
|:----|:----|
|?Int64|首次找到目标字符串时返回位置索引，未找到时返回 None。|

### func isEmpty()

```cangjie
public func isEmpty(): Bool
```

**功能：** 是否为空字符串。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|Bool|是否为空字符串。|

### func isCompressed()

```cangjie
public func isCompressed(): Bool
```

**功能：** 判断内容是否被压缩。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|Bool| 是否被压缩 |

### func lastIndexOf(Utf16String)

```cangjie
public func lastIndexOf(target: Utf16String): ?Int64
```

**功能：** 向前查找字符所在的位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|[Utf16String](#class-utf16string)|是|-|目标字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|?Int64|首次找到目标字符串时返回位置索引，未找到时返回 None。|