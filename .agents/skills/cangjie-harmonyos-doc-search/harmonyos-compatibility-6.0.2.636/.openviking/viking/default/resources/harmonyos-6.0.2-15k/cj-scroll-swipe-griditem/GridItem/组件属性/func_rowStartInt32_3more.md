### func rowStart(Int32)

```cangjie
public func rowStart(rowStart: Int32): This
```

**功能：** 设置当前元素起始行号。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rowStart|Int32|是|-|当前元素起始行号，与rowEnd配套使用。需要指定GridItem起始行列号和所占行列数的场景推荐使用[Grid的layoutOptions参数](./cj-scroll-swipe-grid.md#class-gridlayoutoptions)，详细可参考[Grid的示例1](./cj-scroll-swipe-grid.md#示例1固定行列grid)和[Grid的示例3](./cj-scroll-swipe-grid.md#示例3可滚动grid设置跨行跨列节点)。<br/>取值范围：[0, 总行数-1]|

### func rowEnd(Int32)

```cangjie
public func rowEnd(rowEnd: Int32): This
```

**功能：** 设置当前元素终点行号。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rowEnd|Int32|是|-|当前元素终点行号，与rowStart配套使用。需要指定GridItem起始行列号和所占行列数的场景推荐使用[Grid的layoutOptions参数](./cj-scroll-swipe-grid.md#class-gridlayoutoptions)，详细可参考[Grid的示例1](./cj-scroll-swipe-grid.md#示例1固定行列grid)和[Grid的示例3](./cj-scroll-swipe-grid.md#示例3可滚动grid设置跨行跨列节点)。<br/>取值范围：[0, 总行数-1]|

### func columnStart(Int32)

```cangjie
public func columnStart(columnStart: Int32): This
```

**功能：** 设置当前元素起始列号。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|columnStart|Int32|是|-|当前元素起始列号，与columnEnd配套使用。需要指定GridItem起始行列号和所占行列数的场景推荐使用[Grid的layoutOptions参数](./cj-scroll-swipe-grid.md#class-gridlayoutoptions)，详细可参考[Grid的示例1](./cj-scroll-swipe-grid.md#示例1固定行列grid)和[Grid的示例3](./cj-scroll-swipe-grid.md#示例3可滚动grid设置跨行跨列节点)。<br/>取值范围：[0, 总列数-1]|