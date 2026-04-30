# 应用开发准备

在开始应用开发前，需要先完成以下准备工作。

## 注册成为开发者

在华为开发者联盟网站上，[注册成为开发者](https://developer.huawei.com/consumer/cn/doc/start/registration-and-verification-0000001053628148)，并完成[实名认证](https://developer.huawei.com/consumer/cn/doc/start/rna-0000001062530373)，从而享受联盟开放的各类能力和服务。

## 创建应用

在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)（简称AGC）上，参考[创建项目](https://developer.huawei.com/consumer/cn/doc/app/agc-help-createproject-0000001100334664)和[创建应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-createharmonyapp-0000001945392297)完成**HarmonyOS应用**的创建，从而使用各类服务。

## 配置安装DevEco Studio

安装最新版DevEco Studio。具体安装指导请参见[下载与安装DevEco Studio](../../Cangjie_Deveco_Studio/source_zh_cn/getting-started/cj-start-install-software.md)。

## 使用DevEco Studio创建应用工程

使用DevEco Studio创建应用工程。具体创建工程指导请参见[创建一个新的工程](../../Cangjie_Deveco_Studio/source_zh_cn/project-manager/cj-project-create-new-project.md)。

## 配置签名信息

使用模拟器和预览器调试无需配置签名信息，使用真机设备调试则需要对HAP进行签名。

目前提供了两种签名方式，请根据实际情况选择：

- [自动签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing)：如果您只需要使用一台调试设备，建议使用DevEco Studio提供的自动签名。

- 手动签名：如果您使用多台调试设备或者会在断网情况下调试，您需要在AGC中[申请调试证书](https://developer.huawei.com/consumer/cn/doc/app/agc-help-add-debugcert-0000001914263178)、[注册调试设备](https://developer.huawei.com/consumer/cn/doc/app/agc-help-add-device-0000001946142249)、[申请调试Profile后](https://developer.huawei.com/consumer/cn/doc/app/agc-help-add-debugprofile-0000001914423102)，再[手动配置签名信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section112371245115818)。
