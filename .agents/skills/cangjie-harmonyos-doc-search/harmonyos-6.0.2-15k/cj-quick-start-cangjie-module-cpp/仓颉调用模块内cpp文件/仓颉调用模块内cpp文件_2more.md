# 仓颉调用模块内cpp文件

本文档介绍如何使用DevEco Studio，实现在仓颉代码中调用模块内cpp文件的功能。

## 开发示例

1. 创建一个纯仓颉 "[Cangjie] Empty Ability" 工程

   ![cangjieTemplate](../../figures/start-cangjieTemplate.png)

2. 右键单击 **entry** 文件夹，选择 **New -> C/C++ File(Napi)**，如下图所示：

   ![cangjiecangjieNewCpp](../../figures/start-cangjieNewCpp.png)

   会自动生成 **entry > src > main > cpp > napi_init.cpp** 文件。

3. 打开**napi_init.cpp**文件，编写cpp代码，示例如下：

   ```cpp
   #include <stdint.h>
   #include <stdio.h>

   extern "C" int32_t sum(int32_t a, int32_t b) { return a + b; }

   extern "C" int32_t sub(int32_t a, int32_t b) {
       printf("sub\n");
       return a - b;
   }
   ```

4. 打开 **entry > src > main > cangjie > index.cj** 文件，编写仓颉调用cpp代码，示例如下：

   ```cangjie
      package ohos_app_cangjie_entry
      internal import ohos.base.LengthProp
      internal import ohos.component.Column
      internal import ohos.component.Row
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
      foreign {
          func sum(a: Int32, b: Int32): Int32
          func sub(a: Int32, b: Int32): Int32
      }
      @Entry
      @Component
      class EntryView {
          @State
          var message: String = "1 + 2"
          func build() {
              Row {
                  Column {
                      Text(this.message)
                          .fontSize(50)
                          .fontWeight(FontWeight.Bold)
                          .onClick {
                              evt => unsafe {
                                  this.message = "result: ${sum(1, 2)}"
                              }
                          }
                  }.width(100.percent)
              }.height(100.percent)
          }
      }
      ```

5. 添加 cjpm.toml 中 cpp 依赖。打开 **entry > cjpm.toml** 文件，增加配置ffi.c依赖如下，配置完成后同步工程。

   ```toml
   [ffi]
     [ffi.c]
       [ffi.c.entry]
         path = "./libs/${ABI}"
   ```