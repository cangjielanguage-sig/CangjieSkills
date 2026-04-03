## 实现页面间的跳转

页面间的导航可以通过页面路由router来实现。router根据页面url找到目标页面，从而实现跳转。使用页面路由请导入router模块。

1. 第一个页面跳转到第二个页面。

   在第一个页面中，跳转按钮绑定onClick事件，单击按钮时跳转到第二页。**index.cj**文件的示例如下：

   <!-- compile -->

   ```cangjie
   // index.cj
   package ohos_app_cangjie_entry

   import kit.ArkUI.*
   import ohos.arkui.state_macro_manage.*

   @Entry
   @Component
   class EntryView {
       @State
       var message: String = "Hello Cangjie"

       func build() {
           Row {
               Column() {
                   Text(this.message)
                    .fontSize(50)
                    .fontWeight(FontWeight.Bold)
                    .onClick ({
                        evt => this.message = "Hello Cangjie"
                    })
                   // 添加按钮，以响应用户点击
                   Button("Next")
                   .onClick ({
                       evt => getUIContext().getRouter().pushUrl(url: "Second") // 实现到第二页的跳转
                   })
                   .fontSize(30)
                   .width(180)
                   .height(50)
                   .margin(top: 20)
               }.width(100.percent)
           }.height(100.percent)
       }
   }

   ```

2. 从第二个页面返回到第一个页面。

   在第二个页面中，返回按钮绑定onClick事件，单击时返回到第一页。**second.cj**文件的示例如下：

   <!-- compile -->

   ```cangjie
   // second.cj
   package ohos_app_cangjie_entry

   import ohos.arkui.state_macro_manage.Entry
   import ohos.arkui.state_macro_manage.Component
   import ohos.arkui.state_macro_manage.State
   import ohos.arkui.state_macro_manage.r
   import ohos.arkui.ui_context.* // 导入页面路由模块
   import ohos.hilog.Hilog
   import kit.ArkUI.*

   @Entry
   @Component
   class Second {
       @State
       var message: String = "Hi there"

       func build() {
           Row {
               Column() {
                   Text(this.message)
                       .fontSize(50)
                       .fontWeight(FontWeight.Bold)
                   Button("Back")
                       .onClick ({
                           evt => getUIContext().getRouter().back(url: "EntryView") // 实现返回第一页
                       })
                       .fontSize(30)
                       .width(180)
                       .height(50)
                       .margin(top: 20)
               }.width(100.percent)
           }.height(100.percent)
       }
   }

   ```

## 使用真机或模拟器运行应用

### 使用真机运行应用

1. 将搭载OpenHarmony系统的真机与电脑连接。

2. 真机连接成功后，进入**File > Project Structure > Project > Signing Configs**界面勾选**Automatically generate signature**，单击界面提示的**Sign In**，使用用户账号登录。等待自动签名完成后，单击**OK**即可。如下图所示：

   ![buildSign](../../figures/buildSignN.png)

3. 在编辑窗口右上角的工具栏，单击![runButton](../../figures/runButton.png)按钮运行。效果如下图所示：

   ![cangjieFirstDemo](../../figures/cangjieFirstDemo.png)

### 使用模拟器

仓颉语言编写的OpenHarmony应用/服务，支持在DevEco Studio提供的模拟器（Emulator）上运行。

1. 创建一个类型为Phone的模拟器设备，并在DevEco Studio右上角的设备列表中，选中该设备。

2. 仓颉工程默认编译架构为**arm64-v8a**，因此在使用**x86模拟器**时（即，当前开发环境为**Windows/x86_64**或**MacOS/x86_64**时），仓颉工程及三方库需要编译出x86_64版本的so，请在仓颉模块的**build-profile.json5**配置文件中，为**cangjieOptions/abiFilters**的值增加“**x86_64**”，具体编译配置如下：

   ```json
   "buildOption": {      // 配置项目在构建过程中使用的相关配置
     "cangjieOptions": { // 仓颉相关配置
       "path": "./cjpm.toml", // cjpm配置文件路径，提供仓颉构建配置
       "abiFilters": ["arm64-v8a", "x86_64"]   // 自定义仓颉编译架构，默认编译架构为arm64-v8a
     }
   }
   ```

3. 在编辑窗口右上角的工具栏，单击![runButton](../../figures/runButton.png)按钮运行。效果同使用真机运行。

您已经成功构建第一个仓颉应用。
<!--RP1--><!--RP1End-->