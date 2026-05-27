## 构建第二个页面

1. 创建第二个页面。

   在**Project**页面，进入**entry > src > main > cangjie**目录，右键单击**cangjie**文件夹，选择**New > Cangjie File**，命名为**second**，单击**OK**。文件目录结构如下：

   ```text
   entry
   └── src
        └── main
             ├── cangjie
             │    ├── ability_stage.cj
             │    ├── index.cj
             │    ├── main_ability.cj
             │    └── second.cj
             ├── resources
             └── module.json5
   ```

2. 添加文本及按钮。

   参照第一个页面，在第二个页面添加Text组件和Button组件，并设置其样式。**second.cj**文件的示例如下：

   ```cangjie
   // second.cj
   package ohos_app_cangjie_entry

   import ohos.state_macro_manage.Entry
   import ohos.state_macro_manage.Component
   import ohos.state_macro_manage.State
   import ohos.state_macro_manage.r
   import ohos.component.Button

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
                       .onClick {
                           evt => AppLog.info("Hi there")
                       }
                       .fontSize(30)
                       .width(180)
                       .height(50)
                       .margin(top: 20)
               }.width(100.percent)
           }.height(100.percent)
       }
   }
   ```

## 实现页面间的跳转

页面间的导航可以通过页面路由router来实现。页面路由router根据页面url找到目标页面，从而实现跳转。使用页面路由请导入router模块。

1. 第一个页面跳转到第二个页面。

   在第一个页面中，跳转按钮绑定onClick事件，单击按钮时跳转到第二页。**index.cj**文件的示例如下：

   ```cangjie
   // index.cj
   package ohos_app_cangjie_entry

   internal import ohos.base.LengthProp
   internal import ohos.component.Column
   internal import ohos.component.Row
   internal import ohos.component.Button
   internal import ohos.component.Text
   internal import ohos.component.CustomView
   internal import ohos.component.CJEntry
   internal import ohos.component.loadNativeView
   internal import ohos.component.FontWeight
   internal import ohos.state_manage.SubscriberManager
   internal import ohos.state_manage.ObservedProperty
   internal import ohos.state_manage.LocalStorage
   import ohos.state_macro_manage.Entry
   import ohos.state_macro_manage.Component
   import ohos.state_macro_manage.State
   import ohos.state_macro_manage.r
   import ohos.router.Router // 导入页面路由模块

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
                    .onClick {
                        evt => this.message = "Hello Cangjie"
                    }
                   // 添加按钮，以响应用户点击
                   Button("Next")
                   .onClick {
                       evt => Router.push(url: "Second") // 实现到第二页的跳转
                   }
                   .fontSize(30)
                   .width(180)
                   .height(50)
                   .margin(top: 20)
               }.width(100.percent)
           }.height(100.percent)
       }
   }
   ```

2. 第二个页面返回到第一个页面。

   在第二个页面中，返回按钮绑定onClick事件，单击按钮时返回到第一页。**second.cj**文件的示例如下：

   ```cangjie
   // second.cj
   package ohos_app_cangjie_entry

   import ohos.state_macro_manage.Entry
   import ohos.state_macro_manage.Component
   import ohos.state_macro_manage.State
   import ohos.state_macro_manage.r
   import ohos.component.Button
   import ohos.router.Router // 导入页面路由模块

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
                       .onClick {
                           evt => Router.back(url: "EntryView") // 实现返回第一页
                       }
                       .fontSize(30)
                       .width(180)
                       .height(50)
                       .margin(top: 20)
               }.width(100.percent)
           }.height(100.percent)
       }
   }
   ```