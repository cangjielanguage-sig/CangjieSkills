# 构建第一个仓颉与ArkTS混合应用

> **说明：**
>
> 为确保运行效果，本文以**DevEco Studio 5.0.2 Release** 和 **DevEco Studio-Cangjie Plugin 5.0.7.100 Beta1** 版本为例，点击[此处](https://developer.huawei.com/consumer/cn/download/)获取最新版本的下载链接。

本文档适用于对仓颉语言、ArkTS语言、UI框架等有基本概念的OpenHarmony应用开发者。通过构建一个简单的具有页面跳转/返回功能的仓颉与ArkTS混合开发的应用（如下图所示），快速了解工程目录的主要文件，熟悉混合应用的开发流程。

![hybridExampleRunning](../../figures/hybridExampleRunning.png)

## 创建仓颉与ArkTS混合工程

1. 若首次打开**DevEco Studio**，请单击**Create Project**创建工程。如果已经打开了一个工程，请在菜单栏选择**File** > **New** > **Create Project**来创建一个新工程。
2. 选择**Application**应用开发，选择模板 **[Cangjie] Hybrid Ability**，单击**Next**进行下一步配置。

   > **注意：**
   >
   > 若开发者需要进行纯仓颉工程开发，请选择 **[Cangjie] Empty Ability**模块。

   ![buildChooseCangjieHybridTemplate](../../figures/buildChooseCangjieHybridTemplate.png)

3. 进入配置工程界面，参数保持默认设置即可。

   > **注意：**
   >
   > 仓颉混合页面支持的最低Compatible SDK版本为5.0.1(13)。

   ![buildConfigCangjieHybridTyplate](../../figures/buildConfigCangjieHybridTemplate.png)

4. 单击**Finish**，DevEco Studio会自动生成示例代码和相关资源，等待工程创建完成。