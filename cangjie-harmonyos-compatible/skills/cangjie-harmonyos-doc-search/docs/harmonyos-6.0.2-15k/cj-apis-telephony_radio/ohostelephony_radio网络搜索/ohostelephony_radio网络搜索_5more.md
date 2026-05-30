# ohos.telephony_radio（网络搜索）

网络搜索模块提供管理网络搜索的一些基础功能，包括获取当前接入的CS域和PS域无线接入技术、获取网络状态、获取当前选网模式、获取注册网络所在国家的ISO国家码、获取主卡所在卡槽的索引号、获取指定SIM卡槽对应的注册网络信号强度信息列表、获取运营商名称，判断当前设备是否支持NR(New Radio)、判断主卡的Radio是否打开等。

## 导入模块

```cangjie
import kit.TelephonyKit.*
```

## 权限列表

ohos.permission.GET_NETWORK_INFO

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## class NetworkRadioTech

```cangjie
public class NetworkRadioTech {
    public NetworkRadioTech(
        public let psRadioTech: RadioTechnology,
        public let csRadioTech: RadioTechnology
    )
}
```

**功能：** 网络中packet service (PS)和circuit service(CS)无线接入技术。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

### let csRadioTech

```cangjie
public let csRadioTech: RadioTechnology
```

**功能：** CS无线接入技术。

**类型：** [RadioTechnology](#enum-radiotechnology)

**读写能力：** 只读

**起始版本：** 19

### let psRadioTech

```cangjie
public let psRadioTech: RadioTechnology
```

**功能：** PS无线接入技术。

**类型：** [RadioTechnology](#enum-radiotechnology)

**读写能力：** 只读

**起始版本：** 19

### NetworkRadioTech(RadioTechnology, RadioTechnology)

```cangjie
public NetworkRadioTech(
    public let psRadioTech: RadioTechnology,
    public let csRadioTech: RadioTechnology
)
```

**功能：** 构造NetworkRadioTech实例。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|psRadioTech|[RadioTechnology](#enum-radiotechnology)|是|-|PS无线接入技术。|
|csRadioTech|[RadioTechnology](#enum-radiotechnology)|是|-|CS无线接入技术。|