### func style(TextInputStyle)

```cangjie
public func style(value: TextInputStyle): This
```

**功能：** 设置输入框为默认风格或内联输入风格，内联输入风格只支持InputType.Normal类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[TextInputStyle](#enum-textinputstyle)|是|-|输入框为默认风格或内联输入风格。<br>初始值:TextInputStyle.Default。|

### func textAlign(TextAlign)

```cangjie
public func textAlign(value: TextAlign): This
```

**功能：** 设置文本在输入框中的水平对齐方式。

> **说明：**
>
> - 仅支持TextAlign.Start、TextAlign.Center和TextAlign.End。
> - 可通过[align](./cj-universal-attribute-location.md#func-alignalignment)属性控制文本段落在垂直方向上的位置，此组件中不可通过align属性控制文本段落在水平方向上的位置，即align属性中Alignment.TopStart、Alignment.Top、Alignment.TopEnd效果相同，控制内容在顶部，Alignment.Start、Alignment.Center、Alignment.End效果相同，控制内容垂直居中，Alignment.BottomStart、Alignment.Bottom、Alignment.BottomEnd效果相同，控制内容在底部。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[TextAlign](./cj-common-types.md#enum-textalign)|是|-|水平对齐方式。仅支持TextAlign.Start、TextAlign.Center和TextAlign.End。<br>初始值:TextAlign.Start。|

### func textIndent(Length)

```cangjie
public func textIndent(value: Length): This
```

**功能：** 设置首行文本缩进。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|首行文本缩进。<br>初始值:0。|

### func textOverflow(TextOverflow)

```cangjie
public func textOverflow(value: TextOverflow): This
```

**功能：** 设置文本超长时的显示方式。

> **说明：**
>
> - 仅在内联模式的编辑态、非编辑态下支持。
> - 文本截断是按字截断。例如，英文以单词为最小单位进行截断，若需要以字母为单位进行截断，[wordBreak](#func-wordbreakwordbreak)属性可设置为WordBreak.BREAK_ALL。
> - 设置TextOverflow.None与TextOverflow.Clip效果一样。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[TextOverflow](./cj-common-types.md#enum-textoverflow)|是|-|文本超长时的显示方式。<br>内联模式非编辑态下初始值：TextOverflow.Ellipsis。<br>内联模式编辑态下初始值：TextOverflow.Clip。|

### func underlineColor(ResourceColor)

```cangjie
public func underlineColor(color: ResourceColor): This
```

**功能：** 开启下划线时，支持配置下划线颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|下划线颜色。当设置下划线颜色模式时，修改下划线颜色。当只设定非特殊状态下的颜色，可以直接输入ResourceColor。<br>初始值：主题配置的下划线颜色。主题配置的默认下划线颜色为：0x33182431。|