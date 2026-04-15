### enum LeadingMarginType

```cangjie
public enum LeadingMarginType {
    | LengthType(Length)
    | PlaceholderType(LeadingMarginPlaceholder)
    | None
    | ...
}
```

**功能：** 定义首行缩进类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### LengthType(Length)

```cangjie
LengthType(Length)
```

**功能：** 长度类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### PlaceholderType(LeadingMarginPlaceholder)

```cangjie
PlaceholderType(LeadingMarginPlaceholder)
```

**功能：** 占位符类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### None

```cangjie
None
```

**功能：** 无。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### type PasteEventCallback

```cangjie
public type PasteEventCallback = (PasteEvent) -> Unit
```

**功能：** 执行粘贴操作时的回调函数。

**类型：** ([PasteEvent](#class-pasteevent)) -> Unit

### type OnDidChangeCallback

```cangjie
public type OnDidChangeCallback = (rangeBefore: TextRange, rangeAfter: TextRange) -> Unit
```

**功能：** 内容更改后的回调函数。

**类型：** ([TextRange](#class-textrange), [TextRange](#class-textrange)) -> Unit