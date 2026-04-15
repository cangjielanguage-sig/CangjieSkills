### ArkTS 代码中使用仓颉模块

仓颉互操作模块实现后，在 ArkTS 代码中导入仓颉 ohos_app_cangjie_entry 模块，即可加载自定义的仓颉互操作模块，并调用相关的接口。

在 ArkTS 应用中使用仓颉互操作模块提供的 addF64 函数示例如下：

```typescript
// 导入仓颉动态库，该动态库名称为仓颉包名的名称，该名称需要和互操作接口所在的包名一致
import { addF64 } from "libohos_app_cangjie_entry.so"

// 调用仓颉接口
console.log("result " + addF64(1, 2))
```