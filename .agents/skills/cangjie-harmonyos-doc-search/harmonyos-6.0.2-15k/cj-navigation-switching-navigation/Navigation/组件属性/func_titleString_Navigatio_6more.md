### func title(String, NavigationTitleOptions)

```cangjie
public func title(title: String, options!: ?NavigationTitleOptions = None): This
```

**功能：** 设置页面标题。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|title|String|是|-|页面标题。|
| options | ?[NavigationTitleOptions](#class-navigationtitleoptions) | 否  | None|标题栏选项。|

### func title(AppResource, NavigationTitleOptions)

```cangjie
public func title(title: AppResource, options!: ?NavigationTitleOptions = None): This
```

**功能：** 设置页面标题。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|title|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|页面标题。|
| options | ?[NavigationTitleOptions](#class-navigationtitleoptions) | 否  | None| 标题栏选项。|

### func title(() -> Unit, NavigationTitleOptions)

```cangjie
public func title(builder: () -> Unit, options!: ?NavigationTitleOptions = None): This
```

**功能：** 设置页面标题。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| builder |() -> Unit|是|-|页面标题。|
| options | ?[NavigationTitleOptions](#class-navigationtitleoptions) | 否  | None| 标题栏选项。|

### func title(String, String, NavigationTitleOptions)

```cangjie
public func title(mainTitle: String, subTitle: String, options!: ?NavigationTitleOptions = None): This
```

**功能：** 设置页面主副标题。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| builder |String|是|-|页面主标题。|
| mainTitle |String|是|-|页面副标题。|
| options | ?[NavigationTitleOptions](#class-navigationtitleoptions) | 否  | None| 标题栏选项。字符串超长时，如果不设置副标题，先缩小再换行（2行）最后截断。如果设置副标题，先缩小最后截断。|

### func title(() -> Unit, Length, NavigationTitleOptions)

```cangjie
public func title(builder: () -> Unit, height: Length, options!: ?NavigationTitleOptions = None): This
```

**功能：** 设置页面主副标题。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| builder |() -> Unit|是|-|页面标题。|
| height |[Length](./cj-common-types.md#interface-length)|是|-|标题高度。|
| options | ?[NavigationTitleOptions](#class-navigationtitleoptions) | 否  | None| 标题栏选项。|

### func title(NavigationCommonTitle, NavigationTitleOptions)

```cangjie
public func title(value: NavigationCommonTitle, options!: ?NavigationTitleOptions = None): This
```

**功能：** 设置页面主副标题。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| value |[NavigationCommonTitle](#class-navigationcommontitle)|是|-|页面标题。|
| options | ?[NavigationTitleOptions](#class-navigationtitleoptions) | 否  | None| 标题栏选项。|