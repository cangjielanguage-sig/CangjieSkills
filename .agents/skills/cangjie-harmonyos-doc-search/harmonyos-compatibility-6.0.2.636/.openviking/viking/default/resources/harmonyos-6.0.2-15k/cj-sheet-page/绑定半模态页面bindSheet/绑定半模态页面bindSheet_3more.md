# 绑定半模态页面（bindSheet）

[半模态页面（bindSheet）](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-sheettransition.md#func-bindsheetbool----unit-sheetoptions)默认是模态形式的非全屏弹窗式交互页面，允许部分底层父视图可见，帮助用户在与半模态交互时保留其父视图环境。

半模态页面适用于展示简单的任务或信息面板，例如，个人信息、文本简介、分享面板、创建日程、添加内容等。若需展示可能影响父视图的半模态页面，半模态支持配置为非模态交互形式。

半模态在不同宽度的设备上存在不同的形态能力，开发者对不同宽度的设备上有不同的形态诉求请参见([preferType](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-sheettransition.md#class-sheetoptions))属性。可以使用bindSheet构建半模态转场效果，详见[模态转场](./cj-modal-transition.md)。对于复杂或者冗长的用户流程，建议考虑其他的转场方式替代半模态。如[全模态转场](./cj-contentcover-page.md)和[Navigation转场](./cj-navigation-transition.md)。

## 使用约束

- 若无二次确认或者自定义关闭行为的场景，不建议使用[shouldDismiss/onWilDismiss](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-sheettransition.md#class-sheetoptions)接口。

## 生命周期

半模态页面提供了生命周期函数，用于通知用户该弹窗的生命周期状态。生命周期的触发顺序依次为：onWillAppear -> onAppear -> onWillDisappear -> onDisappear。

|名称|类型|说明|
|:---|:---|:---|
|onWillAppear|() -> Unit|半模态页面显示（动画开始前）回调函数。|
|onAppear|() -> Unit|半模态页面显示（动画结束后）回调函数。|
|onWillDisappear|() -> Unit|半模态页面回退（动画开始前）回调函数。|
|onDisappear|() -> Unit|半模态页面回退（动画结束后）回调函数。|