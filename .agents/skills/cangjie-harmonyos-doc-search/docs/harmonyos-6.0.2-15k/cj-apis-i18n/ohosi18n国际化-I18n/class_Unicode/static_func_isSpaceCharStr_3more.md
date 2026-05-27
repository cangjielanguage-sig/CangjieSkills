### static func isSpaceChar(String)

```cangjie
public static func isSpaceChar(text: String): Bool
```

**功能：** 判断字符串char是否是空格符。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|输入字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示输入的字符是空格符，返回false表示输入的字符不是空格符。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let isspacechar = Unicode.isSpaceChar("a") // isspacechar = false
```

### static func isUpperCase(String)

```cangjie
public static func isUpperCase(text: String): Bool
```

**功能：** 判断字符串char是否是大写字母。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|输入字符。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示输入的字符是大写字母，返回false表示输入的字符不是大写字母。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let isuppercase = Unicode.isUpperCase("a") // isuppercase = false
```

### static func isWhitespace(String)

```cangjie
public static func isWhitespace(text: String): Bool
```

**功能：** 判断字符串char是否是空白符。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示输入的字符是空白符，返回false表示输入的字符不是空白符。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let iswhitespace = Unicode.isWhitespace("a") // iswhitespace = false
```