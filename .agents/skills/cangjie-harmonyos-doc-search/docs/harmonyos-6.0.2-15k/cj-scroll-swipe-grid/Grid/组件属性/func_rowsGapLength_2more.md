### func rowsGap(Length)

```cangjie
public func rowsGap(value: Length): This
```

**功能：** 设置行与行的间距。设置为小于0的值时，按初始值显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](cj-common-types.md#interface-length)|是|-|用于设置行与行的间距。<br> 初始值：0 <br> 取值范围：[0, +∞)|

### func rowsTemplate(String)

```cangjie
public func rowsTemplate(value: String): This
```

**功能：** 设置当前网格布局行的数量、固定行高或最小行高值，不设置时默认1行。

例如，'1fr 1fr 2fr'是将父组件分3行，将父组件允许的高分为4等份，第一行占1份，第二行占一份，第三行占2份。

- rowsTemplate('repeat(auto-fit, track-size)')是设置最小行高值为track-size，自动计算行数和实际行高。
- rowsTemplate('repeat(auto-fill, track-size)')是设置固定行高值为track-size，自动计算行数。
- rowsTemplate('repeat(auto-stretch, track-size)')是设置固定行高值为track-size，使用rowsGap为最小行间距，自动计算行数和实际行间距。

其中repeat、auto-fit、auto-fill、auto-stretch为关键字。track-size为行高，支持的单位包括px、vp、%或有效数字，默认单位为vp，track-size至少包括一个有效行高。

> **说明：**
>
> - auto-stretch模式下只支持track-size为一个有效行高值，并且track-size只支持px、vp和有效数字，不支持%。
> - value设置为'0fr'时，这一行的行宽为0，这一行GridItem不显示。设置为其他非法值时，按固定1行处理。

Grid组件根据rowsTemplate、columnsTemplate属性的设置情况，可分为以下三种布局模式：

1. rowsTemplate、columnsTemplate同时设置：

    - Grid只展示固定行列数的元素，其余元素不展示，且Grid不可滚动。
    - 此模式下以下属性不生效：layoutDirection、maxCount、minCount、cellLength。
    - Grid的宽高没有设置时，默认适应父组件尺寸。
    - Grid网格列大小按照Grid自身内容区域大小减去所有行列Gap后按各个行列所占比重分配。
    - GridItem默认填满网格大小。

2. rowsTemplate、columnsTemplate仅设置其中的一个：

    - 元素按照设置的方向进行排布，超出Grid显示区域后，Grid可通过滚动的方式展示。
    - 如果设置了columnsTemplate，Grid滚动方向为垂直方向，主轴方向为垂直方向，交叉轴方向为水平方向。
    - 如果设置了rowsTemplate，Grid滚动方向为水平方向，主轴方向为水平方向，交叉轴方向为垂直方向。
    - 此模式下以下属性不生效：layoutDirection、maxCount、minCount、cellLength。
    - 网格交叉轴方向尺寸根据Grid自身内容区域交叉轴尺寸减去交叉轴方向所有Gap后按所占比重分配。
    - 网格主轴方向尺寸取当前网格交叉轴方向所有GridItem高度最大值。

3. rowsTemplate、columnsTemplate都不设置：

    - 元素在layoutDirection方向上排布，列数由Grid的宽度、首个元素的宽度、minCount、maxCount、columnsGap共同决定。
    - 行数由Grid高度、首个元素高度、cellLength、rowsGap共同决定。超出行列容纳范围的元素不显示，也不能通过滚动进行展示。
    - 此模式下仅生效以下属性：layoutDirection、maxCount、minCount、cellLength、editMode、columnsGap、rowsGap。
    - 当前layoutDirection设置为Row时，先从左到右排列，排满一行再排下一行。剩余高度不足时不再布局，整体内容顶部居中。
    - 当前layoutDirection设置为Column时，先从上到下排列，排满一列再排下一列，剩余宽度不足时不再布局。整体内容顶部居中。
    - 当前Grid下面没有GridItem时，Grid的宽高为0。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|当前网格布局行的数量或最小行高值。|