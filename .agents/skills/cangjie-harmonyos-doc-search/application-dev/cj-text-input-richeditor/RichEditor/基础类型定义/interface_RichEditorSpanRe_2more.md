### interface RichEditorSpanResult

```cangjie
public interface RichEditorSpanResult {}
```

**功能：** 定义RichEditor span结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### class RichEditorSpanPosition

```cangjie
public class RichEditorSpanPosition {
    public var spanIndex: ?Int32
    public var spanRange: ?(Int32, Int32)
    public init(
        spanIndex: ?Int32,
        spanRange: ?(Int32, Int32)
    )
}
```

**功能：** 定义span位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var spanIndex

```cangjie
public var spanIndex: ?Int32
```

**功能：** 定义span的索引。

**类型：** ?Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var spanRange

```cangjie
public var spanRange: ?(Int32, Int32)
```

**功能：** span的范围。

**类型：** ?(Int32, Int32)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?Int32, ?(Int32, Int32))

```cangjie
public init(
    spanIndex: ?Int32,
    spanRange: ?(Int32, Int32)
)
```

**功能：** RichEditorSpanPosition构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|spanIndex|?Int32|是|-|span索引。初始值：0。|
|spanRange|?(Int32, Int32)|是|-|span范围。初始值：(0, 0)。|