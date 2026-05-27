### class TextCascadePickerRangeContent

```cangjie
public class TextCascadePickerRangeContent {
    public TextCascadePickerRangeContent(
        public var text: String,
        public var children!: Option<Array<TextCascadePickerRangeContent>> = Option.None
    )
}
```

**功能：** 多列联动数据选择器的数据选择列表。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var children

```cangjie
public var children: Option<Array<TextCascadePickerRangeContent>> = Option.None
```

**功能：** 联动数据。

**类型：** Option\<Array\<[TextCascadePickerRangeContent](#class-textcascadepickerrangecontent)>>

**读写能力：** 可读写

**起始版本：** 19

#### var text

```cangjie
public var text: String
```

**功能：** 文本信息。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

#### TextCascadePickerRangeContent(String, Option\<Array\<TextCascadePickerRangeContent>>)

```cangjie
public TextCascadePickerRangeContent(
    public var text: String,
    public var children!: Option<Array<TextCascadePickerRangeContent>> = Option.None
)
```

**功能：** 构造TextCascadePickerRangeContent对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|是|-|文本信息。<br>**说明：**<br>如果文本长度大于列宽时，文本被截断。|
|children|Option\<Array\<[TextCascadePickerRangeContent](#class-textcascadepickerrangecontent)>>|否|Option.None| **命名参数。** 联动数据。|