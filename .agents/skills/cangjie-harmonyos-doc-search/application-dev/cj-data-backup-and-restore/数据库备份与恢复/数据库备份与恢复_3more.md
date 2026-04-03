# 数据库备份与恢复

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

## 场景介绍

当应用在处理一项重要的操作时不能被打断，例如：写入多个表关联的事务。此时，每个表的写入都是单独的，但是表与表之间的事务关联性不能被分割。

如果操作的过程中出现问题，开发者可以使用恢复功能，将数据库恢复到之前的状态，重新对数据库进行操作。

在数据库被篡改、删除、或者设备断电场景下，数据库可能会因为数据丢失、数据损坏、脏数据等而不可用，可以通过数据库的备份恢复能力将数据库恢复至可用状态。

键值型数据库和关系型数据库均支持对数据库的备份和恢复。另外，键值型数据库还支持删除数据库备份，以释放本地存储空间。

## 键值型数据库备份、恢复与删除

键值型数据库，通过backup接口实现数据库备份，通过restore接口实现数据库恢复，通过deletebackup接口删除数据库备份。具体接口及功能，请参见[分布式键值数据库](../reference/ArkData/cj-apis-distributed_kv_store.md)。

1. 创建数据库。

    a. 获取context。

    <!-- compile -->

    ```cangjie
    // main_ability.cj
    import kit.PerformanceAnalysisKit.Hilog
    import kit.AbilityKit.{UIAbility, Want, LaunchParam, LaunchReason, UIAbilityContext}

    var globalAbilityContext: Option<UIAbilityContext> = Option<UIAbilityContext>.None

    class MainAbility <: UIAbility {
        public init() {
            super()
            registerSelf()
        }

        public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
            // 获取context
            globalAbilityContext = this.context

            match (launchParam.launchReason) {
                case LaunchReason.StartAbility => Hilog.info(0, "cangjie", "StartAbility")
                case _ => ()
            }
        } 
        // ...
    }
    ```

    b. 创建kvStore。

    为实现创建kvStore功能，需要导入如下包：

    <!-- compile -->

    ```cangjie
    // xxx.cj
    import kit.ArkData.*
    import kit.PerformanceAnalysisKit.Hilog
    import ohos.business_exception.BusinessException
    ```

    实现创建kvStore功能的核心代码是：

    <!-- compile -->

    ```cangjie
    var kvManager: Option<KVManager> = Option<KVManager>.None
    var kvStore: Option<SingleKVStore> = Option<SingleKVStore>.None

    try {
        // 1. 创建kvManager
        let kvManagerConfig = KVManagerConfig(globalAbilityContext.getOrThrow(), "com.example.datamanagertest")
        kvManager = DistributedKVStore.createKVManager(kvManagerConfig)
        // 2. 配置数据库参数
        let options = KVOptions(
            KVSecurityLevel.S3,
            createIfMissing: true,
            encrypt: true,
            backup: false,
            autoSync: false,
        )
        // 3. 创建kvStore
        kvStore = kvManager.getOrThrow().getKVStore("storeId", options)
    } catch (e: BusinessException) {
        Hilog.error(0, "ErrorCode: ${e.code}", e.message)
    }
   ```

2. 使用put()方法插入数据。

    实现插入数据功能的核心代码是：

    <!-- compile -->

    ```cangjie
    const KEY_TEST_STRING_ELEMENT: String = "key_test_string"
    const VALUE_TEST_STRING_ELEMENT: String = "value_test_string"

    try {
        kvStore.getOrThrow().put(KEY_TEST_STRING_ELEMENT, KVValueType.StringValue(VALUE_TEST_STRING_ELEMENT))
    } catch (e: BusinessException) {
        Hilog.error(0, "ErrorCode: ${e.code}", e.message)
    }
    ```

3. 使用backup()方法备份数据。

    <!-- compile -->

    ```cangjie
    try {
        kvStore.getOrThrow().backup("BK001")
    } catch (e: BusinessException) {
        Hilog.error(0, "ErrorCode: ${e.code}", e.message)
    }
    ```

4. 使用delete()方法删除数据（模拟意外删除、篡改场景）。

    <!-- compile -->

    ```cangjie
    try {
        kvStore.getOrThrow().delete(KEY_TEST_STRING_ELEMENT)
    } catch (e: BusinessException) {
        Hilog.error(0, "ErrorCode: ${e.code}", e.message)
    }
    ```

5. 使用restore()方法恢复数据。

    <!-- compile -->

    ```cangjie
    try {
        kvStore.getOrThrow().restore("BK001")
    } catch (e: BusinessException) {
        Hilog.error(0, "ErrorCode: ${e.code}", e.message)
    }
    ```