### 在同一个工程内，纯ArkTS工程跨模块调用仓颉函数

1. 在仓颉侧开发业务代码，并暴露接口给ArkTS。

   在**Project**窗口，单击**my_module > src > main > cangjie**，打开**index.cj**文件，编写代码，示例如下：

   ```cangjie
   // index.cj
   package ohos_app_cangjie_my_module // 注意包名需要跟cjpm.toml里的[package] name字段保持相同

   import ohos.base.*
   import ohos.ark_interop.*
   import ohos.ark_interop_macro.*
   import std.core.sleep
   import std.core.Duration

   // 同步接口：在主线程上同步执行
   @Interop[ArkTS]
   public func callSync(msg: String): String {
       // do something
       return "callSync: ${msg}"
   }

   // 异步接口：在仓颉轻量级线程上异步执行
   @Interop[ArkTS, Async]
   public func callAsync(msg: String): String {
       // 通过 sleep 函数，模拟耗时操作，调用异步接口后耗时5s组件刷新
       sleep(Duration.second * 5)
       return "callAsync: ${msg}"
   }
   ```

2. 自动生成仓颉-ArkTS互操作接口声明。

   打开上述**index.cj**文件，在文件编辑界面中右键单击选择**Generate... > Cangjie-ArkTS Interop API**，则会在**entry > src > main > cangjie > types > libohos_app_cangjie_entry**目录下的**Index.d.ts**文件中自动生成仓颉暴露给ArkTS的.d.ts接口声明，目录结构如下所示：

   ```text
   my_module
   ├── build
   ├── libs
   ├── oh_modules
   └── src
        └── main
             ├── cangjie
             │    ├── ark_interop_api
             │    ├── types
             │    │    └── libohos_app_cangjie_entry
             │    │         │── Index.d.ts
             │    │         └── oh-package.json5
             │    └── index.cj
             └── ets
   ```

   接口声明如下所示：

   ```typescript
   // Index.d.ts
   export declare function callSync(msg: string): string
   export declare function callAsync(msg: string): Promise<string>
   ```

   > **说明：**
   >
   > 创建Cangjie Hybrid Ability混合工程之后，在模块下**my_module > oh-package.json5**文件中会自动将**libohos_app_cangjie_my_module**库添加到**dependencies**字段中作为依赖。

3. 仓颉暴露给ArkTS的.d.ts接口声明生成后，如果需要在纯ArkTS模块中引入仓颉接口，需要先修改纯ArkTS模块的**hvigorfile.ts**文件。如本例中，需要修改  **entry > hvigorfile.ts**  ，将首行接口 import { hapTasks } from '@ohos/hvigor-ohos-plugin' 修改为 import { hapTasks } from '@ohos/cangjie-build-support'。

4. 完成纯ArkTS模块的**hvigorfile.ts**文件修改后，可以直接在ArkTS文件中引入.d.ts文件中接口的依赖。

   修改 **my_module > src > main > ets > pages > MyModulePage.ets**文件，示例代码如下：

   ```typescript
   // MyModulePage.ets
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

5. 使用真机或模拟器运行应用。

   应用编译安装成功后，先跳转到**MyModulePage**页面，再单击按钮触发函数调用，其效果如下：

   ![HybridExample2_ArkTSCallCangjieFunctionDemo](../../figures/start-HybridExample2_ArkTSCallCangjieFunctionDemo.png)