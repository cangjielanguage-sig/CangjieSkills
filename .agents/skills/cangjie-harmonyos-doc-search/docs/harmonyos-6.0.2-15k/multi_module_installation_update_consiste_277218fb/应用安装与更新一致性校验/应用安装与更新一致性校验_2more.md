# 应用安装与更新一致性校验

随着应用发展越来越复杂，应用也被拆成多个模块进行开发维护，不同的团队负责单个或者多个模块，应用在安装更新过程中会针对不同的字段进行一致性校验和验证，保证应用的安全合法性。本文介绍多模块安装或更新时，签名证书、配置文件的一致性校验规则。

> **说明**
>
> [app.json5配置文件](./app-configuration-file.md)中versionCode字段一致，表示安装或更新包同版本，否则为不同版本。
>
> 如果使用打包工具进行打包，打包过程中存在合法性校验，具体请参考[打包工具](../../tools/cj-packing-tool.md#打包工具)。

## 签名证书一致性校验

|字段名称|说明|安装一致性校验规则|更新一致性校验规则|
|--|--|--|--|
|appId|应用的appId，组成方式为bundleName_公钥的base64编码。|是|appId和appIdentifier任一相同即可。|
|appIdentifier|应用的唯一标识，是AppGallery Connect创建应用时分配的[APP ID](https://developer.huawei.com/consumer/cn/doc/app/agc-help-createharmonyapp-0000001945392297)，为云端统一分配的随机字符串。该ID在应用全生命周期中不会发生变化，包括版本升级、证书变更、开发者公私钥变更、应用转移等。|是|appId和appIdentifier任一相同即可。|
|appDistributionType|<!--RP1-->应用<!--RP1-->[签名证书](../../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-bundle_manager.md#let-appdistributiontype)中的app-distribution-type，标识应用的分发类型。<!--RP1End-->|是|更新不同版本时无校验，同版本有校验。|
|appProvisionType|应用签名[证书类型](https://developer.huawei.com/consumer/cn/doc/app/agc-help-add-debugprofile-0000001914423102)，分为debug和release。debug为本地调试使用，release为上架应用市场使用。|是|更新不同版本时无校验，同版本有校验。|
|apl|表示应用程序的[APL等级](../../security/AccessToken/cj-app-permission-mgmt-overview.md#权限机制中的基本概念)，系统定义的apl包括：normal、system_basic和system_core。|是|更新不同版本时无校验，同版本有校验。|