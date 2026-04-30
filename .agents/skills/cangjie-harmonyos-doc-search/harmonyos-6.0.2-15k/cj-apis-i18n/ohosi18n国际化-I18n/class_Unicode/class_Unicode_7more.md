## class Unicode

```cangjie
public class Unicode {}
```

**功能：** 字符转换对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

### static func getType(String)

```cangjie
public static func getType(text: String): String
```

**功能：** 获取输入字符串的一般类别值。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|输入字符。|

**返回值：**

|类型|说明|
|:----|:----|
|String|输入字符的一般类别值。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let unicodeType = Unicode.getType("a") // unicodeType = "U_LOWERCASE_LETTER"
```

### static func isDigit(String)

```cangjie
public static func isDigit(text: String): Bool
```

**功能：** 判断字符串char是否是数字。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|输入字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示输入的字符是数字，返回false表示输入的字符不是数字。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let isdigit = Unicode.isDigit("a") // isdigit = false
```

### static func isIdeograph(String)

```cangjie
public static func isIdeograph(text: String): Bool
```

**功能：** 判断字符串char是否是表意文字。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|输入字符。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示输入的字符是表意文字，返回false表示输入的字符不是表意文字。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let isideograph = Unicode.isIdeograph("a") // isideograph = false
```

### static func isLetter(String)

```cangjie
public static func isLetter(text: String): Bool
```

**功能：** 判断字符串char是否是字母。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|输入字符。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示输入的字符是字母，返回false表示输入的字符不是字母。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let isletter = Unicode.isLetter("a") // isletter = true
```

### static func isLowerCase(String)

```cangjie
public static func isLowerCase(text: String): Bool
```

**功能：** 判断字符串char是否是小写字母。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|输入字符。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示输入的字符是小写字母，返回false表示输入的字符不是小写字母。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let islowercase = Unicode.isLowerCase("a") // islowercase = true
```

### static func isRTL(String)

```cangjie
public static func isRTL(text: String): Bool
```

**功能：** 判断字符串char是否是从右到左语言的字符。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|输入字符。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示输入的字符是从右到左语言的字符，返回false表示输入的字符不是从右到左语言的字符。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let isrtl = Unicode.isRTL("a") // isrtl = false
```