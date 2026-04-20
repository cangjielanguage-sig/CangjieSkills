## 如何获取应用信息中appIdentifier

- 可以调用[bundleManager.getBundleInfoForSelf](../../reference/AbilityKit/cj-apis-bundle_manager.md#static-func-getbundleinfoforselfint32)获取自身的BundleInfo应用包信息，应用包信息中包含signatureInfo签名信息，签名信息中包含appIdentifier信息。

    <!-- compile -->

    ```cangjie
    import kit.AbilityKit.*
    import ohos.business_exception.BusinessException
    import ohos.hilog.Hilog

    let bundleFlags =  BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION | BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO
    try {
        let res = BundleManager.getBundleInfoForSelf(bundleFlags)
        let appIdentifier = res.signatureInfo.appIdentifier
        Hilog.info(1, "1", "info", "getBundleInfoForSelf successfully, appIdentifier: ${appIdentifier}")
    } catch (e: BusinessException)  {
        Hilog.error(1, "info", "Failed to getBundleInfoForSelf. Code is ${e.code}, message is ${e.message}")
    }
    ```

- 通过[bm工具](../../tools/cj-bm-tool.md)获取。

    ```shell
    hdc shell
    # 需将com.example.myapplication替换为实际应用的包名
    bm dump -n com.example.myapplication | grep appIdentifier
    ```

    ![alt text](figures/get_appIdentifier.png)

## 什么是appId

appId是应用的唯一标识，由包名、下划线和证书公钥的Base64编码组成。由于appId和签名信息相关，如果签名证书的公钥更换，appId也会跟随变化，所以应用的唯一标识推荐使用[appIdentifier](#什么是appidentifier)。

## 如何获取应用信息中的appId

- 可以调用[bundleManager.getBundleInfoForSelf](../../reference/AbilityKit/cj-apis-bundle_manager.md#static-func-getbundleinfoforselfint32)获取自身的BundleInfo应用包信息，应用包信息中包含signatureInfo签名信息，签名信息中包含appIdentifier信息。

    <!-- compile -->

    ```cangjie
    import kit.AbilityKit.*
    import ohos.business_exception.BusinessException
    import ohos.hilog.Hilog

    let bundleFlags =  BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION | BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO
    try {
        let res = BundleManager.getBundleInfoForSelf(bundleFlags)
        let appId = res.signatureInfo.appId
        Hilog.info(1, "1", "info", "getBundleInfoForSelf successfully, appId: ${appId}")
    } catch (e: BusinessException)  {
        Hilog.error(1, "info", "Failed to getBundleInfoForSelf. Code is ${e.code}, message is ${e.message}")
    }
    ```


- 通过[bm工具](../../tools/cj-bm-tool.md)获取。

    ```shell
    hdc shell
    # 需将com.example.myapplication替换为实际应用的包名
    bm dump -n com.example.myapplication |grep '"appId":'
    ```
    ![alt text](figures/get_appId.png)