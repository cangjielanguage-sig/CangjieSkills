# 拖拽控制

设置组件是否可以响应拖拽事件。

> **说明：**
>
> ArkUI框架对以下组件实现了默认的拖拽能力，支持对数据的拖出或拖入响应。开发者也可以通过实现通用拖拽事件来自定义拖拽响应。
>
> - 默认支持拖出能力的组件（可从组件上拖出数据）：[Search](./cj-text-input-search.md)、[TextInput](./cj-text-input-textinput.md)、[TextArea](./cj-text-input-textarea.md)、[RichEditor](./cj-text-input-richeditor.md)、[Text](./cj-text-input-text.md)、[Image](./cj-image-video-image.md)、[Hyperlink](./cj-text-input-hyperlink.md)，开发者可通过设置这些组件的draggable属性来控制对默认拖拽能力的使用。
>
> - 默认支持拖入能力的组件（目标组件可响应拖入数据）：[Search](./cj-text-input-search.md)、[TextInput](./cj-text-input-textinput.md)、[TextArea](./cj-text-input-textarea.md)、[RichEditor](./cj-text-input-richeditor.md)。
>
> Text、TextInput、TextArea、Hyperlink、Image、RichEditor和Web组件的draggable属性默认为true，默认支持拖出能力。其他组件需要开发者将draggable属性设置为true，并在onDragStart等接口中实现数据传输相关内容，才能正确处理拖拽。
>
> Text组件需配合[copyOption](./cj-text-input-text.md#func-copyoptioncopyoptions)一起使用，设置copyOptions为CopyOptions.InApp或者CopyOptions.LocalDevice。

## func draggable(Bool)

```cangjie
public open func draggable(value: Bool): This
```

**功能：** 设置该组件是否允许进行拖拽。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|组件是否允许进行拖拽。true表示允许拖拽，false表示不允许拖拽。<br/>初始值：false。|

## func dragPreview(DragItemInfo)

```cangjie
public func dragPreview(value: DragItemInfo): This
```

**功能：** 设置组件拖拽过程中的预览图。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[DragItemInfo](./cj-universal-event-drag.md#struct-dragiteminfo)|是|-|组件拖拽过程中的预览图，仅在[onDragStart](./cj-universal-event-drag.md#func-ondragstartdrageventstring---dragiteminfo)拖拽方式中有效。<br/>当组件支持拖拽并同时设置[bindContextMenu](./cj-universal-attribute-menu.md#func-bindcontextmenu---unit-responsetype)的预览图时，则长按浮起的预览图以[bindContextMenu](./cj-universal-attribute-menu.md#func-bindcontextmenu---unit-responsetype)设置的预览图为准。开发者在[onDragStart](./cj-universal-event-drag.md#func-ondragstartdrageventstring------unit)中返回的背板图优先级低于[dragPreview](./cj-universal-attribute-dragcontrol.md#func-dragpreviewdragiteminfo)设置的预览图，当设置了[dragPreview](./cj-universal-attribute-dragcontrol.md#func-dragpreview---unit)预览图时，拖拽过程中的背板图使用[dragPreview](./cj-universal-attribute-dragcontrol.md#func-dragpreview---unit)预览图。<br>当传入类型为string的id时，则将id对应组件的截图作为预览图。如果id对应的组件无法查找到，或者id对应的组件Visibility属性设置成none/hidden，则对组件自身进行截图作为拖拽预览图。目前截图不含有亮度、阴影、模糊和旋转等视觉效果。<br>初始值：空。|