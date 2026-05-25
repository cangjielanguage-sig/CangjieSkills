## enum RelateType

```cangjie
public enum RelateType {
    | FILL
    | FIT
}
```

**功能：** 子组件缩放状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### FILL

```cangjie
FILL
```

**功能：** 缩放当前子组件以填充满父组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### FIT

```cangjie
FIT
```

**功能：** 缩放当前子组件以自适应父组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum Repetition

```cangjie
public enum Repetition {
    | repeat
    | repeat_x
    | repeat_y
    | no_repeat
    | clamp
    | mirror
}
```

**功能：** 设置图像重复的方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### clamp

```cangjie
clamp
```

**功能：** 在原始边界外绘制时，超出部分使用边缘的颜色绘制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### mirror

```cangjie
mirror
```

**功能：** 沿x轴和y轴重复翻转绘制图像。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### no_repeat

```cangjie
no_repeat
```

**功能：** 不重复绘制图像。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### repeat

```cangjie
repeat
```

**功能：** 沿x轴和y轴重复绘制图像。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### repeat_x

```cangjie
repeat_x
```

**功能：** 沿x轴重复绘制图像。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### repeat_y

```cangjie
repeat_y
```

**功能：** 沿y轴重复绘制图像。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum ResourceType

```cangjie
public enum ResourceType {
    | ResColor
    | Float
    | String
    | Plural
    | Boolean
    | IntArray
    | Integer
    | Pattern
    | StrArray
    | Media
    | Rawfile
}
```

**功能：** 写入资源的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Boolean

```cangjie
Boolean
```

**功能：** Bool类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Float

```cangjie
Float
```

**功能：** Float类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### IntArray

```cangjie
IntArray
```

**功能：** int数组类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Integer

```cangjie
Integer
```

**功能：** Integer类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Media

```cangjie
Media
```

**功能：** Media类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Pattern

```cangjie
Pattern
```

**功能：** Pattern类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Plural

```cangjie
Plural
```

**功能：** Plural类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Rawfile

```cangjie
Rawfile
```

**功能：** Rawfile类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### ResColor

```cangjie
ResColor
```

**功能：** ResColor类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### StrArray

```cangjie
StrArray
```

**功能：** StrArray类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### String

```cangjie
String
```

**功能：** String类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum ResponseType

```cangjie
public enum ResponseType {
    | RightClick
    | LongPress
}
```

**功能：** 响应类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### LongPress

```cangjie
LongPress
```

**功能：** 通过长按触发菜单弹出。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### RightClick

```cangjie
RightClick
```

**功能：** 通过鼠标右键触发菜单弹出。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12