### class RichEditorDeleteValue

```cangjie
public class RichEditorDeleteValue {
    public var offset: Int32
    public var direction: RichEditorDeleteDirection
    public var length: Int32
    public var richEditorDeleteSpans: ArrayList<RichEditorSpanResult>
    public init(
        offset: Int32,
        direction: RichEditorDeleteDirection,
        length: Int32,
        richEditorDeleteSpans: ArrayList<RichEditorSpanResult>
    )
}
```

**功能：** 提供从文本中删除值的接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var offset

```cangjie
public var offset: Int32
```

**功能：** 删除的偏移量。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var direction

```cangjie
public var direction: RichEditorDeleteDirection
```

**功能：** 删除的方向。

**类型：** [RichEditorDeleteDirection](./cj-common-types.md#enum-richeditordeletedirection)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var length

```cangjie
public var length: Int32
```

**功能：** 删除的文本长度。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var richEditorDeleteSpans

```cangjie
public var richEditorDeleteSpans: ArrayList<RichEditorSpanResult>
```

**功能：** 删除的span对象。

**类型：** ArrayList\<[RichEditorSpanResult](#interface-richeditorspanresult)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(Int32, RichEditorDeleteDirection, Int32, ArrayList\<RichEditorSpanResult>)

```cangjie
public init(
    offset: Int32,
    direction: RichEditorDeleteDirection,
    length: Int32,
    richEditorDeleteSpans: ArrayList<RichEditorSpanResult>
)
```

**功能：** RichEditorDeleteValue构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offset|Int32|是|-|删除的偏移量。|
|direction|[RichEditorDeleteDirection](./cj-common-types.md#enum-richeditordeletedirection)|是|-|删除的方向。|
|length|Int32|是|-|删除的文本长度。|
|richEditorDeleteSpans|ArrayList\<[RichEditorSpanResult](#interface-richeditorspanresult)>|是|-|删除的span对象。|