### class FocusBoxStyle

```cangjie
public class FocusBoxStyle {
    public FocusBoxStyle (
        public var margin!: ?Length = None,
        public var strokeColor!: ?ColorMetrics = None,
        public var strokeWidth!: ?Length = None
    )
}
```

**功能：** 系统焦点框样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var margin

```cangjie
public var margin: ?Length = None
```

**功能：** 焦点框相对组件边缘的距离。正数代表外侧，负数代表内侧。不支持百分比。

**类型：**  [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**起始版本：** 19

#### var strokeColor

```cangjie
public var strokeColor: ?ColorMetrics = None
```

**功能：** 焦点框颜色。

**类型：** [ColorMetrics](./cj-universal-attribute-focus.md#class-colormetrics)

**读写能力：** 可读写

**起始版本：** 19

#### var strokeWidth

```cangjie
public var strokeWidth: ?Length = None
```

**功能：** 焦点框宽度。不支持负数与百分比。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**起始版本：** 19

#### FocusBoxStyle (public var margin!: ?Length = None, public var strokeColor!: ?ColorMetrics = None, public var strokeWidth!: ?Length = None)

```cangjie
public FocusBoxStyle (public var margin!: ?Length = None, public var strokeColor!: ?ColorMetrics = None, public var strokeWidth!: ?Length = None)
```

**功能：** 构造一个FocusBoxStyle类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
| :---- | :---- | :--- | :----- | :----------- |
| margin | [Length](./cj-common-types.md#interface-length) | 否   | None  | **命名参数。**  焦点框相对组件边缘的距离。<br>正数代表外侧，负数代表内侧。不支持百分比。 |
| strokeColor | [ColorMetrics](./cj-universal-attribute-focus.md#class-colormetrics) | 否   | None | **命名参数。**  焦点框颜色。 |
| strokeWidth | [Length](./cj-common-types.md#interface-length) | 否   | None  | **命名参数。**  焦点框宽度。<br>不支持负数与百分比。 |