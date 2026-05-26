## 使用须知

- 在申请目标权限前，建议开发者先阅读[应用权限管控概述-权限组和子权限](./cj-app-permission-mgmt-overview.md#权限组和子权限)，了解相关概念，再合理申请对应的权限组。
- 当应用请求权限时，同一个权限组的权限将会在一个弹窗内一起请求用户授权，用户同意授权后，权限组内权限将被统一授权。地理位置、通讯录、通话记录、电话、信息、日历权限组除外。

  以位置信息和相机权限组举例说明：

    - 当应用只申请了权限ohos.permission.APPROXIMATELY_LOCATION（属于位置信息权限组）时，应用用户将收到一个请求位置信息的弹窗，包含单个权限的申请。
    - 当应用同时申请权限ohos.permission.APPROXIMATELY_LOCATION和ohos.permission.LOCATION（均属于位置信息权限组）时，应用用户将收到一个请求位置信息的弹窗，包含两个权限的申请。
    - 当应用同时申请权限ohos.permission.APPROXIMATELY_LOCATION（属于位置信息权限组）和ohos.permission.CAMERA（属于相机权限组）时，应用用户将收到请求位置信息、请求使用相机的两个弹窗。

- 当前系统支持的权限组如下所示，各子权限的含义请查阅[应用权限列表](./cj-permissions-for-all-user.md)。

## 位置信息

- [ohos.permission.LOCATION_IN_BACKGROUND](./cj-permissions-for-all-user.md#ohospermissionlocation_in_background)
- [ohos.permission.LOCATION](./cj-permissions-for-all-user.md#ohospermissionlocation)
- [ohos.permission.APPROXIMATELY_LOCATION](./cj-permissions-for-all-user.md#ohospermissionapproximately_location)

## 相机

- [ohos.permission.CAMERA](./cj-permissions-for-all-user.md#ohospermissioncamera)

## 麦克风

- [ohos.permission.MICROPHONE](./cj-permissions-for-all-user.md#ohospermissionmicrophone)

## 通讯录

- [ohos.permission.READ_CONTACTS](./cj-permissions-for-acl.md#ohospermissionread_contacts)
- [ohos.permission.WRITE_CONTACTS](./cj-permissions-for-acl.md#ohospermissionwrite_contacts)

## 日历

- [ohos.permission.READ_CALENDAR](./cj-permissions-for-all-user.md#ohospermissionread_calendar)
- [ohos.permission.WRITE_CALENDAR](./cj-permissions-for-all-user.md#ohospermissionwrite_calendar)

## 运动数据

> **说明：**
>
> 由于2in1设备无相关传感器，此权限不支持在2in1设备上申请。

- [ohos.permission.ACTIVITY_MOTION](./cj-permissions-for-all-user.md#ohospermissionactivity_motion)

## 身体传感器

> **说明：**
>
> 仅穿戴设备可申请。

- [ohos.permission.READ_HEALTH_DATA](./cj-permissions-for-all-user.md#ohospermissionread_health_data)

## 图片和视频

- [ohos.permission.WRITE_IMAGEVIDEO](./cj-permissions-for-acl.md#ohospermissionwrite_imagevideo)
- [ohos.permission.READ_IMAGEVIDEO](./cj-permissions-for-acl.md#ohospermissionread_imagevideo)
- [ohos.permission.MEDIA_LOCATION](./cj-permissions-for-all-user.md#ohospermissionmedia_location)

## 音乐和音频

- [ohos.permission.WRITE_AUDIO](./cj-permissions-for-acl.md#ohospermissionwrite_audio)
- [ohos.permission.READ_AUDIO](./cj-permissions-for-acl.md#ohospermissionread_audio)

## 跨应用关联

- [ohos.permission.APP_TRACKING_CONSENT](./cj-permissions-for-all-user.md#ohospermissionapp_tracking_consent)

## 设备发现和连接

- [ohos.permission.ACCESS_BLUETOOTH](./cj-permissions-for-all-user.md#ohospermissionaccess_bluetooth)
- [ohos.permission.ACCESS_NEARLINK](./cj-permissions-for-all-user.md#ohospermissionaccess_nearlink)
- [ohos.permission.DISTRIBUTED_DATASYNC](./cj-permissions-for-all-user.md#ohospermissiondistributed_datasync)

## 剪切板

- [ohos.permission.READ_PASTEBOARD](./cj-permissions-for-acl.md#ohospermissionread_pasteboard)