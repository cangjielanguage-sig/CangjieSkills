#### func labelStyle(LabelStyle)

```cangjie
public func labelStyle(value: LabelStyle): SubTabBarStyle
```

**功能：** 设置子页签的label文本和字体的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[LabelStyle](#class-labelstyle)|是|-|子页签的label文本和字体的样式对象。|

**返回值：**

|类型|说明|
|:----|:----|
|[SubTabBarStyle](#class-subtabbarstyle)|返回SubTabBarStyle对象本身。|

#### func padding(Padding)

```cangjie
public func padding(value: Padding): SubTabBarStyle
```

**功能：** 设置子页签的内边距属性（不支持百分比设置），四个方向内边距同时生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Padding](cj-common-types.md#class-padding)|是|-|子页签的内边距属性。<br> 初始值：{left:8.0.vp,right:8.0.vp,top:17.0.vp,bottom:18.0.vp}|

**返回值：**

|类型|说明|
|:----|:----|
|[SubTabBarStyle](#class-subtabbarstyle)|返回SubTabBarStyle对象本身。|

#### func padding(Length)

```cangjie
public func padding(value: Length): SubTabBarStyle
```

**功能：** 设置子页签的内边距属性（不支持百分比设置），四个方向内边距同时生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](cj-common-types.md#interface-length)|是|-|子页签的内边距属性。<br> 初始值：{left:8.0.vp,right:8.0.vp,top:17.0.vp,bottom:18.0.vp}|

**返回值：**

|类型|说明|
|:----|:----|
|[SubTabBarStyle](#class-subtabbarstyle)|返回SubTabBarStyle对象本身。|

#### func padding(LocalizedPadding)

```cangjie
public func padding(value: LocalizedPadding): SubTabBarStyle
```

**功能：** 设置子页签的内边距属性（不支持百分比设置）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[LocalizedPadding](cj-common-types.md#class-localizedpadding)|是|-|子页签的内边距属性。<br> 初始值：{left:8.0.vp,right:8.0.vp,top:17.0.vp,bottom:18.0.vp}|

**返回值：**

|类型|说明|
|:----|:----|
|[SubTabBarStyle](#class-subtabbarstyle)|返回SubTabBarStyle对象本身。|

#### func selectedMode(SelectedMode)

```cangjie
public func selectedMode(value: SelectedMode): SubTabBarStyle
```

**功能：** 设置选中子页签的显示方式。子页签的显示方式仅在水平模式下有效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[SelectedMode](#enum-selectedmode)|是|-|选中子页签的显示方式。<br> 初始值：SelectedMode.INDICATOR。|

**返回值：**

|类型|说明|
|:----|:----|
|[SubTabBarStyle](#class-subtabbarstyle)|返回SubTabBarStyle对象本身。|