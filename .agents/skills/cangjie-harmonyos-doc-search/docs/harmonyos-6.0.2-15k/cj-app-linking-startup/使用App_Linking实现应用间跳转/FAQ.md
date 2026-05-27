## FAQ

### 应用的module.json5文件skills设置不正确，如何处理？

检查"host"字段中应用所对应的域名是否设置正确。

### 开发者网站服务器配置不正确，如何处理？

* 检查服务器的JSON配置，并确保appIdentifier的值正确无误。
* 检查applinking.json是否放置在正确的目录（.well-known）下，通过浏览器等方式访问该json文件的地址：`https://*your.domain.name*/.well-known/applinking.json`，确保能正常访问。

### 系统尚未完成域名校验，如何处理？

按照以下步骤排查：

1. 在设备上安装应用，需等待至少20秒，以确保系统完成域名校验的流程。
2. 系统进行域名校验时，如存在断网、弱网等情况，可能导致域名校验失败，域名校验失败后，系统将在24小时内重新进行域名校验。

### 如何确认域名校验是否成功？

如需查看应用域名验证结果，请在Deveco Studio中打开终端，并使用以下命令查询验证结果：

```text
hdc shell hidumper -s AppDomainVerifyManager
```

运行hidumper命令后，即可在控制台上看到success消息。

```text
BundleName:
  appIdentifier:123456789
   domain verify status:
    https://www.example.com:success
```

* 如果您看到client-error消息，请按照以下步骤排查：
    1. 检查消息中的appIdentifier是否与AGC控制台的appid一致。
    2. 检查AGC控制台配置的域名发布是否成功。
* 如果您看到http\_unknown消息，请确保设备可以访问网络，并重新安装应用。
* 如果您看到其他消息，请联系[技术支持](https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/support)获取帮助。

### 设备首次启动，若无法通过AppLinking拉起系统预装应用，如何处理？

设备首次启动后，系统将在20分钟内尝试对预装应用进行域名校验，若在20分钟内设备一直无法访问网络，则可能导致预装应用域名校验失败。若出现此类问题，请重启手机，或者等待24小时后重试。系统将在下次开机或24小时后对预装应用重新尝试进行域名校验。

### 访问CDN时发现内容未及时更新，如何处理？

CDN缓存时间为10分钟，请您耐心等待一段时间后再次访问。

### 应用和域名的对应关系如何？

应用和域名的关系是多对多的关系：一个应用可以关联多个不同的域名，同样地，一个域名也可以关联多个不同的应用。

### 如果同一域名关联了多个应用，那么该域名的链接将拉起哪个应用？

开发者可以通过配置applinking.json以关联多个应用。如果每个应用的module.json5的uris字段配置的都是一样的，那么系统将弹出列表框供用户选择要拉起的目标应用。 为了更好的体验，开发者也可以通过链接的path去区分拉起的目标应用，如链接`https://www.example.com/path1`拉起目标应用1，链接`https://www.example.com/path2`拉起目标应用2。