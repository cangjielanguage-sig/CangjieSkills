### class RichEditorDeleteValue

```cangjie
public class RichEditorDeleteValue {
    public RichEditorDeleteValue(
        public var offset: Int32,
        public var direction: RichEditorDeleteDirection,
        public var length: Int32,
        public var richEditorDeleteSpans: ArrayList<RichEditorSpanResult>
    )
}
```

**功能：** 删除操作的信息和被删除内容的信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var direction

```cangjie
public var direction: RichEditorDeleteDirection
```

**功能：** 表示删除操作的方向。

**类型：** [RichEditorDeleteDirection](#enum-richeditordeletedirection)

**读写能力：** 可读写

**起始版本：** 12

#### var length

```cangjie
public var length: Int32
```

**功能：** 表示删除内容长度。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 12

#### var offset

```cangjie
public var offset: Int32
```

**功能：** 表示删除内容的偏移位置。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 12

#### var richEditorDeleteSpans

```cangjie
public var richEditorDeleteSpans: ArrayList<RichEditorSpanResult>
```

**功能：** 表示删除的文本或者图片Span的具体信息。

**类型：** ArrayList\<[RichEditorSpanResult](#class-richeditorspanresult)>

**读写能力：** 可读写

**起始版本：** 12

#### RichEditorDeleteValue(Int32, RichEditorDeleteDirection, Int32, ArrayList\<RichEditorSpanResult>)

```cangjie
public RichEditorDeleteValue(
    public var offset: Int32,
    public var direction: RichEditorDeleteDirection,
    public var length: Int32,
    public var richEditorDeleteSpans: ArrayList<RichEditorSpanResult>
)
```

**功能：** 创建RichEditorDeleteValue类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offset|Int32|是|-|删除内容的偏移位置。|
|direction|[RichEditorDeleteDirection](#enum-richeditordeletedirection)|是|-|删除操作的方向。|
|length|Int32|是|-|删除内容长度。|
|richEditorDeleteSpans|ArrayList\<[RichEditorSpanResult](#class-richeditorspanresult)>|是|-|删除的文本或者图片Span的具体信息。|