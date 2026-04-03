## class BreakIterator

```cangjie
public class BreakIterator {}
```

**功能：** 用于进行断句的处理器。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

### func current()

```cangjie
public func current(): Int32
```

**功能：** 获取[BreakIterator](#class-breakiterator)对象在当前处理的文本中的位置。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|BreakIterator在当前所处理的文本中的位置。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let iterator = getLineInstance("en")
iterator.setLineBreakText("Apple is my favorite fruit.")
let currentpos = iterator.current() // 0
```

### func first()

```cangjie
public func first(): Int32
```

**功能：** 将[BreakIterator](#class-breakiterator)对象设置到第一个可断句的分割点。第一个分割点总是被处理的文本的起始位置。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|被处理文本的第一个分割点的偏移量。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let iterator = getLineInstance("en")
iterator.setLineBreakText("Apple is my favorite fruit.")
let firstPos = iterator.first() // 0
```

### func following(Int32)

```cangjie
public func following(offset: Int32): Int32
```

**功能：** 将BreakIterator设置到指定位置的后面一个分割点。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offset|Int32|是|-|指定的位置。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回BreakIterator移动后的位置，如果由offset所指定的位置的下一个分割点超出了文本的范围则返回-1。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let iterator = getLineInstance("en")
iterator.setLineBreakText("Apple is my favorite fruit.")
var pos = iterator.following(0) // 6
pos = iterator.following(100) // -1
pos = iterator.current() // 27
```

### func getLineBreakText()

```cangjie
public func getLineBreakText(): String
```

**功能：** 获取BreakIterator当前处理的文本。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|[BreakIterator](#class-breakiterator)对象正在处理的文本。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let iterator = getLineInstance("en")
iterator.setLineBreakText("Apple is my favorite fruit.")
let res = iterator.getLineBreakText() // "Apple is my favorite fruit."
```

### func isBoundary(Int32)

```cangjie
public func isBoundary(offset: Int32): Bool
```

**功能：** 判断文本指定位置是否为分割点。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offset|Int32|是|-|指定的位置。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true表示offset指定的文本位置是一个分割点，false表示offset指定的文本位置不是一个分割点。返回true时，会将[BreakIterator](#class-breakiterator)对象移动到offset指定的位置，否则相当于调用following。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let iterator = getLineInstance("en")
iterator.setLineBreakText("Apple is my favorite fruit.")
var isBounDary = iterator.isBoundary(0) // true
isBounDary = iterator.isBoundary(5) // false
```