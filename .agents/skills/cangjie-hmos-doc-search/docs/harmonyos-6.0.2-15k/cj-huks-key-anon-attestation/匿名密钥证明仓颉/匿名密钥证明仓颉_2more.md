# 匿名密钥证明（仓颉）

在使用本功能时，需确保网络通畅。

## 开发步骤

1. 确定密钥别名keyAlias，密钥别名最大长度为128字节。

2. 初始化参数集。

    [HuksOptions](../../cj-apis-security_huks/.overview.md)中的properties字段中的参数必须包含[HUKS_TAG_ATTESTATION_CHALLENGE](../../cj-apis-security_huks/.overview.md)属性,可选参数包含[HUKS_TAG_ATTESTATION_ID_VERSION_INFO](../../cj-apis-security_huks/.overview.md)，[HUKS_TAG_ATTESTATION_ID_ALIAS](../../cj-apis-security_huks/.overview.md)属性。

3. 生成非对称密钥，具体请参见[密钥生成](./cj-huks-key-generation-overview.md)。

4. 将密钥别名与参数集作为参数传入[anonAttestKeyItem](../../cj-apis-security_huks/.overview.md)方法中，即可证明密钥。