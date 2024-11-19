import os
import json
from typing import List
from urllib.parse import quote
import requests


class AListUploader:
    def __init__(self, base_url, username, password):
        """
        初始化 AListUploader 实例。

        :param base_url: AList 服务的基础 URL
        :param username: 用户名
        :param password: 密码
        """
        self.base_url = base_url
        self.username = username
        self.password = password
        self.token = self.login()

    def login(self):
        """
        登录到 AList 服务并获取访问令牌。

        :return: 访问令牌或 None
        """
        url = f"{self.base_url}/api/auth/login"
        payload = json.dumps({
            "username": self.username,
            "password": self.password
        })
        headers = {'Content-Type': 'application/json'}

        response = requests.post(url, headers=headers, data=payload)
        data = response.json()

        if data.get("code") == 200:
            return data["data"].get("token")
        else:
            print(f"登录失败: {data.get('message')}")
            return None

    def fs_mkdir(self, target_path: str) -> bool:
        """
        确保 AList 上的指定路径存在，不存在则创建。

        :param target_path: 目标路径
        :return: 是否成功创建目录
        """
        url = f"{self.base_url}/api/fs/mkdir"
        headers = {
            'Authorization': self.token,
            'Content-Type': 'application/json'
        }
        payload = json.dumps({"path": target_path})

        response = requests.post(url, headers=headers, data=payload)
        result = response.json()

        if result.get("code") == 200:
            return True
        else:
            print(f"创建目录失败: {result.get('message')}")
            return False

    def fs_put(self, local_file_path: str, remote_file_path: str) -> bool:
        """
        使用 PUT 方法上传文件到 AList。

        :param local_file_path: 本地文件路径
        :param remote_file_path: 远程文件路径（包括文件名）
        """
        if not os.path.exists(local_file_path):
            print(f"文件不存在: {local_file_path}")
            return False

        url = f"{self.base_url}/api/fs/put"

        with open(local_file_path, 'rb') as file:
            file_data = file.read()

        encoded_remote_file_path = quote(remote_file_path)
        headers = {
            'Authorization': self.token,
            'File-Path': encoded_remote_file_path,
            'As-Task': 'true',
            'Content-Type': 'application/octet-stream',
            'Content-Length': str(len(file_data))
        }

        response = requests.put(url, headers=headers, data=file_data)
        result = response.json()

        if result.get("code") == 200:
            print(f"上传成功: {local_file_path} -> {remote_file_path}")
            return True

        else:
            print(f"上传失败: {local_file_path}, 错误信息: {result.get('message')}")
            return False

    def fs_put_folder(self, local_folder: str, remote_folder: str):
        """
        上传整个文件夹内容到 AList，保持目录结构。

        :param local_folder: 本地文件夹路径
        :param remote_folder: AList 远程文件夹路径
        """
        for item in os.listdir(local_folder):
            local_item_path = os.path.join(local_folder, item)
            remote_item_path = os.path.join(remote_folder, item).replace("\\", "/")

            if os.path.isdir(local_item_path):
                self.fs_mkdir(remote_item_path)
                self.fs_put_folder(local_item_path, remote_item_path)
            else:
                self.fs_put(local_item_path, remote_item_path)

    def fs_list(self, remote_path: str) -> dict:
        """
        列出 AList 上指定路径的文件。

        :param remote_path: 远程路径
        """
        url = f"{self.base_url}/api/fs/list"
        payload = json.dumps({
            "path": remote_path,
            "password": "",
            "page": 1,
            "per_page": 0,
            "refresh": False
        })
        headers = {
            'Authorization': self.token,
            'Content-Type': 'application/json'
        }

        response = requests.post(url, headers=headers, data=payload)
        result = response.json()
        if result.get("code") == 200:
            print(f"文件列表: {result.get('data')}")
            return result.get("data")
        else:
            print(f"获取文件列表失败: {result.get('message')}")
            return None

    def fs_dirs(self, remote_path: str) -> List[dict]:
        """
        获取目录
        :param remote_path: 远程路径
        :return:
        """
        url = f"{self.base_url}/api/fs/dirs"
        payload = json.dumps({
            "path": remote_path,
            "password": "",
            "force_root": False
        })
        headers = {
            'Authorization': self.token,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        result = json.loads(response.text)
        if result.get("code") == 200:
            return result.get("data")
        else:
            return None

    def fs_search(self, keywords: str, remote_path: str, scope=0, page=1, per_page=10, password=None) -> dict:
        """
        搜索文件或文件夹
        :param keywords: 关键词
        :param remote_path: 搜索目录
        :param scope: 搜索类型 0-全部 1-文件夹 2-文件
        :param page: 页数
        :param per_page: 每页数目
        :param password: 密码
        :return:
        """
        url = f"{self.base_url}/api/fs/search"
        payload = json.dumps({
            "parent": remote_path,
            "keywords": keywords,
            "scope": scope,
            "page": page,
            "per_page": per_page,
            "password": password
        })
        headers = {
            'Authorization': self.token,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        result = json.loads(response.text)
        if result.get("code") == 200:
            return result.get("data")
        else:
            return None

    def fs_rename(self, name: str, path: str) -> bool:
        """
        重命名文件
        :param name: 目标文件名，不支持'/
        :param path: 源文件名
        :return: True/False
        """
        url = f"{self.base_url}/api/fs/rename"

        payload = json.dumps({
            "name": name,
            "path": path
        })
        headers = {
            'Authorization': self.token,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        result = json.loads(response.text)
        if result.get("code") == 200:
            return True
        else:
            return False

    def fs_batch_rename(self, src_dir: str, rename_objects: list) -> bool:
        """
        重命名文件
        :param src_dir: 源目录
        :param rename_objects: {"src_name": "test.txt","new_name": "aaas2.txt"}  src_name 原文件名 new_name 新名称

        :return: True/False
        """
        url = f"{self.base_url}/api/fs/rename"

        payload = json.dumps({
            "src_dir": src_dir,
            "rename_objects": rename_objects
        })
        headers = {
            'Authorization': self.token,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        result = json.loads(response.text)
        if result.get("code") == 200:
            return True
        else:
            return False

    def fs_move(self, src_dir: str, dst_dir: str, names: list) -> bool:
        """
        移动文件
        :param src_dir: 源文件夹
        :param dst_dir: 目标文件夹
        :param names: 文件名
        :return:
        """
        url = f"{self.base_url}/api/fs/move"

        payload = json.dumps({
            "src_dir": src_dir,
            "dst_dir": dst_dir,
            "names": names
        })
        headers = {
            'Authorization': self.token,
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        result = json.loads(response.text)
        if result.get("code") == 200:
            return True
        else:
            return False

    def fs_remove(self, names: list, dir: str) -> bool:
        """
        删除文件或文件夹
        :param names: ["name"] 文件名
        :param dir: 目录
        :return:
        """
        url = f"{self.base_url}/api/fs/remove"

        payload = json.dumps({
            "names": names,
            "dir": dir
        })
        headers = {
            'Authorization': self.token,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        result = json.loads(response.text)
        if result.get("code") == 200:
            return True
        else:
            return False

    def fs_remove_empty_directory(self, src_dir: str) -> bool:
        """
        删除指定文件夹下的空文件夹
        :param src_dir: 目录
        :return:
        """
        url = f"{self.base_url}/api/fs/remove_empty_directory"

        payload = json.dumps({
            "src_dir": src_dir
        })
        headers = {
            'Authorization': self.token,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        result = json.loads(response.text)
        if result.get("code") == 200:
            return True
        else:
            return False

    def get_download_url(self, file_path: str) -> str:
        """
        获取文件下载地址
        :param file_path: 文件远程路径
        :return:
        """
        file_url = f"{self.base_url}/api/fs/get"
        headers = {"Authorization": f"{self.token}"}
        payload = {"path": file_path}
        response = requests.post(file_url, json=payload, headers=headers)
        if response.status_code == 200 and response.json().get("code") == 200:
            return response.json()["data"]["raw_url"]
        else:
            print("获取下载链接失败：", response.json().get("message"))
            return None

    def fs_download(self, file_path, save_path):
        """
        下载文件, 保存到指定位置
        :param file_path:
        :param save_path:
        :return:
        """
        url = self.get_download_url(file_path)
        if url is not None:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open(save_path, "wb") as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
                print(f"文件已保存到: {save_path}")
            else:
                print("下载失败：", response.status_code)
        else:
            print("未获取到下载链接")
