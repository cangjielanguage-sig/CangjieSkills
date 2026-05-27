### ohos.permission.ACCESS_BLUETOOTH

允许应用接入蓝牙并使用蓝牙能力，例如配对、连接外围设备等。

**权限级别：** normal

**授权方式：** user_grant

**起始版本：** 12

### ohos.permission.MEDIA_LOCATION

允许应用访问用户媒体文件中的地理位置信息。

**权限级别：** normal

**授权方式：** user_grant

**起始版本：** 12

### ohos.permission.APP_TRACKING_CONSENT

允许应用读取开放匿名设备标识符。

**权限级别：** normal

**授权方式：** user_grant

**起始版本：** 12

### ohos.permission.ACTIVITY_MOTION

允许应用读取用户的运动状态。

**权限级别：** normal

**授权方式：** user_grant

**起始版本：** 12

### ohos.permission.CAMERA

允许应用使用相机。

**权限级别：** normal

**授权方式：** user_grant

**起始版本：** 12

### ohos.permission.DISTRIBUTED_DATASYNC

允许不同设备间的数据交换。

**权限级别：** normal

**授权方式：** user_grant

**起始版本：** 12

### ohos.permission.LOCATION_IN_BACKGROUND

允许应用在后台运行时获取设备位置信息。

由于安全隐私要求，应用不能通过弹窗的形式被授予后台位置权限，应用如果需要使用后台位置权限，需要引导用户到设置界面手动授予。

**申请流程：**

1. 在“module.json5”配置文件中[声明权限](./cj-declare-permissions.md)。

    由于在申请后台权限前，必须先申请前台位置权限，因此开发者在配置时，应同时配置后台位置权限ohos.permission.LOCATION_IN_BACKGROUND和前台位置权限。前台位置权限的申请有两种允许情况：
    - 申请前台模糊位置权限：[ohos.permission.APPROXIMATELY_LOCATION](#ohospermissionapproximately_location)。
    - 申请前台精确位置权限：[ohos.permission.APPROXIMATELY_LOCATION](#ohospermissionapproximately_location)和[ohos.permission.LOCATION](#ohospermissionlocation)。
2. 应用需通过弹窗向用户申请对应的前台位置权限。
3. 当用户点击弹窗授予前台位置权限后，应用应通过弹窗、提示窗等形式告知用户前往设置界面授予后台位置权限。
4. 用户在设置界面中的选择“始终允许”应用访问位置信息权限，完成手动授予。

    设置路径：

    - 路径一：设置 > 隐私与安全 > 位置 > 具体应用
    - 路径二：设置 > 应用和元服务 > 具体应用 > 位置

**权限级别：** normal

**授权方式：** user_grant

**起始版本：** 12

### ohos.permission.LOCATION

允许应用获取设备位置信息。

**申请条件：** 需要与模糊位置权限[ohos.permission.APPROXIMATELY_LOCATION](#ohospermissionapproximately_location)一起，才可申请此权限。

**权限级别：** normal

**授权方式：** user_grant

**起始版本：** 12

### ohos.permission.APPROXIMATELY_LOCATION

允许应用获取设备模糊位置信息。

**权限级别：** normal

**授权方式：** user_grant

**起始版本：** 12

### ohos.permission.MICROPHONE

允许应用使用麦克风。

**权限级别：** normal

**授权方式：** user_grant

**起始版本：** 12

### ohos.permission.READ_CALENDAR

允许应用读取日历信息。

**权限级别：** normal

**授权方式：** user_grant

**起始版本：** 12

### ohos.permission.WRITE_CALENDAR

允许应用添加、移除或更改日历活动。

**权限级别：** normal

**授权方式：** user_grant

**起始版本：** 12

### ohos.permission.READ_HEALTH_DATA

允许应用读取用户的健康数据。

**权限级别：** normal

**授权方式：** user_grant

**起始版本：** 12

### ohos.permission.ACCESS_NEARLINK

允许应用接入星闪并使用星闪能力，例如配对、连接外围设备等。

**权限级别：** normal

**授权方式：** user_grant

**起始版本：** 12

### ohos.permission.READ_WRITE_DOWNLOAD_DIRECTORY

允许应用访问公共目录下Download目录及子目录。

当前仅2in1设备应用可申请此权限。

**权限级别：** normal

**授权方式：** user_grant

**起始版本：** 12