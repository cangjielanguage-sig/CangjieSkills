### enum TextSpanType

```cangjie
public enum TextSpanType {
    | TEXT
    | IMAGE
    | MIXED
}
```

**功能：** 表示[Span](./cj-text-input-span.md#span)类型信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### IMAGE

```cangjie
IMAGE
```

**功能：** 表示Span为图像类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### MIXED

```cangjie
MIXED
```

**功能：** 表示Span为图文混合类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### TEXT

```cangjie
TEXT
```

**功能：** 表示Span为文字类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### enum TextResponseType

```cangjie
public enum TextResponseType {
    | RIGHT_CLICK
    | LONG_PRESS
    | SELECT
}
```

**功能：** 表示文本选择菜单的响应类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### LONG_PRESS

```cangjie
LONG_PRESS
```

**功能：** 表示通过长按触发菜单弹出。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### RIGHT_CLICK

```cangjie
RIGHT_CLICK
```

**功能：** 表示通过鼠标右键触发菜单弹出。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### SELECT

```cangjie
SELECT
```

**功能：** 表示通过鼠标选中触发菜单弹出。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### enum TextDataDetectorType

```cangjie
public enum TextDataDetectorType {
    | PHONE_NUMBER
    | URL
    | EMAIL
    | ADDRESS
    | DATE_TIME
}
```

**功能：** 表示文本识别的实体类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### ADDRESS

```cangjie
ADDRESS
```

**功能：** 表示地址。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### DATE_TIME

```cangjie
DATE_TIME
```

**功能：** 表示时间。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### EMAIL

```cangjie
EMAIL
```

**功能：** 表示邮箱。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### PHONE_NUMBER

```cangjie
PHONE_NUMBER
```

**功能：** 表示电话号码。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### URL

```cangjie
URL
```

**功能：** 表示链接。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### enum TextSelectable

```cangjie
public enum TextSelectable {
    | SELECTABLE_UNFOCUSABLE
    | SELECTABLE_FOCUSABLE
    | UNSELECTABLE
}
```

**功能：** 表示文本是否支持可选择、可获焦。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### SELECTABLE_FOCUSABLE

```cangjie
SELECTABLE_FOCUSABLE
```

**功能：** 表示文本可选择，可获焦并Touch后获得焦点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### SELECTABLE_UNFOCUSABLE

```cangjie
SELECTABLE_UNFOCUSABLE
```

**功能：** 表示文本可选择，但不可获焦，设置属性selection、bindSelectionMenu、copyOption不影响当前行为。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### UNSELECTABLE

```cangjie
UNSELECTABLE
```

**功能：** 表示文本不可选择，不可获焦，设置属性selection、bindSelectionMenu、copyOption都不生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19