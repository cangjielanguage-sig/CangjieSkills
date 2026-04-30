## 构建第二个页面（ArkTS与仓颉混合页面）

> **说明：**
>
> 在仓颉与ArkTS混合开发场景中，仓颉页面不是一个真正意义上具有完整生命周期的页面，只能以组件的形式嵌入到ArkTS页面中，因此需要在ArkTS侧提供一个@Entry的页面作为容器，来加载仓颉页面组件。
>
> 仓颉与ArkTS混合UI的详细内容请参见 [混合开发](https://developer.huawei.com/consumer/cn/doc/cangjie-guides/cj-appendix-hybrid)。

1. 创建仓颉页面。

    - 在**Project**窗口，打开**entry > src > main**，右键单击**cangjie**文件夹，选择**New -> Cangjie HybridComponent File**，**Component name**命名为**Second**，**Language** 中选中**Cangjie**选项，**Type** 中选中**With ArkTS Wrapper**选项,如下图所示：

       ![inputPageName](../../figures/start-inputPageName.png)

    - 单击**OK**，可以看到文件目录结构如下：

       ```text
        entry
        ├── .preview
        ├── build
        ├── libs
        ├── oh_modules
        └── src
             └── main
                  ├── cangjie
                  │    ├── types
                  │    ├── index.cj
                  │    └── second.cj
                  ├── ets
                  │    ├── entryability
                  │    ├── entrybackupability
                  │    └── pages
                  │         ├── Index.ets
                  │         └── second.ets
                  ├── resources
                  └── module.json5
       ```

       可以看到，在**src > main > cangjie**目录中会创建一个**second.cj**的仓颉源码文件，并且在**src > main > ets > pages**文件夹下自动生成**second.ets**的ArkTS侧仓颉页面容器。

    - 参考第一个ArkTS页面的样式，在仓颉页面中添加Text组件、Button组件等，并设置其样式。**second.cj**文件的示例如下：

       ```cangjie
       // second.cj
       package ohos_app_cangjie_entry

       import ohos.base.*
       import ohos.component.*
       import ohos.hybrid_base.*
       import ohos.state_macro_manage.*
       import ohos.state_manage.*

       @HybridComponentEntry
       @Component
       class Second {
           @State var msg: String = "Hello Cangjie"

           public func build() {
               Row() {
                   Column() {
                       Text(this.msg)
                           .fontSize(50)
                           .fontWeight(FontWeight.Bold)

                       Button() {
                           Text("Back")
                               .fontSize(30)
                               .fontWeight(FontWeight.Bold)
                       }
                       .shape(ShapeType.Capsule)
                       .margin(top: 20)
                       .backgroundColor(Color(0x0D9FFB))
                       .width(40.percent)
                       .height(5.percent)
                   }
                   .width(100.percent)
               }
               .height(100.percent)
           }
       }
       ```

2. 创建ArkTS侧仓颉页面的容器。

    - 在 ArkTS 页面中嵌入仓颉页面。**src > main > ets > pages > second.ets**文件的示例如下：

       ```typescript
       // second.ets
       // 在 ArkTS 页面中嵌入仓颉页面
       import { CJHybridComponentV2 } from '@cangjie/cjhybridview';

       @Entry
       @Component
       struct Second {
         build() {
           Row() {
             // 通过 CJHybridComponentV2 接口嵌入仓颉页面
             CJHybridComponentV2({
               library: "ohos_app_cangjie_entry", // 仓颉页面所在的 package 名字
               component: "Second"                // 仓颉页面对应的 class 名字
             })
           }
           .height('100%')
           .width('100%')
         }
       }
       ```

    > **说明：**
    >
    > 开发者需要自行开发ArkTS代码作为容器来嵌入仓颉页面，具体请参见[混合开发](https://developer.huawei.com/consumer/cn/doc/cangjie-guides/cj-appendix-hybrid)。

3. 配置第二个页面的路由。

- 在**Project**窗口，打开**entry > src > main > resources > base > profile**，在main_pages.json文件中的"src"下已经自动生成第二个页面的路由"pages/second"。示例如下：

   ```json
   {
     "src": [
       "pages/Index",
       "pages/second"
     ]
   }
   ```