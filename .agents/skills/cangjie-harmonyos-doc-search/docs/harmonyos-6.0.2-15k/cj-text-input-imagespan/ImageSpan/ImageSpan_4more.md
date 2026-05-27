# ImageSpan

作为[Text](./cj-text-input-text.md)组件的子组件，用于显示行内图片。

## 子组件

无

## 创建组件

### init(AppResource)

```cangjie
public init(src: AppResource)
```

**功能：** 创建ImageSpan组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|图片的数据源，支持本地图片和网络图片。<br>支持的图片格式包括png、jpg、bmp、svg、gif和heif。|

### init(PixelMap)

```cangjie
public init(src: PixelMap)
```

**功能：** 创建ImageSpan组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|[PixelMap](../apis/ImageKit/cj-apis-image.md#class-pixelmap)|是|-|图片的数据源，支持本地图片和网络图片。<br>PixelMap格式为像素图，常用于图片编辑的场景。<br>支持Base64字符串。格式data:image[png\|jpeg\|bmp\|webp\|heif]；base64，[base64 data]，其中[base64 data]为Base64字符串数据。|

### init(String)

```cangjie
public init(src: String)
```

**功能：** 创建ImageSpan组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|String|是|-|图片的数据源，支持本地图片和网络图片。<br>支持 file:///data/storage 路径前缀的字符串，用于读取本应用安装目录下files文件夹下的图片资源。需要保证目录包路径下的文件有可读权限。|

## 通用属性/通用事件

通用属性：支持[尺寸设置](./cj-universal-attribute-size.md)、[背景设置](./cj-universal-attribute-background.md)、[边框设置](./cj-universal-attribute-border.md)。

通用事件：仅支持[点击事件](./cj-universal-event-click.md)。