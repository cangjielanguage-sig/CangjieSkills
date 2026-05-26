### enum SearchType

```cangjie
public enum SearchType {
    | NORMAL
    | NUMBER
    | PHONE_NUMBER
    | EMAIL
    | NUMBER_DECIMAL
    | URL
}
```

**功能：** 表示输入框样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### EMAIL

```cangjie
EMAIL
```

**功能：** 表示邮箱地址输入模式。支持数字，字母，下划线、小数点、!、#、$、%、&、'、*、+、-、/、=、?、^、`、{、|、}、~，以及@字符（只能存在一个@字符）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### NORMAL

```cangjie
NORMAL
```

**功能：** 表示基本输入模式。支持输入数字、字母、下划线、空格、特殊字符。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### NUMBER

```cangjie
NUMBER
```

**功能：** 表示纯数字输入模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### NUMBER_DECIMAL

```cangjie
NUMBER_DECIMAL
```

**功能：** 表示带小数点的数字输入模式。支持数字、小数点（只能存在一个小数点）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### PHONE_NUMBER

```cangjie
PHONE_NUMBER
```

**功能：** 表示电话号码输入模式。支持输入数字、空格、+ 、-、*、#、(、)，长度不限。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### URL

```cangjie
URL
```

**功能：** 表示带URL的输入模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### enum CancelButtonStyle

```cangjie
public enum CancelButtonStyle {
    | CONSTANT
    | INVISIBLE
    | INPUT
}
```

**功能：** 表示文本清除按钮样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### CONSTANT

```cangjie
CONSTANT
```

**功能：** 表示清除按钮常显样式。

**起始版本：** 19

#### INPUT

```cangjie
INPUT
```

**功能：** 表示清除按钮输入样式。

**起始版本：** 19

#### INVISIBLE

```cangjie
INVISIBLE
```

**功能：** 表示清除按钮常隐样式。

**起始版本：** 19