### func responseRegion(Rectangle)

```cangjie
public func responseRegion(rect: Rectangle): This
```

**功能：** 设置一个或多个触摸热区。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rect|[Rectangle](cj-common-types.md#class-rectangle)|是|-|一个或多个触摸热区，包括位置和大小。默认触摸热区为整个组件。<br>初始值：{x:0, y:0, width：'100%', height：'100%'}。|

### func responseRegionArray(Array\<Rectangle>)

```cangjie
public func responseRegionArray(array: Array<Rectangle>): This
```

**功能：** 设置一个或多个触摸热区。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|array|Array\<[Rectangle](cj-common-types.md#class-rectangle)>|是|-|一个或多个触摸热区，包括位置和大小。默认触摸热区为整个组件。<br>初始值：{x:0, y:0, width：'100%', height：'100%'}。|

### func selection(Int32, Int32)

```cangjie
public func selection(start: Int32, end: Int32): This
```

**功能：** 设置选中区域。

> **说明：**
>
> - 选中区域高亮且显示手柄和文本选择菜单。
> - 当copyOption设置为CopyOptions.None时，设置selection属性不生效。
> - 当overflow设置为TextOverflow.MARQUEE时，设置selection属性不生效。
> - 当selectionStart大于等于selectionEnd时不选中。可选范围为[0, textSize]，textSize为文本内容最大字符数，入参小于0处理为0，大于textSize处理为textSize。
> - 当selectionStart或selectionEnd在截断不可见区域时不选中。截断为false时超出父组件的文本选中区域生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|start|Int32|是|-|所选文本的起始位置。<br>初始值：-1。|
|end|Int32|是|-|所选文本的结束位置。<br>初始值：-1。|

### func textAlign(TextAlign)

```cangjie
public func textAlign(value: TextAlign): This
```

**功能：** 设置文本段落在水平方向的对齐方式。

> **说明：**
>
> - 文本段落宽度占满Text组件宽度。
> - 可通过[align](./cj-universal-attribute-location.md#func-alignalignment)属性控制文本段落在垂直方向上的位置，此组件中不可通过align属性控制文本段落在水平方向上的位置，具体效果如下：
Alignment.TopStart、Alignment.Top、Alignment.TopEnd：内容顶部对其。
Alignment.Start、Alignment.Center、Alignment.End：内容垂直居中。
Alignment.BottomStart、Alignment.Bottom、Alignment.BottomEnd：内容底部对齐。
> - 当textAlign属性设置为TextAlign.JUSTIFY时，需要根据文本内容设置[wordBreak](#func-wordbreakwordbreak)属性，且最后一行文本不参与两端对齐，为水平对齐首部效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[TextAlign](cj-common-types.md#enum-textalign)|是|-|多行文本的文本对齐方式。<br>初始值：TextAlign.Start。|

### func textCase(TextCase)

```cangjie
public func textCase(value: TextCase): This
```

**功能：** 设置文本大小写。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[TextCase](cj-common-types.md#enum-textcase)|是|-|文本大小写。<br>初始值：TextCase.Normal。|