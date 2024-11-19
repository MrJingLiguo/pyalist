# pyalist

#### 介绍
使用python使用api访问操作alist服务上的文件


#### 使用说明

class AListUploader(builtins.object)
 |  AListUploader(base_url, username, password)
 |  
 |  Methods defined here:
 |  
 |  __init__(self, base_url, username, password)
 |      初始化 AListUploader 实例。
 |      
 |      :param base_url: AList 服务的基础 URL
 |      :param username: 用户名
 |      :param password: 密码
 |  
 |  fs_batch_rename(self, src_dir: str, rename_objects: list) -> bool
 |      重命名文件
 |      :param src_dir: 源目录
 |      :param rename_objects: {"src_name": "test.txt","new_name": "aaas2.txt"}  src_name 原文件名 new_name 新名称
 |      
 |      :return: True/False
 |  
 |  fs_dirs(self, remote_path: str) -> List[dict]
 |      获取目录
 |      :param remote_path: 远程路径
 |      :return:
 |  
 |  fs_download(self, file_path, save_path)
 |      下载文件, 保存到指定位置
 |      :param file_path:
 |      :param save_path:
 |      :return:
 |  
 |  fs_list(self, remote_path: str) -> dict
 |      列出 AList 上指定路径的文件。
 |      
 |      :param remote_path: 远程路径
 |  
 |  fs_mkdir(self, target_path: str) -> bool
 |      确保 AList 上的指定路径存在，不存在则创建。
 |      
 |      :param target_path: 目标路径
 |      :return: 是否成功创建目录
 |  
 |  fs_move(self, src_dir: str, dst_dir: str, names: list) -> bool
 |      移动文件
 |      :param src_dir: 源文件夹
 |      :param dst_dir: 目标文件夹
 |      :param names: 文件名
 |      :return:
 |  
 |  fs_put(self, local_file_path: str, remote_file_path: str) -> bool
 |      使用 PUT 方法上传文件到 AList。
 |      
 |      :param local_file_path: 本地文件路径
 |      :param remote_file_path: 远程文件路径（包括文件名）
 |  
 |  fs_put_folder(self, local_folder: str, remote_folder: str)
 |      上传整个文件夹内容到 AList，保持目录结构。
 |      
 |      :param local_folder: 本地文件夹路径
 |      :param remote_folder: AList 远程文件夹路径
 |  
 |  fs_remove(self, names: list, dir: str) -> bool
 |      删除文件或文件夹
 |      :param names: ["name"] 文件名
 |      :param dir: 目录
 |      :return:
 |  
 |  fs_remove_empty_directory(self, src_dir: str) -> bool
 |      删除指定文件夹下的空文件夹
 |      :param src_dir: 目录
 |      :return:
 |  
 |  fs_rename(self, name: str, path: str) -> bool
 |      重命名文件
 |      :param name: 目标文件名，不支持'/
 |      :param path: 源文件名
 |      :return: True/False
 |  
 |  fs_search(self, keywords: str, remote_path: str, scope=0, page=1, per_page=10, password=None) -> dict
 |      搜索文件或文件夹
 |      :param keywords: 关键词
 |      :param remote_path: 搜索目录
 |      :param scope: 搜索类型 0-全部 1-文件夹 2-文件
 |      :param page: 页数
 |      :param per_page: 每页数目
 |      :param password: 密码
 |      :return:
 |  
 |  get_download_url(self, file_path: str) -> str
 |      获取文件下载地址
 |      :param file_path: 文件远程路径
 |      :return:
 |  
 |  login(self)
 |      登录到 AList 服务并获取访问令牌。
 |      
 |      :return: 访问令牌或 None
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
