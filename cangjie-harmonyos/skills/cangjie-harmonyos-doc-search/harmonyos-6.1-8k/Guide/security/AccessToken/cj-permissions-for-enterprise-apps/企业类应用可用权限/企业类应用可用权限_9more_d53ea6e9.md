# 企业类应用可用权限

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

以下权限面向<!--Del-->系统应用和<!--DelEnd-->企业类应用开放，企业类应用包括企业普通应用和MDM（Mobile Device Management）设备管理应用。

企业类应用有以下特征：

- 仅在企业定制设备上运行，不会在普通消费者设备上运行。

- 分发类型分别为enterprise_normal（企业普通应用）和enterprise_mdm（MDM应用）。

<!--RP1--><!--RP1End-->

企业类应用请参见[声明权限](./cj-declare-permissions.md)，申请以下权限。

> **注意：**
>
> 以下权限不支持自动签名，因此在调试和发布阶段，均需参照[手动签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section297715173233)的步骤，完成手动签名。

## ohos.permission.SET_FILE_GUARD_POLICY

允许应用下发文件管控策略。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

<!--Del-->
**ACL使能：** true<!--DelEnd-->

**起始版本：** 12

**变更信息：** API 12-14时，其权限级别为system_core，仅面向MDM应用开放；从API 14开始，权限级别变更为system_basic，开发范围变更为企业普通应用。

## ohos.permission.FILE_GUARD_MANAGER

允许应用进行公共目录扫描及设置文件扩展属性。

当前扩展属性包括文件密级、文件标签。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

<!--Del-->
**ACL使能：** true<!--DelEnd-->

**起始版本：** 12

**变更信息：** API 12-14时，其权限级别为system_core，仅面向MDM应用开放；从API 14开始，权限级别变更为system_basic，开发范围变更为企业普通应用。

## ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

允许应用跨系统本地账号交互。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

<!--Del-->
**ACL使能：** true<!--DelEnd-->

**起始版本：** 12

**变更信息：** API 12-13该权限仅向系统应用开放；从API 14开始，开放范围从系统应用变更为企业普通应用。

## ohos.permission.GET_RUNNING_INFO

允许应用获取运行态信息。

可获取其他应用的运行态信息，包括Ability、Extension、Application的信息。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

<!--Del-->
**ACL使能：** true<!--DelEnd-->

**起始版本：** 12

**变更信息：** API 12-13该权限仅向系统应用开放；从API 14开始，开放范围从系统应用变更为企业普通应用。

## ohos.permission.RUNNING_STATE_OBSERVER

允许应用监听应用状态。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

<!--Del-->
**ACL使能：** true<!--DelEnd-->

**起始版本：** 12

**变更信息：** API 12-13该权限仅向系统应用开放；从API 14开始，开放范围从系统应用变更为企业普通应用。

## ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

允许查询应用的基本信息和其他敏感信息。

如应用包名，版本等信息。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

<!--Del-->
**ACL使能：** true<!--DelEnd-->

**起始版本：** 12

**变更信息：** API 12-13该权限仅向系统应用开放；从API 14开始，开放范围从系统应用变更为企业普通应用。

## ohos.permission.SET_WIFI_CONFIG

允许应用配置Wi-Fi信息。

该权限允许应用添加、删除Wi-Fi，以及修改Wi-Fi的配置信息。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

<!--Del-->
**ACL使能：** true<!--DelEnd-->

**起始版本：** 12

**变更信息：** API 12-14该权限仅向系统应用开放；从API 15开始，开放范围变更为企业普通应用。

## ohos.permission.GET_DOMAIN_ACCOUNTS

允许应用查询域账号信息。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

<!--Del-->
**ACL使能：** true<!--DelEnd-->

**起始版本：** 12

**变更信息：** API 12-13该权限仅向系统应用开放；从API 14开始，开放范围变更为企业普通应用。