# 增加仓颉模块

该章节介绍如何在 DevEco Studio 的 ArkTS 工程中添加仓颉模块，主要分为在同一个 module 中添加仓颉模块及添加仓颉静态库模块，然后进行互操作调用。

## 在同一个 module 中添加仓颉模块

1. 按照下图所示，选中 ArkTS 的 entry 目录中的任意文件，单击右键，选择 **New -> Cangjie(Interop)**。

   ![interop-create-new-project](../../figures/interop-create-new-project.png)

2. 点击 **Cangjie(Interop)** 按钮后，在选中的 ArkTS 模块下，自动创建 cjpm 的配置文件 cjpm.toml 和名为 `cangjie` 的文件夹。文件夹内包含模板代码文件 index.cj、用于存放仓颉的互操作接口声明文件 `types` 文件夹。如下图所示：

      ![image-20250222174232257](../../figures/generate-interop-file.png)

      并在 **entry -> oh-package.json5** 中自动生成仓颉的依赖：

      ![image-20250222181831627](../../figures/generate-dependency.png)

3. 仓颉互操作模块实现后，在 ArkTS 代码中导入仓颉 ohos_app_cangjie_entry 模块，即可加载自定义的仓颉互操作模块，并调用相关的接口。

   ```typescript
   // 加载自定义的仓颉互操作模块
   import testCJ from "libohos_app_cangjie_entry.so"
   ```

4. 自定义的仓颉互操作模块加载成功后，即可在 ArkTS 工程中调用仓颉互操作模块提供的接口。

在 ArkTS 应用中调用仓颉互操作模块提供的 testCJ 函数示例如下：

```typescript
// 调用仓颉接口
console.log(testCJ("Cangjie"))
```