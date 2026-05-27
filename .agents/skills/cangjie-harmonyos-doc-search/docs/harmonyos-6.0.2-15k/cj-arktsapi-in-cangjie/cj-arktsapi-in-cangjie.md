# 在仓颉应用中使用ArkTS的API

## 概述

仓颉支持与ArkTS跨语言互通，因此，开发者可以在仓颉语言开发的应用中调用ArkTS提供的应用开发API、标准库等。

> **说明：**
>
> 仓颉提供的应用开发API、语言库正在持续完善中，使用仓颉语言的应用开发者如果遇到仓颉暂未提供所需的API，可以调用ArkTS的API完成应用开发。ArkTS提供的API请参见[API参考](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/development-intro-api)。

## 使用指导

此处介绍如何在仓颉开发的应用中使用ArkTS的API。

### 创建ArkTS运行时

开发者可以在仓颉应用中创建JSRuntime对象，表示一个ArkTS运行时实例。通过JSRuntime对象，可以加载ArkTS模块；通过 JSRuntime对象中的mainContext互操作上下文，可以创建、访问ArkTS数据对象等。目前创建ArkTS运行时只能在主线程上创建。

创建JSRuntime对象并通过该对象中的mainContext获取互操作上下文的示例如下：

```cangjie
import ohos.ark_interop.*

func tryLoadArkTSSo() {
    // 创建新的 ArkTS 运行时
    let runtime = JSRuntime()
    // 获取互操作上下文
    let context = runtime.mainContext
    ...
}
```

### 加载ArkTS模块

创建JSRuntime对象成功后，仓颉可以加载和运行已完成预编译的ArkTS模块。已完成预编译的ArkTS模块主要有两种：

- NAPI模块（C/C++）编译出的动态库.so文件
- ArkTS模块编译出的abc字节码文件

> **说明：**
>
> 当前仓颉仅支持部分加载和运行部分ArkTS模块，调用不支持的ArkTS模块时，程序会运行失败。

假设有一个ArkTS系统模块someModule（.so文件），可以在仓颉中通过 `requireSystemNativeModule` 方法将其加载，示例如下：

```cangjie
// 获取互操作上下文
let context = runtime.mainContext
let module = context.requireSystemNativeModule("someModule")
```

### 调用ArkTS接口

成功加载和运行ArkTS模块后，开发者可以通过call方法调用ArkTS模块提供的API。

假设上述ArkTS模块someModule导出了一个无入参的ArkTS接口someFunc，则可以通过如下方式进行调用：

```cangjie
let jsFunc: JSFunction = module["someFunc"].asFunction(context)
let result = jsFunc.call()
```

## 参考文档

仓颉与ArkTS互操作的详细内容和API请参见：

[仓颉-ArkTS 互操作](https://developer.huawei.com/consumer/cn/doc/cangjie-guides/cj-cangjie_arkts_overview)

[仓颉与ArkTS互操作库](https://developer.huawei.com/consumer/cn/doc/cangjie-references/cj-apis-ark_interop)
