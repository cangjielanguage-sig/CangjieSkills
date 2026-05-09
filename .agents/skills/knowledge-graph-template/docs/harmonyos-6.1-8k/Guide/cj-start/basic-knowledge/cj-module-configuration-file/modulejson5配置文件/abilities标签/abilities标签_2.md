| 属性名称 | 含义   | 数据类型 | 是否可缺省 |
|----------|---------------| -------- | -------- |
| srcEntry  | 标识入口UIAbility的类路径，取值为长度不超过127字节的字符串。 | 字符串 | 该标签不可缺省。 |
| [launchType](../../application-models/cj-uiability-launch-type.md) | 标识当前UIAbility组件的启动模式，支持的取值如下：<br/>-&nbsp;multiton：多实例模式，每次启动创建一个新实例。<br/>-&nbsp;singleton：单实例模式，仅第一次启动创建新实例。<br/>-&nbsp;specified：指定实例模式，运行时由开发者决定是否创建新实例。<br/>-&nbsp;standard：multiton的曾用名，效果与多实例模式一致。 | 字符串 | 该标签可缺省，该标签缺省为“singleton”。 |
| description | 标识当前UIAbility组件的描述信息，开发者可以通过该字段描述当前组件的功能与作用，取值为长度不超过255字节的字符串。要求采用描述信息的资源索引，以支持多语言。 | 字符串 | 该标签可缺省，缺省值为空。 |
| icon  | 标识当前UIAbility组件的[图标](../../application-models/cj-application-component-configuration-stage.md#生成机制)，取值为图标资源文件的索引。 | 字符串 | 该标签可缺省，缺省值为空。 |
| label | 标识当前UIAbility组件对用户显示的[名称](../../application-models/cj-application-component-configuration-stage.md#生成机制)，要求采用该名称的资源索引，以支持多语言。取值为长度不超过255字节的字符串。  | 字符串 | 该标签可缺省，缺省值为空。 |
| permissions | 标识当前UIAbility组件自定义的权限信息。其他应用访问该UIAbility时，需要申请相应的权限信息。<br/>一个数组元素为一个权限名称，权限名称采用反向域名格式（不超过255字节），取值为系统预定义的权限。 | 字符串数组 | 该标签可缺省，缺省值为空。 |
| [metadata](#metadata标签) | 标识当前UIAbility组件的元信息。   | 对象数组 | 该标签可缺省，缺省值为空。 |
| exported  | 标识当前UIAbility组件是否可以被其他应用拉起。<br/>-&nbsp;true：表示可以被其他应用拉起。<br/>-&nbsp;false：表示不可以被其他应用拉起，只能由同应用或者具有ohos.permission.START_INVISIBLE_ABILITY权限（该权限仅系统应用支持申请）的应用拉起。<br/> 例如，配置为false时，桌面具备该权限，桌面点击应用图标、快捷方式或push通知消息可以拉起当前UIAbility组件，但aa命令行工具没有权限无法拉起。 |布尔值 | 该标签可缺省，缺省值为false。 |
| continuable | 标识当前UIAbility组件是否支持跨端迁移。<br/>-&nbsp;true：表示支持迁移。<br/>-&nbsp;false：表示不支持迁移。   | 布尔值 | 该标签可缺省，缺省值为false。 |
| [skills](#skills标签)   | 标识当前UIAbility组件能够接收的[Want](../../application-models/cj-want-overview.md)特征集，为数组格式。<br/>配置规则：<br/>-&nbsp;对于Entry类型的HAP，应用可以配置多个具有入口能力的skills标签（即配置了ohos.want.action.home和entity.system.home）。<br/>-&nbsp;对于Feature类型的HAP，只有应用可以配置具有入口能力的skills标签，服务不允许配置。    | 对象数组 | 该标签可缺省，缺省值为空。 |
| backgroundModes    | 标识当前UIAbility组件的长时任务集合，指定用于满足特定类型的长时任务。<br/>长时任务类型有如下：<br/>-&nbsp;dataTransfer：通过网络/对端设备进行数据下载、备份、分享、传输等。<br/>-&nbsp;audioPlayback：音频播放。<br/>-&nbsp;audioRecording：录音。<br/>-&nbsp;location：定位、导航。<br/>-&nbsp;bluetoothInteraction：蓝牙扫描、连接、传输（穿戴）。<br/>-&nbsp;multiDeviceConnection：多设备互联。<br/>-&nbsp;taskKeeping：计算。  | 字符串数组 | 该标签可缺省，缺省值为空。 |
| [startWindow](#startwindow标签)  | 标识当前UIAbility组件启动页面profile资源，取值为长度不超过255字节的字符串，如果配置了该字段，startWindowIcon和startWindowBackground字段均不生效。<br/>**说明：** <br/>从API version 18开始，支持该字段。  | 字符串 | 该标签可缺省，缺省值为空。 |
| startWindowIcon    | 标识当前UIAbility组件启动页面图标资源文件的索引，取值为长度不超过255字节的字符串。  | 字符串 | 该标签不可缺省。 |
| startWindowBackground | 标识当前UIAbility组件启动页面背景颜色资源文件的索引，取值为长度不超过255字节的字符串。<br/>取值示例：$color:red。    | 字符串 | 该标签不可缺省。 |
| removeMissionAfterTerminate    | 标识当前UIAbility组件销毁后，是否从任务列表中移除任务。<br/>-&nbsp;true表示销毁后移除任务。<br/>-&nbsp;false表示销毁后不移除任务。  | 布尔值 | 该标签可缺省，缺省值为false。 |
| orientation | 标识当前UIAbility组件启动时的方向，支持配置枚举，或启动方向资源索引。<br/>**启动方向枚举支持的取值如下：**<br/>-&nbsp;unspecified：未指定方向，由系统自动判断显示方向。<br/>-&nbsp;landscape：横屏。<br/>-&nbsp;portrait：竖屏。<br/>-&nbsp;follow_recent：跟随背景窗口的旋转模式。<br/>-&nbsp;landscape_inverted：反向横屏。<br/>-&nbsp;portrait_inverted：反向竖屏。<br/>-&nbsp;auto_rotation：随传感器旋转。<br/>-&nbsp;auto_rotation_landscape：传感器横屏旋转，包括横屏和反向横屏。<br/>-&nbsp;auto_rotation_portrait：传感器竖屏旋转，包括竖屏和反向竖屏。<br/>-&nbsp;auto_rotation_restricted：传感器开关打开，方向可随传感器旋转。<br/>-&nbsp;auto_rotation_landscape_restricted：传感器开关打开，方向可随传感器旋转为横屏，&nbsp;包括横屏和反向横屏。<br/>-&nbsp;auto_rotation_portrait_restricted：传感器开关打开，方向随可传感器旋转为竖屏，&nbsp;包括竖屏和反向竖屏。<br/>-&nbsp;locked：传感器开关关闭，方向锁定。<br/>-&nbsp;auto_rotation_unspecified：受开关控制和由系统判定的自动旋转模式。<br/>-&nbsp;follow_desktop：跟随桌面的旋转模式。<br/>&nbsp;**配置启动方向的资源索引时**，取值为长度不超过255字节的字符串，配置示例：$string:orientation。<br/>&nbsp;**说明：**<br/>&nbsp;-&nbsp;从API version 14开始，支持配置启动方向资源索引。 | 字符串 | 该标签可缺省，缺省值为unspecified。 |
| supportWindowMode  | 标识当前UIAbility组件所支持的窗口模式。支持的取值如下：<br/>-&nbsp;fullscreen：全屏模式。<br/>-&nbsp;split：分屏模式。<br/>-&nbsp;floating：悬浮窗模式。  | 字符串数组 | 该标签可缺省，缺省值为<br/>["fullscreen",&nbsp;"split",&nbsp;"floating"]。 |
| <!--DelRow-->priority | 标识当前UIAbility组件的优先级。[隐式查询](../../application-models/cj-explicit-implicit-want-mappings.md)时，优先级越高，UIAbility在返回列表越靠前。取值范围0~10，数值越大，优先级越高。<br/>**说明：**<br/>三方应用的配置不生效，当前配置仅在系统应用中有效。  | 整型数值 | 该标签可缺省，缺省值为0。 |
| maxWindowRatio | 标识当前UIAbility组件支持的最大的宽高比。该标签最小取值为0。  | 数值 | 该标签可缺省，缺省值为平台支持的最大的宽高比。 |
| minWindowRatio | 标识当前UIAbility组件支持的最小的宽高比。该标签最小取值为0。  | 数值 | 该标签可缺省，缺省值为平台支持的最小的宽高比。 |
| maxWindowWidth | 标识当前UIAbility组件支持的最大的窗口宽度，宽度单位为vp。<br/>最小取值为minWindowWidth，最大取值为平台支持的最大窗口宽度。 | 数值 | 该标签可缺省，缺省值为平台支持的最大的窗口宽度。 |
| minWindowWidth | 标识当前UIAbility组件支持的最小的窗口宽度，&nbsp;宽度单位为vp。<br/>最小取值为平台支持的最小窗口宽度，最大取值为maxWindowWidth。  | 数值 | 该标签可缺省，缺省值为平台支持的最小的窗口宽度。 |
| maxWindowHeight    | 标识当前UIAbility组件支持的最大的窗口高度，&nbsp;高度单位为vp。<br/>最小取值为minWindowHeight，最大取值为平台支持的最大窗口高度。 | 数值 | 该标签可缺省，缺省值为平台支持的最大的窗口高度。 |
| minWindowHeight    | 标识当前UIAbility组件支持的最小的窗口高度，&nbsp;高度单位为vp。<br/>最小取值为平台支持的最小窗口高度，最大取值为maxWindowHeight。   | 数值 | 该标签可缺省，缺省值为平台支持的最小的窗口高度。 |
| <!--DelRow-->excludeFromMissions | 标识当前UIAbility组件是否在最近任务列表中显示。<br/>-&nbsp;true：表示不在任务列表中显示。<br/>-&nbsp;false：表示在任务列表中显示。<br/>**说明：**<br/>三方应用的配置不生效，当前配置仅在系统应用中有效，若要使系统应用配置生效，需申请应用特权AllowAbilityExcludeFromMissions，详见[应用特权配置指导](https://docs.openharmony.cn/pages/v5.1/zh-cn/device-dev/subsystems/subsys-app-privilege-config-guide.md)。 | 布尔值 | 该标签可缺省，缺省值为false。 |
| recoverable | 标识当前UIAbility组件是否支持在检测到应用故障后，恢复到应用原界面。<br/>-&nbsp;true：支持检测到出现故障后，恢复到原界面。<br/>-&nbsp;false：不支持检测到出现故障后，恢复到原界面。  | 布尔值 | 该标签可缺省，缺省值为false。 |
| <!--DelRow-->unclearableMission  | 标识当前UIAbility组件是否支持从最近任务列表中移除。<br/>-&nbsp;true：表示在任务列表中不可移除。<br/>-&nbsp;false：表示在任务列表中可以移除。<br/>**说明：**<br/>三方应用的配置不生效，当前配置仅在系统应用中有效，若要使系统应用配置生效，需申请应用特权AllowMissionNotCleared，详见[应用特权配置指导](https://docs.openharmony.cn/pages/v5.1/zh-cn/device-dev/subsystems/subsys-app-privilege-config-guide.md)。 | 布尔值 | 该标签可缺省，缺省值为false。 |
| isolationProcess   | 标识组件能否运行在独立的进程中。<br/>-&nbsp;true：表示能运行在独立的进程中。<br/>-&nbsp;false：表示不能运行在独立的进程中。<br/>**说明：**<br/>仅2in1和tablet设备支持将UIAbility设置为独立进程。 | 布尔值 | 该标签可缺省，缺省值为false。 |
| excludeFromDock    | 标识当前UIAbility组件是否支持从dock区域隐藏图标。<br/>-&nbs