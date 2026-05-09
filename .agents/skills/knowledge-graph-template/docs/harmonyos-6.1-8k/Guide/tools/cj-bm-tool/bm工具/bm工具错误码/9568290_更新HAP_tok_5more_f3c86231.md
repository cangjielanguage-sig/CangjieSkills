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

<!--Del-->

### 9568291 singleton不一致导致安装失败

**错误信息**

error: install failed due to singleton not same.

**错误描述**

应用更新时，应用已安装的HAP包和更新包app.json5配置文件中singleton配置不一致。

**可能原因**

应用已安装的HAP包和更新包app.json5配置文件中singleton配置不一致。

**处理步骤**

方案1：卸载已安装的应用包，再安装新的应用包。

方案2：更新包调整singleton配置，与已安装包配置一致，重新打包，再更新应用包。<!--DelEnd-->

<!--Del-->

### 9568294 应用类别不一致导致的安装失败

**错误信息**

error: install failed due to apptype not same.

**错误描述**

应用安装时，应用已安装HAP包和待安装HAP包的签名文件中[app-feature](https://docs.openharmony.cn/pages/v4.1/zh-cn/application-dev/security/app-provision-structure.md)配置不一致，导致安装失败。

**可能原因**

应用已安装HAP包和待安装HAP包包名一致，但签名文件中app-feature配置不一致。

**处理步骤**

- 方案1：卸载已安装的HAP包，再安装新的HAP包。
- 方案2：修改待安装HAP包的签名文件中的app-feature字段，确保与已安装包配置一致，重新打包、[签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing)，再重试安装。<!--DelEnd-->

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

- 场景二：对于需要运行在OpenHarmony设备上的应用，请确认runtimeOS已改为OpenHarmony。

### 9568300 应用模块名不唯一导致安装失败

**错误信息：**

error: moduleName is not unique.

**错误描述：**

多模块应用安装过程中，由于模块命名冲突，模块唯一性校验失败，导致安装失败。

**可能原因：**

多模块应用安装过程中，存在模块名称冲突。

**处理步骤：**

查看当前应用所有模块名，与各个模块的module.json5中的name进行比较，保证不一致后，重新打包，进行应用安装。