# Image

Image为图片组件，常用于在应用中显示图片。支持png、jpg、jpeg、bmp、svg、webp、gif和heif类型的图片格式。

> 说明：
>
> - 使用快捷组合键对Image组件复制时，Image组件必须处于[获焦状态](../../../Dev_Guide/arkui-cj/cj-common-events-focus-event.md)。Image组件默认不获焦，需将[focusable](../../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-focus.md#func-focusablebool)属性设置为true，即可使用TAB键将焦点切换到组件上，再将[focusOnTouch](../../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-focus.md#func-focusontouchbool)属性设置为true，即可实现点击获焦。
> - 图片格式支持SVG图源，SVG标签文档请参考[SVG标签说明](../apis/ImageKit/cj-apis-image.md#svg标签说明)。
> - 动图的播放依赖于Image节点的可见性变化，其默认行为是不播放的。当节点可见时，通过回调启动动画，当节点不可见时，停止动画。可见性状态的判断是通过[onVisibleAreaChange](../../../API_Reference/source_zh_cn/arkui-cj/cj-universal-event-visibleareachange.md#func-onvisibleareachangearrayfloat64-bool-float64-unit---unit)事件触发的，当可见阈值ratios大于0时，表明Image处于可见状态。

## 需要权限

使用网络图片时，需要在 module.json5 对应的"requestPermissions"中添加网络使用权限ohos.permission.INTERNET。

```json
"requestPermissions": [
    { "name": "ohos.permission.INTERNET"}
]
```

## 子组件

无