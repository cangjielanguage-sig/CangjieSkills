### func setPathAllowingUniversalAccess(Array\<String>)

```cangjie
public func setPathAllowingUniversalAccess(pathList: Array<String>): Unit
```

**功能：** 设置一个路径列表，当file协议访问该路径列表中的资源时，允许跨域访问本地文件。此外，当设置了路径列表时，file协议仅允许访问路径列表中的资源（fileAccess的行为将会被此接口行为覆盖）。路径列表中的路径必须满足以下路径格式之一：

1.应用文件目录的子目录（应用文件目录通过Ability Kit中的Context.filesDir获取），例如：

/data/storage/el2/base/files/example

/data/storage/el2/base/haps/entry/files/example

2.应用资源目录及其子目录（应用资源目录通过Ability Kit中的Context.resourceDir获取），例如：

/data/storage/el1/bundle/entry/resource/resfile

/data/storage/el1/bundle/entry/resource/resfile/example

当路径列表中有其中一个路径不满足以上条件之一，则会抛出异常码401，并且设置路径列表失败。当设置的路径列表为空，则file协议可访问范围以fileAccess的行为为准。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pathList|Array\<String>|是|-|路径列表。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Parameter string is too long. 3.Parameter verification failed.|
  |17100001|Init error. The WebviewController must be associated with a Web component.|

**示例：**

<!-- compile -->

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
            // 此处路径是参照函数说明给出的一个实例路径。
            Button("setPathAllowingUniversalAccess").onClick {
                event: ClickEvent => webController.setPathAllowingUniversalAccess(
                    ["/data/storage/el2/base/haps/entry/files/example"])
            }
        }
    }
}
```