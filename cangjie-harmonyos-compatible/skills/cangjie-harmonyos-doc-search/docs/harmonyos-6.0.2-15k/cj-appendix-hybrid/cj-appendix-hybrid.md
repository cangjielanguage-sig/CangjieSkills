# 混合开发

> **说明：**
>
> 在该场景下使用CJHybridComponentV2替代CJHybridComponent。

## 背景

仓颉作为HarmonyOS应用开发语言，开发者使用仓颉进行应用开发涉及以下2种场景：

- 场景1：开发纯仓颉应用，即应用中全量功能都使用仓颉语言开发。
- 场景2：在ArkTS应用中，使用仓颉开发部分应用逻辑。

后者会涉及混合使用ArkTS和仓颉两种语言开发UI逻辑的情况，即UI页面中同时包含由ArkTS和仓颉开发的页面/组件。

借助ArkUI的NodeContainer的能力，以及仓颉与ArkTS互操作，可以实现仓颉和ArkTS的混合开发。仓颉组件可作为NodeContainer的内容嵌入ArkTS页面中。

## 与纯仓颉开发模式的异同

相同点：

- 混合UI场景下的页面和纯仓颉写法基本一致。
- 状态管理支持@State、@Link、@Prop、@Observed、@Publish、@Provide、@Consume，但不支持跨语言的状态同步。

不同点：
区别体现在生命周期和页面跳转上。

- 混合UI场景的仓颉页面不是一个真正意义上具有完整生命周期的页面，不支持页面生命周期接口。
- 无法在仓颉页面中使用仓颉的router进行页面跳转。

## 混合页面工程

混合页面工程，依赖仓颉与 ArkTS 互操作能力，首先需要参考 "[在 ArkTS （+ C++）的HAP或HAR中创建仓颉模块](../../../Cangjie_Deveco_Studio/source_zh_cn/project-manager/cj-module-management.md#在arkts-c的hap或har中创建仓颉模块)" 章节，创建一个 ArkTS 仓颉混合工程，然后参考 "[添加供ArkTS调用的页面组件](../../../Cangjie_Deveco_Studio/source_zh_cn/project-manager/cj-module-management.md#添加供arkts调用的页面组件)" 章节，添加一个混合页面，按照以上步骤可以完成混合UI工程的配置。

## 示例代码

### 添加仓颉UI代码

修改./entry/src/main/cangjie/newfile.cj，示例代码如下

```cangjie
package ohos_app_cangjie_entry

import ohos.component.Text
import ohos.component.Button
import ohos.component.Column
import ohos.component.CustomView
import ohos.state_macro_manage.State
import ohos.state_macro_manage.Component
import ohos.state_manage.LocalStorage
import ohos.state_manage.ObservedProperty
import ohos.state_manage.SubscriberManager
import ohos.state_manage.ViewStackProcessor
import ohos.state_macro_manage.HybridComponentEntry
import ohos.hybrid_base.HybridComponentBase

@HybridComponentEntry
@Component
class Test {
    @State
    var msg: String = "Hello"

    public func build() {
        Column {
            Text(msg)
            Button("click to change Text").onClick {
                => msg = "world"
            }
        }
    }
}
```

### ArkTS页面中插入仓颉UI

修改./entry/src/main/ets/pages/Index.ets，示例如下

```cangjie

import { CJHybridComponentV2 } from "cjhybridview" // 导入CJHybridComponentV2

@Entry
@Component
class Index {
  build() {
    Column() {
      CJHybridComponentV2({
        library: "ohos_app_cangjie_entry",      // 指定加载的仓颉package，对应上面的仓颉UI所在的包名
        component: "Test"    // 指定加载的仓颉class，对应上面仓颉UI中使用@HybridComponentEntry修饰的class
      })
    }
    .height('100%')
    .width('100%')
  }
}
```

按照上述操作，可以完成一个简单的混合UI工程创建。

![img1](figures/hybrid_1.png)
