### static func deleteOrigin(String)

```cangjie
public static func deleteOrigin(origin: String): Unit
```

**功能：** 清除指定源所使用的存储。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|origin|String|是|-|指定源的字符串索引，来自于[getOrigins](#static-func-getoriginsasynccallbackarraywebstorageorigin)。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.|
  |17100011|Invalid origin.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

package ohos_app_cangjie_entry

import ohos.base.*
import kit.ArkWeb.*
import kit.ArkWeb.Error as webError
import kit.UIKit.Web
import kit.LocalizationKit.*

@Entry
@Component
class EntryView {
    let webController = WebviewController()
    func build() {
        Column(10) {
            Button("deleteOrigin").onClick {
                evt =>
                AppLog.info("deleteOrigin")
                WebStorage.deleteOrigin("resource://rawfile/")
            }.width(400.px).height(150.px)
            Web(src: @rawfile("storage.html"), controller: webController).onPageBegin(
                {
                evt => AppLog.info("page begin url: ${evt.url}")
            }).onPageEnd({
                evt => AppLog.info("page end url: ${evt.url}")
            })
        }
    }
}
```

加载的html文件。

```html
<!-- storage.html -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>test</title>
    <script type="text/javascript">
        var db = openDatabase('mydb','1.0','Test DB',2 * 1024 * 1024);
        var msg;

        db.transaction(function(tx){
            tx.executeSql('INSERT INTO LOGS (id,log) VALUES(1,"test1")');
            tx.executeSql('INSERT INTO LOGS (id,log) VALUES(2,"test2")');
            msg = '<p>数据表已创建,且插入了两条数据。</p>';

            document.querySelector('#status').innerHTML = msg;
        });

        db.transaction(function(tx){
            tx.executeSql('SELECT * FROM LOGS', [], function (tx, results) {
                var len = results.rows.length,i;
                msg = "<p>查询记录条数：" + len + "</p>";

                document.querySelector('#status').innerHTML += msg;

                for(i = 0; i < len; i++){
                    msg = "<p><b>" + results.rows.item(i).log + "</b></p>";
                    document.querySelector('#status').innerHTML += msg;
                }
            }, null);
        });
    </script>
</head>
<body>
<div id="status" name="status">状态信息</div>
</body>
</html>
```