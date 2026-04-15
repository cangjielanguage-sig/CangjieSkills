### ohos.permission.SYSTEM_FLOAT_WINDOW

允许应用使用悬浮窗的能力。

<!--RP25--><!--RP25End-->

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**起始版本：** 12

### ohos.permission.READ_CONTACTS

允许应用读取联系人数据。

<!--RP33--><!--RP33End-->

**权限级别：** system_basic

**授权方式：** 用户授权（user_grant）

**起始版本：** 12

### ohos.permission.WRITE_CONTACTS

允许应用添加、移除或更改联系人数据。

<!--RP34--><!--RP34End-->

**权限级别：** system_basic

**授权方式：** 用户授权（user_grant）

**起始版本：** 12

### ohos.permission.READ_AUDIO

允许读取用户公共目录的音频文件。

<!--RP26--><!--RP26End-->

**权限级别：** system_basic

**授权方式：** 用户授权（user_grant）

**起始版本：** 12

### ohos.permission.WRITE_AUDIO

允许修改用户公共目录的音频文件。

<!--RP28--><!--RP28End-->

**权限级别：** system_basic

**授权方式：** 用户授权（user_grant）

**起始版本：** 12

### ohos.permission.READ_IMAGEVIDEO

允许读取用户公共目录的图片或视频文件。

<!--RP27--><!--RP27End-->

**权限级别：** system_basic

**授权方式：** 用户授权（user_grant）

**起始版本：** 12

### ohos.permission.WRITE_IMAGEVIDEO

允许修改用户公共目录的图片或视频文件。

<!--RP29--><!--RP29End-->

**权限级别：** system_basic

**授权方式：** 用户授权（user_grant）

**起始版本：** 12

### ohos.permission.READ_PASTEBOARD

允许应用读取剪贴板。

<!--RP32--><!--RP32End-->

**权限级别：** system_basic

**授权方式：** 用户授权（user_grant）

**起始版本：** 12

### ohos.permission.FILE_ACCESS_PERSIST

允许应用支持持久化访问文件Uri。

**权限级别：** normal

**授权方式：** 系统授权（system_grant）

**起始版本：** 12

### ohos.permission.INPUT_MONITORING

允许应用监听输入事件。

<!--RP23--><!--RP23End-->

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**起始版本：** 7

### ohos.permission.SHORT_TERM_WRITE_IMAGEVIDEO

允许应用保存图片、视频到用户公共目录。

应用获取此权限后，最长可获得30分钟的短时授权，来保存图片/视频。如果超过30分钟，将再次弹窗，需要用户再次确认。

<!--RP21--><!--RP21End-->

**权限级别：** system_basic

**授权方式：** 用户授权（user_grant）

**起始版本：** 12

### ohos.permission.GET_WIFI_PEERS_MAC

允许应用获取对端Wi-Fi设备的MAC地址。

在获取Wi-Fi扫描结果时，如果需要获取对端设备的MAC地址，则需要申请该权限。

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**起始版本：** 12

**变更信息：** API 12，权限等级为system_core；从API 15开始，权限等级变更为system_basic，向普通应用开放。

### ohos.permission.kernel.DISABLE_CODE_MEMORY_PROTECTION

允许应用禁用本应用的代码运行时完整性保护。

<!--RP11-->
针对使用跨平台框架开发的应用，用于应用豁免代码运行时的完整性保护。当前仅平板设备应用可申请此权限。
<!--RP11End-->

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**起始版本：** 12

### ohos.permission.kernel.ALLOW_WRITABLE_CODE_MEMORY

允许应用申请可写可执行匿名内存。

<!--RP10-->
针对使用跨平台框架开发的应用，用于应用申请可写可执行的匿名内存。当前仅平板设备应用可申请此权限。
<!--RP10End-->

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**起始版本：** 12

### ohos.permission.kernel.ALLOW_EXECUTABLE_FORT_MEMORY

允许系统JS引擎申请带MAP_FORT标识的匿名可执行内存。

应用申请此权限后，系统引擎可申请带MAP_FORT的匿名可执行内存，做即时编译，提高与形式执行效率。

<!--RP13--><!--RP13End-->

**权限级别：** system_basic

**授权方式：** 系统授权（system_grant）

**起始版本：** 12