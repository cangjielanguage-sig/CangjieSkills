# 证书扩展信息对象的创建、解析和校验

以获取证书指定OID域段，并判断是否为CA证书为例，完成证书扩展信息对象的创建、解析和校验。

## 开发步骤

1. 导入[证书算法库框架模块](../../../API_Reference/source_zh_cn/apis/DeviceCertificateKit/cj-apis-cert.md)。

    ```cangjie
    import kit.DeviceCertificateKit.*
    ```

2. 解析证书扩展域段数据，调用[createCertExtension](../../../API_Reference/source_zh_cn/apis/DeviceCertificateKit/cj-apis-cert.md#func-createcertextensionencodingblob)创建证书扩展域段对象。

3. 调用[CertExtension.getEntry](../../../API_Reference/source_zh_cn/apis/DeviceCertificateKit/cj-apis-cert.md#func-getentryextensionentrytype-datablob)获取指定OID证书扩展域段信息。比如，证书扩展域段对象标识符列表，根据对象标识符获取具体数据等。

4. 调用[CertExtension.checkCA](../../../API_Reference/source_zh_cn/apis/DeviceCertificateKit/cj-apis-cert.md#func-checkca)判断证书是否为CA证书。

    ```cangjie
    import kit.DeviceCertificateKit.*
    import ohos.base.BusinessException

    // 证书扩展数据，以下只是一个示例。需要根据具体业务来赋值。
    let extData: Array<UInt8> = [0x30, 0x40, 0x30, 0x0F, 0x06, 0x03, 0x55, 0x1D, 0x13, 0x01, 0x01, 0xFF, 0x04, 0x05, 0x30,
        0x03, 0x01, 0x01, 0xFF, 0x30, 0x0E, 0x06, 0x03, 0x55, 0x1D, 0x0F, 0x01, 0x01, 0xFF, 0x04, 0x04, 0x03, 0x02, 0x01,
        0xC6, 0x30, 0x1D, 0x06, 0x03, 0x55, 0x1D, 0x0E, 0x04, 0x16, 0x04, 0x14, 0xE0, 0x8C, 0x9B, 0xDB, 0x25, 0x49, 0xB3,
        0xF1, 0x7C, 0x86, 0xD6, 0xB2, 0x42, 0x87, 0x0B, 0xD0, 0x6B, 0xA0, 0xD9, 0xE4]

    // 证书扩展示例
    func certExtensionSample(): Unit {
        let encodingBlob = EncodingBlob(
            extData.toArray(),
            // 证书扩展格式，目前仅支持DER格式。
            EncodingFormat.FORMAT_DER
        )

        var ext: CertExtension
        // 创建一个证书扩展实例。
        try {
            ext = createCertExtension(encodingBlob)
        } catch (e: BusinessException) {
            // 证书扩展实例创建失败。
            AppLog.error('createCertExtension failed, errCode:${e.code}, errMsg:${e.message}')
            return
        }
        // 证书扩展实例创建成功。
        AppLog.info('createCertExtension success')

        try {
            // 根据OID获取证书扩展信息。
            let entry = ext.getEntry(ExtensionEntryType.EXTENSION_ENTRY_TYPE_ENTRY, DataBlob("demo_str".toArray())).data
            // 检查证书是否为CA证书。
            let ca = ext.checkCA()
            AppLog.info('test cert extension success');
        } catch (e: BusinessException) {
            AppLog.error('operation failed, message:${e.message} ,code:${e.code}')
        }
    }
    ```
