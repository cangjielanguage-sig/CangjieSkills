### 在AGC控制台开通App Linking服务

请先参考“[应用开发准备](../application-dev-prepare/application-dev-prepare.md)”完成基本准备工作，再继续进行以下开发活动。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“我的项目”。

2. 在项目列表中点击您的项目。

3. 在左侧导航栏中选择“增长 > App Linking”，进入App Linking页面，点击“立即开通”。
    ![app-link-enable](figures/app-linking-startup-enable.png)

4. 如果您的项目此时未设置数据处理位置，请在提示框内启用数据处理位置和设置默认数据处理位置，点击“确定”。
    ![app-link-ok](figures/app-linking-startup-ok.png)

5. 进入“项目设置 > 常规”页面，选择创建的HarmonyOS应用，查看应用的APP ID，后续开发需要使用该ID。
    ![app-link-id](figures/app-linking-startup-id.png)

### 在开发者网站上关联应用

在开发者的网站域名服务器上做如下配置。后续当您配置该网站域名时，系统会通过此文件确认哪些应用才是合法归属于此域名的，使链接更加安全可靠。

1. 创建域名配置文件applinking.json。内容如下：

   ```json
   {
    "applinking": {
      "apps": [
        {
          "appIdentifier": "1234567"
        }
      ]
    }
   }
   ```

    > **说明：**
    >
    > * appIdentifier填写创建应用时生成的APP ID。
    > * 同一个网站域名可以关联多个应用，只需要在"apps"列表里放置多个"appIdentifier"元素即可，其中每个"appIdentifier"元素对应每个应用。

2. 将配置文件放在域名服务器的固定目录下：

   `https://domain.name/.well-known/applinking.json`

   例如开发者的域名为`www.example.com`，则需将applinking.json文件放在如下位置：

   `https://www.example.com/.well-known/applinking.json`

### 在AGC控制台关联网址域名

基于HarmonyOS应用链接能力，需要为HarmonyOS应用创建关联的网址域名。如果用户已安装HarmonyOS应用，则用户点击域名下网址链接后，系统会默认打开该HarmonyOS应用内的相关页面。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“我的项目”。

2. 在项目列表中点击您的项目。

3. 在左侧导航栏中选择“增长 > App Linking”，选择“应用链接（API>=12适用）”页签，点击“创建”。
    > **说明：**
    >
    > * HarmonyOS原生应用开发者仅需关注“应用链接（API>=12适用）”页签，其他页签为其他系统适用的配置，无需关注。
    > * 如果界面未展示“应用链接（API>=12适用）”页签，请在右侧的“自定义配置”中勾选。

    ![app-link-ok](figures/app-linking-startup-domain-1.png)

4. 填写HarmonyOS应用关联的网址域名，即[创建域名配置文件](#在开发者网站上关联应用)的网址，例如：`https://www.example.com`。必须输入精确的域名，不可输入包含特殊字符的模糊网址。

    > **说明：**
    >
    > 不允许在域名后面添加`/`，即不支持“`https://www.example.com/`”形式。

    ![app-linking-startup-domain-2](figures/app-linking-startup-domain-2.png)

5. 设置完成后单击“发布”，AGC会对该网站域名的配置文件所包含的应用与本项目内的应用列表进行交集校验。

    > **说明：**
    >
    > 应用链接发布完成后，如果距离上次更新超过24小时，系统会去域名服务器上重新获取配置文件进行交集校验。
    >
    > 例如：您在4月7日17:21创建了应用链接，系统会在4月8日17:30去域名服务器上重新获取配置文件，然后进行交集校验，更新发布状态。

    ![app-linking-startup-domain-3](figures/app-linking-startup-domain-3.png)

    * 如果域名的配置文件中有应用存在本项目中，则发布成功，单击“查看”可显示该域名关联的应用信息。

        ![app-linking-startup-domain-4](figures/app-linking-startup-domain-4.png)

    * 如果异步校验中，则状态为“发布中”。
    * 如果配置文件中没有任何应用在本项目中，则发布失败，单击“查看”可显示发布失败原因。

        ![app-linking-startup-domain-5](figures/app-linking-startup-domain-5.png)