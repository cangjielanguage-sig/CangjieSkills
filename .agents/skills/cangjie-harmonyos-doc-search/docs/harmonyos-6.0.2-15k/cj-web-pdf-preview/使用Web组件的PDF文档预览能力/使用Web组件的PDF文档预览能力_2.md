- 预览加载应用内PDF资源文件，有两种使用形式。`@rawfile("test.pdf")`形式无法指定下面介绍的预览参数。

    ```cangjie
    import kit.LocalizationKit.{__GenerateResource__}

    Web(src: @rawfile("test.pdf"), controller: this.webController)
        .domStorageAccess(true)
    ```

    ```cangjie
    Web(src: "resource://rawfile/test.pdf", controller: this.webController)
        .domStorageAccess(true)
    ```

此外，通过配置PDF文件预览参数，可以控制打开预览时页面状态。

当前支持如下参数:

| 语法  | 描述  |
| :--------- | :---------- |
| nameddest=destination  |  指定PDF文档中的命名目标。 |
| page=pagenum  | 使用整数指定文档中的页码，文档第一页的pagenum值为1。|
| zoom=scale    zoom=scale,left,top | 使用浮点或整数值设置缩放和滚动系数。 例如：缩放值100表示缩放值为100%。 向左和向上滚动值位于坐标系中，0,0 表示可见页面的左上角，无论文档如何旋转。 |
| toolbar=1 \| 0 | 打开或关闭顶部工具栏。 |
| navpanes=1 \| 0 | 打开或关闭侧边导航窗格。 |

URL示例:

```text
https://example.com/test.pdf#Chapter6
https://example.com/test.pdf#page=3
https://example.com/test.pdf#zoom=50
https://example.com/test.pdf#page=3&zoom=200,250,100
https://example.com/test.pdf#toolbar=0
https://example.com/test.pdf#navpanes=0
```