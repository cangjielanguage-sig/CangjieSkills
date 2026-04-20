### func columnEnd(Int32)

```cangjie
public func columnEnd(columnEnd: Int32): This
```

**功能：** 设置当前元素终点列号。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|columnEnd|Int32|是|-|当前元素终点列号，与columnStart配套使用。需要指定GridItem起始行列号和所占行列数的场景推荐使用[Grid的layoutOptions参数](./cj-scroll-swipe-grid.md#class-gridlayoutoptions)，详细可参考[Grid的示例1](./cj-scroll-swipe-grid.md#示例1固定行列grid)和[Grid的示例3](./cj-scroll-swipe-grid.md#示例3可滚动grid设置跨行跨列节点)。<br/>取值范围：[0, 总列数-1]。|

> **说明：**
>
> 需要指定GridItem起始行列号和所占行列数的场景推荐使用[Grid的layoutOptions参数](./cj-scroll-swipe-grid.md#class-gridlayoutoptions)，详细可参考[Grid的示例1](./cj-scroll-swipe-grid.md#示例1固定行列grid)和[Grid的示例3](./cj-scroll-swipe-grid.md#示例3可滚动grid设置跨行跨列节点)。
>
> 起始行号、终点行号、起始列号、终点列号生效规则如下：
>
> - rowStart/rowEnd合理取值范围为0~总行数-1，columnStart/columnEnd合理取值范围为0~总列数-1。
> - 如果设置了rowStart/rowEnd/columnStart/columnEnd，GridItem会占据指定的行数(rowEnd-rowStart+1)或列数(columnEnd-columnStart+1)。
> - 只有在设置columnTemplate和rowTemplate的Grid中，设置合理的rowStart/rowEnd/columnStart/columnEnd四个属性的GridItem才能按照指定的行列号布局。
> - 在设置columnTemplate和rowTemplate的Grid中，单独设置行号rowStart/rowEnd或列号columnStart/columnEnd的GridItem会按照一行一列进行布局。
> - 在只设置columnTemplate的Grid中设置列号columnStart/columnEnd的GridItem按照列数布局。在该区域位置存在GridItem布局，则直接换行进行放置。
> - 在只设置rowTemplate的Grid中设置行号rowStart/rowEnd的GridItem按照行数布局。在该区域位置存在GridItem布局，则直接换列进行放置。
> - 在只设置columnTemplate的Grid中，在GridItem上设置了不合理的值，GridItem按照一行一列进行布局。
> - columnTemplate和rowTemplate都不设置的Grid中GridItem的行列号属性无效。