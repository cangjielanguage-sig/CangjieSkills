# Search

提供搜索框组件，用于提供用户搜索内容的输入区域。

## 子组件

无

## 创建组件

### init(String, String, Option\<AppResource>, Option\<SearchController>)

```cangjie
public init(
    value!: String = "",
    placeholder!: String = "",
    icon!: Option<AppResource> = Option.None,
    controller!: Option<SearchController> = Option.None
)
```

**功能：** 创建Search组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|否|""| **命名参数。** 当前显示的搜索文本内容。|
|placeholder|String|否|""| **命名参数。** 无输入时的提示文本。|
|icon|Option\<[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)>|否|Option.None|搜索图标路径，默认使用系统搜索图标。<br>**说明：** <br>icon的数据源支持本地图片和网络图片。<br> - 支持的图片格式包括png、jpg、bmp、svg、gif、pixelmap和heif。<br> - 支持Base64字符串。格式data:image/[png\|jpeg\|bmp\|webp\| **命名参数。** heif];base64,[base64 data], 其中[base64 data]为Base64字符串数据。<br>如果与属性searchIcon同时设置，则searchIcon优先。|
|controller|Option\<[SearchController](#class-searchcontroller)>|否|Option.None| **命名参数。** Search组件控制器。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。