# TextPicker

滑动选择文本内容的组件。

## 子组件

无

## 创建组件

### init(TextPickerOptions)

```cangjie
public init(options:TextPickerOptions)
```

**功能：** 根据range指定的选择范围创建文本选择器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[TextPickerOptions](#class-textpickeroptions)|是|-|配置文本选择器的参数。|

### init(Array\<String>, Option\<UInt32>, Option\<String>)

```cangjie
public init(
    range: Array<String>,
    selected!: Option<UInt32> = Option.None,
    value!: Option<String> = Option.None
)
```

**功能：** 根据range指定的选择范围创建文本选择器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|range|Array\<String>|是|-|选择器的数据选择列表。不可设置为空数组，若设置为空数组，则不显示；若动态变化为空数组，则保持当前正常值显示。|
|selected|Option\<UInt32>|否|Option.None| **命名参数。** 设置默认选中项在数组中的索引值。<br>初始值：0。|
|value|Option\<String>|否|Option.None| **命名参数。** 设置默认选中项的值，优先级低于selected。<br>初始值：第一个元素值。<br>**说明：**<br>只有显示文本列表时该值有效。显示图片或图片加文本的列表时，该值无效。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。