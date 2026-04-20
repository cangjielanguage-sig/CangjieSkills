### struct CJCaretOffset

```cangjie
public struct CJCaretOffset {
    public CJCaretOffset(
        public var index: Float64,
        public var x: Float64,
        public var y: Float64
    )
}
```

**功能：** 当前光标所在位置信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var index

```cangjie
public var index: Float64
```

**功能：** 设置光标所在位置的索引值。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

#### var x

```cangjie
public var x: Float64
```

**功能：** 设置光标相对输入框的x坐标位值。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

#### var y

```cangjie
public var y: Float64
```

**功能：** 设置光标相对输入框的y坐标位值。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

#### CJCaretOffset(Float64, Float64, Float64)

```cangjie
public CJCaretOffset(public var index: Float64, public var x: Float64, public var y: Float64)
```

**功能：** 创建CJCaretOffset的类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

| 参数名 | 类型 | 必填 | 默认值 | 说明                                |
| :----- | :------- | :--- | :----- | :---------------------------------- |
| index  | Float64  | 是   | -      | 光标所在位置的索引值。              |
| x      | Float64  | 是   | -      | 光标相对输入框的x坐标位值，单位：像素(px)。 |
| y      | Float64  | 是   | -      | 光标相对输入框的y坐标位值，单位：像素(px)。 |

### struct CJRectResult

```cangjie
public struct CJRectResult {
    public CJRectResult(
        public var x: Float64,
        public var y: Float64,
        public var width: Float64,
        public var height: Float64
    )
}
```

**功能：** 位置和尺寸类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var x

```cangjie
public var x: Float64
```

**功能：** 设置水平方向横坐标。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

#### var y

```cangjie
public var y: Float64
```

**功能：** 设置竖直方向纵坐标。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

#### var width

```cangjie
public var width: Float64
```

**功能：** 设置内容宽度大小。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

#### var height

```cangjie
public var height: Float64
```

**功能：** 设置内容高度大小。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

#### CJRectResult(Float64, Float64, Float64, Float64)

```cangjie
public CJRectResult(public var x: Float64, public var y: Float64, public var width: Float64, public var height: Float64)
```

**功能：** 创建CJRectResult类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

| 参数名 | 类型 | 必填 | 默认值 | 说明             |
| :----- | :------- | :--- | :----- | :--------------- |
| x      | Float64  | 是   | -      | 水平方向横坐标。 |
| y      | Float64  | 是   | -      | 竖直方向纵坐标。 |
| width  | Float64  | 是   | -      | 内容宽度大小。   |
| height | Float64  | 是   | -      | 内容高度大小。   |