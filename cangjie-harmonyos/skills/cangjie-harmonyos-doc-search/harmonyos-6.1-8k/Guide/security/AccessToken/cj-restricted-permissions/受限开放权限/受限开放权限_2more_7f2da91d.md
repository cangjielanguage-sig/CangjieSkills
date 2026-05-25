# 受限开放权限

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

## 申请方式

<!--RP1-->

以下权限的开放范围为普通应用，但需要通过[访问控制列表（ACL）](./cj-app-permission-mgmt-overview.md#权限机制中的基本概念)的方式跨级别申请。

normal等级的应用需要将自身的APL等级声明为system_basic及以上，在开发应用安装包时，需要修改应用的HarmonyAppProvision配置文件即SDK目录下的“`Toolchains / _{Version} _/ lib / UnsgnedReleasedProfileTemplate.json`”文件，并重新进行应用签名。

**修改方式：**

HarmonyAppProvision配置文件示例如下所示，修改"bundle-info" &gt; "apl" 字段。

```json
"bundle-info" : {
    // ...
    "apl": "system_basic",
    // ...
},
```

> **说明：**
>
> 直接修改HarmonyAppProvision配置文件的方式，仅用于应用调试阶段使用，不可用于发布上架应用市场。如果需要开发商用版本的应用，请在对应的应用市场进行发布证书和Profile文件的申请。

<!--RP1End-->