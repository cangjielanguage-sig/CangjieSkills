# 使用Web组件打印前端页面

Web组件打印html页面时可通过W3C标准协议接口和应用接口两种方式实现。

使用打印功能前，请在module.json5中配置相关权限，添加方法请参见[在配置文件中声明权限](../security/AccessToken/cj-declare-permissions.md)。

```json
"requestPermissions":[
  {
    "name" : "ohos.permission.PRINT"
  }
]
```

## 使用W3C标准协议接口拉起打印

通过创建打印适配器，拉起打印应用，并对当前Web页面内容进行渲染，渲染后生成的PDF文件信息通过fd传递给打印框架。W3C标准协议接口window.print()方法用于打印当前页面或弹出打印对话框。该方法没有任何参数，只需要在JavaScript中调用即可。

可通过前端css样式控制是否打印，例如@media print。再通过web加载该html页面的方式运行。

- print.html页面代码：

    ```html
    <!-- resources/rawfile/print.html  -->
    <!DOCTYPE html>
    <html>

    <head>
        <meta charset="utf-8">
        <title>printTest</title>
        <style>
            @media print {
                h1 {
                    display: none;
                }
            }
        </style>
    </head>

    <body>
        <div>
            <h1><b>
                    <center>This is a test page for printing</center>
                </b>
                <hr color=#00cc00 width=95%>
            </h1>
            <button class="Button Button--outline" onclick="window.print();">Print</button>
            <p> content content content </p>
            <div id="printableTable">
                <table>
                    <thead>
                        <tr>
                            <td>Thing</td>
                            <td>Chairs</td>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>1</td>
                            <td>blue</td>
                        </tr>
                        <tr>
                            <td>2</td>
                            <td>green</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p> content content content </p>
            <p> content content content </p>
        </div>
    </body>
    ```

- 应用侧代码：

    ```cangjie
    // index.cj
    import ohos.state_macro_manage.*
    import kit.ArkWeb.WebviewController
    import kit.UIKit.Web
    import kit.LocalizationKit.{__GenerateResource__}

    @Entry
    @Component
    class EntryView {
        let webController = WebviewController()

        func build() {
            Row {
                Column {
                    Web(src: @rawfile("print.html"), controller: this.webController).javaScriptAccess(true)
                }.width(100.percent)
            }.width(100.percent)
        }
    }
    ```
