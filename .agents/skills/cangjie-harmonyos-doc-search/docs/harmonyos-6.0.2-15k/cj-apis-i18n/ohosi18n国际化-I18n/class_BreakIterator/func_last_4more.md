### func last()

```cangjie
public func last(): Int32
```

**功能：** 将[BreakIterator](#class-breakiterator)对象的位置设置到最后一个可断句的分割点。最后一个分割点总是被处理文本末尾的下一个位置。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|被处理的文本的最后一个分割点的偏移量。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let iterator = getLineInstance("en")
iterator.setLineBreakText("Apple is my favorite fruit.")
let lastPos = iterator.last() // 27
```

### func next(Int32)

```cangjie
public func next(index!: Int32 = 1): Int32
```

**功能：** 将BreakIterator向后移动相应个分割点。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|否|1| **命名参数。** BreakIterator将要移动的分割点数。正数代表向后移动，即将BreakIterator向后移动number个可断句的分割点；负数代表向前移动，即向前移动相应个分割点。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回移动了index个分割点后，当前BreakIterator在文本中的位置。若移动index个分割点后超出了所处理的文本的长度范围，返回-1。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let iterator = getLineInstance("en")
iterator.setLineBreakText("Apple is my favorite fruit.")
var pos = iterator.first() // 0
pos = iterator.next() // 6
pos = iterator.next(10) // -1
```

### func previous()

```cangjie
public func previous(): Int32
```

**功能：** 将BreakIterator向前移动一个分割点。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回移动到前一个分割点后，当前BreakIterator在文本中的位置。若移动index个分割点后超出了所处理的文本的长度范围，返回-1。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let iterator = getLineInstance("en")
iterator.setLineBreakText("Apple is my favorite fruit.")
var pos = iterator.first() // 0
pos = iterator.next(3) // 12
pos = iterator.previous() // 9
```

### func setLineBreakText(String)

```cangjie
public func setLineBreakText(text: String): Unit
```

**功能：** 设置BreakIterator要处理的文本。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|指定BreakIterator进行断句的文本。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*

let iterator = getLineInstance("en")
iterator.setLineBreakText("Apple is my favorite fruit.") // 设置断句文本
```