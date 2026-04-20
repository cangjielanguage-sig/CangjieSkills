### class SelectOption

```cangjie
public class SelectOption {
    public var value: String
    public var icon: String
    public init(value: String, icon!: String)
    public init(value: String, icon!: AppResource)
    public init(value: AppResource, icon!: String)
    public init(value: AppResource, icon!: AppResource)
}
```

**功能：** 设置下拉菜单组件参数的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var icon

```cangjie
public var icon: String
```

**功能：** 下拉选项图标。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var value

```cangjie
public var value: String
```

**功能：** 下拉选项内容。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(String, String)

```cangjie
public init(value: String, icon!: String)
```

**功能：** 构造SelectOption对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|下拉选项内容。|
|icon|String|是|-| **命名参数。** 下拉选项图标。|

#### init(String, AppResource)

```cangjie
public init(value: String, icon!: AppResource)
```

**功能：** 构造SelectOption对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|下拉选项内容。|
|icon|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 下拉选项图标。|

#### init(AppResource, String)

```cangjie
public init(value: AppResource, icon!: String)
```

**功能：** 构造SelectOption对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|下拉选项内容。|
|icon|String|是|-| **命名参数。** 下拉选项图标。|

#### init(AppResource, AppResource)

```cangjie
public init(value: AppResource, icon!: AppResource)
```

**功能：** 构造SelectOption对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|下拉选项内容。|
|icon|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 下拉选项图标。|