# 在已有ArkTS工程中增量使用仓颉

本文档适用于对仓颉语言、ArkTS语言、UI框架等有基本概念的HarmonyOS应用开发者。基于一个简单的、支持页面跳转/返回功能的、纯ArkTS开发的应用，通过引入仓颉来开发一些增量业务（比如，仓颉提供一个同步接口给ArkTS调用，仓颉提供一个异步接口给ArkTS调用，在原ArkTS页面中嵌入一个仓颉组件），来帮助开发者快速了解如何在存量ArkTS业务中，快速引入仓颉进行开发，熟悉混合应用的开发流程。

假设原ArkTS应用的初始运行效果如下图所示（有两个页面，支持页面跳转/返回）：

![HybridExample2_ArkTSProjectDemo](../../figures/start-HybridExample2_ArkTSProjectDemo.png)

现在引入仓颉期望实现以下两个效果：

1. 在ArkTS页面中，新增两个Button按钮，单击时会分别触发调用仓颉的同步接口和异步接口，更新Text文本，如下图所示。

   ![HybridExample2_ArkTSCallCangjieFunctionDemo](../../figures/start-HybridExample2_ArkTSCallCangjieFunctionDemo.png)

2. 在ArkTS页面中，嵌入一个仓颉组件，并在仓颉组件中提供一个Button按钮，单击时会更新Text文本，如下图所示。

   ![HybridExample2_ArkTSCallCangjieUIDemo](../../figures/start-HybridExample2_ArkTSCallCangjieUIDemo.png)