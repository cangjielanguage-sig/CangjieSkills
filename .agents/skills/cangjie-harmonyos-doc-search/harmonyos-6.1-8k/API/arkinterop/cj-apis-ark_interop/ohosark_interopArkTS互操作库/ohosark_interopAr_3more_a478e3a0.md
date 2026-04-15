# ohos.ark_interop（ArkTS互操作库）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

ArkTS 应用的开发语言包括 ArkTS、typescript、javascript，ArkTS 互操作库为仓颉语言提供与 ArkTS 语言进行互操作的能力。

## 导入模块

```cangjie
import ohos.ark_interop.*
```

> **说明：**
>
> 当前暂不支持Kit化的导入方式，预计在下个版本支持。

## interface JSInteropByte

```cangjie
sealed interface JSInteropByte {}
```

**功能：** 该接口用于为可用于声明式互操作宏的Array的泛型约束实现。声明式互操作宏框架场景使用，开发者不需要使用此API。

如下类型扩展了此接口：

- Byte

**起始版本：** 22