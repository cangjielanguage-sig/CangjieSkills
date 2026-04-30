# 拖拽事件

拖拽事件提供了一种通过鼠标或手势触屏传递数据的机制，即从一个组件位置拖出（drag）数据并将其拖入（drop）到另一个组件位置，以触发响应。在这一过程中，拖出方提供数据，而拖入方负责接收和处理数据。这一操作使用户能够便捷地移动、复制或删除指定内容。

## 基本概念

- 拖拽操作：在可响应拖出的组件上长按并滑动以触发拖拽行为，当用户释放手指或鼠标时，拖拽操作即告结束。
- 拖拽背景（背板）：用户拖动数据时的形象化表示。开发者可以通过[onDragStart](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-event-drag.md#func-ondragstartdrageventstring------unit)的()-> Unit或[DragItemInfo](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-event-drag.md#struct-dragiteminfo)进行设置，也可以通过[dragPreview](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-dragcontrol.md#func-dragpreviewdragiteminfo)通用属性进行自定义。
- 拖拽内容：被拖动的数据，使用UDMF统一API [UnifiedData](../../API_Reference/source_zh_cn/apis/ArkData/cj-apis-unifiedDataChannel.md#class-unifieddata) 进行封装，确保数据的一致性和安全性。
- 拖出对象：触发拖拽操作并提供数据的组件，通常具有响应拖拽的特性。
- 拖入目标：可接收并处理拖动数据的组件，能够根据拖入的数据执行相应的操作。
- 拖拽点：鼠标或手指与屏幕的接触位置，用于判断是否进入组件范围。判定依据是接触点是否位于组件的范围内。