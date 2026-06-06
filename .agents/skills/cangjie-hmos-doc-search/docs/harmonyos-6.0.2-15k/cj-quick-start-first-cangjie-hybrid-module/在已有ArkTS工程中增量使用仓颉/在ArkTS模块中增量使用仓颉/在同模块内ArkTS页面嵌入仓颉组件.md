### 在同模块内，ArkTS页面嵌入仓颉组件

1. 创建仓颉页面。

   在**Project**窗口，打开**my_module > src > main**，右键单击**cangjie**文件夹，选择**New -> Cangjie HybridComponent File**，**Component name**命名为**CangjiePage**，并选中**Cangjie**选项，最后单击**OK**，可以看到文件目录结构如下：

   ```text
   my_module
   ├── build
   ├── libs
   ├── oh_modules
   └── src
        ├── main
        │    ├── cangjie
        │    │    ├── ark_interop_api
        │    │    ├── types
        │    │    ├── cangjie_page.cj
        │    │    └── index.cj
        │    ├── ets
        │    │    └── pages
        │    │         └── MyModulePage.ets
        │    ├── resources
        │    └── module.json5
        ├── ohosTest
        └── test
   ```

    - 在仓颉页面中添加Text组件、Button组件等，并设置其样式。**cangjie_page.cj**文件的示例如下：

   ```cangjie
   // cangjie_page.cj
   package ohos_app_cangjie_my_module

   import ohos.base.*
   import ohos.component.*
   import ohos.state_macro_manage.*
   import ohos.state_manage.*
   import ohos.hybrid_base.*

   @HybridComponentEntry
   @Component
   class CangjiePage {
       @State
       var msg: String = "Hi, this is Cangjie"

       public func build() {
           Column {
               Text(msg)
                   .fontSize(20)
                   .fontWeight(FontWeight.Bold)
               Button("点击修改上方文本")
                   .shape(ShapeType.Capsule)
                   .width(80.percent)
                   .height(40)
                   .margin(20)
                   .onClick {
                       msg = "Okay, Cangjie clicked"
                   }
           }
           .width(100.percent)
           .height(100.percent)
       }
   }
   ```

2. 在ArkTS侧嵌入该仓颉页面。

   在**Project**窗口，打开**my_module > src > main > pages**，修改**MyModulePage.ets**文件，示例如下：

   ```typescript
   // MyModulePage.ets
   // 在 ArkTS 页面中嵌入仓颉页面
   import { CJHybridComponentV2 } from '@cangjie/cjhybridview'
   // 导入 libohos_app_cangjie_entry.so 中的 callSync 和 callAsync 接口
   import cjlib from 'libohos_app_cangjie_my_module.so'

   @Builder
   export function MyModulePageBuilder() {
     MyModulePage()
   }

   @Component
   export struct MyModulePage {
     pathStack: NavPathStack = new NavPathStack()
     @State msg: string = "Hello"

     build() {
       NavDestination() {
         Column() {
           Button('回到首页')
             .type(ButtonType.Capsule)
             .width('80%')
             .height(40)
             .margin(20)
             .onClick(() => {
               this.pathStack.clear()
             })

             // 添加一个文本组件，用于显示 this.msg 的变化
           Text(`msg = ${this.msg}`)
             .fontSize(20)
             .fontWeight(FontWeight.Bold)

           // 添加两个按钮，触发调用
           Button('调用 cjlib.callSync')
             .width('80%')
             .height(40)
             .margin(20)
             .onClick(() => {
               // 调用同步接口
               this.msg = cjlib.callSync('Hello')
             })
           Button('调用 cjlib.callAsync')
             .width('80%')
             .height(40)
             .margin(20)
             .onClick(() => {
               // 调用异步接口
               cjlib.callAsync('Hello')
                 .then((res) => {
                   this.msg = res
                 })
             })
             // 通过 CJHybridComponent 嵌入仓颉页面
           CJHybridComponentV2({
             library: 'ohos_app_cangjie_my_module', // 仓颉页面所在的 package 名字
             component: 'CangjiePage'               // 仓颉页面对应的 class 名字
           })
         }
         .width('100%')
         .height('100%')
       }
       .title('MyModulePage')
       .onReady((context: NavDestinationContext) => {
         this.pathStack = context.pathStack
       })
     }
   }
   ```

3. 使用真机或模拟器运行应用。

   应用编译安装成功后，先跳转到 **MyModulePage** 页面，再单击仓颉Button触发仓颉Text更新文本，其效果如下：

   ![HybridExample2_ArkTSCallCangjieUIDemo](../../figures/start-HybridExample2_ArkTSCallCangjieUIDemo.png)

   > **说明：**
   >
   > 使用真机或模拟器运行应用的具体步骤请参见[构建第一个HarmonyOS应用（仓颉）](./cj-quick-start-first-cangjie-hybrid-app.md#使用真机或模拟器运行应用)。

恭喜您已经在ArkTS应用中成功使用仓颉完成业务模块开发。