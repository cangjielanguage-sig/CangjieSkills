### func alignListItem(?ListItemAlign)

```cangjie
public func alignListItem(value: ?ListItemAlign): This
```

**功能：** 设置List交叉轴方向宽度大于ListItem交叉轴宽度 * lanes时，ListItem在List交叉轴方向的布局方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ListItemAlign](./cj-common-types.md#enum-listitemalign)|是|-|交叉轴方向的布局方式。初始值：ListItemAlign.Start。|

### func cachedCount(?Int32)

```cangjie
public func cachedCount(value: ?Int32): This
```

**功能：** 设置列表中ListItem/ListItemGroup的预加载数量，懒加载场景只会预加载List显示区域外cachedCount的内容，非懒加载场景会全部加载。懒加载、非懒加载都只布局List显示区域+List显示区域外cachedCount的内容。

List设置cachedCount后，显示区域外上下各会预加载并布局cachedCount行ListItem。计算ListItem行数时，会计算ListItemGroup内部的ListItem行数。如果ListItemGroup内没有ListItem，则整个ListItemGroup算一行。

List下嵌套使用LazyForEach，并且LazyForEach下嵌套使用ListItemGroup时，LazyForEach会在List显示区域外上下各会创建cachedCount个ListItemGroup。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Int32|是|-|列表中ListItem/ListItemGroup的预加载数量。初始值：1。|

### func chainAnimation(?Bool)

```cangjie
public func chainAnimation(value: ?Bool): This
```

**功能：** 设置是否启用链式动画，链式动画效果在列表滚动或拖拽到顶部或底部边界时提供视觉上的连接或"链式"效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Bool|是|-|是否启用链式动画。初始值：false。|

### func divider(Option\<ListDividerOptions>)

```cangjie
public func divider(value: Option<ListDividerOptions>): This
```

**功能：** 设置列表项的分割线样式。默认情况下没有分割线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Option\<[ListDividerOptions](./cj-scroll-swipe-listgroup.md#class-listdivideroptions)>|是|-|分割线样式配置。|

### func edgeEffect(?EdgeEffect)

```cangjie
public func edgeEffect(value: ?EdgeEffect): This
```

**功能：** 设置滚动到边界时使用的边缘效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[EdgeEffect](./cj-common-types.md#enum-edgeeffect)|是|-|边缘效果类型。初始值：EdgeEffect.Spring。|

### func lanes(?Int32)

```cangjie
public func lanes(value: ?Int32): This
```

**功能：** 设置列表中列或行的数量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Int32|是|-|列表中列或行的数量。初始值：1。|

### func lanes(?Length, ?Length)

```cangjie
public func lanes(minLength!: ?Length, maxLength!: ?Length): This
```

**功能：** 设置列表中列或行的数量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|minLength|?[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 列或行的最小长度。初始值：(-1.0).vp。|
|maxLength|?[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 列或行的最大长度。初始值：(-1.0).vp。|