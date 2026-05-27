## 使用场景

开发者可以通过调用[startAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-startabilitywant)接口，由系统从已安装的应用中寻找符合要求的应用，打开特定文件。

例如，浏览器下应用下载PDF文件，可以调用此接口选择文件处理应用打开此PDF文件。开发者需要在请求中设置待打开文件的URI路径（[uri](#接口关键参数说明)）、文件格式（[type](#接口关键参数说明)）等字段，以便系统能够识别，直接拉起文件打开应用或弹出一个选择框，让用户选择合适的应用来打开文件，效果示意如下图所示。

图1 效果示意图

![file-open](figures/file-open.jpeg)

## 接口关键参数说明

开发者通过调用[startAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-startabilitywant)接口即可实现由已安装的垂域应用来打开文件。

**表1** startAbility请求中[Want](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-want)相关参数说明

| 参数名称 | 类型   | 是否必填 | 说明                                                                                                                                                                                   |
|----------|--------|----------|----------|
| uri      | String | 是       | 表示待打开文件的URI路径，一般配合type使用。<br/>uri格式为：file:\/\/bundleName\/path<br/>- file：文件URI的标志。<br/>- bundleName：该文件资源的属主。<br/>- path：文件资源在应用沙箱中的路径。 |
| type     | String | 否       | 表示打开文件的类型，推荐使用[UTD类型](../database/cj-uniform-data-type-descriptors.md)，比如：'general.plain-text'、'general.image'。目前也可以兼容使用[MIME type类型](https://www.iana.org/assignments/media-types/media-types.xhtml?utm_source=ld246.com)，如：'text/xml' 、 'image/*'等。<br/>**说明：** <br/>1. type为可选字段，如果不传type，系统会尝试根据uri后缀名判断文件类型进行匹配；如果传入type，必须确保与uri的文件类型一致，否则会导致无法匹配到合适的应用。文件后缀与文件类型的映射关系参见[Uniform Type Descriptor(UTD)预置列表](../database/cj-uniform-data-type-list.md)。<br/>2. 不支持传\*/\*。|
| parameters | String      | 否         | 表示由系统定义，由开发者按需赋值的自定义参数，文件打开场景请参见表2。                                                                                                                                                                                       |
| flags | UInt32 | 否 | 表示处理方式，文件打开场景请参见表3。                                                                                                                                                                                       |

**表2** [parameters](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#enum-params)相关参数说明

| 参数名称                              | 类型    | 说明                                                                                                                                                                |
|---------------------------------------|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ability.params.stream                 | String  | 指示携带的文件URI要授权给目标方，用于待打开的文件存在其他文件依赖的场景。例如打开本地html文件依赖本地其余资源文件的场景等。对应的value必须是string类型的文件URI数组。文件URI的获取参考表1中uri参数。 |
| ohos.ability.params.showDefaultPicker | Bool | 表示是否强制展示文件打开方式的选择弹框，缺省为false。<br/>- false：表示由系统策略或默认应用设置决定直接拉起文件打开应用还是展示弹框。<br/>- true：表示始终展示弹框。                                                                            |
| showCaller                            | Bool | 表示调用方本身是否作为目标方应用之一参与匹配，缺省为false。<br/>- false：不参与匹配。<br/>- true：参与匹配。                                                                            |

**表3** [flags](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#enum-flags)相关参数说明

| 参数名称                       | 值         | 说明                       |
|--------------------------------|------------|----------------------------|
| FLAG_AUTH_READ_URI_PERMISSION  | 0x00000001 | 指对URI执行读取操作的授权。 |
| FLAG_AUTH_WRITE_URI_PERMISSION | 0x00000002 | 指对URI执行写入操作的授权。 |