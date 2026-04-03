## enum WordBreak

```cangjie
public enum WordBreak <: Equatable<WordBreak> {
    | Normal
    | BreakAll
    | BreakWord
    | ...
}
```

**功能：** 设置文本断行规则。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[WordBreak](#enum-wordbreak)>

### Normal

```cangjie
Normal
```

**功能：** CJK(中文、日文、韩文)文本可以在任意2个字符间断行，而Non-CJK文本（如英文等）只能在空白符处断行。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### BreakAll

```cangjie
BreakAll
```

**功能：** 对于Non-CJK的文本，可在任意2个字符间断行。对于CJK与NORMAL效果一致。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### BreakWord

```cangjie
BreakWord
```

**功能：** 与BREAKALL相同，对于Non-CJK的文本可在任意2个字符间断行，一行文本中有断行破发点（如空白符）时，优先按破发点换行，保障单词优先完整显示。若整一行文本均无断行破发点时，则在任意2个字符间断行。对于CJK与NORMAL效果一致。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(WordBreak)

```cangjie
public operator func ==(other: WordBreak): Bool
```

**功能：** 判断两个WordBreak枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WordBreak](#enum-wordbreak)|是|-|要比较的另一个WordBreak枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(WordBreak)

```cangjie
public operator func !=(other: WordBreak): Bool
```

**功能：** 判断两个WordBreak枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WordBreak](#enum-wordbreak)|是|-|要比较的另一个WordBreak枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|