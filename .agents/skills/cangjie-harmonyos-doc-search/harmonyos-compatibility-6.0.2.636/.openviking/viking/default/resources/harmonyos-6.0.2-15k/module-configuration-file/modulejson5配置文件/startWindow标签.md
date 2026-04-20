## startWindow标签

该标签指向一个profile文件资源，用于指定UIAbility组件启动页面的配置文件，在开发视图的resources/base/profile下面定义配置文件start_window.json，如果配置了该字段，startWindowIcon和startWindowBackground字段将不生效。从API version 18开始，支持该字段。

**表25** startWindow标签配置说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| -------- | -------- | -------- | -------- |
| startWindowAppIcon | 标识当前UIAbility组件启动页面图标资源文件的索引，取值为长度不超过255字节的字符串。| 字符串 | 可缺省，缺省值为空。 |
| startWindowIllustration | 标识当前UIAbility组件启动页面插画资源文件的索引，取值为长度不超过255字节的字符串。 | 字符串 | 可缺省，缺省值为空。 |
| startWindowBrandingImage | 标识当前UIAbility组件启动页面品牌标识资源文件的索引，取值为长度不超过255字节的字符串。 | 字符串 | 可缺省，缺省值为空。 |
| startWindowBackgroundColor | 标识当前UIAbility组件启动页面背景颜色资源文件的索引，取值为长度不超过255字节的字符串。 | 字符串 | 不可缺省。 |
| startWindowBackgroundImage | 标识当前UIAbility组件启动页面背景图片资源文件的索引，取值为长度不超过255字节的字符串。 | 字符串 | 可缺省，缺省值为空。 |
| startWindowBackgroundImageFit | 标识当前UIAbility组件启动页面背景图像适应方式，支持的取值如下：<br/>-&nbsp;Contain：按照宽高比进行缩小或放大，图片完全显示在显示边界内。<br/>-&nbsp;Cover：按照宽高比进行缩小或放大，图片两边都大于或等于显示边界。<br/>-&nbsp;Auto：自适应显示。<br/>-&nbsp;Fill：不按照宽高比进行放大或缩小，图片充满显示边界。<br/>-&nbsp;ScaleDown：按照宽高比显示，图片缩小或保持不变。<br/>-&nbsp;None：保持原有尺寸显示。 | 字符串 | 可缺省，缺省值为Cover。 |

resources/base/profile路径下的start_window.json资源文件示例如下：

```json
{
  "startWindowAppIcon": "$media:start_window_app_icon",
  "startWindowIllustration": "$media:start_window_illustration",
  "startWindowBrandingImage": "$media:start_window_branding_image",
  "startWindowBackgroundColor": "$color:start_window_back_ground_color",
  "startWindowBackgroundImage": "$media:start_window_back_ground_image",
  "startWindowBackgroundImageFit": "Cover"
}
```