### func precompileJavaScript(String, Array\<UInt8>, CacheOptions)

```cangjie
public func precompileJavaScript(url: String, script: Array<UInt8>, cacheOptions: CacheOptions): Int32
```

**功能：** 预编译JavaScript生成字节码缓存或根据提供的参数更新已有的字节码缓存。 接口通过提供的文件信息、E-Tag响应头和Last-Modified响应头判断是否需要更新已有的字节码缓存。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-|本地JavaScript文件对应的网络地址，即业务网页请求该文件的服务器版本时使用的网络地址。网络地址仅支持http或https协议，长度不超过2048。如果该网络地址对应的缓存失效，则业务网页将通过网络请求对应的资源。|
|script|Array\<UInt8>|是|-|本地JavaScript的文本内容。内容不能为空。|
|cacheOptions|[CacheOptions](#class-cacheoptions)|是|-|用于控制字节码缓存更新。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|生成字节码缓存的错误码，0表示无错误，-1表示内部错误。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Invalid input parameter.|
  |17100001|Init error.|

**示例：**

```cangjie

// index.cj
import ohos.base.*
import kit.ArkWeb.*

@Entry
@Component
class EntryView {
    let webController = WebviewController()
    func build() {
        Column(10) {
            Button("precompileJavaScript").onClick {
                evt =>
                AppLog.info("precompileJavaScript")
                try {
                    let url = "https://www.example.com/business.html"
                    let script = "1234"
                    let web1 = WebHeader("123", "456")
                    let web2 = WebHeader("234", "567")
                    let cacheOptions = CacheOptions([web1, web2])
                    let javaScript = webController.precompileJavaScript(url, script, cacheOptions)
                    AppLog.info("precompileJavaScript: ${javaScript}")
                } catch (e: BusinessException) {
                    AppLog.error("ErrorCode: ${e.code},  Message: ${e.message}")
                }
            }
        }
    }
}
```