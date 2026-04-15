## ohos.permission.QUERY_AUDIT_EVENT

允许企业安全类应用查询安全审计事件。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

<!--Del-->
**ACL使能：** true<!--DelEnd-->

**起始版本：** 12

**变更信息：** API 12-13该权限仅面向MDM应用开放；从API 14开始，开放范围从MDM应用变为更为企业普通应用。

## ohos.permission.KILL_APP_PROCESSES

允许系统应用结束其他应用进程。

获取权限后，可终止其他正在运行中的应用，允许它在必要时对系统中的进程进行管理和控制。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

<!--Del-->
**ACL使能：** true<!--DelEnd-->

**起始版本：** 12

**变更信息：** API 12-13该权限仅向系统应用开放；从API 14开始，开放范围从系统应用变更为企业普通应用。

## ohos.permission.SET_TELEPHONY_ESIM_STATE_OPEN

允许系统应用和运营商应用设置eSIM昵称和激活eSIM。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

<!--Del-->
**ACL使能：** true<!--DelEnd-->

**起始版本：** 14

**变更信息：** 在API 13，权限等级为normal；从API 14开始，权限等级变更为system_basic。

## ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION

允许应用管理Wi-Fi的连接。

获取该权限后，可执行开启/关闭、连接、断开Wi-Fi等操作。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 15

## ohos.permission.ACCESS_ENTERPRISE_USER_TRUSTED_CERT

允许应用管理企业设备的用户CA证书。

在企业设备上企业应用使用私有的CA证书认证企业服务器时，该权限用于允许企业应用把私有CA证书安装到企业设备上，并对安装的CA证书进行管理操作。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

<!--Del-->
**ACL使能：** true<!--DelEnd-->

**起始版本：** 18

## ohos.permission.GET_DOMAIN_ACCOUNT_SERVER_CONFIGS

允许应用获取域账号服务器配置。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

<!--Del-->
**ACL使能：** true<!--DelEnd-->

**起始版本：** 18

## ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS

允许应用管理域账号服务器配置。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

<!--Del-->
**ACL使能：** true<!--DelEnd-->

**起始版本：** 18

## ohos.permission.MANAGE_DOMAIN_ACCOUNTS

允许应用管理域账号。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

<!--Del-->
**ACL使能：** true<!--DelEnd-->

**起始版本：** 18

## ohos.permission.GET_SIGNATURE_INFO

允许应用获取应用包的签名信息。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

<!--Del-->
**ACL使能：** true<!--DelEnd-->

**起始版本：** 18

## ohos.permission.VISIBLE_WINDOW_INFO

允许应用获取当前屏幕的可见窗口信息。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

<!--Del-->
**ACL使能：** true<!--DelEnd-->

**起始版本：** 18