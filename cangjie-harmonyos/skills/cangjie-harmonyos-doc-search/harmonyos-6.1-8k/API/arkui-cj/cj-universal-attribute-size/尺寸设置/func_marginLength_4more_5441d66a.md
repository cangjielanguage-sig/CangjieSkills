## func margin(?Length, ?Length, ?Length, ?Length)

```cangjie
func margin(top!: ?Length, right!: ?Length, bottom!: ?Length, left!: ?Length): T
```

**功能：** 分别设置组件四个方向的外边距。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|top|?[Length](./cj-common-types.md#interface-length)|是|-|**命名参数。** 上外边距<br>初始值：0.vp。|
|right|?[Length](./cj-common-types.md#interface-length)|是|-|**命名参数。** 右外边距<br>初始值：0.vp。|
|bottom|?[Length](./cj-common-types.md#interface-length)|是|-|**命名参数。** 下外边距<br>初始值：0.vp。|
|left|?[Length](./cj-common-types.md#interface-length)|是|-|**命名参数。** 左外边距<br>初始值：0.vp。|

**返回值：**

|类型|说明|
|:---|:---|
|T|返回通用方法接口类型。|

## func layoutWeight(?Int32)

```cangjie
func layoutWeight(value: ?Int32): T
```

**功能：** 设置组件的布局权重。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Int32|是|-|组件的布局权重<br>初始值：0。|

**返回值：**

|类型|说明|
|:---|:---|
|T|返回通用方法接口类型。|

## func aspectRatio(Float64)

```cangjie
func aspectRatio(value: Float64): T
```

**功能：** 设置组件的宽高比。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|-|组件的宽高比|

**返回值：**

|类型|说明|
|:---|:---|
|T|返回通用方法接口类型。|

## func displayPriority(?Int32)

```cangjie
func displayPriority(value: ?Int32): T
```

**功能：** 设置组件的显示优先级。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Int32|是|-|组件的显示优先级<br>初始值：1。|

**返回值：**

|类型|说明|
|:---|:---|
|T|返回通用方法接口类型。|