### 获取版本信息

```bash
hdc shell uitest --version
```

### 拉起uitest测试进程

```shell
hdc shell uitest start-daemon
```

> **说明**
>
> 设备需调成开发者模式。
>
> 仅由aa test命令拉起的进程才具备调用UITest接口的能力；例如由aa start所拉起的Ability在调用UITest接口时将报错。
>
> 测试hap的[APL等级级别](../security/AccessToken/cj-app-permission-mgmt-overview.md#权限机制中的基本概念)需为system_basic、normal。