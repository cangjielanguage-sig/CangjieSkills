#### func fling(Float64)

```cangjie
public func fling(velocity: Float64): Unit
```

**功能：** 根据传入的初始速度执行惯性滚动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|velocity|Float64|是|-|惯性滚动的初始速度值。如果值为0，则视为无效值，不会生效。正值表示向顶部滚动，负值表示向底部滚动。|

#### func scrollPage(Bool, ?Bool)

```cangjie
public func scrollPage(next: Bool, animation!: ?Bool = None): Unit
```

**功能：** 设置翻页模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|next|Bool|是|-|是否下一页。|
|animation|?Bool|否|None|**命名参数。** 是否启用动画。初始值：false。|

#### func currentOffset()

```cangjie
public func currentOffset(): Option<OffsetResult>
```

**功能：** 获取当前滚动偏移量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**返回值：**

|类型|说明|
|:---|:---|
|Option\<[OffsetResult](#class-offsetresult)>|返回当前的滚动偏移量。|

#### func scrollToIndex(Int32, ?Bool, ?ScrollAlign, ?ScrollToIndexOptions)

```cangjie
public func scrollToIndex(
    index: Int32,
    smooth!: ?Bool = None,
    align!: ?ScrollAlign = None,
    options!: ?ScrollToIndexOptions = None
): Unit
```

**功能：** 滚动到指定索引，支持设置额外的滚动偏移量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-|索引值。|
|smooth|?Bool|否|None|**命名参数。** 是否平滑滚动。初始值：false。|
|align|?[ScrollAlign](#enum-scrollalign)|否|None|**命名参数。** 对齐方式。初始值：ScrollAlign.Start。|
|options|?[ScrollToIndexOptions](#class-scrolltoindexoptions)|否|None|**命名参数。** 滚动到索引选项。初始值：ScrollToIndexOptions()。|

#### func isAtEnd()

```cangjie
public func isAtEnd(): Bool
```

**功能：** 检查组件是否已滚动到底部。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**返回值：**

|类型|说明|
|:---|:---|
|Bool|返回组件是否滚动到底部。|

#### func getItemRect(?Int32)

```cangjie
public func getItemRect(index: ?Int32): RectResult
```

**功能：** 获取子组件的大小和位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|?Int32|是|-|子组件的索引。初始值：-1。|

**返回值：**

|类型|说明|
|:---|:---|
|[RectResult](#class-rectresult)|子组件的大小和位置。|

#### func getItemIndex(Float64, Float64)

```cangjie
public func getItemIndex(x: Float64, y: Float64): Int32
```

**功能：** 根据坐标获取子组件的索引。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|x坐标。|
|y|Float64|是|-|y坐标。|

**返回值：**

|类型|说明|
|:---|:---|
|Int32|子组件的索引。|