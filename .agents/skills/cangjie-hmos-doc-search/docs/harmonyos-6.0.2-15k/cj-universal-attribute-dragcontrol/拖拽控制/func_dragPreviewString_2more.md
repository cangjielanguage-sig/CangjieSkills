## func dragPreview(String)

```cangjie
public func dragPreview(value: String): This
```

**功能：** 设置组件拖拽过程中的预览图。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|组件拖拽过程中的预览图，仅在[onDragStart](./cj-universal-event-drag.md#func-ondragstartdrageventstring---dragiteminfo)拖拽方式中有效。<br/>当组件支持拖拽并同时设置[bindContextMenu](./cj-universal-attribute-menu.md#func-bindcontextmenu---unit-responsetype)的预览图时，则长按浮起的预览图以[bindContextMenu](./cj-universal-attribute-menu.md#func-bindcontextmenu---unit-responsetype)设置的预览图为准。开发者在[onDragStart](./cj-universal-event-drag.md#func-ondragstartdrageventstring---dragiteminfo)中返回的背板图优先级低于[dragPreview](./cj-universal-attribute-dragcontrol.md#func-dragpreview---unit)设置的预览图，当设置了[dragPreview](./cj-universal-attribute-dragcontrol.md#func-dragpreview---unit)预览图时，拖拽过程中的背板图使用[dragPreview](./cj-universal-attribute-dragcontrol.md#func-dragpreview---unit)预览图。<br>当传入类型为string的id时，则将id对应组件的截图作为预览图。如果id对应的组件无法查找到，或者id对应的组件Visibility属性设置成none/hidden，则对组件自身进行截图作为拖拽预览图。目前截图不含有亮度、阴影、模糊和旋转等视觉效果。<br>初始值：空。|

## func dragPreview(() -> Unit)

```cangjie
public func dragPreview(builder: () -> Unit): This
```

**功能：** 设置组件拖拽过程中的预览图。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|builder|() -> Unit|是|-|组件拖拽过程中的预览图，仅在[onDragStart](./cj-universal-event-drag.md#func-ondragstartdrageventstring---dragiteminfo)拖拽方式中有效。<br/>当组件支持拖拽并同时设置[bindContextMenu](./cj-universal-attribute-menu.md#func-bindcontextmenu---unit-responsetype)的预览图时，则长按浮起的预览图以[bindContextMenu](./cj-universal-attribute-menu.md#func-bindcontextmenu---unit-responsetype)设置的预览图为准。开发者在[onDragStart](./cj-universal-event-drag.md#func-ondragstartdrageventstring---dragiteminfo)中返回的背板图优先级低于[dragPreview](./cj-universal-attribute-dragcontrol.md#func-dragpreview---unit)设置的预览图，当设置了[dragPreview](./cj-universal-attribute-dragcontrol.md#func-dragpreview---unit)预览图时，拖拽过程中的背板图使用[dragPreview](./cj-universal-attribute-dragcontrol.md#func-dragpreview---unit)预览图。<br>当传入类型为string的id时，则将id对应组件的截图作为预览图。如果id对应的组件无法查找到，或者id对应的组件Visibility属性设置成none/hidden，则对组件自身进行截图作为拖拽预览图。目前截图不含有亮度、阴影、模糊和旋转等视觉效果。<br>初始值：空。使用时结合[@Builder](../../../Dev_Guide/arkui-cj/paradigm/cj-macro-builder.md)和[bind](./cj-ui-framework.md#func-bindcustomview---viewbuilder-customview)方法使用。|