## enum TextMoveUnit

```cangjie
public enum TextMoveUnit <: Equatable<TextMoveUnit> & ToString {
    | TEXTMOVEUNIT_CHAR
    | TEXTMOVEUNIT_WORD
    | TEXTMOVEUNIT_LINE
    | TEXTMOVEUNIT_PAGE
    | TEXTMOVEUNIT_PARAGRAPH
    | ...
}
```

**功能：** 文本无障碍导航移动粒度。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**父类型：**

- Equatable\<TextMoveUnit>
- ToString

### TEXTMOVEUNIT_CHAR

```cangjie
TEXTMOVEUNIT_CHAR
```

**功能：** 表示以字符为移动粒度遍历节点文本。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### TEXTMOVEUNIT_LINE

```cangjie
TEXTMOVEUNIT_LINE
```

**功能：** 表示以行为移动粒度遍历节点文本。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### TEXTMOVEUNIT_PAGE

```cangjie
TEXTMOVEUNIT_PAGE
```

**功能：** 表示以页为移动粒度遍历节点文本。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### TEXTMOVEUNIT_PARAGRAPH

```cangjie
TEXTMOVEUNIT_PARAGRAPH
```

**功能：** 表示以段落为移动粒度遍历节点文本。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### TEXTMOVEUNIT_WORD

```cangjie
TEXTMOVEUNIT_WORD
```

**功能：** 表示以词为移动粒度遍历节点文本。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### func !=(TextMoveUnit)

```cangjie
public operator func !=(other: TextMoveUnit): Bool
```

**功能：** 对文本移动粒度进行判不等。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[TextMoveUnit](#enum-textmoveunit)|是|-|文本移动粒度。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|若对文本移动粒度不同，返回true，否则返回false。|

### func ==(TextMoveUnit)

```cangjie
public operator func ==(other: TextMoveUnit): Bool
```

**功能：** 对文本移动粒度进行判等。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[TextMoveUnit](#enum-textmoveunit)|是|-|文本移动粒度。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|若对文本移动粒度相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 将文本移动粒度转换为字符串。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|文本移动粒度的字符串表示。|