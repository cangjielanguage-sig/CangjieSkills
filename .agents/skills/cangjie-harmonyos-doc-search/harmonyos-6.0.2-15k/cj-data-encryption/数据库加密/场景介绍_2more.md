## 场景介绍

为了增强数据库的安全性，数据库提供了一个安全适用的数据库加密能力，从而对数据库存储的内容实施有效保护。通过数据库加密等安全方法实现了数据库数据存储的保密性和完整性要求，使得数据库以密文方式存储并在密态方式下工作，确保了数据安全。

加密后的数据库只能通过接口进行访问，无法通过其它方式打开数据库文件。数据库的加密属性在创建数据库时确认，无法变更。

键值型数据库和关系型数据库均支持数据库加密操作。

## 键值型数据库加密

键值型数据库，通过options中encrypt参数来设置是否加密，默认为false，表示不加密。encrypt参数为true时表示加密。

具体接口及功能，请参见[分布式键值数据库](../../API_Reference/source_zh_cn/apis/ArkData/cj-apis-distributed_kv_store.md)。

1. 获取context。

    ```cangjie
    // main_ability.cj
    internal import ohos.base.AppLog
    internal import ohos.ability.AbilityStage
    internal import ohos.ability.LaunchReason
    import kit.AbilityKit.{UIAbility, UIAbilityContext, LaunchParam, Want}

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
        // ...
    }
    ```

2. 键值型数据库加密设置。

    ```cangjie
    // xxx.cj
    import kit.ArkData.*
    import kit.UIKit.BusinessException
    import kit.AbilityKit.getStageContext

    try {
        // globalAbilityContext 在Ability onCreate时获取
        let context = globalAbilityContext.getOrThrow()
        let kvManagerConfig = KVManagerConfig(getStageContext(context), "com.example.datamanagertest")
        // 创建KVManager实例
        let kvManager = DistributedKVStore.createKVManager(kvManagerConfig)
        AppLog.info("Succeeded in creating KVManager.")

        let options = KVOptions(
            KVSecurityLevel.S3,
            createIfMissing: true,
            encrypt: true, // 设置数据库加密
            backup: false,
            autoSync: false,
        )
        let kvStore = kvManager.getSingleKVStore("storeId", options)
        AppLog.info("getSingleKVStore success")
    } catch (e: BusinessException) {
        AppLog.error("ErrorCode: ${e.code}, Message: ${e.message}")
    }
    // 进行其它数据库相关的操作
    // ...
    ```