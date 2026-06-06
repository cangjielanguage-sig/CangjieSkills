# 签名/验签介绍及算法规格

为实现数据完整性保护和防抵赖，可使用生成/导入的密钥，对数据进行签名验签操作。

## 支持的算法

以下为密钥签名/验签支持的规格说明。

### 标准设备规格

| 算法/摘要算法/填充模式 | 备注 | API级别 |
| :-------- | :-------- | :-------- |
| RSA/SHA256/PKCS1_V1_5<br/>RSA/SHA384/PKCS1_V1_5<br/>RSA/SHA512/PKCS1_V1_5<br/>RSA/SHA256/PSS<br/>RSA/SHA384/PSS<br/>RSA/SHA512/PSS | 对于PSS模式，salt长度支持设置为摘要长度和最大长度（最大长度=密钥长度-摘要长度-2），对应枚举值详见[HuksRsaPssSaltLenType](../../../API_Reference/source_zh_cn/apis/UniversalKeystoreKit/cj-apis-security_huks.md#class-huksrsapsssaltlentype)。 | 15+ |
| RSA/NoDigest/PKCS1_V1_5 | NoDigest需要指定TAG HuksKeyDigest.HUKS_DIGEST_NONE。由业务对明文做哈希，再将哈希后的数据传入，哈希后的数据长度必须满足RSA签名验签支持的摘要算法规格。 | 15+ |
| ECC/SHA256<br/>ECC/SHA384<br/>ECC/SHA512 | ECC算法支持的椭圆曲线函数包括：P-256、P-384、P-521。 | 15+ |
| ED25519/NoDigest | NoDigest需要指定TAG HuksKeyDigest.HUKS_DIGEST_NONE。 | 15+ |
| SM2/SM3 | - | 15+ |

### 轻设备设备规格

| 算法/摘要算法/填充模式 | 备注 | API级别 |
| :-------- | :-------- | :-------- |
| RSA/SHA256/PKCS1_V1_5 | - | 15+ |
| RSA/SHA256/PSS | - | 15+ |
| RSA/SHA1/ISO_IEC_9796_2 | 数据最小长度=密钥长度-21字节 | 15+ |
