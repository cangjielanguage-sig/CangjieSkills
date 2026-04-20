### func enableDataDetector(Bool)

```cangjie
public func enableDataDetector(value: Bool): This
```

**功能：** 设置是否进行文本特殊实体识别。

> **说明：**
>
> - 该接口依赖设备底层应具有文本识别能力，否则设置不会生效。
> - 当enableDataDetector设置为true，同时不设置dataDetectorConfig属性时，默认识别所有类型的实体，所识别实体的color为0xff007dff、decorationType为TextDecorationType.Underline、decorationColor为0xff007dff、decorationStyle为TextDecorationStyle.SOLID。
> - 触摸点击和鼠标右键点击实体，会根据实体类型弹出对应的实体操作菜单，鼠标左键点击实体会直接响应菜单的第一个选项。
> - 当overflow设置为TextOverflow.MARQUEE时，该功能不会生效。
> - 当copyOption设置为CopyOptions.None时，点击实体弹出的菜单没有选择文本和复制功能。当copyOption不为CopyOptions.None，且textSelectable设置为TextSelectableMode.UNSELECTABLE时，仍然具有实体复制功能，但没有选择文本功能。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|使能文本识别。<br>初始值： false。|

### func font(TextFont)

```cangjie
public func font(value: TextFont): This
```

**功能：** 设置文本样式，支持设置字体配置项。仅Text组件生效，其子组件不生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[TextFont](#class-textfont)|是|-|文本样式。|

### func fontColor(ResourceColor)

```cangjie
public func fontColor(value: ResourceColor): This
```

**功能：** 设置字体颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](cj-common-types.md#interface-resourcecolor)|是|-|使用引入资源的方式设置字体颜色。<br>初始值：'e6182431'。|

### func fontFamily(String)

```cangjie
public func fontFamily(value: String): This
```

**功能：** 设置字体列表。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|字体列表。默认字体'HarmonyOS Sans'。|

### func fontFamily(AppResource)

```cangjie
public func fontFamily(content: AppResource): This
```

**功能：** 设置字体列表。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|使用引入资源的方式设置字体列表。默认字体'HarmonyOS Sans'。|