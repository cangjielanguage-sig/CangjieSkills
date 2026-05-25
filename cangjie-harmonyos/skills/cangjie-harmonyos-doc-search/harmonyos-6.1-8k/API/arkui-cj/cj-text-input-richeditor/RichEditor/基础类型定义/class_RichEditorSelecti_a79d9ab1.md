### class RichEditorSelection

```cangjie
public class RichEditorSelection {
    public var selection: (Int32, Int32)
    public var spans: ArrayList<RichEditorSpanResult>
    public init(selection: ?(Int32, Int32), spans: ?ArrayList<RichEditorSpanResult>)
}
```

**功能：** 选中内容信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var selection

```cangjie
public var selection: (Int32, Int32)
```

**功能：** 选中范围。

**类型：** (Int32, Int32)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var spans

```cangjie
public var spans: ArrayList<RichEditorSpanResult>
```

**功能：** 选中的文本内容。

**类型：** ArrayList\<[RichEditorSpanResult](#interface-richeditorspanresult)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?(Int32, Int32), ?ArrayList\<RichEditorSpanResult>)

```cangjie
public init(selection: ?(Int32, Int32), spans: ?ArrayList<RichEditorSpanResult>)
```

**功能：** RichEditorSelection构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|selection|?(Int32, Int32)|是|-|选中范围。初始值：(0, 0)。|
|spans|?ArrayList\<[RichEditorSpanResult](#interface-richeditorspanresult)>|是|-|选中的文本内容。初始值：ArrayList\<RichEditorSpanResult>()。|