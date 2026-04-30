### enum WaterFlowLayoutMode

```cangjie
public enum WaterFlowLayoutMode {
    | ALWAYS_TOP_DOWN
    | SLIDING_WINDOW
}
```

**功能：** WaterFlow的布局模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### ALWAYS_TOP_DOWN

```cangjie
ALWAYS_TOP_DOWN
```

**功能：** 默认的从上到下的布局模式。视窗内的FlowItem依赖视窗上方所有FlowItem的布局信息。因此跳转或切换列数时，需要计算出上方所有的FlowItem的布局信息。

**起始版本：** 19

#### SLIDING_WINDOW

```cangjie
SLIDING_WINDOW
```

**功能：** 移动窗口式的布局模式。只考虑视窗内的布局信息，对视窗上方的FlowItem没有依赖关系，因此向后跳转或切换列数时只需要布局视窗内的FlowItem。有频繁切换列数的场景的应用建议使用该模式。

> **说明：**
>
> 1.无动画跳转到较远的位置时，会以目标位置为基准，向前或向后布局FlowItem。这之后如果滑回跳转前的位置，内容的布局效果可能和之前不一致。 这个效果会导致跳转后回滑到顶部时，顶部节点可能不对齐。所以该布局模式下会在滑动到顶部后自动调整布局，保证顶部对齐。在有多个分组的情况下，会在滑动结束时调整在视窗内的分组。<br/>
> 2.该模式不支持使用滚动条，就算设置了滚动条也无法显示。<br/>
> 3.不支持[scroller](./cj-scroll-swipe-scroll.md#class-scroller)的[scrollTo](./cj-scroll-swipe-scroll.md#func-scrolltoindexint32-bool-scrollalign)接口。<br/>
> 4.[scroller](./cj-scroll-swipe-scroll.md#class-scroller)的[currentOffset](./cj-scroll-swipe-scroll.md#func-currentoffset)接口返回的总偏移量在触发跳转或数据更新后不准确，在回滑到顶部时会重新校准。<br/>
> 5.如果在同一帧内调用跳转（如无动画的[scrollToIndex](./cj-scroll-swipe-scroll.md#func-scrolltoindexint32-bool-scrollalign-length)、[scrollEdge](cj-scroll-swipe-scroll.md#func-scrolledgeedge-int32)）和输入偏移量（如滑动手势或滚动动画），两者都会生效。<br/>
> 6.调用无动画的[scrollToIndex](./cj-scroll-swipe-scroll.md#func-scrolltoindexint32-bool-scrollalign-length)进行跳转，如果跳转到较远位置（超过视窗内的FlowItem数量的位置）时，由于移动窗口模式对总偏移量没有估算，此时总偏移量没有变化，所以不会触发[onDidScroll](./cj-scroll-swipe-scroll.md#func-ondidscrollfloat64float64scrollstate---unit)事件。