## 接口说明

应用故障恢复接口由appRecovery模块提供，开发者可以通过import引入，详情请参见[开发示例](#开发示例)。

### 应用恢复接口功能介绍

| 接口名称                                                       | 说明                                                 |
| ------------------------------------------------------------ | ---------------------------------------------------- |
| enableAppRecovery(restart!: RestartFlag = ALWAYS_RESTART,saveOccasion!: SaveOccasionFlag = SAVE_WHEN_ERROR, saveMode!: SaveModeFlag = SAVE_WITH_FILE): Unit<sup>18</sup> | 使能应用恢复功能，参数按顺序填入。该接口调用后，应用从启动器启动时第一个Ability支持恢复。|
| saveAppState(context!: ?UIAbilityContext = None): Bool<sup>12+</sup> | 主动保存当前应用中支持恢复的Ability的状态。 |
| restartApp(): Unit<sup>12+</sup> | 重启当前进程，并拉起应用启动时第一个Ability，如果该Ability存在已经保存的状态，这些状态数据会在Ability的OnCreate生命周期回调的want参数中作为wantParam属性传入。|
| setRestartWant(want: Want): Unit<sup>12+</sup> | 设置下次恢复主动拉起场景下的Ability。该Ability必须为当前包下的Ability。|

由于上述接口可能在故障处理时使用，所以不会返回异常，需要开发者熟悉使用的场景。

**enableAppRecovery：** 需要在应用初始化阶段调用，比如AbilityStage的OnCreate调用。具体其各参数定义详情请参见[参数说明](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-enableapprecoveryrestartflag-saveoccasionflag-savemodeflag)

**saveAppState：** 调用后框架会回调当前进程中所有支持恢复的Ability的onSaveState方法。如果在onSaveState方法中同意保存数据，则会将相关数据及Ability的页面栈持久化到应用的本地缓存。如果需要保存指定Ability，则需要指定Ability对应的Context。

**setRestartWant：** 指定由appRecovery发起重启的Ability。

**restartApp：** 调用后框架会杀死当前应用进程，并重新拉起由**setRestartWant**指定的Ability，其中启动原因为APP_RECOVERY。未使用**setRestartWant**指定Ability的场景，会拉起最后一个支持恢复且在前台的Ability，如果当前前台的Ability不支持恢复，则应用表现闪退。如果重启的Ability存在已经保存的状态，这些状态数据会在Ability的OnCreate生命周期回调的want参数中作为wantParam属性传入。两次重启的间隔应大于一分钟，一分钟之内重复调用此接口只会退出应用不会重启应用。自动重启的行为与主动重启一致。