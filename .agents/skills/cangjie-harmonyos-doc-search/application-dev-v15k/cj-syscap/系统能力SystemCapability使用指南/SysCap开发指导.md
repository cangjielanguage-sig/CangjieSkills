## SysCap开发指导

### 加入自定义syscap

在某具体的设备型号上，能力可能超出工程默认设备定义的能力集范围，如果需要使用此部分能力，需要额外配置自定义的syscap。

请在DevEco Studio工程的模块/src/main目录下，手动创建syscap.json文件。如在entry/src/main目录右键，点击New > File。

![image-New-File](./figures/image-New-File.png)

新建文件命名为syscap.json。打开新建的syscap.json文件。

![image-SysCap-Json](./figures/image-SysCap-Json.png)

按如下格式填入所需要使用的SysCaps。以使用NFC能力为例，syscap.json文件示例如下。

```text
{
  "devices": {
    "general": [
      // 每一个典型设备对应一个syscap支持能力集，可配置多个典型设备，应与工程所选择的设备一致
      "phone"
    ]
  },
  "development": {
    // addedSysCaps内的sycap集合与devices中配置的各设备支持的syscap集合的并集共同构成联想能力集。
    "addedSysCaps": [
      "SystemCapability.Communication.NFC.Core",
      "SystemCapability.Communication.NFC.CardEmulation",
      "SystemCapability.Communication.NFC.Tag"
    ]
  }
}
```

### 单设备应用开发

默认应用的联想能力集，要求系统能力集和设备的支持系统能力集相等，开发者修改要求能力集需要慎重。

![image-Single-device-app-dev-view](figures/image-Single-device-app-dev-view.png)

### 跨设备应用开发

默认应用的联想能力集是多个设备支持能力集的并集，要求能力集则是交集。

![image-Cross-device-app-dev-view](figures/image-Cross-device-app-dev-view.png)

### 判断API是否可以使用

当前提供了Cangjie API用于帮助判断某个API是否可以使用。

```cangjie
import ohos.base.canIUse

if(canIUse("SystemCapability.ArkUI.ArkUI.Full")){
    Hilog.info(0, "SysCap", "支持系统能力SystemCapability.ArkUI.ArkUI.Full")
}else{
    Hilog.info(0, "SysCap", "不支持系统能力SystemCapability.ArkUI.ArkUI.Full")
}
```

### 不同设备相同能力的差异检查

即使是相同的系统能力，在不同的设备下，也会有能力的差异。

```cangjie
import ohos.base.*
import kit.UserAuthenticationKit.*

try {
    let userAuthInstance = getUserAuthInstance(
        AuthParam([], [UserAuthType.PIN], AuthTrustLevel.ATL1),
        WidgetParam("TEST PIN_ATL1", "")
    )
    userAuthInstance.on("result", {u => userAuthInstance.off("result")})
    userAuthInstance.start()
} catch (e: Exception) {
    AppLog.info("auth catch error: ${e.toString()}")
}
```

### 设备间的SysCap差异如何产生的

设备的SysCap因产品解决方案厂商拼装的部件组合不同而不同，整体流程如下图：

![image-SysCap-diff](figures/image-SysCap-diff.png)

1. 一套操作系统源码由可选和必选部件集组成，不同的部件为对外体现的系统能力不同，即部件与 SysCap 之间映射关系。

2. 发布归一化的SDK，API与SysCap之间存在映射关系。

3. 产品解决方案厂商按硬件能力和产品诉求，可按需拼装部件。

4. 产品配置的部件可以是系统部件，也可以是三方开发的私有部件，由于部件与SysCap间存在映射，所有拼装后即可得到该产品的SysCap集合。

5. SysCap集编码生成 PCID (Product Compatibility ID， 产品兼容性标识)，应用开发者可将PCID导入DevEco Studio，解码成SysCap，开发时对设备的SysCap差异做兼容性处理。

6. 部署到设备上的系统参数中包含了SysCap集，系统提供了native的接口和应用接口，可供系统内的部件和应用查询某个SysCap是否存在。

7. 应用开发过程中，应用必要的SysCap将被编码成RPCID（Required Product Compatibility ID），并写入应用安装包中。应用安装时，包管理器将解码RPCID得到应用需要的 SysCap，与设备当前具备的SysCap比较，若应用要求的SysCap都被满足，则安装成功。

8. 应用运行时，可通过canIUse接口查询设备的SysCap，保证在不同设备上的兼容性。