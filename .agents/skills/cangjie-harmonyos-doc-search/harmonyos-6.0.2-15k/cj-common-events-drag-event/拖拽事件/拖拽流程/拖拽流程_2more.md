## 拖拽流程

拖拽流程包含手势拖拽流程和鼠标拖拽流程，可帮助开发者理解回调事件触发的时机。

### ​手势拖拽流程

对于手势长按触发拖拽的场景，ArkUI在发起拖拽前会校验当前组件是否具备拖拽功能。对于默认可拖出的组件（[Search](../../API_Reference/source_zh_cn/arkui-cj/cj-text-input-search.md)、[TextInput](../../API_Reference/source_zh_cn/arkui-cj/cj-text-input-textinput.md)、[TextArea](../../API_Reference/source_zh_cn/arkui-cj/cj-text-input-textarea.md)、[RichEditor](../../API_Reference/source_zh_cn/arkui-cj/cj-text-input-richeditor.md)、[Text](../../API_Reference/source_zh_cn/arkui-cj/cj-text-input-text.md)、[Image](../../API_Reference/source_zh_cn/arkui-cj/cj-image-video-image.md)、[Hyperlink](../../API_Reference/source_zh_cn/arkui-cj/cj-text-input-hyperlink.md)）需要判断是否设置了[draggable](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-dragcontrol.md#func-draggablebool)，需检查是否已设置draggable属性为true（若系统使能分层参数，draggable属性默认为true）。其他组件则需额外确认是否已设置onDragStart回调函数。在满足上述条件后，长按时间达到或超过500ms即可触发拖拽，而长按800ms时，系统开始执行预览图的浮起动效。若与Menu功能结合使用，并通过isShow控制其显示与隐藏，建议避免在用户操作800ms后才控制菜单显示，此举可能引发非预期的行为。

手势拖拽（手指/手写笔）触发拖拽流程：

![Drag](./figures/Drag.png)