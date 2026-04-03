# 密钥协商（仓颉）

以协商密钥类型为X25519，并密钥仅在HUKS内使用为例，完成密钥协商。具体的场景介绍及支持的算法规格，请参见[密钥生成支持的算法](./cj-huks-key-generation-overview.md#支持的算法)。

## 开发步骤

### 生成密钥

设备A、设备B各自生成一个非对称密钥，具体请参见[密钥生成](./cj-huks-key-generation-overview.md)或[密钥导入](./cj-huks-key-import-overview.md)。

密钥生成时，可指定参数HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG（可选），用于标识基于该密钥协商出的密钥是否由HUKS管理。

- 当TAG设置为HUKS_STORAGE_ONLY_USED_IN_HUKS时，表示基于该密钥协商出的密钥，由HUKS管理，可保证协商密钥全生命周期不出安全环境。

- 当TAG设置为HUKS_STORAGE_KEY_EXPORT_ALLOWED时，表示基于该密钥协商出的密钥，返回给调用方管理，由业务自行保证密钥安全。

- 若业务未设置TAG的具体值，表示基于该密钥协商出的密钥，可由HUKS管理，也可返回给调用方管理，业务可在后续协商时再选择使用何种方式保护密钥。

### 导出密钥

设备A、B导出非对称密钥对的公钥材料，具体请参见[密钥导出](./cj-huks-export-key.md)。

### 密钥协商

设备A、B分别基于本端私钥和对端设备的公钥，协商出共享密钥。

密钥协商时，可指定参数HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG（可选），用于标识协商得到的密钥是否由HUKS管理。

| 生成 | 协商 | 规格 |
| :-------- | :-------- | :-------- |
| HUKS_STORAGE_ONLY_USED_IN_HUKS | HUKS_STORAGE_ONLY_USED_IN_HUKS | 密钥由HUKS管理 |
| HUKS_STORAGE_KEY_EXPORT_ALLOWED | HUKS_STORAGE_KEY_EXPORT_ALLOWED | 密钥返回给调用方管理 |
| 未指定TAG具体值 | HUKS_STORAGE_ONLY_USED_IN_HUKS | 密钥由HUKS管理 |
| 未指定TAG具体值 | HUKS_STORAGE_KEY_EXPORT_ALLOWED | 密钥返回给调用方管理 |
| 未指定TAG具体值 | 未指定TAG具体值 | 密钥返回给调用方管理 |

协商时指定的TAG值，不可与生成时指定的TAG值冲突。表格中仅列举有效的指定方式。

### 删除密钥

当密钥废弃不用时，设备A、B均需要删除密钥，具体请参见[密钥删除](./cj-huks-delete-key.md)。