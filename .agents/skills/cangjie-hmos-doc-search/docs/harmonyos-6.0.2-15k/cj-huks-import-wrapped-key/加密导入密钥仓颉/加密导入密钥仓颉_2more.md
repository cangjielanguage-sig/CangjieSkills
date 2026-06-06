# 加密导入密钥（仓颉）

以加密导入ECDH密钥对为例，涉及业务侧加密密钥的[密钥生成](./cj-huks-key-generation-overview.md)、[协商](./cj-huks-key-agreement-overview.md)等操作不在本示例中体现。

具体的场景介绍及支持的算法规格，请参见[密钥导入的支持的算法](./cj-huks-key-import-overview.md#支持的算法)。

## 开发步骤

1. 设备A（导入设备）将待导入密钥转换成[HUKS密钥材料格式](./cj-huks-concepts.md#密钥材料格式)To_Import_Key（仅针对非对称密钥，若待导入密钥是对称密钥则可省略此步骤）。

2. 设备B（被导入设备）生成一个加密导入用途的、用于协商的非对称密钥对Wrapping_Key（公钥Wrapping_Pk，私钥Wrapping_Sk），其密钥用途设置为unwrap，导出Wrapping_Key的公钥材料Wrapping_Pk并保存。

3. 设备A使用和设备B同样的算法，生成一个加密导入用途的、用于协商的非对称密钥对Caller_Key（公钥Caller_Pk，私钥Caller_Sk），导出Caller_Key的公钥材料Caller_Pk并保存。

4. 设备A生成一个对称密钥Caller_Kek，该密钥后续将用于加密To_Import_Key。

5. 设备A基于Caller_Key的私钥Caller_Sk和设备B Wrapping_Key的公钥Wrapping_Pk，协商出Shared_Key。

6. 设备A使用Caller_Kek加密To_Import_Key，生成To_Import_Key_Enc。

7. 设备A使用Shared_Key加密Caller_Kek，生成Caller_Kek_Enc。

8. 设备A封装Caller_Pk、Caller_Kek_Enc、To_Import_Key_Enc等加密导入的密钥材料并发送给设备B，加密导入密钥材料格式见[加密导入密钥材料格式](./cj-huks-key-import-overview.md#加密导入密钥材料格式)。

9. 设备B导入封装的加密密钥材料。

10. 设备A、B删除用于加密导入的密钥。