# 文本显示（Text/Span）

Text是文本组件，通常用于展示用户视图，如显示文章的文字内容，支持绑定自定义文本选择菜单，用户可根据需要选择不同功能，同时还可以扩展自定义菜单，丰富可用选项，进一步提升用户体验。Span则用于呈现显示行内文本。具体用法请参见[Text](../../API_Reference/source_zh_cn/arkui-cj/cj-text-input-text.md)和[Span](../../API_Reference/source_zh_cn/arkui-cj/cj-text-input-span.md)组件的使用说明。

## 创建文本

Text可通过以下两种方式来创建：

- string字符串。

    ```cangjie
    Text('我是一段文本')
    ```

    ![Textdisply](figures/Textdisply.png)

- 引用AppResource资源。

    资源引用类型可以通过@r创建AppResource类型对象，文件位置为/resources/base/element/string.json，具体内容如下：

    ```cangjie
    {
      "string": [
        {
          "name": "module_desc",
          "value": "模块描述"
        }
      ]
    }
    ```

    ```cangjie
    Text(@r(app.string.module_desc))
      .baselineOffset(0)
      .fontSize(30)
      .border(width: 1)
      .padding(10)
      .width(300)
    ```

    ![Textdisply1](figures/Textdisply1.png)