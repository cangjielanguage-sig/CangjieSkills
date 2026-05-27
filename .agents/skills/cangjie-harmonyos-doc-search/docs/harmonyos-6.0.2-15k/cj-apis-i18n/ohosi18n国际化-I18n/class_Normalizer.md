## class Normalizer

```cangjie
public class Normalizer {}
```

**功能：** 正则序列化对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

### static func getInstance(NormalizerMode)

```cangjie
public static func getInstance(mode: NormalizerMode): Normalizer
```

**功能：** 获取文本正则化对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mode|[NormalizerMode](#enum-normalizermode)|是|-|文本正则化范式。|

**返回值：**

|类型|说明|
|:----|:----|
|[Normalizer](#class-normalizer)|返回指定范式的文本正则化对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let normalizer = Normalizer.getInstance(NormalizerMode.NFC)
```

### func normalize(String)

```cangjie
public func normalize(text: String): String
```

**功能：** 对字符串进行正则化。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|待正则化的字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|String|正则化后的字符串。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let normalizer = Normalizer.getInstance(NormalizerMode.NFC)
let normalizedText = normalizer.normalize("\u{1E9B}\u{0323}") // normalizedText = ẛ̣
```