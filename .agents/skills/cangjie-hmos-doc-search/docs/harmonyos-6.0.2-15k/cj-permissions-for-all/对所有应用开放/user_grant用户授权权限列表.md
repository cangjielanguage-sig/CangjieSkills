## user_grant（用户授权）权限列表

以下权限的授权方式均为 user_grant（用户授权），申请方式请参考声明权限 &gt; 向用户申请授权 。

### ohos.permission.ACCESS_BLUETOOTH

允许应用接入蓝牙并使用蓝牙能力，例如配对、连接外围设备等。

**权限级别**：normal

**授权方式**：user_grant

**ACL使能**：false

### ohos.permission.MEDIA_LOCATION

允许应用访问用户媒体文件中的地理位置信息。

**权限级别**：normal

**授权方式**：user_grant

**ACL使能**：true

### ohos.permission.APP_TRACKING_CONSENT

允许应用读取开放匿名设备标识符。

**权限级别**：normal

**授权方式**：user_grant

**ACL使能**：true

### ohos.permission.ACTIVITY_MOTION

允许应用读取用户的运动状态。

**权限级别**：normal

**授权方式**：user_grant

**ACL使能**：true

### ohos.permission.CAMERA

允许应用使用相机。

**权限级别**：normal

**授权方式**：user_grant

**ACL使能**：true

### ohos.permission.DISTRIBUTED_DATASYNC

允许不同设备间的数据交换。

**权限级别**：normal

**授权方式**：user_grant

**ACL使能**：true

### ohos.permission.LOCATION_IN_BACKGROUND

允许应用在后台运行时获取设备位置信息。

**申请条件**：需要先申请前台位置权限[ohos.permission.LOCATION](#ohospermissionlocation)和[ohos.permission.APPROXIMATELY_LOCATION](#ohospermissionapproximately_location)后，才可申请此权限。

**权限级别**：normal

**授权方式**：user_grant

**ACL使能**：false

### ohos.permission.LOCATION

允许应用获取设备位置信息。

**申请条件**：需要先申请模糊位置权限[ohos.permission.APPROXIMATELY_LOCATION](#ohospermissionapproximately_location)，才可申请此权限。

**权限级别**：normal

**授权方式**：user_grant

**ACL使能**：true

### ohos.permission.APPROXIMATELY_LOCATION

允许应用获取设备模糊位置信息。

**权限级别**：normal

**授权方式**：user_grant

**ACL使能**：false

### ohos.permission.MICROPHONE

允许应用使用麦克风。

**权限级别**：normal

**授权方式**：user_grant

**ACL使能**：true

### ohos.permission.READ_CALENDAR

允许应用读取日历信息。

**权限级别**：normal

**授权方式**：user_grant

**ACL使能**：true

### ohos.permission.READ_HEALTH_DATA

允许应用读取用户的健康数据。

**权限级别**：normal

**授权方式**：user_grant

**ACL使能**：true

### ohos.permission.READ_MEDIA

允许应用读取用户外部存储中的媒体文件信息。

**权限级别**：normal

**授权方式**：user_grant

**ACL使能**：true

### ohos.permission.WRITE_CALENDAR

允许应用添加、移除或更改日历活动。

**权限级别**：normal

**授权方式**：user_grant

**ACL使能**：true

### ohos.permission.WRITE_MEDIA

允许应用读写用户外部存储中的媒体文件信息。

**权限级别**：normal

**授权方式**：user_grant

**ACL使能**：true