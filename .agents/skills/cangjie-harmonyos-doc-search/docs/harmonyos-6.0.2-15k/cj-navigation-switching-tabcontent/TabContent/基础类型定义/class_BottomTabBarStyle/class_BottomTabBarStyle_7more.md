### class BottomTabBarStyle

```cangjie
public class BottomTabBarStyle {
    public init(icon: String, text: String)
    public init(icon: AppResource, text: AppResource)
    public init(icon: AppResource, text: String)
    public init(icon: String, text: AppResource)
}
```

**功能：** 底部页签和侧边页签样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(String, String)

```cangjie
public init(icon: String, text: String)
```

**功能：** BottomTabBarStyle的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|icon|String|是|-|页签内的图片内容。|
|text|String|是|-|页签内的文字内容。|

#### init(AppResource, AppResource)

```cangjie
public init(icon: AppResource, text: AppResource)
```

**功能：** BottomTabBarStyle的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|icon|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|页签内的图片内容。|
|text|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|页签内的文字内容。|

#### init(AppResource, String)

```cangjie
public init(icon: AppResource, text: String)
```

**功能：** BottomTabBarStyle的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|icon|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|页签内的图片内容。|
|text|String|是|-|页签内的文字内容。|

#### init(String, AppResource)

```cangjie
public init(icon: String, text: AppResource)
```

**功能：** BottomTabBarStyle的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|icon|String|是|-|页签内的图片内容。|
|text|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|页签内的文字内容。|

#### static func of(String, String)

```cangjie
public static func of(icon: String, text: String): BottomTabBarStyle
```

**功能：** BottomTabBarStyle的静态构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|icon|String|是|-|页签内的图片内容。|
|text|String|是|-|页签内的文字内容。|

**返回值：**

|类型|说明|
|:----|:----|
|[BottomTabBarStyle](#class-bottomtabbarstyle)|返回创建的BottomTabBarStyle对象。|

#### static func of(AppResource, AppResource)

```cangjie
public static func of(icon: AppResource, text: AppResource): BottomTabBarStyle
```

**功能：** BottomTabBarStyle的静态构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|icon|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|页签内的图片内容。|
|text|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|页签内的文字内容。|

**返回值：**

|类型|说明|
|:----|:----|
|[BottomTabBarStyle](#class-bottomtabbarstyle)|返回创建的BottomTabBarStyle对象。|