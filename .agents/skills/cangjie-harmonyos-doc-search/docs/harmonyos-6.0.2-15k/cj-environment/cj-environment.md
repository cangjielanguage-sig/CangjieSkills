# Environment：设备环境查询

开发者如果需要应用程序运行的设备的环境参数，以此来作出不同的场景判断，比如多语言，深浅色模式等，需要用到Environment设备环境查询。

Environment是ArkUI框架在应用程序启动时创建的单例对象。它为AppStorage提供了一系列描述应用程序运行状态的属性。Environment的所有属性都是不可变的（即应用不可写入），所有的属性都是简单类型。

Environment提供了读取系统某些环境变量的能力，具体见[Environment内置参数](#environment内置参数)，并将其值写入AppStorage里，所以开发者需要通过AppStorage才能获取环境变量的值。

在阅读本文档前，建议提前阅读：[AppStorage](./cj-appstorage.md)。

## Environment内置参数

|键|数据类型|描述|
|:---|:---|:---|
|accessibilityEnabled|Bool|获取无障碍屏幕读取是否启用。|
|colorMode|ColorMode|色彩模型类型：选项为ColorMode.LIGHT: 浅色，ColorMode.DARK: 深色。|
|fontScale|Float64|字体大小比例。范围: [0.85, 1.45]。|
|fontWeightScale|Float64|字体粗细程度。范围: [0.6, 1.6]。|
|layoutDirection|LayoutDirection|布局方向类型：包括LayoutDirection.Ltr: 从左到右，LayoutDirection.Rtl: 从右到左。|
|languageCode|String|当前系统语言值，取值必须为小写字母, 例如zh。|

## 使用场景

### 从UI中访问Environment参数

- 使用Environment.envProp将设备运行的环境变量存入AppStorage中。

    ```cangjie
    // 将设备的语言code存入AppStorage，默认值为en
    Environment.envProp<String>("languageCode", "en")
    ```

- 可以使用@StorageProp链接到Component中。

    ```cangjie
    @StorageProp["languageCode"]
    let languageCode: String = "en"
    ```

设备环境到Component的更新链：Environment --> AppStorage -->Component。

> **说明：**
>
> @StorageProp关联的环境参数可以在本地更改，但不能同步回AppStorage中，因为应用对环境变量参数是不可写的，只能在Environment中查询。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    let SysLanguageCode = Environment.envProp<String>("languageCode", "en")
    @StorageProp["languageCode"]
    let languageCode: String = "en"
    func build() {
        Row() {
            Column() {
                // 输出当前设备的languageCode
                Text(this.languageCode)
            }
        }
    }
}
```

### 应用逻辑使用Environment

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.hilog.Hilog

@Entry
@Component
class EntryView {
    // 使用Environment.EnvProp将设备运行languageCode存入AppStorage中；
    let SysLanguageCode = Environment.envProp<String>("languageCode", "en")
    // 从AppStorage获取单向绑定的languageCode的变量
    let lang: ObservedProperty<String> = AppStorage.`prop`<String>('languageCode').getOrThrow()
    func build() {
        Row() {
            Column() {
                Button("lang").onClick {
                    => if (lang.get() == 'zh') {
                        Hilog.info(0, "Chinese", "你好")
                    } else {
                        Hilog.info(0, "En", "Hello")
                    }
                }
            }
        }
    }
}
```
