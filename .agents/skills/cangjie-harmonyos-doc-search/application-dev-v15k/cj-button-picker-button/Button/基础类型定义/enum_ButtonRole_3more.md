### enum ButtonRole

```cangjie
public enum ButtonRole {
    | NORMAL
    | ERROR
}
```

**功能：** 按钮的角色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### ERROR

```cangjie
ERROR
```

**功能：** 警示按钮。

**起始版本：** 19

#### NORMAL

```cangjie
NORMAL
```

**功能：** 正常按钮。

**起始版本：** 19

#### func getValue()<sup>(deprecated)</sup>

```cangjie
public func getValue(): Int32
```

**功能：** 获取类型值。

**返回值：**

|类型|说明|
|:----|:----|
|Int32|按钮角色类型值，0为正常按钮，1为警示按钮。|

### enum ButtonStyleMode

```cangjie
public enum ButtonStyleMode {
    | NORMAL
    | EMPHASIZED
    | TEXTUAL
}
```

**功能：** 按钮的重要程度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### EMPHASIZED

```cangjie
EMPHASIZED
```

**功能：** 强调按钮（用于强调当前操作）。

**起始版本：** 19

#### NORMAL

```cangjie
NORMAL
```

**功能：** 普通按钮（一般界面操作）。

**起始版本：** 19

#### TEXTUAL

```cangjie
TEXTUAL
```

**功能：** 文本按钮（纯文本，无背景颜色）。

**起始版本：** 19

#### func getValue()<sup>(deprecated)</sup>

```cangjie
public func getValue(): Int32
```

**功能：** 获取类型值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|0代表普通按钮，1代表强调按钮，2代表文本按钮。|

### enum ButtonType

```cangjie
public enum ButtonType {
    | Normal
    | Capsule
    | Circle
    | ROUNDED_RECTANGLE
}
```

**功能：** 按键形状类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### Capsule

```cangjie
Capsule
```

**功能：** 胶囊型按钮（圆角默认为高度的一半）。

**起始版本：** 19

#### Circle

```cangjie
Circle
```

**功能：** 圆形按钮。

**起始版本：** 19

#### Normal

```cangjie
Normal
```

**功能：** 普通按钮（默认不带圆角）。

**起始版本：** 19

#### ROUNDED_RECTANGLE

```cangjie
ROUNDED_RECTANGLE
```

**功能：** 圆角矩形按钮。

**起始版本：** 19