#### func padding(Padding)

```cangjie
public func padding(value: Padding): BottomTabBarStyle
```

**功能：** 设置底部页签的内边距属性（不支持百分比设置），四个方向内边距同时生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Padding](cj-common-types.md#class-padding)|是|-|底部页签的内边距。<br> 初始值：{left:4.0.vp,right:4.0.vp,top:0.0.vp,bottom:0.0.vp}|

**返回值：**

|类型|说明|
|:----|:----|
|[BottomTabBarStyle](#class-bottomtabbarstyle)|返回BottomTabBarStyle对象本身。|

#### func padding(Length)

```cangjie
public func padding(value: Length): BottomTabBarStyle
```

**功能：** 设置底部页签的内边距属性（不支持百分比设置），四个方向内边距同时生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](cj-common-types.md#interface-length)|是|-|底部页签的内边距。<br> 初始值：{left:4.0.vp,right:4.0.vp,top:0.0.vp,bottom:0.0.vp}|

**返回值：**

|类型|说明|
|:----|:----|
|[BottomTabBarStyle](#class-bottomtabbarstyle)|返回BottomTabBarStyle对象本身。|

#### func padding(LocalizedPadding)

```cangjie
public func padding(value: LocalizedPadding): BottomTabBarStyle
```

**功能：** 设置底部页签的内边距属性（不支持百分比设置）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[LocalizedPadding](cj-common-types.md#class-localizedpadding)|是|-|底部页签的内边距，支持镜像能力。<br>初始值：{start:4.vp,end:4.vp,top:0.vp,bottom:0.vp}|

**返回值：**

|类型|说明|
|:----|:----|
|[BottomTabBarStyle](#class-bottomtabbarstyle)|返回BottomTabBarStyle对象本身。|

#### func symmetricExtensible(Bool)

```cangjie
public func symmetricExtensible(value: Bool): BottomTabBarStyle
```

**功能：** 设置底部页签的图片、文字是否可以对称借左右底部页签的空余位置中的最小值，仅fixed水平模式下在底部页签之间有效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|底部页签的图片、文字是否可以对称借左右底部页签的空余位置中的最小值。初始值为：false，底部页签的图片、文字不可以对称借用左右底部页签的空余位置中的最小值。|

**返回值：**

|类型|说明|
|:----|:----|
|[BottomTabBarStyle](#class-bottomtabbarstyle)|返回BottomTabBarStyle对象本身。|

#### func verticalAlign(VerticalAlign)

```cangjie
public func verticalAlign(value: VerticalAlign): BottomTabBarStyle
```

**功能：** 设置底部页签的图片、文字在垂直方向上的对齐格式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[VerticalAlign](cj-common-types.md#enum-verticalalign)|是|-|底部页签的图片、文字在垂直方向上的对齐格式。<br>初始值：VerticalAlign.Center|

**返回值：**

|类型|说明|
|:----|:----|
|[BottomTabBarStyle](#class-bottomtabbarstyle)|返回BottomTabBarStyle对象本身。|