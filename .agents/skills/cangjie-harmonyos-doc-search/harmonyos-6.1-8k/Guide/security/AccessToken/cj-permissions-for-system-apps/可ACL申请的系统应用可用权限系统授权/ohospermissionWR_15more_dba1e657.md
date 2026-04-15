## ohos.permission.WRITE_DHA

允许应用写入设备健康证明信息。

**权限级别：** system_core

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 18

## ohos.permission.NOTIFY_DHA

允许应用通知设备健康证明事件。

**权限级别：** system_core

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 18

## ohos.permission.CHANGE_DEFAULT_APPLICATION

允许应用监听“默认应用”变化事件。

用户可以为系统设置“默认应用”，如设置默认使用某一应用打开指定类型文件。当“默认应用”变化时，将触发“默认应用”变化事件。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 19

## ohos.permission.SEND_NOTIFICATION_CROSS_USER

允许应用发送通知给系统中指定用户。

**权限级别：** system_core

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 18

## ohos.permission.ALLOW_ACCESS_TIPS

允许系统应用拉起Tips提供的组件。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 18

### ohos.permission.UPDATE_FONT

允许应用安装和卸载字体。

**权限级别：** system_basic

**授权方式：** system_grant

**ACL使能：** true

**起始版本：** 19

## ohos.permission.ACCESSIBILITY_EXTENSION_ABILITY

允许应用通过无障碍服务接口查询和操作界面上的组件。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**支持设备：** General

**ACL使能：** true

**起始版本：** 20

## ohos.permission.READ_SOUND_RECORD_IN_FILE_MANAGER

允许应用从文件管理目录读取录音文件。

**权限级别：** system_core

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**支持设备：** Phone | Tablet

**起始版本：** 20

## ohos.permission.WRITE_SOUND_RECORD_IN_FILE_MANAGER

允许应用向文件管理目录写入录音文件。

**权限级别：** system_core

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**支持设备：** Phone | Tablet

**起始版本：** 20

## ohos.permission.SANDBOX_ACCESS_MANAGER

允许应用访问其它应用的沙箱目录。

**权限级别：** system_core

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**起始版本：** 17

## ohos.permission.REQUEST_DISABLE_NOTIFICATION

允许应用运行的后台上传下载任务不在通知栏显示。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**支持设备：** General

**起始版本：** 20

## ohos.permission.RESTORE_APP

允许系统应用拉起恢复弹窗以恢复应用。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**支持设备：** Phone | Tablet

**起始版本：** 20

## ohos.permission.ALLOW_IOURING

允许系统应用调用io_uring相关系统调用实现异步IO操作。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**支持设备：** General

**起始版本：** 20

## ohos.permission.NFC_NOTIFICATION

允许应用发布NFC通知相关的公共事件。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**支持设备：** Phone

**起始版本：** 20

## ohos.permission.kernel.ALLOW_APP_CODE_DECRYPT

允许系统应用或系统服务调用内核接口进行代码解密。

应用或服务拥有此权限后，可跨进程访问内核接口，针对已加密的代码内容请求解密，可避免非法访问，进一步保护应用代码资产。

**权限级别：** system_core

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**支持设备：** General

**起始版本：** 20

## ohos.permission.GRANT_URI_PERMISSION_AS_CALLER

允许应用以调用方的身份将URI访问权限授权给目标应用。

**权限级别：** system_core

**授权方式：** 系统授权（system_grant）

**ACL使能：** true

**支持设备：** General

**起始版本：** 20