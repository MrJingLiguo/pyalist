# pyalist

#### 介绍
使用python使用api访问操作alist服务上的文件


# AListUploader Class

## 初始化方法
### `__init__(self, base_url, username, password)`
初始化 AListUploader 实例。

- **参数:**
  - `base_url` (str): AList 服务的基础 URL。
  - `username` (str): 用户名。
  - `password` (str): 密码。

---

## 方法

### `fs_batch_rename(self, src_dir: str, rename_objects: list) -> bool`
批量重命名文件。

- **参数:**
  - `src_dir` (str): 源目录。
  - `rename_objects` (list): 重命名对象列表，格式为：
    ```json
    [{"src_name": "test.txt", "new_name": "new_name.txt"}]
    ```

- **返回值:**
  - `bool`: 重命名是否成功。

---

### `fs_dirs(self, remote_path: str) -> List[dict]`
获取目录信息。

- **参数:**
  - `remote_path` (str): 远程路径。

- **返回值:**
  - `List[dict]`: 包含目录信息的列表。

---

### `fs_download(self, file_path: str, save_path: str)`
下载文件并保存到指定位置。

- **参数:**
  - `file_path` (str): 远程文件路径。
  - `save_path` (str): 本地保存路径。

---

### `fs_list(self, remote_path: str) -> dict`
列出指定路径的文件。

- **参数:**
  - `remote_path` (str): 远程路径。

- **返回值:**
  - `dict`: 文件列表。

---

### `fs_mkdir(self, target_path: str) -> bool`
确保指定路径存在，不存在则创建。

- **参数:**
  - `target_path` (str): 目标路径。

- **返回值:**
  - `bool`: 是否成功创建目录。

---

### `fs_move(self, src_dir: str, dst_dir: str, names: list) -> bool`
移动文件。

- **参数:**
  - `src_dir` (str): 源文件夹。
  - `dst_dir` (str): 目标文件夹。
  - `names` (list): 文件名列表。

- **返回值:**
  - `bool`: 移动是否成功。

---

### `fs_put(self, local_file_path: str, remote_file_path: str) -> bool`
使用 PUT 方法上传文件。

- **参数:**
  - `local_file_path` (str): 本地文件路径。
  - `remote_file_path` (str): 远程文件路径（包括文件名）。

- **返回值:**
  - `bool`: 上传是否成功。

---

### `fs_put_folder(self, local_folder: str, remote_folder: str)`
上传整个文件夹内容，保持目录结构。

- **参数:**
  - `local_folder` (str): 本地文件夹路径。
  - `remote_folder` (str): 远程文件夹路径。

---

### `fs_remove(self, names: list, dir: str) -> bool`
删除文件或文件夹。

- **参数:**
  - `names` (list): 文件名列表。
  - `dir` (str): 文件所在目录。

- **返回值:**
  - `bool`: 删除是否成功。

---

### `fs_remove_empty_directory(self, src_dir: str) -> bool`
删除指定目录下的空文件夹。

- **参数:**
  - `src_dir` (str): 目录路径。

- **返回值:**
  - `bool`: 是否成功删除。

---

### `fs_rename(self, name: str, path: str) -> bool`
重命名文件。

- **参数:**
  - `name` (str): 新文件名（不支持 `'/'`）。
  - `path` (str): 源文件路径。

- **返回值:**
  - `bool`: 是否成功重命名。

---

### `fs_search(self, keywords: str, remote_path: str, scope=0, page=1, per_page=10, password=None) -> dict`
搜索文件或文件夹。

- **参数:**
  - `keywords` (str): 搜索关键词。
  - `remote_path` (str): 搜索目录。
  - `scope` (int): 搜索类型（`0-全部`，`1-文件夹`，`2-文件`）。
  - `page` (int): 页数。
  - `per_page` (int): 每页结果数量。
  - `password` (str, 可选): 目录密码。

- **返回值:**
  - `dict`: 搜索结果。

---

### `get_download_url(self, file_path: str) -> str`
获取文件下载地址。

- **参数:**
  - `file_path` (str): 文件的远程路径。

- **返回值:**
  - `str`: 文件下载地址。

---

### `login(self)`
登录到 AList 服务并获取访问令牌。

- **返回值:**
  - `str`: 访问令牌，或者 `None`。

---

## 属性
### `__dict__`
实例变量的字典。


