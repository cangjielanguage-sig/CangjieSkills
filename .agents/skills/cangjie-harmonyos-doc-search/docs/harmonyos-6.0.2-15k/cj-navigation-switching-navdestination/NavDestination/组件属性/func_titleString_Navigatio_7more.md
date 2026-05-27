### func title(String, ?NavigationTitleOptions)

```cangjie
public func title(value: String, options!: ?NavigationTitleOptions = None): This
```

**功能：** 设置页面标题。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|页面标题。|
|options|?[NavigationTitleOptions](./cj-navigation-switching-navigation.md#class-navigationtitleoptions)|否|None|标题栏选项。|

### func title(() -> Unit, ?NavigationTitleOptions)

```cangjie
public func title(builder: () -> Unit, options!: ?NavigationTitleOptions = None): This
```

**功能：** 设置页面标题。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|builder|() -> Unit|是|-|页面标题。|
|options|?[NavigationTitleOptions](./cj-navigation-switching-navigation.md#class-navigationtitleoptions)|否|None|标题栏选项。|

### func title(NavDestinationCommonTitle, ?NavigationTitleOptions)

```cangjie
public func title(value: NavDestinationCommonTitle, options!: ?NavigationTitleOptions = None): This
```

**功能：** 设置页面标题。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[NavDestinationCommonTitle](#class-navdestinationcommontitle)|是|-|页面标题。|
|options|?[NavigationTitleOptions](./cj-navigation-switching-navigation.md#class-navigationtitleoptions)|否|None|标题栏选项。|

### func title(() -> Unit, Length, ?NavigationTitleOptions)

```cangjie
public func title(builder: () -> Unit, height: Length, options!: ?NavigationTitleOptions = None): This
```

**功能：** 设置页面标题。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|builder|() -> Unit|是|-|标题栏内容。|
|height|[Length](./cj-common-types.md#interface-length)|是|-|标题栏高度。取值范围：[0, +∞)。|
|options|?[NavigationTitleOptions](./cj-navigation-switching-navigation.md#class-navigationtitleoptions)|否|None|标题栏选项。|

### func hideTitleBar(Bool)

```cangjie
public func hideTitleBar(value: Bool): This
```

**功能：** 设置是否隐藏标题栏。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|是否隐藏标题栏。<br>true:隐藏标题栏。<br>false:显示标题栏。|

### func mode(NavDestinationMode)

```cangjie
public func mode(value: NavDestinationMode): This
```

**功能：** 设置NavDestination类型，不支持动态修改。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[NavDestinationMode](#enum-navdestinationmode)|是|-|NavDestination类型。|

### func backButtonIcon(String)

```cangjie
public func backButtonIcon(value: String): This
```

**功能：** 设置标题栏返回键图标。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|返回键图片资源。|