# 开发准备

应用需要先获取相册管理模块实例，才能访问和修改相册中的媒体数据信息。相册管理模块涉及用户个人数据信息，因此应用需要向用户申请相册管理模块读写操作权限，以确保功能的正常运行。在使用相册管理模块的相关接口时，如无特别说明，默认是在工程代码的 `pages/index.cj` 或其他自定义的cj文件中使用。

## 获取相册管理模块实例

应用需要使用应用上下文Context通过接口[getPhotoAccessHelper](../../../API_Reference/source_zh_cn/apis/MediaLibraryKit/cj-apis-multimedia-photo_accesshelper.md#func-getphotoaccesshelperabilitycontext)，获取相册管理模块实例，用于访问和修改相册中媒体数据信息（如图片、视频）。

**开发步骤**

1. 导入photoAccessHelper模块以使用相册管理模块相关接口。
2. 通过context获取应用上下文。
3. 获取相册管理模块实例。

```cangjie
import kit.MediaLibraryKit.*

// 此处获取的photoAccessHelper实例为全局对象，后续文档中使用到的地方默认为使用此处获取的对象，如未添加此段代码报未定义的错误请自行添加。
let context = ctx.getOrThrow()
let phAccessHelper = getPhotoAccessHelper(context)
```

```cangjie
// main_ability.cj
import kit.AbilityKit.{LaunchReason, LaunchParam, Want, UIAbility}
import kit.ArkUI.WindowStage
import kit.UIKit.AppLog

class MainAbility <: UIAbility {
    public init() {
        super()
        registerSelf()
    }

    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        AppLog.info("MainAbility OnCreated.${want.abilityName}")
        match (launchParam.launchReason) {
            case LaunchReason.START_ABILITY => AppLog.info("START_ABILITY")
            case _ => ()
        }
    }

    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
        AppLog.info("MainAbility onWindowStageCreate.")
        windowStage.loadContent("EntryView")
        // declared in index.cj
        ctx = this.context
    }
}
```

## 申请相册管理模块功能相关权限

相册管理模块的读写操作需要相应权限，在申请权限前，请保证符合[权限使用的基本原则](../../security/AccessToken/cj-app-permission-mgmt-overview.md)。涉及的权限如下表。

| 权限名                         | 说明                                       | 授权方式   |
| ------------------------------ | ------------------------------------------ | ---------- |
| ohos.permission.READ_IMAGEVIDEO     | 允许应用读取媒体库的图片和视频媒体文件信息。 | user_grant |
| ohos.permission.WRITE_IMAGEVIDEO    | 允许应用读写媒体库的图片和视频媒体文件信息。 | user_grant |

以上权限的授权方式均为user_grant（用户授权），即开发者在module.json5文件中配置对应的权限后，需要使用接口[requestPermissionsFromUser](../../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability_access_ctrl.md#func-requestpermissionsfromuserstagecontext-arraypermissions-asynccallbackpermissionrequestresult)去校验当前用户是否已授权。如果是，应用可以直接访问/操作目标对象；否则需要弹框向用户申请授权。

**开发步骤**
<!--RP1-->

1. 上述权限均为受控权限，申请前需要额外申请ACL白名单，请参见[声明ACL权限](../../security/AccessToken/cj-declare-permissions-in-acl.md)

<!--RP1End-->

1. [在配置文件module.json5中声明权限](../../security/AccessToken/cj-declare-permissions.md)。
2. [向用户申请授权](../../security/AccessToken/cj-request-user-authorization.md)。

> **说明：**
>
> 即使用户曾经授予权限，应用在调用受此权限保护的接口前，也应该先检查是否有权限。不能把之前授予的状态持久化，因为用户在动态授予后还可以通过“设置”取消应用的权限。
