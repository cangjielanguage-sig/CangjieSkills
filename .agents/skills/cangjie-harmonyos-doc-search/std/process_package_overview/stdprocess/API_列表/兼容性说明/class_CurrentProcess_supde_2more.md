#### class CurrentProcess <sup>(deprecated)</sup>

> **注意：**
>
> 未来版本即将废弃，可在 std.env 中找到代替功能。

| 成员 |  支持平台 |
| ------------ | ------------ |
| [arguments](./process_package_api/process_package_classes.md#prop-arguments) | `Linux` `Windows` `macOS` |
| [homeDirectory](./process_package_api/process_package_classes.md#prop-homedirectory) | `Linux` `Windows` `macOS` |
| [tempDirectory](./process_package_api/process_package_classes.md#prop-tempdirectory) | `Linux` `Windows` `macOS` |
| [stdIn](./process_package_api/process_package_classes.md#prop-stdin) | `Linux` `Windows` `macOS` |
| [stdOut](./process_package_api/process_package_classes.md#prop-stdout) | `Linux` `Windows` `macOS` |
| [stdErr](./process_package_api/process_package_classes.md#prop-stderr) | `Linux` `Windows` `macOS` |
| [atExit(() -> Unit)](./process_package_api/process_package_classes.md#func-atexit---unit) | `Linux` `Windows` `macOS` |
| [exit(Int64)](./process_package_api/process_package_classes.md#func-exitint64) | `Linux` `Windows` `macOS` |
| [getEnv(String)](./process_package_api/process_package_classes.md#func-getenvstring) | `Linux` `Windows` `macOS` |
| [removeEnv(String)](./process_package_api/process_package_classes.md#func-removeenvstring) | `Linux` `Windows` `macOS` |
| [setEnv(String, String)](./process_package_api/process_package_classes.md#func-setenvstring-string) | `Linux` `Windows` `macOS` |

#### class SubProcess

| 成员 |  支持平台 |
| ------------ | ------------ |
| [stdIn <sup>(deprecated)</sup>](./process_package_api/process_package_classes.md#prop-stdin-deprecated) | `Linux` `Windows` `macOS` |
| [stdInPipe](./process_package_api/process_package_classes.md#prop-stdinpipe) | `Linux` `Windows` `macOS` |
| [stdOut <sup>(deprecated)</sup>](./process_package_api/process_package_classes.md#prop-stdout-deprecated) | `Linux` `Windows` `macOS` |
| [stdOutPipe](./process_package_api/process_package_classes.md#prop-stdoutpipe) | `Linux` `Windows` `macOS` |
| [stdErr <sup>(deprecated)</sup>](./process_package_api/process_package_classes.md#prop-stderr-deprecated) | `Linux` `Windows` `macOS` |
| [stdErrPipe](./process_package_api/process_package_classes.md#prop-stderrpipe) | `Linux` `Windows` `macOS` |
| [wait(Duration)](./process_package_api/process_package_classes.md#func-waitduration) | `Linux` `Windows` `macOS` |
| [waitOutput()](./process_package_api/process_package_classes.md#func-waitoutput) | `Linux` `Windows` `macOS` |