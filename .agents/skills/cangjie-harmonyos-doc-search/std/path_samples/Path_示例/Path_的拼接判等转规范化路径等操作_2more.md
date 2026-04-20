## Path 的拼接、判等、转规范化路径等操作

代码如下：
<!-- verify -->

```cangjie
import std.fs.*

main() {
    let dirPath: Path = Path("./a/b/c")
    if (!exists(dirPath)) {
        Directory.create(dirPath, recursive: true)
    }

    let filePath: Path = dirPath.join("d.cj") // ./a/b/c/d.cj
    if (filePath == Path("./a/b/c/d.cj")) {
        println("filePath.join: success")
    }
    if (!exists(filePath)) {
        File.create(filePath).close()
    }

    let curCanonicalizedPath: Path = canonicalize(Path("."))
    let fileCanonicalizedPath: Path = canonicalize(Path("././././a/./../a/b/../../a/b/c/.././../../a/b/c/d.cj"))
    if (fileCanonicalizedPath == canonicalize(filePath) && fileCanonicalizedPath.toString() ==
        curCanonicalizedPath.toString() + "/a/b/c/d.cj") {
        println("canonicalize filePath: success")
    }

    remove(dirPath, recursive: true)
    return 0
}
```

运行结果：

```text
filePath.join: success
canonicalize filePath: success
```

## 通过 Path 创建文件和目录

代码如下：
<!-- verify -->

```cangjie
import std.fs.*

main() {
    let curPath: Path = Path("./")
    let dirPath: Path = curPath.join("tempDir")
    let filePath: Path = dirPath.join("tempFile.txt")
    if (exists(dirPath)) {
        remove(dirPath, recursive: true)
    }

    Directory.create(dirPath)
    if (exists(dirPath)) {
        println("Directory 'tempDir' is created successfully.")
    }

    File.create(filePath).close()
    if (exists(filePath)) {
        println("File 'tempFile.txt' is created successfully in directory 'tempDir'.")
    }

    remove(dirPath, recursive: true)
    return 0
}
```

运行结果：

```text
Directory 'tempDir' is created successfully.
File 'tempFile.txt' is created successfully in directory 'tempDir'.
```