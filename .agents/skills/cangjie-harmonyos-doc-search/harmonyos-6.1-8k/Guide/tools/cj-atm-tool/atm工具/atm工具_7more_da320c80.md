# atm工具

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

Access Token Manager (程序访问控制管理工具，简称atm工具)，是用于查询<!--Del-->或设置<!--DelEnd-->应用进程的权限、使用类型等信息的工具，为开发者提供了根据tokenid、包名、进程名等信息进行访问控制管理的能力。

## 环境说明

在使用本工具前，开发者需要先获取[hdc工具](./cj-hdc.md)，执行hdc shell。

## atm工具命令列表

| 命令    | 描述 |
| ------- | -----------|
| help    | 帮助命令，显示atm支持的命令信息。 |
| <!--DelRow-->perm   | 权限命令，为应用进程授予或取消权限。 |
| <!--DelRow-->toggle | 弹窗开关/权限使用记录开关状态命令，设置或获取权限弹窗/权限使用记录开关状态。 此命令仅在root版本下可用。|
| dump | 查询命令，用于查询访问控制相关数据信息。 |

## 帮助命令

```bash
# 显示帮助信息
atm help
```

<!--Del-->

## 权限命令

```bash
atm perm [-h] [-g -i <token-id> -p <permission-name>] [-c -i <token-id> -p <permission-name>]
```

**权限命令参数列表**

| 参数                                               | 参数说明                  |
| :-------------------------------------------------- | :---------------------- |
| -h                                        | 帮助信息。atm perm支持的命令集合。 |
| -g&nbsp;-i \<token-id>&nbsp;-p \<permission-name> | -g、-i、-p均为必选参数，通过应用进程的tokenid授予指定权限。返回是否成功。    |
| -c&nbsp;-i \<token-id>&nbsp;-p \<permission-name> | -c、-i、-p均为必选参数，通过应用进程的tokenid取消指定权限。返回是否成功。    |

示例：

```bash
# 显示atm perm的帮助信息
atm perm -h

# 为应用进程授予相机权限
atm perm -g -i ********* -p ohos.permission.CAMERA

# 为应用进程取消相机权限
atm perm -c -i ********* -p ohos.permission.CAMERA
```

## 弹窗开关状态命令

```bash
atm toggle [-h] [-r -s -i <user-id> -p <permission-name> -k <status>] [-r -o -i <user-id> -p <permission-name>]
```

**弹窗开关状态命令参数列表**

| 参数                                           | 参数说明                                |
| :------------------------------------------------------- | :----------------------------------- |
| -h                                                     | 帮助信息。              |
| -r&nbsp;-s&nbsp;-i \<user-id>&nbsp;-p \<permission-name>&nbsp;-k \<status> | -r、-s、-i、-p、-k均为必选参数，在指定用户下，设置指定权限的弹窗开关状态为status。返回是否成功。 |
| -r&nbsp;-o&nbsp;-i \<user-id>&nbsp;-p \<permission-name> | -r、-o、-i、-p均为必选参数，在指定用户下，返回指定权限的弹窗开关状态。 |

示例：

```bash
# 显示atm toggle的帮助信息
atm toggle -h

# 设置用户0下相机权限的弹窗开关状态为开启
atm toggle -r -s -i 0 -p ohos.permission.CAMERA -k 1

# 获取用户0下相机权限的弹窗开关状态
atm toggle -r -o -i 0 -p ohos.permission.CAMERA
```

## 权限使用记录开关状态命令

```bash
atm toggle [-h] [-u -s -i <user-id> -k <status>] [-u -o -i <user-id>]
```

**权限使用记录开关状态命令参数列表**

| 参数                                                           | 参数说明                                |
| :----------------------------------------------------------------- | :----------------------------------- |
| -h                                                     | 帮助信息。              |
| -u&nbsp;-s&nbsp;-i \<user-id>&nbsp;-k \<status> | -u、-s、-i、-k均为必选参数，在指定用户下，设置权限使用记录开关状态为status。返回是否成功。 |
| -u&nbsp;-o&nbsp;-i \<user-id>&nbsp; | -u、-o、-i均为必选参数，在指定用户下，返回权限使用记录开关状态。 |

示例：

```bash
# 显示atm toggle的帮助信息
atm toggle -h

# 设置用户0下权限使用记录开关状态为开启
atm toggle -u -s -i 0 -k 1

# 获取用户0下权限使用记录开关状态
atm toggle -u -o -i 0
```

<!--DelEnd-->