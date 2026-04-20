### 使用 import 语法加载仓颉静态库模块并调用接口

1. 在 ArkTS 工程中创建仓颉静态库模块 cangjielib，详情请参见[添加仓颉静态库模块](./add_cangjie_module.md)。

2. 仓颉侧互操作接口的实现：

    - 实现互操作接口 addNumber：

        <!--compile-->
        ```cangjie
        // cangjielib/src/main/cangjie/index.cj
        // 包名
        package ohos_app_cangjie_cangjielib

        // 导入文件
        internal import ohos.ark_interop.JSModule
        internal import ohos.ark_interop.JSContext
        internal import ohos.ark_interop.JSCallInfo
        internal import ohos.ark_interop.JSValue

        // 互操作函数
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

        let EXPORT_MODULE = JSModule.registerModule {
            runtime, exports => exports["addNumber"] = runtime.function(addNumber).toJSValue()
        }
        ```

    - 在 cangjielib->src->main->cangjie->types->libohos_app_cangjie_cangjielib 文件夹下的 Index.d.ts 文件中，提供 ArkTS 侧接口声明：

        ```typescript
        // cangjielib/src/main/cangjie/types/libohos_app_cangjie_cangjielib/Index.d.ts
        export declare function addNumber(a: number, b: number): number;
        ```

    - 在 cangjielib->src->main->cangjie->types->libohos_app_cangjie_cangjielib 文件夹下的 oh-package.json5 文件中将 Index.d.ts 与仓颉模块对应的 so 库关联起来：

        > **说明：**
        >
        > 以下代码无须复制，创建仓颉模块以后在工程中已配置好。

        ```json
        // cangjielib/src/main/cangjie/types/libohos_app_cangjie_cangjielib/oh-package.json5
        {
            "name": "libohos_app_cangjie_cangjielib.so",
            "types": "./Index.d.ts",
            "version": "1.0.0",
            "description": ""
        }
        ```

3. 在 ArkTS 模块内的 oh-package.json5 文件中的 dependencies 字段配置对仓颉静态库模块的依赖：

    ```json
    // entry/oh-package.json5
    {
        "dependencies": {
            // ...
            "cangjielib": "../cangjielib",
            "libohos_app_cangjie_cangjielib.so": "file:../cangjielib/src/main/cangjie/types/ohos_app_cangjie_cangjielib"
            // ...
        }
    }
    ```

4. ArkTS 侧使用 import 语法直接导入仓颉模块，并调用仓颉 addNumber 接口：

    ```typescript
    // 导入仓颉动态库，该动态库名称为仓颉包名的名称，该名称需要和互操作接口所在的包名一致
    import { addNumber } from "libohos_app_cangjie_cangjielib.so";

    // 调用仓颉接口
    let result = addNumber(1, 2);
    console.log(`1 + 2 = ${result}`);
    ```