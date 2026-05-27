### class TextPickerOptions

```cangjie
public class TextPickerOptions {
    public TextPickerOptions(
        public var range : Array<String>,
        public var selected!: Option<UInt32> = Option.None,
        public var value!: Option<String> = Option.None
    )
}
```

**功能：** 配置文本选择器的参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var range

```cangjie
public var range: Array<String>
```

**功能：** 选择器的数据选择列表。不可设置为空数组，若设置为空数组，则不显示；若动态变化为空数组，则保持当前正常值显示。

**类型：** Array\<String>

**读写能力：** 可读写

**起始版本：** 19

#### var selected

```cangjie
public var selected: Option<UInt32> = Option.None
```

**功能：** 设置默认选中项在数组中的索引值。

**类型：** Option\<UInt32>

**读写能力：** 可读写

**起始版本：** 19

#### var value

```cangjie
public var value: Option<String> = Option.None
```

**功能：** 设置默认选中项的值，优先级低于selected。

**类型：** Option\<String>

**读写能力：** 可读写

**起始版本：** 19

#### TextPickerOptions(Array\<String>, Option\<UInt32>, Option\<String>)

```cangjie
public TextPickerOptions(
    public var range : Array<String>,
    public var selected!: Option<UInt32> = Option.None,
    public var value!: Option<String> = Option.None
)
```

**功能：** 构造TextPickerOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|range|Array\<String>|是|-|选择器的数据选择列表。不可设置为空数组，若设置为空数组，则不显示；若动态变化为空数组，则保持当前正常值显示。|
|selected|Option\<UInt32>|否|Option.None| **命名参数。** 设置默认选中项在数组中的索引值。<br>初始值：0|
|value|Option\<String>|否|Option.None| **命名参数。** 设置默认选中项的值，优先级低于selected。<br>初始值：第一个元素值<br>**说明：**<br>只有显示文本列表时该值有效。显示图片或图片加文本的列表时，该值无效。|