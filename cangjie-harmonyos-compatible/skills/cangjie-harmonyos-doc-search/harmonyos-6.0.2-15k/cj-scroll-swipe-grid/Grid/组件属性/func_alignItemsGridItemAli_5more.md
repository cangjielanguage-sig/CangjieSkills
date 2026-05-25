### func alignItems(GridItemAlignment)

```cangjie
public func alignItems(alignment: GridItemAlignment): This
```

**功能：** 设置Grid中GridItem的对齐方式， 使用方法可以参考[示例4](#示例4自适应grid)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|alignment|[GridItemAlignment](#enum-griditemalignment)|是|-|设置Grid中GridItem的对齐方式。<br> 初始值：GridItemAlignment.DEFAULT|

### func cachedCount(Int32)

```cangjie
public func cachedCount(cacheCount: Int32): This
```

**功能：** 设置预加载的GridItem的数量，只在[LazyForEach](cj-state-rendering-lazyforeach.md)中生效。

设置缓存后会在Grid显示区域上下各缓存cachedCount*列数个GridItem。

[LazyForEach](cj-state-rendering-lazyforeach.md)超出显示和缓存范围的GridItem会被释放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cacheCount|Int32|是|-|预加载的GridItem的数量。<br>初始值：垂直滚动时为一个屏幕内可显示的行数，水平滚动时为一个屏幕内可显示的列数，最大值为16。 <br> 取值范围：[0, +∞)，设置为小于0的值时，按1处理。|

### func cachedCount(Int32, Bool)

```cangjie
public func cachedCount(cacheCount: Int32, show: Bool): This
```

**功能：** 设置预加载的GridItem数量，并配置是否显示预加载节点。

设置缓存后会在Grid显示区域上下各缓存cachedCount*列数个GridItem。配合[裁剪](cj-universal-attribute-shapclip.md#func-clipbool)或[内容裁剪](cj-scroll-swipe-common.md#func-clipcontentcontentclipmode)属性可以显示出预加载节点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cacheCount|Int32|是|-|预加载的GridItem的数量。<br>初始值：垂直滚动时为一个屏幕内可显示的行数，水平滚动时为一个屏幕内可显示的列数，最大值为16。<br> 取值范围：[0, +∞)，设置为小于0的值时，按1处理。|
|show|Bool|是|-|被预加载的GridItem是否需要显示。<br>初始值：false，不显示预加载的GridItem。|

### func cellLength(Int32)

```cangjie
public func cellLength(value: Int32): This
```

**功能：** 设置一行的高度或者一列的宽度。

当layoutDirection是Row/RowReverse时，表示一行的高度。

当layoutDirection是Column/ColumnReverse时，表示一列的宽度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|一行的高度或者一列的宽度。<br/> 初始值：第一个元素的大小 <br/>单位：vp <br> 取值范围：[0, +∞)，设置为小于0的值时，按初始值显示。|

### func columnsGap(Length)

```cangjie
public func columnsGap(value: Length): This
```

**功能：** 设置列与列的间距。设置为小于0的值时，按初始值显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](cj-common-types.md#interface-length)|是|-|列与列的间距。<br> 初始值：0 <br> 取值范围：[0, +∞)|