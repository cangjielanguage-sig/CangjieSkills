# 开发准备

本文档适用于仓颉应用开发的初学者。通过构建一个简单的具有页面跳转/返回功能的应用（如下图所示），快速了解工程目录的主要文件，熟悉仓颉应用开发流程。

![cangjieFirstDemo](../../figures/start-cangjieFirstDemo.png)

在开始之前，您需要了解有关仓颉应用的两个基本概念：UI框架和应用模型。

## 基本概念

### UI框架

仓颉提供了一套UI开发框架，可为开发者提供应用UI开发所必需的能力，比如多种组件、布局计算、UI交互、绘制等。

### 应用模型

应用模型是HarmonyOS为开发者提供的应用程序所需能力的抽象提炼，它提供了应用程序必备的组件和运行机制。有了应用模型，开发者可以基于一套统一的模型进行应用开发，使应用开发更简单、高效。

仓颉应用使用Stage模型。在该模型中，由于提供了AbilityStage、WindowStage等类作为应用组件和Window窗口的“舞台”，因此称这种应用模型为Stage模型。Stage模型开发可见[Stage模型开发概述](../../../application-models/cj-stage-model-development-overview.md)。

快速入门提供了一个含有两个页面的开发实例，并基于stage模型构建第一个HarmonyOS应用（仓颉），以便开发者理解以上基本概念及应用开发流程。

- [构建第一个HarmonyOS应用（仓颉）](./cj-quick-start-first-cangjie-app.md)：构建一个简单的具有页面跳转/返回功能的纯仓颉应用。
- [构建第一个仓颉与ArkTS混合应用](./cj-quick-start-first-cangjie-hybrid-app.md)：构建一个简单的具有页面跳转/返回功能的仓颉与ArkTS混合开发的应用。
- [在已有ArkTS工程中增量使用仓颉](./cj-quick-start-first-cangjie-hybrid-module.md)：基于一个简单的、支持页面跳转/返回功能的、纯ArkTS开发的应用，通过引入仓颉来开发一些增量业务。
- [仓颉调用ArkTS三方模块](./cj-quick-start-dts2cj-plugin-usage.md)：在仓颉代码中调用ArkTS三方库的功能。

## 工具准备

请下载并安装最新版[DevEco Studio](https://developer.huawei.com/consumer/cn/deveco-studio)，具体可参照[下载与安装DevEco Studio](../../../../Cangjie_Deveco_Studio/source_zh_cn/getting-started/cj-start-install-software.md)，更多工具使用指导可见[工具概述](../../../../Cangjie_Deveco_Studio/source_zh_cn/cj-ide-tools-overview.md)。

完成上述操作及基本概念的理解后，可参照[构建第一个HarmonyOS应用（仓颉）](cj-quick-start-first-cangjie-app.md)进行下一步体验和学习。
