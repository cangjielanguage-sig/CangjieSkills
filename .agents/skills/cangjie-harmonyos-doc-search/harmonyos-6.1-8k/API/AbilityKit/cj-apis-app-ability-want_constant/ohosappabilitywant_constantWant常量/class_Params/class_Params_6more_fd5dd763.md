## class Params

```cangjie
public class Params {
    public static const ABILITY_BACK_TO_OTHER_MISSION_STACK: String = "ability.params.backToOtherMissionStack"
    public static const ABILITY_RECOVERY_RESTART: String = "ohos.ability.params.abilityRecoveryRestart"
    public static const CONTENT_TITLE_KEY: String = "ohos.extra.param.key.contentTitle"
    public static const SHARE_ABSTRACT_KEY: String = "ohos.extra.param.key.shareAbstract"
    public static const SHARE_URL_KEY: String = "ohos.extra.param.key.shareUrl"
    public static const SUPPORT_CONTINUE_PAGE_STACK_KEY: String = "ohos.extra.param.key.supportContinuePageStack"
    public static const SUPPORT_CONTINUE_SOURCE_EXIT_KEY: String = "ohos.extra.param.key.supportContinueSourceExit"
}
```

**功能：** [Want.parameters](./cj-apis-app-ability-want.md#class-want)字段常用的系统预置关键字。开发者可以通过这些预置关键字设置或获取应用跳转等场景中额外携带的参数信息。例如在[UIAbility](./cj-apis-app-ability-ui_ability.md)的启动阶段，如果从onCreate回调的入参want字段中获取到ABILITY_RECOVERY_RESTART的值为true，则表示当前UIAbility发生了故障重启。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22

### static const ABILITY_BACK_TO_OTHER_MISSION_STACK

```cangjie
public static const ABILITY_BACK_TO_OTHER_MISSION_STACK: String = "ability.params.backToOtherMissionStack"
```

**功能：** 表示是否支持跨任务链返回。

该参数用于控制跨任务链返回逻辑，其核心作用是改变用户执行返回键时的应用跳转行为。例如，现有UIAbility A和UIAbility B，前台显示的是UIAbility A，随后系统服务拉起UIAbility B（同时在Want的Params字段配置该参数为true）。如果配置了该参数，当UIAbility B退出时，会返回到UIAbility A（即返回到最近一次的访问任务）；如果未配置该参数，则默认直接返回桌面。

需要注意的是，该字段仅支持系统设置，三方应用传入该字段不生效。

**类型：** String

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22

### static const ABILITY_RECOVERY_RESTART

```cangjie
public static const ABILITY_RECOVERY_RESTART: String = "ohos.ability.params.abilityRecoveryRestart"
```

**功能：** 表示当前Ability是否发生了故障恢复重启。

**类型：** String

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22

### static const CONTENT_TITLE_KEY

```cangjie
public static const CONTENT_TITLE_KEY: String = "ohos.extra.param.key.contentTitle"
```

**功能：** 表示原子化服务分享的标题。

在跨端分享的onShare回调中，开发者可通过该字段设置分享的标题。

**类型：** String

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22

### static const SHARE_ABSTRACT_KEY

```cangjie
public static const SHARE_ABSTRACT_KEY: String = "ohos.extra.param.key.shareAbstract"
```

**功能：** 表示原子化服务分享的内容摘要。

在跨端分享的onShare回调中，开发者可通过该字段设置分享的摘要。

**类型：** String

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22

### static const SHARE_URL_KEY

```cangjie
public static const SHARE_URL_KEY: String = "ohos.extra.param.key.shareUrl"
```

**功能：** 表示原子化服务分享的URL链接。

在跨端分享的onShare回调中，开发者可通过该字段设置分享的URL链接。

**类型：** String

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22