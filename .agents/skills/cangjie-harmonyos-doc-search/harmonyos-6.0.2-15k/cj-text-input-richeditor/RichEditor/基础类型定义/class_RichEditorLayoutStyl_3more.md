### class RichEditorLayoutStyleResult

```cangjie
public class RichEditorLayoutStyleResult {
    public var borderRadius: String = ""
    public var margin: String = ""
}
```

**功能：** 图片布局风格。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var borderRadius

```cangjie
public var borderRadius: String = ""
```

**功能：** 圆角类型，用于描述组件边框圆角半径。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var margin

```cangjie
public var margin: String = ""
```

**功能：** 外边距类型，用于描述组件不同方向的外边距。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### class RichEditorSelection

```cangjie
public class RichEditorSelection {
    public RichEditorSelection(
        public var selection: (Int32, Int32),
        public var spans: ArrayList<RichEditorSpanResult>
    )
}
```

**功能：** 选中内容信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var selection

```cangjie
public var selection:(Int32, Int32)
```

**功能：** 表示选中范围。

**类型：** (Int32, Int32)

**读写能力：** 可读写

**起始版本：** 12

#### var spans

```cangjie
public var spans: ArrayList<RichEditorSpanResult>
```

**功能：** 表示Span信息。

**类型：** ArrayList\<[RichEditorSpanResult](#class-richeditorspanresult)>

**读写能力：** 可读写

**起始版本：** 12

#### RichEditorSelection((Int32, Int32), ArrayList\<RichEditorSpanResult>)

```cangjie
public RichEditorSelection(
    public var selection: (Int32, Int32),
    public var spans: ArrayList<RichEditorSpanResult>
)
```

**功能：** 创建RichEditorSelection类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|selection|(Int32, Int32)|是|-|选中范围。|
|spans|ArrayList\<[RichEditorSpanResult](#class-richeditorspanresult)>|是|-|Span信息。|

### class RichEditorSpanPosition

```cangjie
public class RichEditorSpanPosition {
    public RichEditorSpanPosition(
        public var spanIndex: Int32,
        public var spanRange: (Int32, Int32)
    )
}
```

**功能：** Span位置信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var spanIndex

```cangjie
public var spanIndex: Int32
```

**功能：** 表示Span索引值。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 12

#### var spanRange

```cangjie
public var spanRange:(Int32, Int32)
```

**功能：** 表示Span内容在RichEditor内的起始和结束位置。

**类型：** (Int32, Int32)

**读写能力：** 可读写

**起始版本：** 12

#### RichEditorSpanPosition(Int32, (Int32, Int32))

```cangjie
public RichEditorSpanPosition(
    public var spanIndex: Int32,
    public var spanRange: (Int32, Int32)
)
```

**功能：** 创建RichEditorSpanPosition类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|spanIndex|Int32|是|-|Span索引值。|
|spanRange|(Int32, Int32)|是|-|Span内容在RichEditor内的起始和结束位置。|