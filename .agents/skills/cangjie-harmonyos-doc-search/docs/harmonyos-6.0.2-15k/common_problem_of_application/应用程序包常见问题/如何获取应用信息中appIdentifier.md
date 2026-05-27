## 如何获取应用信息中appIdentifier

1. 可以调用[bundleManager.getBundleInfoForSelf](../../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-bundle_manager.md#static-func-getbundleinfoforselfint32)获取自身的BundleInfo应用包信息，应用包信息中包含signatureInfo签名信息，签名信息中包含appIdentifier信息。

    ```cangjie
    import ohos.base.*
    import kit.AbilityKit.*

    let bundleFlags =  GET_BUNDLE_INFO_WITH_APPLICATION.getValue() | GET_BUNDLE_INFO_WITH_SIGNATURE.getValue()
    try {
        let res = BundleManager.getBundleInfoForSelf(bundleFlags)
        let appIdentifier = res.signatureInfo.appIdentifier
        AppLog.info("getBundleInfoForSelf successfully, appIdentifier: ${appIdentifier}")
    } catch (e: BusinessException)  {
        AppLog.error("Failed to getBundleInfoForSelf. Code is ${e.code}, message is ${e.message}")
    }
    ```

2. 通过[bm工具](../../tools/cj-bm-tool.md#bm工具)获取。

    ```shell
    hdc shell
    # 需将com.example.myapplication替换为实际应用的包名
    bm dump -n com.example.myapplication | grep appIdentifier
    ```

    ![alt text](figures/get_appIdentifier.png)