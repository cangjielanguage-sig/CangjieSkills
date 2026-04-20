### class SubTabBarStyle

```cangjie
public class SubTabBarStyle {
    public init(content: String)
    public init(content: AppResource)
}
```

**功能：** 子页签样式。打开后在切换页签时会播放跳转动画。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(String)

```cangjie
public init(content: String)
```

**功能：** SubTabBarStyle的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|String|是|-|页签内的文字内容。|

#### init(AppResource)

```cangjie
public init(content: AppResource)
```

**功能：** SubTabBarStyle的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|页签内的文字内容。|

#### static func of(String)

```cangjie
public static func of(content: String): SubTabBarStyle
```

**功能：** SubTabBarStyle的静态构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|String|是|-|页签内的文字内容。|

**返回值：**

|类型|说明|
|:----|:----|
|[SubTabBarStyle](#class-subtabbarstyle)|返回创建的SubTabBarStyle对象。|

#### static func of(AppResource)

```cangjie
public static func of(content: AppResource): SubTabBarStyle
```

**功能：** SubTabBarStyle的静态构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|页签内的文字内容。|

**返回值：**

|类型|说明|
|:----|:----|
|[SubTabBarStyle](#class-subtabbarstyle)|返回创建的SubTabBarStyle对象。|

#### func board(BoardStyle)

```cangjie
public func board(value: BoardStyle): SubTabBarStyle
```

**功能：** 设置选中子页签的背板风格。子页签的背板风格仅在水平模式下有效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[BoardStyle](#class-boardstyle)|是|-|选中子页签的背板风格对象。|

**返回值：**

|类型|说明|
|:----|:----|
|[SubTabBarStyle](#class-subtabbarstyle)|返回SubTabBarStyle对象本身。|

#### func id(String)

```cangjie
public func id(value: String): SubTabBarStyle
```

**功能：** 设置子页签的id。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|子页签的[id](cj-universal-attribute-componentid.md)。|

**返回值：**

|类型|说明|
|:----|:----|
|[SubTabBarStyle](#class-subtabbarstyle)|返回SubTabBarStyle对象本身。|

#### func indicator(IndicatorStyle)

```cangjie
public func indicator(value: IndicatorStyle): SubTabBarStyle
```

**功能：** 设置选中子页签的下划线风格。子页签的下划线风格仅在水平模式下有效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[IndicatorStyle](#class-indicatorstyle)|是|-|选中子页签的下划线风格对象。|

**返回值：**

|类型|说明|
|:----|:----|
|[SubTabBarStyle](#class-subtabbarstyle)|返回SubTabBarStyle对象本身。|