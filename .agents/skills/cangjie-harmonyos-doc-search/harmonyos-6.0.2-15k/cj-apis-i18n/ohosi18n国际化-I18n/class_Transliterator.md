## class Transliterator

```cangjie
public class Transliterator {}
```

**功能：** 音译对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

### static func getAvailableIDs()

```cangjie
public static func getAvailableIDs(): Array<String>
```

**功能：** 获取音译支持的ID列表。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|音译支持的ID列表。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

// ids共支持742个。每一个id由使用中划线分割的两部分组成，格式为source-destination。例如ids = ["Han-Latin","Latin-ASCII", "Amharic-Latin/BGN","Accents-Any", ...]，Han-Latin表示汉语转为译拉丁文，Amharic-Latin表示阿姆哈拉语转为拉丁文。
// 更多使用信息可以参考ISO-15924。
let ids = Transliterator.getAvailableIDs()
```

### static func getInstance(String)

```cangjie
public static func getInstance(id: String): Transliterator
```

**功能：** 创建音译对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|String|是|-|音译支持的ID。|

**返回值：**

|类型|说明|
|:----|:----|
|[Transliterator](#class-transliterator)|音译对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let transliterator = Transliterator.getInstance("Any-Latn")
```

### func transform(String)

```cangjie
public func transform(text: String): String
```

**功能：** 将输入字符串从源格式转换为目标格式。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|输入字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|String|转换后的字符串。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let transliterator = Transliterator.getInstance("Any-Latn")
let res = transliterator.transform("中国") // res = "zhōng guó"
```