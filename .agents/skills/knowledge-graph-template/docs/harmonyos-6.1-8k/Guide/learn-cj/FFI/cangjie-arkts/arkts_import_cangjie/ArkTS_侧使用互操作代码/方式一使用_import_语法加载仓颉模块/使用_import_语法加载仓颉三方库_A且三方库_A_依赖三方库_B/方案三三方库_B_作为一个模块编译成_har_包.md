#### 方案三：三方库 B 作为一个模块，编译成 har 包

1. 在 ArkTS 工程中创建仓颉静态库模块 package_b，详情请参见[添加仓颉静态库模块](./add_cangjie_module.md)。在模块 package_b 下声明 returnB 接口：

    <!-- compile -arkts_import_cangjie-example3 -->
    <!-- cfg="-p ohos_app_cangjie_package_b --output-type=dylib" -->
    ```cangjie
    // package_b/src/main/cangjie/index.cj
    package ohos_app_cangjie_package_b

    public func returnB(): String {
        return "B"
    }
    ```

2. 在 ArkTS 模块内的 oh-package.json5 文件中的 dependencies 字段配置对仓颉静态库模块 package_b 的依赖：

    ```json
    // entry/oh-package.json5
    {
        "dependencies": {
            // ...
            "package_b": "../package_b",
            // ...
        }
    }
    ```

3. 在 ArkTS 工程中创建仓颉模块，详情请参见[在 ArkTS 工程中添加仓颉模块](./add_cangjie_module.md)。

4. 在 cangjie 文件夹下新建 package_a 目录，在 package_a 目录下新建 src->a.cj 文件 和 cjpm.toml 文件。

    - a.cj

        <!-- compile -arkts_import_cangjie-example3 -->
        <!-- cfg="libohos_app_cangjie_package_b.so" -->
        ```cangjie
        // entry/src/main/cangjie/package_a/src/a.cj

        package package_a
        // 导入互操作库
        import ohos.ark_interop.JSModule
        import ohos.ark_interop.JSContext
        import ohos.ark_interop.JSCallInfo
        import ohos.ark_interop.JSValue
        // 导入三方库 B
        import ohos_app_cangjie_package_b.returnB
        
        // 定义三方库 A 中的 returnA 接口
        public func returnA(context: JSContext, callInfo: JSCallInfo): JSValue {
            let result = "A " + returnB()
            return context.string(result).toJSValue()
        }

        // 注册该函数到JSModule中
        let EXPORT_MODULE = JSModule.registerModule {
            runtime, exports => exports["returnA"] = runtime.function(returnA).toJSValue()
        }
        ```

    - 在三方库 A 的 cjpm.toml 的 dependencies 字段添加对三方库 B 的依赖：

        ```toml
        # entry/src/main/cangjie/package_a/cjpm.toml
        [dependencies]
          [dependencies.ohos_app_cangjie_package_b]
            path = ${package_b}
        ```

5. 在 ArkTS 侧创建仓颉三方库 A 接口声明。

    - 在 types->libpackage_a 文件夹下新建 Index.d.ts 文件，提供 ArkTS 侧接口声明：

        ```typescript
        // entry/src/main/cangjie/types/libpackage_a/Index.d.ts
        export declare function returnA(): string;
        ```

    - 在 types->libpackage_a 文件夹下新建 oh-package.json5 文件，将 Index.d.ts 与仓颉三方库 A 关联起来。

        ```json
        // entry/src/main/cangjie/types/libpackage_a/oh-package.json5
        {
            "name": "libpackage_a.so",
            "types": "./Index.d.ts",
            "version": "1.0.0",
            "description": ""
        }
        ```

6. 在 ArkTS 模块内的 oh-package.json5 文件中声明仓颉三方库 A 和静态库模块 package_b 的路径：

    ```json
    // entry/oh-package.json5
    {
        "dependencies": {
            // ...
            "package_b": "../package_b",
            "libpackage_a.so": "file:./src/main/cangjie/types/libpackage_a"
            // ...
        }
    }
    ```

7. 在 entry 模块内的 cjpm.toml 文件中的 dependencies 字段声明仓颉三方库 A 的路径：

    ```toml
    # entry/cjpm.toml
    [dependencies]
      [dependencies.package_a]
        path = "../package_a"
    ```

8. ArkTS 侧使用 import 语法直接导入仓颉三方库 A，并调用仓颉 returnA 接口：

    ```typescript
    // 导入仓颉动态库，该动态库名称为仓颉三方库的名称，该名称需要和互操作接口所在的包名一致
    import { returnA } from "libpackage_a.so";

    // 调用仓颉接口
    let result = returnA();
    console.log(${result});
    ```