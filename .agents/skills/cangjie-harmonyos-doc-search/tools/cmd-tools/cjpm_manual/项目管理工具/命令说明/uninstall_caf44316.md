### uninstall

`uninstall` 用于卸载仓颉项目，清除对应的可执行文件和依赖文件。

`uninstall` 需要配置参数 `name`，以卸载名为 `name` 的产物，配置多个 `name` 时会依次删除。`uninstall` 可以通过 `--root <value>` 指定卸载的可执行文件路径，不配置时 `Linux` / `macOS` 系统下默认为 `$HOME/.cjpm`，`Windows` 系统下默认为 `%USERPROFILE%/.cjpm`，配置时将会卸载安装于 `value/bin` 的产物和安装于 `value/libs` 的依赖。

> **注意：**
>
> `cjpm` 在 `Windows` 平台暂不支持在中文路径下使用，如果遇到问题，请通过修改目录名规避。