# 全屏模态转场

通过bindContentCover属性为组件绑定全屏模态页面，在组件插入和删除时可通过设置转场参数ModalTransition显示过渡动效。

> **说明：**
>
> - 不支持横竖屏切换。
> - 不支持路由跳转。

## func bindContentCover(Bool, () -> Unit, ContentCoverOptions)

```cangjie
public func bindContentCover(isShow: Bool, builder: () -> Unit, contentCoverOptions: ContentCoverOptions): This
```

**功能：** 给组件绑定全屏模态页面，点击后显示模态页面。模态页面内容自定义，显示方式可设置无动画过渡，上下切换过渡以及透明渐变过渡方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
| :-------   | :---------- | :------- | :-------- | :----------|
| isShow | Bool |  是   |   \-   | 是否显示全屏模态页面。 |
| builder | () -> Unit |    是  |    \-  |  配置全屏模态页面内容。 |
| contentCoverOptions | [ContentCoverOptions](./cj-universal-attribute-bindcontentcover.md#class-contentcoveroptions) |   是   |   \-   |  配置全屏模态页面的可选属性。 |