#### static func of(AppResource, String)

```cangjie
public static func of(icon: AppResource, text: String): BottomTabBarStyle
```

**功能：** BottomTabBarStyle的静态构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|icon|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|页签内的图片内容。|
|text|String|是|-|页签内的文字内容。|

**返回值：**

|类型|说明|
|:----|:----|
|[BottomTabBarStyle](#class-bottomtabbarstyle)|返回创建的BottomTabBarStyle对象。|

#### static func of(String, AppResource)

```cangjie
public static func of(icon: String, text: AppResource): BottomTabBarStyle
```

**功能：** BottomTabBarStyle的静态构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|icon|String|是|-|页签内的图片内容。|
|text|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|页签内的文字内容。|

**返回值：**

|类型|说明|
|:----|:----|
|[BottomTabBarStyle](#class-bottomtabbarstyle)|返回创建的BottomTabBarStyle对象。|

#### func iconStyle(TabBarIconStyle)

```cangjie
public func iconStyle(value: TabBarIconStyle): BottomTabBarStyle
```

**功能：** 设置底部页签的label图标的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[TabBarIconStyle](#class-tabbariconstyle)|是|-|底部页签的label图标的样式。|

**返回值：**

|类型|说明|
|:----|:----|
|[BottomTabBarStyle](#class-bottomtabbarstyle)|返回BottomTabBarStyle对象本身。|

#### func id(String)

```cangjie
public func id(value: String): BottomTabBarStyle
```

**功能：** 设置底部页签的id。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|设置底部页签的[id](cj-universal-attribute-componentid.md)。|

**返回值：**

|类型|说明|
|:----|:----|
|[BottomTabBarStyle](#class-bottomtabbarstyle)|返回BottomTabBarStyle对象本身。|

#### func labelStyle(LabelStyle)

```cangjie
public func labelStyle(value: LabelStyle): BottomTabBarStyle
```

**功能：** 设置底部页签的label文本和字体的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[LabelStyle](#class-labelstyle)|是|-|底部页签的label文本和字体的样式。|

**返回值：**

|类型|说明|
|:----|:----|
|[BottomTabBarStyle](#class-bottomtabbarstyle)|返回BottomTabBarStyle对象本身。|

#### func layoutMode(LayoutMode)

```cangjie
public func layoutMode(value: LayoutMode): BottomTabBarStyle
```

**功能：** 设置底部页签的图片、文字排布的方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[LayoutMode](#enum-layoutmode)|是|-|底部页签的图片、文字排布的方式，具体参照LayoutMode枚举。<br> 初始值：LayoutMode.VERTICAL。|

**返回值：**

|类型|说明|
|:----|:----|
|[BottomTabBarStyle](#class-bottomtabbarstyle)|返回BottomTabBarStyle对象本身。|