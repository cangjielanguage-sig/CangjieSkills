### enum DynamicRangeMode

```cangjie
public enum DynamicRangeMode {
    | HIGH
    | CONSTRAINT
    | STANDARD
}
```

**功能：** 期望展示的图像动态范围。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### CONSTRAINT

```cangjie
CONSTRAINT
```

**功能：** 受限动态范围，受限进行图片提亮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### HIGH

```cangjie
HIGH
```

**功能：** 不受限动态范围，最大限度进行图片提亮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### STANDARD

```cangjie
STANDARD
```

**功能：** 标准动态范围，不进行图片提亮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### enum ImageContent

```cangjie
public enum ImageContent {
    | EMPTY
}
```

**功能：** 指定图像内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### EMPTY

```cangjie
EMPTY
```

**功能：** 空图像。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### enum ImageInterpolation

```cangjie
public enum ImageInterpolation {
    | None
    | High
    | Medium
    | Low
}
```

**功能：** 图片的插值效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### None

```cangjie
None
```

**功能：** 不使用插值图片数据。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### High

```cangjie
High
```

**功能：** 插值图片数据的使用率高，可能会影响图片渲染的速度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### Medium

```cangjie
Medium
```

**功能：** 插值图片数据的使用率中。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### Low

```cangjie
Low
```

**功能：** 插值图片数据的使用率低。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### enum ImageRenderMode

```cangjie
public enum ImageRenderMode {
    | Original
    | Template
}
```

**功能：** 图片渲染的模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### Original

```cangjie
Original
```

**功能：** 按照原图进行渲染，包括颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### Template

```cangjie
Template
```

**功能：** 将图片渲染为模板图片，忽略图片的颜色信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12