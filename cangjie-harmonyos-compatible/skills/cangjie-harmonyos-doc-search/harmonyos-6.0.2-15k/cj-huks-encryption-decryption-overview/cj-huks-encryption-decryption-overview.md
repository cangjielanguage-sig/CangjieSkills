# 加密/解密介绍及算法规格

在HUKS中已经有密钥，需要对一段数据加密或是解密，均可以使用HUKS完成加密/解密操作。

## 支持的算法

以下为密钥加密/解密支持的规格说明。

### 标准设备规格

| 算法/分组模式/填充模式 | 备注 | API级别 |
| :-------- | :-------- | :-------- |
| AES/CBC/NoPadding<br/>AES/CBC/PKCS7<br/>AES/CTR/NoPadding | IV参数必选；CBC模式下，若填充模式选择为NoPadding，因为该模式下要求明文数据必须按照固定长度的块进行加密，如果输入的数据长度不是16的倍数，就需要业务方自行填充，以满足块长度的要求。 | 15+ |
| AES/GCM/NoPadding | 加密：Nonce参数必选。<br/>解密：Nonce、TAG参数必选。 | 15+ |
| RSA/ECB/NoPadding<br/>RSA/ECB/PKCS1_V1_5<br/>RSA/ECB/OAEP | OAEP填充模式支持的摘要算法：SHA256/SHA384/SHA512。 | 15+ |
| SM4/CTR/NoPadding<br/>SM4/CBC/NoPadding<br/>SM4/CFB/NoPadding | IV 参数必选。 | 15+ |
| SM4/OFB/NoPadding | Nonce 参数必选。 | 15+ |
| SM2/-/NoPadding | 摘要算法SM3。 | 15+ |

### 轻量级设备规格

| 算法/分组模式/填充模式 | 备注 | API级别 |
| :-------- | :-------- | :-------- |
| AES/GCM/NoPadding | 加密：Nonce参数必选。<br/>解密：Nonce、TAG参数必选。 | 15+ |
| AES/CBC/NoPadding<br/>AES/CTR/NoPadding | IV参数必选。 | 15+ |
| DES/ECB/NoPadding | - | 15+ |
| DES/CBC/NoPadding | IV参数必选。 | 15+ |
| 3DES/ECB/NoPadding | - | 15+ |
| 3DES/CBC/NoPadding | IV参数必选。 | 15+ |
| RSA/ECB/NoPadding | - | 15+ |
| RSA/ECB/PKCS1_V1_5 | - | 15+ |
| RSA/ECB/OAEP | 摘要算法SHA256。 | 15+ |
