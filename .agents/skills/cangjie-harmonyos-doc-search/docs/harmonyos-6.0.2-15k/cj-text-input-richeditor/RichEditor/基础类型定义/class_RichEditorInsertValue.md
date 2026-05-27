### class RichEditorInsertValue

```cangjie
public class RichEditorInsertValue {
    public var insertOffset: Int32
    public var insertValue: String
    public var previewText: String = ""

    public init(
        insertOffset: Int32,
        insertValue: String
    )
    public init(
        insertOffset: Int32,
        insertValue: String,
        previewText: String
    )
}
```

**功能：** 插入文本信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var insertOffset

```cangjie
public var insertOffset: Int32
```

**功能：** 表示插入的文本偏移位置。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var insertValue

```cangjie
public var insertValue: String
```

**功能：** 表示插入的文本内容。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var previewText

```cangjie
public var previewText: String
```

**功能：** 表示插入的预上屏文本内容。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Int32, String)

```cangjie
public init(
    insertOffset: Int32,
    insertValue: String
)
```

**功能：** 创建RichEditorInsertValue类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|insertOffset|Int32|是|-|插入的文本偏移位置。|
|insertValue|String|是|-|插入的文本内容。|

#### init(Int32, String, String)

```cangjie
public init(
    insertOffset: Int32,
    insertValue: String,
    previewText: String
)
```

**功能：** 创建RichEditorInsertValue类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|insertOffset|Int32|是|-|插入的文本偏移位置。|
|insertValue|String|是|-|插入的文本内容。|
|previewText|String|是|-|插入的预上屏文本内容。|