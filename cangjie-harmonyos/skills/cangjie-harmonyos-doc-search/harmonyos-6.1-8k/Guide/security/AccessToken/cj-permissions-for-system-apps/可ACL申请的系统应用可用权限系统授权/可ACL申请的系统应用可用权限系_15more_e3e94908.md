# 可ACL申请的系统应用可用权限（系统授权）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

在申请目标权限前，建议开发者先了解[不同权限的申请路径](./cj-determine-application-mode.md)，对权限的工作流程有基本了解后，再结合以下权限字段的具体说明，判断应用能否申请目标权限，提高开发效率。

> **说明：**
>
> - 以下权限仅对APL等级为system_basic及以上的应用开放，不向APL等级为normal的应用开放。
> - 以下权限的授权方式均为system_grant（系统授权）。
> - 以下权限可通过[访问控制列表（ACL）](./cj-app-permission-mgmt-overview.md#权限机制中的基本概念)的方式跨级别申请。

申请流程可参考[选择申请权限的方式](./cj-determine-application-mode.md)。

## ohos.permission.PRE_START_ATOMIC_SERVICE

允许应用市场跳过loading弹框并为原子化服务提前打开窗口，并在窗口内部显示加载动效。

**权限级别：** system_core

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 12

## ohos.permission.MANAGE_APP_KEEP_ALIVE

允许对三方应用进程设置保活。

**权限级别：** system_core

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 14

## ohos.permission.ACCESS_BBOX_DIR

允许系统应用读取bbox路径下的日志文件。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 12

## ohos.permission.CONTROL_LOCATION_SWITCH

允许应用打开和关闭位置信息开关。

**权限级别：** system_core

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 12

## ohos.permission.LOCATION_SWITCH_IGNORED

允许系统应用在位置开关关闭的情况下，获取位置信息。

**权限级别：** system_core

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 18

## ohos.permission.SUBSCRIBE_SWING_ABILITY

允许应用使用智慧感知订阅能力。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 12

## ohos.permission.MANAGER_SWING_MOTION

允许应用使用隔空手势自适配能力。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 12

## ohos.permission.MOCK_LOCATION

允许应用使用模拟位置功能。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 12

## ohos.permission.ACCESS_LEARN_MORE_DIALOG

允许系统应用拉起“进一步了解”的展示弹窗，获取更多详细信息。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 13

## ohos.permission.WRITE_PROTECTION_ADVICE_POLICY

允许系统应用修改“安全建议”的数据库。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 17

## ohos.permission.READ_PROTECTION_ADVICE_POLICY

允许系统应用读取“安全建议”的数据库。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 17

## ohos.permission.PROXY_MESSAGE_AUTH

允许系统应用调用“信息”应用授权接口。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**起始版本：** 18

## ohos.permission.MANAGE_SETTINGS

允许应用设置SettingsData中设备级配置数据表和用户级配置数据表。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 12

## ohos.permission.ACCESS_SCREEN_LOCK

允许应用访问锁屏信息。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 12