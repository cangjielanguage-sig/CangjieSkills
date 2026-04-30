### func lastIndexOf(Utf16String, Int64)

```cangjie
public func lastIndexOf(target: Utf16String, fromIndex: Int64): ?Int64
```

**功能：** 向前查找字符所在的位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|[Utf16String](#class-utf16string)|是|-|目标字符串。|
|fromIndex|Int64|是|-|当前字符串的查找起始位置，不填是 size。|

**返回值：**

|类型|说明|
|:----|:----|
|?Int64|首次找到目标字符串时返回位置索引，未找到时返回 None。|

### func lazySplit(Utf16String, Bool)

```cangjie
public func lazySplit(separator: Utf16String, remoteEmpty!: Bool = false): Iterator<Utf16String>
```

**功能：** 懒分割字符串。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|separator|[Utf16String](#class-utf16string)|是|-|分隔符。当分隔符为空字符串时，每个字符都是单独的元素。|
|remoteEmpty|Bool|否|false|是否删除空白元素。|

**返回值：**

|类型|说明|
|:----|:----|
|Iterator\<[Utf16String](#class-utf16string)>|分割后的元素迭代器。|

### func lazySplit(Utf16String, Int64, Bool)

```cangjie
public func lazySplit(separator: Utf16String, maxSplit: Int64, remoteEmpty!: Bool = false): Iterator<Utf16String>
```

**功能：** 懒分割字符串。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|separator|[Utf16String](#class-utf16string)|是|-|分隔符。当分隔符为空字符串时，每个字符都是单独的元素。|
|maxSplit|Int64|是|-|分割最大数量。为 0 时无上限。|
|remoteEmpty|Bool|否|false|是否删除空白元素。|

**返回值：**

|类型|说明|
|:----|:----|
|Iterator\<[Utf16String](#class-utf16string)>|分割后的元素迭代器。|

### func lines()

```cangjie
public func lines(): Iterator<Utf16String>
```

**功能：** 获取行迭代器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|Iterator\<[Utf16String](#class-utf16string)>|行迭代器。|

### func replace(Utf16String, Utf16String, Int64)

```cangjie
public func replace(old: Utf16String, new: Utf16String, count!: Int64 = Int64.Max): Utf16String
```

**功能：** 替换字符串。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|old|[Utf16String](#class-utf16string)|是|-|替换前的元素|
|new|[Utf16String](#class-utf16string)|是|-|替换后的元素|
|count|Int64|否|Int64.Max|替换次数|

**返回值：**

|类型|说明|
|:----|:----|
|[Utf16String](#class-utf16string)| 替换完的字符串 |

### func runes()

```cangjie
public func runes(): Iterator<Rune>
```

**功能：** 获取字符迭代器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|Iterator\<Rune>|字符迭代器。|

### func split(Utf16String, Bool)

```cangjie
public func split(seperator: Utf16String, remoteEmpty!: Bool = false): Array<Utf16String>
```

**功能：** 分割字符串。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|seperator|[Utf16String](#class-utf16string)|是|-|分隔符。当分隔符为空字符串时，每个字符都是单独的元素。|
|remoteEmpty|Bool|否|false|是否删除空白元素。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[Utf16String](#class-utf16string)>|分割后的元素数组。|