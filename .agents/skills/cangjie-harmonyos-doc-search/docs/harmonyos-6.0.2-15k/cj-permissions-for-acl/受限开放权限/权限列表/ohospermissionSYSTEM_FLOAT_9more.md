### ohos.permission.SYSTEM_FLOAT_WINDOW

允许应用使用全局悬浮窗的能力。

**可申请此权限的特殊场景与功能：**

- 多人视频通话。
- 屏幕共享。
- 当前仅2in1设备应用可申请此权限。

> **说明：**
>
> 应用基于悬浮窗提供的窗口界面，必须向用户提供退出窗口的方式。

**其他场景下的使用方案：** 在其他设备或场景下，使用“画中画”功能。

**授权方式：** 系统授权（system_grant）

**起始版本：** 12

### ohos.permission.READ_CONTACTS

允许应用读取联系人数据。

**可申请此权限的特殊场景与功能：** 应用需要克隆、备份或同步联系人信息。

**其他场景下的使用方案：** 使用“联系人Picker”访问联系人数据，使用方式请参见[选择联系人](../../contacts/cj-contacts-intro.md#使用picker选择联系人)。

**授权方式：** 用户授权（user_grant）

**起始版本：** 12

### ohos.permission.WRITE_CONTACTS

允许应用添加、移除或更改联系人数据。

**可申请此权限的特殊场景与功能：** 应用需要克隆、备份或同步联系人信息。

**其他场景下的使用方案：** 除以上特殊场景外，应用不能修改联系人数据，应引导用户到“联系人”应用中修改联系人数据。

**授权方式：** 用户授权（user_grant）

**起始版本：** 12

### ohos.permission.READ_AUDIO

允许读取用户公共目录的音频文件。

**可申请此权限的特殊场景与功能：** 应用需要克隆、备份或同步音频类文件。

**其他场景下的使用方案：** 使用“AudioPicker”访问用户音频文件，使用方式请参见：[（FilePicker）选择音频类文件](../../file-management/cj-select-user-file.md#选择音频类文件)。

**授权方式：** 用户授权（user_grant）

**起始版本：** 12

### ohos.permission.WRITE_AUDIO

允许修改用户公共目录的音频文件。

**可申请此权限的特殊场景与功能：** 应用需要克隆、备份或同步音频类文件。

**其他场景下的使用方案：** 使用“AudioPicker”保存用户音频文件，使用方式请参见：[（FilePicker）保存音频类文件](../../file-management/cj-save-user-file.md#保存音频类文件)。

**授权方式：** 用户授权（user_grant）

**起始版本：** 12

### ohos.permission.READ_IMAGEVIDEO

允许读取用户公共目录的图片或视频文件。

**可申请此权限的特殊场景与功能：** 应用需要克隆、备份或同步图片/视频类文件。

**其他场景下的使用方案：** 使用“PhotoViewPicker”访问用户图片或视频，使用方式请参见：[使用Picker选择媒体库资源](../../media/medialibrary/cj-photoAccessHelper-photoviewpicker.md#使用picker选择媒体库资源)。

**授权方式：** 用户授权（user_grant）

**起始版本：** 12

### ohos.permission.WRITE_IMAGEVIDEO

允许修改用户公共目录的图片或视频文件。

**可申请此权限的特殊场景与功能：** 应用需要克隆、备份或同步图片/视频类文件。

**其他场景下的使用方案：** 使用安全控件或授权弹窗的方式，将用户指定的媒体资源保存到图库中，使用方式请参见：[保存媒体库资源](../../media/medialibrary/cj-photoAccessHelper-savebutton.md)。

**授权方式：** 用户授权（user_grant）

**起始版本：** 12

### ohos.permission.READ_WRITE_DESKTOP_DIRECTORY

允许应用访问公共目录下Desktop目录及子目录。

**可申请此权限的特殊场景与功能：** 当前仅2in1设备应用可申请此权限。

**授权方式：** 用户授权（user_grant）

**起始版本：** 12

### ohos.permission.ACCESS_DDK_USB

允许扩展外设驱动访问USB DDK接口开发USB总线扩展外设驱动。

**可申请此权限的特殊场景与功能：**

- 外接设备总线类型为USB总线，用于支持外接设备实现相应的功能，如外接指纹采集、打印机、身份证、指纹识别等外接设备。
- 当前仅2in1设备应用可申请此权限。

除上述场景外，应用不需要使用此权限保护的系统能力，不涉及申请此权限。

**授权方式：** 系统授权（system_grant）

**起始版本：** 12