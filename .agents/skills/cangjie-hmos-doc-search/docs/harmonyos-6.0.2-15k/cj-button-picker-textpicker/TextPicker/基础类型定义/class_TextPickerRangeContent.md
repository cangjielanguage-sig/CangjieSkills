### class TextPickerRangeContent

```cangjie
public class TextPickerRangeContent {
    public var icon: String
    public var text: Option<String>
    public init(icon: String,text!: ?String = None)
    public init(icon: AppResource,text!: ?String = None)
    public init(icon: String,text!: ?AppResource = None)
    public init(icon: AppResource,text!: ?AppResource = None)
}
```

**功能：** 数据选择器数据选择列表。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var icon

```cangjie
public var icon: String
```

**功能：** 图片资源。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var text

```cangjie
public var text: Option<String>
```

**功能：** 文本信息。

**类型：** Option\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(String, ?String)

```cangjie
public init(icon: String,text!: ?String = None)
```

**功能：** 构建TextPickerRangeContent对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|icon|String|是|-|图片资源，表示图片存放的路径，例如"/common/hello.png"。|
|text|?String|否|None|文本信息。如果文本长度大于列宽时，文本被截断。|

#### init(AppResource, ?String)

```cangjie
public init(icon: AppResource,text!: ?String = None)
```

**功能：** 构建TextPickerRangeContent对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|icon|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|图片资源。|
|text|?String|否|None|文本信息。如果文本长度大于列宽时，文本被截断。|

#### init(String, ?AppResource)

```cangjie
public init(icon: String,text!: ?AppResource = None)
```

**功能：** 构建TextPickerRangeContent对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|icon|String|是|-|图片资源，表示图片存放的路径，例如"/common/hello.png"。|
|text|?[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|否|None|文本信息。如果文本长度大于列宽时，文本被截断。|

#### init(AppResource, ?AppResource)

```cangjie
public init(icon: AppResource,text!: ?AppResource = None)
```

**功能：** 构建TextPickerRangeContent对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|icon|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|图片资源。|
|text|?[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|否|None|文本信息。如果文本长度大于列宽时，文本被截断。|