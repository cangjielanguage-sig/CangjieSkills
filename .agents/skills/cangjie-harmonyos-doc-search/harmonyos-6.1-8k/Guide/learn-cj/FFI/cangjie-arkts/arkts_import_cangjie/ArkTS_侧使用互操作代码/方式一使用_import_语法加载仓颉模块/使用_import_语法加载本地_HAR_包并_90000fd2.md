### 使用 import 语法加载本地 HAR 包并调用仓颉接口

> **说明：**
>
> 假设有本地 HAR 包 cangjielib.har 中包含 libohos_app_cangjie_cangjielib.so，在该 so 中已经实现了 addNumber 接口可供 ArkTS 侧调用。

1. 在 ArkTS 工程中创建仓颉模块，详情请参见[在 ArkTS 工程中添加仓颉模块](./add_cangjie_module.md)。

2. 将本地 HAR 包 cangjielib.har 拷贝到 ArkTS 工程的 libs 目录下。

3. 在 ArkTS 侧创建 libohos_app_cangjie_cangjielib.so 接口声明。

    - 在 types->libohos_app_cangjie_cangjielib 文件夹下新建 Index.d.ts 文件，提供 ArkTS 侧接口声明：

        ```typescript
        // entry/src/main/cangjie/types/libohos_app_cangjie_cangjielib/Index.d.ts
        export declare function addNumber(a: number, b: number): number;
        ```

    - 在 types->libohos_app_cangjie_cangjielib 文件夹下新建 oh-package.json5 文件，将 Index.d.ts 与仓颉库 libohos_app_cangjie_cangjielib.so 关联起来：

        ```json
        // entry/src/main/cangjie/types/libohos_app_cangjie_cangjielib/oh-package.json5
        {
            "name": "libohos_app_cangjie_cangjielib.so",
            "types": "./Index.d.ts",
            "version": "1.0.0",
            "description": ""
        }
        ```

4. 在 ArkTS 模块内的 oh-package.json5 文件中声明 HAR 包和 so 的根目录路径。

    ```json
    // entry/oh-package.json5
    {
        "dependencies": {
            // ...
            "cangjielib": "file:libs/cangjielib.har",
            "libohos_app_cangjie_cangjielib.so": "file:src/main/cangjie/types/ohos_app_cangjie_cangjielib"
            // ...
        }
    }
    ```

5. ArkTS 侧使用 import 语法直接导入仓颉模块，并调用仓颉 addNumber 接口：

    ```typescript
    // 导入仓颉动态库，该动态库名称为仓颉包名的名称，该名称需要和互操作接口所在的包名一致
    import { addNumber } from "libohos_app_cangjie_cangjielib.so";

    // 调用仓颉接口
    let result = addNumber(1, 2);
    console.log(`1 + 2 = ${result}`);
    ```