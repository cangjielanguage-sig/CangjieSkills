## enum LineBreakStrategy

```cangjie
public enum LineBreakStrategy <: Equatable<LineBreakStrategy> {
    | Greedy
    | HighQuality
    | Balanced
    | ...
}
```

**功能：** 文本的折行规则。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[LineBreakStrategy](#enum-linebreakstrategy)>

### Greedy

```cangjie
Greedy
```

**功能：** 使每一行尽量显示多的字符，直到这一行不能显示更多字符再进行折行。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### HighQuality

```cangjie
HighQuality
```

**功能：** 在BALANCED的基础上，尽可能填满行，在最后一行的权重上比较低，可能会出现最后一行留白比较多。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Balanced

```cangjie
Balanced
```

**功能：** 尽可能保证在不拆词的情况下，使一个段落中每一行的宽度相同。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(LineBreakStrategy)

```cangjie
public operator func ==(other: LineBreakStrategy): Bool
```

**功能：** 判断两个LineBreakStrategy枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[LineBreakStrategy](#enum-linebreakstrategy)|是|-|要比较的另一个LineBreakStrategy枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(LineBreakStrategy)

```cangjie
public operator func !=(other: LineBreakStrategy): Bool
```

**功能：** 判断两个LineBreakStrategy枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[LineBreakStrategy](#enum-linebreakstrategy)|是|-|要比较的另一个LineBreakStrategy枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|