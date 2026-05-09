### 使用 import 语法加载仓颉三方库并调用接口

下面为使用 import 语法加载仓颉三方库 libapplication.so 并调用 addNumber 接口的示例：

> **说明：**
>
> 假设仓颉三方库 libapplication.so 已经实现了 addNumber 接口可供 ArkTS 侧调用。

1. 在 ArkTS 工程中创建仓颉模块，详情请参见[在 ArkTS 工程中添加仓颉模块](./add_cangjie_module.md)。

2. 在 ArkTS 工程新建 libs->arm64-v8a 目录，将仓颉三方库 libapplication.so 拷贝到 ArkTS 工程的 libs->arm64-v8a 目录下。

3. 在 ArkTS 侧创建仓颉三方库 libapplication.so 接口声明。

    - 在 types->libapplication 文件夹下新建 Index.d.ts 文件，提供 ArkTS 侧接口声明：

        ```typescript
        // entry/src/main/cangjie/types/libapplication/Index.d.ts
        export declare function addNumber(a: number, b: number): number;
        ```

    - 在 types->libapplication 文件夹下新建 oh-package.json5 文件，将 Index.d.ts 与仓颉三方库 libapplication.so 关联起来：

        ```json
        // entry/src/main/cangjie/types/libapplication/oh-package.json5
        {
            "name": "libapplication.so",
            "types": "./Index.d.ts",
            "version": "1.0.0",
            "description": ""
        }
        ```

4. 在 ArkTS 模块内的 oh-package.json5 文件中声明 so 库的根目录路径。

    ```json
    // entry/oh-package.json5
    {
        "dependencies": {
            // ...
            "libapplication.so": "file:./src/main/cangjie/types/libapplication"
            // ...
        }
    }
    ```

5. ArkTS 侧使用 import 语法直接导入仓颉三方库 libapplication.so，并调用仓颉 addNumber 接口：

    ```typescript
    // 导入仓颉动态库，该动态库名称为仓颉三方库的名称，该名称需要和互操作接口所在的包名一致
    import { addNumber } from "libapplication.so";

    // 调用仓颉接口
    let result = addNumber(1, 2);
    console.log(`1 + 2 = ${result}`);
    ```