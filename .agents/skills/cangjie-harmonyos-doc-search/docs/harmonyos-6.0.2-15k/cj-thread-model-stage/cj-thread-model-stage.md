# 线程模型

线程是操作系统进行运算调度的基本单位，是[进程](../application-models/cj-process-model-stage.md)中的执行流，共享进程的资源。一个进程可以包含多个线程。

## 线程类型

Stage模型下的线程主要有如下两类：

- 主线程
    - 执行UI绘制。
    - 管理其他仓颉线程。
    - 分发交互事件。
    - 处理应用代码的回调，包括事件处理和生命周期管理。
    - 接收仓颉线程发送的消息。
- 仓颉线程

![thread-model-stage](figures/thread-model-stage.png)

> **说明：**
>
> - 同一线程中存在多个组件，例如UIAbility组件和UI组件都存在于主线程中。在Stage模型中目前主要使用[EventHub](#使用eventhub进行线程内通信)进行数据通信。
> - 执行`hdc shell`命令，进入设备的shell命令行。在shell命令行中，执行`ps -p <pid> -T`命令，可以查看指定应用进程的线程信息。其中，`<pid>`为需要指定的应用进程的[进程ID](cj-process-model-stage.md)。

## 使用EventHub进行线程内通信

[EventHub](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-eventhub.md)提供了线程内发送和处理事件的能力，包括对事件订阅、取消订阅、触发事件等。以UIAbility组件与UI之间的数据同步为例，具体使用方法可以参考[UIAbility组件与UI的数据同步](cj-uiability-data-sync-with-ui.md#使用eventhub进行数据通信)。
