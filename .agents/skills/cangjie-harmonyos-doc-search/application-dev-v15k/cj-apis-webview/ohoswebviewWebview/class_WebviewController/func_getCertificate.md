### func getCertificate()

```cangjie
public func getCertificate(): Array<cert.X509Cert>
```

**功能：**  获取当前网站的证书信息。使用Web组件加载https网站，会进行SSL证书校验，该接口会返回当前网站的X509格式证书（X509Cert证书类型定义见[X509Cert](../DeviceCertificateKit/cj-apis-cert.md/#class-x509cert)定义），便于开发者展示网站证书信息。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|Array\<cert.X509Cert>|前加载的https网站的X509格式证书数组。|

**异常：**

- BusinessException：对应错误码如下表，详见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.|
  |17100001|Init error. The WebviewController must be associated with a Web component.|

**示例：**

<!-- compile -->

```cangjie
import kit.ArkWeb.*
import kit.UIKit.Web
import kit.LocalizationKit.*
import kit.UIKit.*
import kit.DeviceCertificateKit as cert

@Entry
@Component
class EntryView {
    @State
    // outputStr在UI界面调试信息
    var outputStr: String = ""

    var webCtrl: WebviewController = WebviewController()

    func build() {
        Row {
            Column {
                List(space: 5, initialIndex: 0) {
                    ListItem() {
                        Button("load example").fontSize(10).fontWeight(FontWeight.Bold).onClick(
                            {
                            // 加载一个https网站，查看网站的证书信息
                            => this.webCtrl.loadUrl("https://www.example.com")
                        }).height(50)
                    }
                    ListItem() {
                        Button("getCertificate").fontSize(10).fontWeight(FontWeight.Bold).onClick(
                            {
                            => try {
                                this.outputStr = parseX509CertInfo(this.webCtrl.getCertificate())
                            } catch (e: BusinessException) {
                                AppLog.error("ErrorCode: ${e.code}, ErrorMessage: ${e.message}")
                            }
                        }).height(50)
                    }
                }.height(20.percent)
                Text(this.outputStr).width(100.percent).fontSize(10)
                Web(src: "https://www.example.com", controller: webCtrl).width(100.percent).height(50.percent)
            }.width(100.percent)
        }.height(100.percent)
    }
}

func parseX509CertInfo(x509CertArray: Array<cert.X509Cert>): String {
    var res: String = "getCertificate success: len = ${x509CertArray.size}";
    for (i in 0..x509CertArray.size) {
        let issuerName: String = uint8ArrayToString(x509CertArray[i].getIssuerName().data)
        let subjectName: String = uint8ArrayToString(x509CertArray[i].getSubjectName().data)
        res = "${res}, index = ${i}, issuer name = ${issuerName}, subjectName=${subjectName}, valid start = ${x509CertArray[i].getNotBeforeTime()}, valid end = ${x509CertArray[i].getNotAfterTime()}"
    }
    return res;
}

func uint8ArrayToString(certBytes: Array<Byte>): String {
    let strBuilder = StringBuilder()
    for (i in 0..certBytes.size) {
        if (certBytes[i] != 0) {
            strBuilder.append(Rune(certBytes[i]))
        }
    }
    return strBuilder.toString();
}
```