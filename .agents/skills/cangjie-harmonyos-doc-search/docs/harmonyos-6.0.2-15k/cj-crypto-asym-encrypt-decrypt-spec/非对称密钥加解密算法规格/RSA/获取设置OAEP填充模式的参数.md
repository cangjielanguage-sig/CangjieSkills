### 获取/设置OAEP填充模式的参数

从API版本12开始支持RSA使用PKCS1_OAEP填充模式时，获取、设置相关参数，“√”表示支持对获取或设置该参数。

| OAEP参数 | 枚举值 | 获取 | 设置 |
| -------- | -------- | -------- | -------- |
| md | OAEP_MD_NAME_STR | √ | - |
| mgf | OAEP_MGF_NAME_STR | √ | - |
| mgf1_md | OAEP_MGF1_MD_STR | √ | - |
| pSource | OAEP_MGF1_PSRC_UINT8ARR | √ | √ |