# 订阅应用冻屏事件

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

## 简介

本文介绍如何使用HiAppEvent提供的仓颉接口订阅应用冻屏事件。接口的详细使用说明（参数限制、取值范围等）请参见[应用事件打点API文档](../reference/PerformanceAnalysisKit/cj-apis-hiappevent.md)。

## 接口说明

| 接口名                                              | 描述                                         |
| --------------------------------------------------- | -------------------------------------------- |
| addWatcher(watcher: Watcher): Option\<AppEventPackageHolder> | 添加应用事件观察者，以添加对应用事件的订阅。 |
| removeWatcher(watcher: Watcher): Unit               | 移除应用事件观察者，以移除对应用事件的订阅。 |