## ohos.permission.WATCH_READ_EMERGENCY_INFO

允许应用读取SOS个人紧急信息数据。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 18

## ohos.permission.WATCH_WRITE_EMERGENCY_INFO

允许应用写入SOS个人紧急信息数据。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 18

## ohos.permission.WATCH_START_SOS_SERVICE

允许应用启用或访问SOS服务。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 18

**变更信息：** API 12-14，该权限仅向系统服务开放；从API 15开始，开放范围变更为系统应用。

## ohos.permission.ACCESS_DLP_HIDE_INFO

允许系统应用拉起防窥保护设置页。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 18

## ohos.permission.DLP_GET_HIDE_STATUS

允许系统应用使用信息隐藏接口，获取信息隐藏状态的能力。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 18

## ohos.permission.GET_ANIM_POLICY

允许系统应用注册动效插件，获取动效使用策略。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 18

## ohos.permission.GET_FAMILY_INFO

允许系统应用获取“家人共享”中的群组信息。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 18

## ohos.permission.ACCESS_FUSION_AWARENESS_DATA

允许系统应用获取融合感知数据。

**权限级别：** system_core

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 18

## ohos.permission.ACCESS_ACCOUNT_RECOMMENDATION_DATA

允许应用读取“账号建议”的数据，以及拉起账号建议列表UIExtensionAbility。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 18

## ohos.permission.GET_PAGE_INFO

允许系统应用获取指定应用页面信息。

**权限级别：** system_core

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 18

## ohos.permission.ACCESS_DDK_DRIVERS

允许扩展外设驱动客户端绑定到扩展外设驱动服务端。

该权限针对扩展外设客户端绑定到扩展外设服务端权限校验，具体规则：

1. 外设扩展驱动客户端权限声明中的value字段中描述的目标扩展驱动服务端已上架或一并上架。
2. 被申请目标扩展驱动服务端对外提供能力与扩展外设驱动客户端业务诉求一致。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**携带额外数据：** 是

**起始版本：** 18

## ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

允许扩展外设驱动访问SCSI DDK接口开发SCSI Peripheral扩展外设驱动。

支持以下类型的外设扩展驱动开发：
外设以USB总线接入主机，且满足：

1. 外设InterfaceClass为Mass Storage(0x08)、InterfaceSubClass为SCSI透明命令集(0x06)。
2. 外设能够以对操作系统透明的方式来模拟SCSI设备。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 18

## ohos.permission.ACCESS_DDK_USB_SERIAL

允许扩展外设驱动访问USBSerial DDK接口开发USB Serial扩展外设驱动。

支持以下类型的外设扩展驱动开发：
外设以USB总线接入主机，且满足：

1. 外设InterfaceClass为通信设备控制类 (0x02)、InterfaceSubClass遵循ACMSubClass模型(0x02)。
2. 外设支持通过USB接口模拟传统的串行通信。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 18

## ohos.permission.ACCESS_CUSTOM_RINGTONE

允许应用访问铃音库。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 18