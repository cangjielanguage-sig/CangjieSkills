### 加载har模块里的文件

1. 模块依赖配置

    ```json5
    // 模块下的 oh-package.json5
    {
      "name": "entry",
      "version": "1.0.0",
      "dependencies": {
        "localhar": "file:../localhar",                 // 本地har，在同一个工程下，用相对路径指向模块根目录
        "remotehar": "file:../prebuilts/remotehar.har", // 远程har，预编译为har（不区分源码har和二进制har），用路径指向har文件
        "@ohos/lottie": "^2.0.0"                        // ohpm har，已发布到ohpm的har，指定版本即可
      },
    }
    ```

2. 在模块的build-profile.json5里进行以下配置

    ```json5
    {
      "buildOption": {
        "arkOptions": {
          "runtimeOnly": {
            "packages": [
              "localhar",
              "remotehar",
              "@ohos/lottie"
            ]
          }
        }
      }
    }
    ```

3. 导入和调用导出的接口

    <!-- compile -->
    ```cangjie
    func loadModule(context: JSContext): Unit {
        // 1. 使用requireArkModule导入模块
        let module = context.requireArkModule("localhar/src/main/ets/Test")     // 导入本地har里的文件
        let module = context.requireArkModule("remotehar/src/main/ets/Test")    // 导入远程har里的文件
        let module = context.requireArkModule("@ohos/lottie/src/main/js/main")  // 导入ohpm har里的文件
        // 2. 把导入内容转换为JSObject
        let test = module.asObject()
        // 3. 读取导出的value变量
        let value = test["value"].toNumber()
        Hilog.info("value is ${value}")
        // 4. 写value变量
        test["value"] = context.number(2).toJSValue()
        // 5. 调用导出的test方法
        test.callMethod("test")
    }
    ```

> **注意：**
>
> 在ArkTS静态导入里存在整包导入的机制，例如：`import * as localhar from "localhar"`。
> 这种导入机制本质上仍然是导入一个文件，在每个(har | hsp)模块的oh-package.json里有一个字段main，
> 该字段指向一个源码文件，整包导入时实际上就是导入该文件。
> 例如localhar的oh-package.json配置为`main: "Index.ets"`，那么用该接口应该这样导入：`context.importArkModule("localhar/Index")`

### 加载hsp模块里的文件

build-profile.json5无需配置，导入和调用方式如下：

<!-- compile -->
```cangjie
func loadModule(context: JSContext): Unit {
    // 1. 使用requireArkModule导入模块
    let module = context.requireArkModule("localhsp/src/main/ets/Test")     // 导入本地hsp里的文件
    // 2. 把导入内容转换为JSObject
    let test = module.asObject()
    // 3. 读取导出的value变量
    let value = test["value"].toNumber()
    Hilog.info("value is ${value}")
    // 4. 写value变量
    test["value"] = context.number(2).toJSValue()
    // 5. 调用导出的test方法
    test.callMethod("test")
}
```

### 加载native模块

针对hap、har和本地hsp里定义的native（napi | 仓颉）模块，都可以通过生成的二进制名称进行加载。

<!-- compile -->
```cangjie
func loadModule(context: JSContext): Unit {
    // 1. 使用requireArkModule导入模块
    let module = context.requireArkModule("libentry.so")     // 导入native模块
    // 2. 把导入内容转换为JSObject
    let test = module.asObject()
    // 3. 读取导出的value变量
    let value = test["value"].toNumber()
    Hilog.info("value is ${value}")
    // 4. 写value变量
    test["value"] = context.number(2).toJSValue()
    // 5. 调用导出的test方法
    test.callMethod("test")
}
```