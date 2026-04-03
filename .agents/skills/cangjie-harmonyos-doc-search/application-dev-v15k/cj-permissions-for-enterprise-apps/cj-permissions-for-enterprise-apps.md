# 企业类应用可用权限

以下权限面向企业类应用开放，企业类应用包括企业普通应用和MDM（Mobile Device Management）设备管理应用。

企业类应用的分发类型分别为enterprise_normal（企业普通应用）和enterprise_mdm（MDM应用），开发者可在Profile文件中查询字段app-distribution-type。

企业类应用请参见[声明权限](./cj-declare-permissions.md)，申请以下权限。

## ohos.permission.SET_FILE_GUARD_POLICY

允许应用下发文件管控策略。

**权限级别：** system_basic

**授权方式：** system_grant

**起始版本：** 12

## ohos.permission.FILE_GUARD_MANAGER

允许应用进行公共目录扫描及设置文件扩展属性。

**权限级别：** system_basic

**授权方式：** system_grant

**起始版本：** 12

## ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

允许应用跨系统本地账号交互。

**权限级别：** system_basic

**授权方式：** system_grant

**起始版本：** 12

## ohos.permission.GET_RUNNING_INFO

允许应用获取运行态信息。

**权限级别：** system_basic

**授权方式：** system_grant

**起始版本：** 12

## ohos.permission.RUNNING_STATE_OBSERVER

允许应用监听应用状态。

**权限级别：** system_basic

**授权方式：** system_grant

**起始版本：** 12

## ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

允许查询应用的基本信息和其他敏感信息。

**权限级别：** system_basic

**授权方式：** system_grant

**起始版本：** 12

## ohos.permission.GET_WIFI_CONFIG

允许应用获取Wi-Fi的配置信息。

**权限级别：** system_basic

**授权方式：** system_grant

**起始版本：** 12

## ohos.permission.MANAGE_NET_FIREWALL

允许系统应用配置防火墙规则。

当前仅2in1设备应用可申请此权限。

**权限级别：** system_basic

**授权方式：** system_grant

**起始版本：** 12

## ohos.permission.GET_NET_FIREWALL

允许系统应用查询防火墙规则和查询防火墙拦截记录。

当前仅2in1设备应用可申请此权限。

**权限级别：** system_basic

**授权方式：** system_grant

**起始版本：** 12

## ohos.permission.SET_WIFI_CONFIG

允许应用配置Wi-Fi信息。

**权限级别：** system_basic

**授权方式：** system_grant

**起始版本：** 12

## ohos.permission.GET_DOMAIN_ACCOUNTS

允许应用查询域账号信息。

**权限级别：** system_basic

**授权方式：** system_grant

**起始版本：** 12

## ohos.permission.QUERY_AUDIT_EVENT

允许应用查询安全审计事件。

**权限级别：** system_basic

**授权方式：** system_grant

**起始版本：** 12

## ohos.permission.KILL_APP_PROCESSES

允许系统应用杀掉其他应用。

**权限级别：** system_basic

**授权方式：** system_grant

**起始版本：** 12

## ohos.permission.SET_TELEPHONY_ESIM_STATE_OPEN

允许系统应用和运营商应用设置eSIM昵称和激活eSIM。

**权限级别：** system_basic

**授权方式：** system_grant

**起始版本：** 14

## ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION

允许应用管理Wi-Fi的连接。

**权限级别：** system_basic

**授权方式：** system_grant

**ACL使能：** true

**起始版本：** 16

## ohos.permission.MANAGE_NET_FIREWALL

允许系统应用配置防火墙规则。

当前仅2in1设备应用可申请此权限。

**权限级别：** system_basic

**授权方式：** system_grant

**起始版本：** 12

## ohos.permission.GET_NET_FIREWALL

允许系统应用查询防火墙规则和查询防火墙拦截记录。

当前仅2in1设备应用可申请此权限。

**权限级别：** system_basic

**授权方式：** system_grant

**起始版本：** 12
