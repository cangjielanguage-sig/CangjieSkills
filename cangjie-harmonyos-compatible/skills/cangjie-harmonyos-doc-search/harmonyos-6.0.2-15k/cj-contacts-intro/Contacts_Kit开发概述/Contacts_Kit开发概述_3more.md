# Contacts Kit开发概述

Contacts Kit可以帮助开发者轻松实现联系人的增删改查等功能。该Kit提供了一系列API，可以让开发者在应用中快速集成联系人管理功能。

详情请参见[ohos.contact API](../../API_Reference/source_zh_cn/apis/ContactsKit/cj-apis-contact.md)。

## 能力范围

通过Contacts Kit，开发者可以对联系人进行管理，包括增加、删除、修改、查询联系人信息。开发者还可以通过Picker的方式，拉起联系人列表。

面向所有应用开放如下能力：

- [Contacts Kit开发概述](#contacts-kit开发概述)
    - [能力范围](#能力范围)
    - [使用Picker选择联系人](#使用picker选择联系人)
    - [联系人管理（受限开放）](#联系人管理受限开放)

面向三方应用受限开放如下能力：

> **注意：**
>
> 当前能力受限开放，需要申请受限开放权限ohos.permission.READ_CONTACTS或ohos.permission.WRITE_CONTACTS。该权限通常不允许三方应用申请，仅符合指定场景的应用可申请该权限。申请方式请参见[申请使用受限权限](../security/AccessToken/cj-declare-permissions-in-acl.md)。

- [联系人管理（受限开放）](#联系人管理受限开放)

## 使用Picker选择联系人

当用户选择联系人的时候，通过Picker的方式，拉起联系人列表，引导用户完成界面操作，接口本身无需申请权限。

1. 导入相关的联系人模块。

    ```cangjie
    import kit.ContactsKit.*
    import ohos.base.*
    ```

2. 调用联系人接口，拉起联系人列表，用户点击对应的联系人后返回。

    a. 获取Context。

    ```cangjie
    // main_ability.cj
    import kit.UIKit.AppLog
    import kit.ArkUI.WindowStage
    import kit.AbilityKit.*
    var globalAbilityContext: Option<UIAbilityContext> = Option<UIAbilityContext>.None

    class MainAbility <: UIAbility {
        public init() {
            super()
            registerSelf()
        }

        public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
            AppLog.info("MainAbility OnCreated.${want.abilityName}")
            // 获取context
            globalAbilityContext = this.context
            match (launchParam.launchReason) {
                case LaunchReason.START_ABILITY => AppLog.info("START_ABILITY")
                case _ => ()
            }
        }
        public override func onWindowStageCreate(windowStage: WindowStage): Unit {
            AppLog.info("MainAbility onWindowStageCreate.")
            windowStage.loadContent("EntryView")
        }
        // ...
    }
    ```

    b. 选择联系人。

    ```cangjie
    // 回调函数
    let callback = { errorCode: Option<AsyncError>, data: Option<Array<Contact>> => match (errorCode) {
        case Some(e) =>
            AppLog.error("selectContacts error: ${e.code}")
        case _ => match (data) {
            case Some(contacts) =>
                AppLog.info("selectContacts: ${contacts.size} contacts selected!")
            case _ =>
                AppLog.error("selectContacts： None contacts returned, error: 0")
        }
    }}
    // 选择联系人
    selectContacts(globalAbilityContext.getOrThrow(), callback, options: ContactSelectOptions(isMultiSelect: false))
    ```

3. 完成操作，通过callback返回想要的data数据。