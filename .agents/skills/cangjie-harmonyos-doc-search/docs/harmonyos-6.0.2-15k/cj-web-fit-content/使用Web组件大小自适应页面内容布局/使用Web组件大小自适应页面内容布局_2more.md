# 使用Web组件大小自适应页面内容布局

使用Web组件大小自适应页面内容布局模式`layoutMode(WebLayoutMode.FIT_CONTENT)`时，能使Web组件的大小根据页面内容自适应变化。

适用于Web组件需要根据网页高度撑开，与其他原生组件一起滚动的场景，如：

- 浏览长文章。Web组件同一布局层级有其他原生组件，如评论区、工具栏等。
- 长页面首页。Web组件同一布局层级有其他原生组件，如宫格菜单。

## 规格与约束

1. 建议配置[过滚动模式](../../API_Reference/source_zh_cn/arkui-cj/cj-web-web.md#func-overscrollmodeoverscrollmode)为关闭状态。当过滚动模式开启时，当用户在Web界面上滑动到边缘时，Web会通过弹性动画弹回界面，会与Scroll组件的回弹相互冲突，影响体验。
2. [键盘避让](../../API_Reference/source_zh_cn/arkui-cj/cj-web-web.md#func-keyboardavoidmodewebkeyboardavoidmode)属性配置为RESIZE_CONTENT时，该避让模式不生效。
3. 不支持对页面进行缩放。
4. 不支持通过Web组件的height属性修改组件高度。
5. 仅支持根据页面内容自适应组件高度，不支持自适应宽度。