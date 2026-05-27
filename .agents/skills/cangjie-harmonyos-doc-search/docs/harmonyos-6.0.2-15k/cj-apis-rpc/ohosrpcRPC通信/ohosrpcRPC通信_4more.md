# ohos.rpc（RPC通信）

本模块提供进程间通信能力，包括设备内的进程间通信（IPC）和设备间的进程间通信（RPC），前者基于Binder驱动，后者基于软总线驱动。

## 导入模块

```cangjie
import kit.IPCKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## interface IRemoteBroker

```cangjie
public interface IRemoteBroker {
    func asObject(): IRemoteObject
}
```

**功能：** 远端对象的代理持有者。用于获取代理对象。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

### func asObject()

```cangjie
func asObject(): IRemoteObject
```

**功能：** 需派生类实现，获取代理或远端对象。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[IRemoteObject](#interface-iremoteobject)|如果调用者是RemoteObject对象，则直接返回本身；如果调用者是[RemoteProxy](#class-remoteproxy)对象，则返回它的持有者[IRemoteObject](#interface-iremoteobject)。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.IPCKit.*

// 此处代码可添加在依赖项定义中
class TestAbility <: IRemoteBroker {
    let remote: IRemoteObject
    init(remote: IRemoteObject) {
        this.remote = remote
    }
    public func asObject(): IRemoteObject {
        return this.remote
    }
}
```