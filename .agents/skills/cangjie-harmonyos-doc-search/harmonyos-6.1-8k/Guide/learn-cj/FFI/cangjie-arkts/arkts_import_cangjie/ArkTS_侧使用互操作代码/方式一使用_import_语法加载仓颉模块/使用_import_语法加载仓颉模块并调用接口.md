### 使用 import 语法加载仓颉模块并调用接口

> **说明：**
>
> 使用 import 语法加载仓颉模块的方式和使用 import 语法加载 native 模块方式一致，详细介绍请参见：[静态方式加载 native 模块](https://docs.openharmony.cn/pages/v6.0/zh-cn/application-dev/arkts-utils/arkts-import-native-module.md)。

下面为使用 import 语法加载仓颉 ohos_app_cangjie_entry 模块并调用 addNumber 接口的示例：

1. 在 ArkTS 工程中创建仓颉模块，详情请参见[在 ArkTS 工程中添加仓颉模块](./add_cangjie_module.md)。

2. 仓颉侧互操作接口的实现：

    - 实现互操作接口 addNumber：

        <!--compile-->
        ```cangjie
        // entry/src/main/cangjie/index.cj

        // 定义包名，该包名需要和 cjpm.toml 的 package name 保持一致
        package ohos_app_cangjie_entry

        // 导入互操作库
        import ohos.ark_interop.*

        // 定义互操作函数，该函数参数类型必须为(JSContext,JSCallInfo)，返回值类型必须为JSValue
        func addNumber(context: JSContext, callInfo: JSCallInfo): JSValue {
            // 从JSCallInfo获取参数列表
            let arg0: JSValue = callInfo[0]
            let arg1: JSValue = callInfo[1]

            // 把JSValue转换为仓颉类型
            let a: Float64 = arg0.toNumber()
            let b: Float64 = arg1.toNumber()

            // 实际仓颉函数行为
            let value = a + b

            // 把结果转换为JSValue
            let result: JSValue = context.number(value).toJSValue()

            // 返回 JSValue
            return result
        }
        // 必须注册该函数到JSModule中
        let EXPORT_MODULE = JSModule.registerModule {
            runtime, exports =>
                exports["addNumber"] = runtime.function(addNumber).toJSValue()
        }
        ```

    - 在 types->libohos_app_cangjie_entry 文件夹下的 Index.d.ts 文件中，提供 ArkTS 侧接口声明：

        ```typescript
        // entry/src/main/cangjie/types/libohos_app_cangjie_entry/Index.d.ts
        export declare function addNumber(a: number, b: number): number;
        ```

    - 在 types->libohos_app_cangjie_entry 文件夹下的 oh-package.json5 文件中将 Index.d.ts 与仓颉模块对应的 so 库关联起来：

        > **说明：**
        >
        > 以下代码无须复制，创建仓颉模块以后在工程中已配置好。

        ```json
        // entry/src/main/cangjie/types/libohos_app_cangjie_entry/oh-package.json5
        {
            "name": "libohos_app_cangjie_entry.so",
            "types": "./Index.d.ts",
            "version": "1.0.0",
            "description": ""
        }
        ```

3. 在 ArkTS 模块内的 oh-package.json5 文件中的 dependencies 字段配置对仓颉模块对应的 so 库的依赖：

    > **说明：**
    >
    > 以下代码无须复制，创建仓颉模块以后在工程中已配置好。

    ```json
    // entry/oh-package.json5
    {
        "dependencies": {
            // ...
            "libohos_app_cangjie_entry.so": "file:./src/main/cangjie/types/libohos_app_cangjie_entry"
            // ...
        }
    }
    ```

4. ArkTS 侧使用 import 语法直接导入仓颉模块，并调用仓颉 addNumber 接口：

    ```typescript
    // 导入仓颉动态库，该动态库名称为仓颉包名的名称，该名称需要和互操作接口所在的包名一致
    import { addNumber } from "libohos_app_cangjie_entry.so";

    // 调用仓颉接口
    let result = addNumber(1, 2);
    console.log(`1 + 2 = ${result}`);
    ```