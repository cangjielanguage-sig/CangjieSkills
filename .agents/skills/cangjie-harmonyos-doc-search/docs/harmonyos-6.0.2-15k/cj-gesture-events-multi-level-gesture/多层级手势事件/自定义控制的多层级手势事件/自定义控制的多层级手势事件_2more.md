## 自定义控制的多层级手势事件

可以通过设置属性，控制默认的多层级手势事件竞争流程，更好的实现手势事件。

目前，responseRegion属性和hitTestBehavior属性可以控制Touch事件的分发，从而可以影响到onTouch事件和手势的响应。而绑定手势方法属性可以控制手势的竞争从而影响手势的响应，但不能影响到onTouch事件。

### responseRegion和responseRegionArray对手势和事件的控制

responseRegion属性和responseRegionArray属性可以实现组件的响应区域范围的变化。响应区域范围可以超出或者小于组件的布局范围。

```cangjie
ComponentA() {
    ComponentB()
    .onTouch({ => })
    .gesture(TapGesture(count: 1))
    .responseRegionArray([Rect1, Rect2, Rect3])
}
.onTouch({ => })
.gesture(TapGesture(count: 1))
.responseRegion(Rect4)
```

当组件A绑定了.responseRegion(Rect4)的属性后，所有落在Rect4区域范围的触摸事件和手势可被组件A对应的回调响应。

当组件B绑定了.responseRegionArray([Rect1, Rect2, Rect3])的属性后，所有落在Rect1，Rect2和Rect3区域范围的触摸事件和手势可被组件B对应的回调响应。

当绑定了responseRegion后，手势与事件的响应区域范围将以所绑定的区域范围为准，而不是以布局区域为准，可能出现布局相关区域不响应手势与事件的情况。

此外，responseRegionArray属性支持由多个Rect组成的数组作为入参，以支持更多开发需求。