# 构建第一个OpenHarmony应用（仓颉）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

> **说明：**
> 
> - DevEco Studio默认创建的工程为HarmonyOS工程，不再支持直接创建OpenHarmony工程。需要基于创建完成的HarmonyOS工程进行一些字段修改，才能得到OpenHarmony工程。
> 
> - 为确保运行效果，本文以使用**最新DevEco Studio版本**为例，点击[此处](https://developer.huawei.com/consumer/cn/download/)获取下载链接。

## 创建仓颉工程

1. 若首次打开**DevEco Studio**，请单击**Create Project**创建工程。如果已经打开了一个工程，请在菜单栏选择**File** > **New** > **Create Project**来创建一个新工程。

2. 选择**Application**应用开发（本文以应用开发为例，仓颉暂不支持元服务开发），选择模板 **[Cangjie] Empty Ability**，然后单击**Next**进行下一步配置。

   ![cangjieTemplate](../../figures/cangjieTemplate.png)

3. 进入配置工程界面，可以修改工程名称和存储路径等工程的基本信息，也可以保持默认设置。

   ![cangjieConfig](../../figures/cangjieConfig.png)

4. 单击 **Finish**，完成工程创建，工具会自动生成基础示例代码和相关资源。<!--Del-->

5. 在完成创建HarmonyOS工程后，根据如下操作修改工程级build-profile.json5文件（即与entry同级）中相关字段：
   
   1. 在工程级build-profile.json5文件添加compileSdkVersion字段。

   2. 将compatibleSdkVersion和compileSdkVersion字段赋值为整数类型，如22，23。

   3. 将runtimeOS从"HarmonyOS"修改为"OpenHarmony"。

   ```json
   "products": [
     {
       "name": "default",
       "signingConfig": "default", 
       "compileSdkVersion": 22,    // 指定OpenHarmony应用/原子化服务编译时的版本
       "compatibleSdkVersion": 22, // 指定OpenHarmony应用/原子化服务兼容的最低版本
       "runtimeOS": "OpenHarmony",
     }
   ],
   ```

6. 单击**Sync Now**进行同步。

   在Sync Check弹窗中点击Yes，同意将module.json5/config.json文件中的phone切换为OpenHarmony支持的default类型，并删除在OpenHarmony不适用的其他设备类型，同步成功无其他报错则OpenHarmony工程创建完成。
<!--DelEnd-->