### 9568290 更新HAP token失败导致安装失败

**错误信息：**

error: install failed due to update hap token failed.

**错误描述：**

应用安装过程中，更新HAP时，应用token授权失败。

**可能原因：**

应用安装或更新时，调用元能力的更新token接口，接口返回失败。

**处理步骤：**

1. 重启手机后再次尝试安装应用。
2. 重复上述步骤3到5次后依旧安装失败，请导出日志文件提[在线工单](https://developer.huawei.com/consumer/cn/support/feedback/#/)获取帮助。

```bash
hdc file recv /data/log/hilog/
```

### 9568297 由于设备sdk版本较低导致安装失败

**错误信息：**

error: install failed due to older sdk version in the device.

![示例图](./figures/zh-cn_image_0000001635521909.png)

**错误描述：**

在启动调试或运行应用/服务时，安装HAP出现错误，提示“error: install failed due to older sdk version in the device”错误信息。

**可能原因：**

该问题是由于编译打包所使用的SDK版本与设备镜像版本不匹配。

**处理步骤：**

- 场景一：设备上的镜像版本低于编译打包的SDK版本，请更新设备镜像版本。查询设备镜像版本命令：

  ```bash
  hdc shell param get const.ohos.apiversion
  ```

  如果镜像提供的api版本为10，且应用编译所使用的SDK版本也为10，仍出现该报错，可能是由于镜像版本较低，未兼容新版本SDK校验规则，请将镜像版本更新为最新版本。

- 场景二：对于需要运行在HarmonyOS设备上的应用，请确认runtimeOS已改为HarmonyOS。

### 9568300 应用模块名不唯一导致安装失败

**错误信息：**

error: moduleName is not unique.

**错误描述：**

多模块应用安装过程中，由于模块命名冲突，模块唯一性校验失败，导致安装失败。

**可能原因：**

多模块应用安装过程中，存在模块名称冲突。

**处理步骤：**

查看当前应用所有模块名，与各个模块的module.json5中的name进行比较，保证不一致后，重新打包，进行应用安装。

### 9568332 签名不一致导致安装失败

**错误信息：**

error: install sign info inconsistent.

![示例图](./figures/zh-cn_image_0000001635761329.png)

**错误描述：**

在启动调试或运行应用/服务时，安装HAP出现错误，提示“error: install sign info inconsistent”错误信息。

**可能原因：**

1. 设备上已安装的应用与新安装的应用中签名不一致或者多个包（HAP和HSP）之间的签名存在差异。如果在“Edit Configurations”中勾选了“Keep Application Data”（即不卸载应用，直接覆盖安装），并且重新进行了签名，将导致该报错。
2. 如果某个应用被卸载但是保留了数据，那么后面安装相同包名的应用时，需要校验其身份信息的一致性。如果两者的签名信息皆不一致，则会导致该报错。

**处理步骤：**

1. 请卸载设备上已安装的应用，或取消勾选“Keep Application Data”后，重新安装新的应用。
2. 如果是因不同团队提供的HSP导致签名不一致问题，可以采用[集成态HSP](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/integrated-hsp)的方式统一提供HSP；在多HAP包的情况下，必须确保所有HAP包的签名一致。
3. 如果某个应用被卸载但是保留了数据，后面安装相同包名但签名信息不一致的应用时，安装失败。如果出现这种情况，则需要把之前已卸载掉的应用重新安装之后，执行不保留数据地卸载，这样相同包名但签名信息不一致的应用才能安装成功。