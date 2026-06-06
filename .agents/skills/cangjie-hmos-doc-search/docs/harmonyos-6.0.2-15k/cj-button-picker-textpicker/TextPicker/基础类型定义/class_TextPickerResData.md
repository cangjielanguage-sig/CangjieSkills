### class TextPickerResData

```cangjie
public class TextPickerResData {
    public var value: String
    public var index: UInt32
    public init(value: String, index: UInt32)
}
```

**功能：** TextPickerResData用做onChange事件的参数，返回当前选择的文本index以及value。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var index

```cangjie
public var index: UInt32
```

**功能：** 当前选中项的索引值。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var value

```cangjie
public var value: String
```

**功能：** 当前选中项的文本。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(String, UInt32)

```cangjie
public init(value: String, index: UInt32)
```

**功能：** 创建TextPickerResData实例。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|设置默认选中项的值，优先级低于selected。初始值：第一个元素值。<br/>**说明：**<br/>只有显示文本列表时该值有效。显示图片或图片加文本的列表时，该值无效。|
|index|UInt32|是|-|设置默认选中项在数组中的索引值。初始值：0。|