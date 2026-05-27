# 证书对象的创建、解析和校验

以校验证书有效性为例，完成证书对象的创建、解析和校验。

## 开发步骤

1. 导入[证书算法库框架模块](../../../API_Reference/source_zh_cn/apis/DeviceCertificateKit/cj-apis-cert.md)。

    ```cangjie
    import kit.DeviceCertificateKit.*
    ```

2. 基于已有的X509证书数据，调用[createX509Cert](../../../API_Reference/source_zh_cn/apis/DeviceCertificateKit/cj-apis-cert.md#func-createx509certencodingblob)创建证书对象。

3. 解析证书的字段信息。
   此处以获取证书版本、证书序列号为例，更多字段信息获取接口请查看[API参考文档](../../../API_Reference/source_zh_cn/apis/DeviceCertificateKit/cj-apis-cert.md#class-x509cert)。

4. 调用[X509Cert.getPublicKey](../../../API_Reference/source_zh_cn/apis/DeviceCertificateKit/cj-apis-cert.md#func-getpublickey)获取证书中的公钥，并调用[X509Cert.verify](../../../API_Reference/source_zh_cn/apis/DeviceCertificateKit/cj-apis-cert.md#func-verifypubkey)校验签名。示例为自验签场景，因此获取的是本证书中的公钥。应用须结合自身场景获取用于验签的公钥。

5. 调用[X509Cert.checkValidityWithDate](../../../API_Reference/source_zh_cn/apis/DeviceCertificateKit/cj-apis-cert.md#func-checkvaliditywithdatestring)校验证书有效期。入参date用于确认此日期是否在X509证书有效期内。

    ```cangjie
    import kit.DeviceCertificateKit.*
    import ohos.base.BusinessException

    // 此处仅为示例的证书二进制数据，需根据业务的不同对证书数据进行赋值。
    let certData = """
            -----BEGIN CERTIFICATE-----
            MIIBLzCB1QIUO/QDVJwZLIpeJyPjyTvE43xvE5cwCgYIKoZIzj0EAwIwGjEYMBYG
            A1UEAwwPRXhhbXBsZSBSb290IENBMB4XDTIzMDkwNDExMjAxOVoXDTI2MDUzMDEx
            MjAxOVowGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYI
            KoZIzj0DAQcDQgAEHjG74yMIueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTa
            tUsU0i/sePnrKglj2H8Abbx9PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEA
            0ce/fvA4tckNZeB865aOApKXKlBjiRlaiuq5mEEqvNACIQDPD9WyC21MXqPBuRUf
            BetUokslUfjT6+s/X4ByaxycAA==
            -----END CERTIFICATE-----
            """

    // 证书示例
    func certSample(): Unit {
        let encodingBlob = EncodingBlob(
            // 将证书数据从string类型转换成Unit8Array。
            certData.toArray(),
            // 证书格式，仅支持PEM和DER。在此示例中，证书为PEM格式。
            EncodingFormat.FORMAT_PEM
        )

        try {
            // 创建X509Cert实例。
            let x509Cert = createX509Cert(encodingBlob)
            // X509Cert实例创建成功。
            AppLog.info('createX509Cert success')

            // 获取证书版本。
            let version = x509Cert.getVersion()
            let serial = x509Cert.getCertSerialNumber()
            AppLog.info('X509 version: ${version} , X509 serial:${serial}')

            // 使用上级证书对象的getPublicKey()方法或本（自签名）证书对象获取公钥对象。
            let pubKey = x509Cert.getPublicKey()
            // 验证证书签名。
            x509Cert.verify(pubKey)
            // 签名验证成功。
            AppLog.info('verify success')

            // 用一个字符串代表时间。
            let date = '20230930000001Z'

            // 验证证书的有效期。
            x509Cert.checkValidityWithDate(date)
        } catch (e: BusinessException) {
            // 签名验证失败。
            AppLog.error("failed, errCode: ${e.code}, errMessage: ${e.message}")
        }
    }
    ```
