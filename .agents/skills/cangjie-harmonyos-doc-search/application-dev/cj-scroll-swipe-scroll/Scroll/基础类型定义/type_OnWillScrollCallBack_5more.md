### type OnWillScrollCallBack

```cangjie
public type OnWillScrollCallBack = (Float64, ScrollState, ScrollSource) -> ScrollResult
```

**功能：** 定义onWillScroll回调函数类型。

**类型：** (Float64, [ScrollState](./cj-common-types.md#enum-scrollstate), [ScrollSource](./cj-common-types.md#enum-scrollsource)) -> [ScrollResult](#class-scrollresult)

### type OnScrollCallBack

```cangjie
public type OnScrollCallBack = (scrollOffset: Float64, scrollState: ScrollState) -> Unit
```

**功能：** 定义onScroll回调函数类型。

**类型：** (Float64, [ScrollState](./cj-common-types.md#enum-scrollstate)) -> Unit

### type ScrollOnScrollCallback

```cangjie
public type ScrollOnScrollCallback = (Float64, Float64, ScrollState) -> Unit
```

**功能：** 定义onDidScroll回调函数类型。

**类型：** (Float64, Float64, [ScrollState](./cj-common-types.md#enum-scrollstate)) -> Unit

### type OnScrollFrameBeginCallback

```cangjie
public type OnScrollFrameBeginCallback = (Float64, ScrollState) -> Float64
```

**功能：** 定义onScrollFrameBegin回调函数类型。

**类型：** (Float64, [ScrollState](./cj-common-types.md#enum-scrollstate)) -> Float64

### type OnScrollEdgeCallback

```cangjie
public type OnScrollEdgeCallback = (Edge) -> Unit
```

**功能：** 定义onScrollEdge回调函数类型。

**类型：** ([Edge](./cj-common-types.md#enum-edge)) -> Unit