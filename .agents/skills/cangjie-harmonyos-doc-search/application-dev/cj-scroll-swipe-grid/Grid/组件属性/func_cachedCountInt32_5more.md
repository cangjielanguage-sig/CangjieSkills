### func cachedCount(?Int32)

```cangjie
public func cachedCount(value: ?Int32): This
```

**功能：** 设置预加载的GridItem的数量，只在[LazyForEach](cj-state-rendering-lazyforeach.md)中生效。

设置缓存后会在Grid显示区域上下各缓存cachedCount*列数个GridItem。

[LazyForEach](cj-state-rendering-lazyforeach.md)超出显示和缓存范围的GridItem会被释放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Int32|是|-|预加载的GridItem的数量。初始值:  1|

### func cachedCount(?Int32, ?Bool)

```cangjie
public func cachedCount(count: ?Int32, show: ?Bool): This
```

**功能：** 设置预加载的GridItem数量，并配置是否显示预加载节点。

设置缓存后会在Grid显示区域上下各缓存cachedCount*列数个GridItem。配合[裁剪](./cj-universal-attribute-shapclip.md#func-clipbool)或[内容裁剪](./cj-universal-attribute-shapclip.md#func-clipbool)属性可以显示出预加载节点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|count|?Int32|是|-|预加载的GridItem的数量。初始值:  1|
|show|?Bool|是|-|被预加载的GridItem是否需要显示。初始值:  false|

### func columnsGap(?Length)

```cangjie
public func columnsGap(value: ?Length): This
```

**功能：** 设置列与列的间距。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[Length](./cj-common-types.md#interface-length)|是|-|列与列的间距。初始值:  0.vp|

### func columnsTemplate(?String)

```cangjie
public func columnsTemplate(value: ?String): This
```

**功能：** 设置当前网格布局列的数量、固定列宽或最小列宽值，不设置时默认1列。

例如, '1fr 1fr 2fr' 是将父组件分3列，将父组件允许的宽分为4等份，第一列占1份，第二列占1份，第三列占2份。

columnsTemplate('repeat(auto-fit, track-size)')是设置最小列宽值为track-size，自动计算列数和实际列宽。

columnsTemplate('repeat(auto-fill, track-size)')是设置固定列宽值为track-size，自动计算列数。

columnsTemplate('repeat(auto-stretch, track-size)')是设置固定列宽值为track-size，使用columnsGap为最小列间距，自动计算列数和实际列间距。

其中repeat、auto-fit、auto-fill、auto-stretch为关键字。track-size为列宽，支持的单位包括px、vp、%或有效数字，默认单位为vp，track-size至少包括一个有效列宽。
auto-stretch模式只支持track-size为一个有效列宽值，并且track-size只支持px、vp和有效数字，不支持%。

使用效果可以参考[示例3](#示例代码)。

设置为'0fr'时，该列的列宽为0，不显示GridItem。设置为其他非法值时，GridItem显示为固定1列。

> **说明：**
>
> 设置包含单位的track-size时，需按照数字+单位的格式，如'16vp'、'20%'，与填写Length类型的格式不同。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?String|是|-|当前网格布局列的数量或最小列宽值。初始值:  "1fr"|

### func rowsGap(?Length)

```cangjie
public func rowsGap(value: ?Length): This
```

**功能：** 设置行与行的间距。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[Length](./cj-common-types.md#interface-length)|是|-|用于设置行与行的间距。初始值:  0.vp|