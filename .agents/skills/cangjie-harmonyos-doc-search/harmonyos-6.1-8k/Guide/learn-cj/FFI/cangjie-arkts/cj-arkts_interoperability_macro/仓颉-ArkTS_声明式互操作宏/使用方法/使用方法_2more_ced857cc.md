## 使用方法

DevEco Studio 的配置可参考[在 ArkTS 工程中添加仓颉模块](./add_cangjie_module.md)。配置完成后，可实现互操作模块。

目前针对希望被 ArkTS 调用的函数（含异步函数）、接口、类和枚举，可以使用互操作声明宏 `@Interop` 进行修饰。以下以普通函数场景作为演示示例，介绍声明式互操作宏的具体使用方法，异步函数、接口、类、枚举等示例请参考[场景详细说明](#场景详细说明)。

### 实现仓颉互操作模块

在 ArkTS 工程中成功插入仓颉互操作模块后，在生成的 index.cj 文件中，可以实现自定义方法。如下示例：

1. 用户实现一个名为 addF64 的仓颉函数，并使用 `@Interop[ArkTS]` 修饰，标注该函数为互操作使用的函数。假设下述文件名为 demo.cj，其内容如下所示：

   <!--compile-->
   ```cangjie
   // 定义包名，该包名需要和 cjpm.toml 的 package name 保持一致
   package ohos_app_cangjie_entry
   // 导入互操作库 ark_interop 和互操作宏
   import ohos.ark_interop.*
   import ohos.ark_interop_macro.*
   // 实现自定义的函数 addF64，入参接收两个number，返回相加后的结果
   @Interop[ArkTS]
   public func addF64(a: Float64, b!: Float64): Float64 {
       a + b
   }
   ```

2. 在 DevEco Studio 中选择上述所说的仓颉文件 demo.cj，在文件编辑界面中右键选择 **Generate... > Cangjie-ArkTS Interop API**，会在 **cangjie->types->libohos_app_cangjie_entry** 目录下生成 Index.d.ts 声明文件和 oh_package.json5 配置文件，以及会在 **cangjie -> ark_interop_api** 目录下生成 ark_interop_api.d.ts 声明文件和 oh_package.json5 配置文件。

    > **说明：**
    >
    > ark_interop_api 目录下生成的 .d.ts 为兼容需要运行在 OpenHarmony 12 Release以上应用生成，如果没有兼容性需求，则可以忽略此文件夹。

   types->libohos_app_cangjie_entry 目录下的 Index.d.ts 内容如下所示：

   ```typescript
   export declare function addF64(a: number, b: number): number
   ```

   types->libohos_app_cangjie_entry 目录下的 oh_package.json5 如下所示：

   ```json
   {
     "name": "libohos_app_cangjie_entry.so",
     "types": "./Index.d.ts",
     "version": "1.0.0",
     "description": ""
   }
   ```

   ark_interop 目录下的 ark_interop_api.d.ts 内容如下所示：

   ```typescript
   export declare interface CustomLib {
       addF64(a: number, b: number): number
   }
   ```

   ark_interop 目录下的 oh_package.json5 如下所示：

   ```json
   {
     "name": "libark_interop_api.so",
     "types": "./ark_interop_api.d.ts",
     "version": "1.0.0",
     "description": ""
   }
   ```

   并在 entry 的 oh-package.json5 文件中自动添加依赖：

   ```json
   "dependencies": {
     // ...
     "libohos_app_cangjie_entry.so": "file:./src/main/cangjie/types/libohos_app_cangjie_entry",
     "libark_interop_api.so": "file:./src/main/cangjie/ark_interop_api",
     // ...
   }
   ```

> **注意：**
>
> 在同一个仓颉模块中（同一个包及其子包中）需遵循如下规则，否则可能出现编译报错或符号覆盖：
>
> - 使用 `@Interop` 修饰的函数、interface、class 不能同名。
>
>   错误示例：
>
>   ```cangjie
>   @Interop[ArkTS]
>   public func addNumber() : Unit {}
>
>   @Interop[ArkTS]
>   public func addNumber(a: Float64) : Unit {} // 同一个包中会出现编译报错；父子包中可能会出现符号覆盖
>   ```
>
> - 使用 `@Interop` 修饰的函数、interface、class 和使用 JSModule.registerModule、JSModule.registerClass、JSModule.registerFunc 注册到 JSModule 中的函数、interface、class 不能同名。
>
>   错误示例：
>
>   ```cangjie
>   @Interop[ArkTS]
>   public func addNumber() : Unit {}
>
>   func addFloat() {}
>   let EXPORT_MODULE = JSModule.registerModule {
>       runtime, exports => exports["addNumber"] = runtime.function(addFloat).toJSValue() // 会覆盖使用 @Interop 修饰的同名函数 addNumber
>   }
>   ```