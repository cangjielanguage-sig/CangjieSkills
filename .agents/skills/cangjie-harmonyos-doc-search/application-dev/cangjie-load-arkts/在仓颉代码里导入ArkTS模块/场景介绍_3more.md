## 场景介绍

ArkTS互操作库里的JSContext.requireArkModule接口可以加载ArkTS模块，当模块被加载后，可以通过互操作接口来访问导出的变量和调用导出的接口。

## 函数说明

```cangjie
public func requireArkModule(path: String): JSValue
```

## 使用限制

* 只能在ArkTS绑定线程使用该接口
* 禁止在全局变量初始化过程和模块导出流程中使用该接口
* 对于部分系统模块（如：ohos.router）只在主运行时上提供，在worker线程导入将产生错误

> **注意：**
>
> 当前在spawn(UIThread)或context.postJSTask的回调里直接调用该接口将失败，该限制计划在后续的版本里移除。