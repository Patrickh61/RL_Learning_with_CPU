# 用CPU来入门强化学习

## 背景

本人之前一直从事嵌入式开发，因此从大一到研二，一台荣耀MagicBook 2019（R5芯片）就完全够用了，无论是keil、stm32ide还是vscode中的platformio，这台电脑都让我很有安全感。
最近具身智能火起来，刚好自己也对机器人感兴趣，于是想从简单的强化学习入手，尝试用目前的电脑运行一些强化学习示例任务，并修改示例代码，以加深对PPO、DQN或SAC等算法的理解，为日后玩机器人运动控制打下基础。

## 环境及配置方法
### 环境
| 功能 | 名称 | 版本 |
| --- | --- | --- |
| 系统 | windows | windows11 |
| 代码编辑器 | Vscode |官网下载最新版|
| 语言 | Python | 3.9.13 |
| 强化学习框架 | stable_baselines3 | 最新版 (2.5.0) |
| 仿真环境 | gymnasium | 最新版 (1.0.0) |
| 仿真物理引擎 | mujoco | 与gymnasium配套 (3.2.7) |

### 配置方法
*用pip工具安装以上环境。由于几个代码库之间有共同的基础代码库依赖（例如numpy、matplotlib等），假如先下载mujoco，pip会自动下载依赖的基础库，而这个版本可能又不在gymnasium依赖的版本范围之内，这时就要重装特定的基础库，比较麻烦。因此建议按照以下的步骤去执行，我在过程中就没有遇到这类问题。*

**Vscode安装**
官网下载安装，可以自定义安装路径。

**Python安装**
1. 新建python文件夹，以后安装的各版本python都在这里
2. 建立子文件夹py39，从官网(https://www.python.org/downloads/release/python-3913/)下载安装包(Windows installer (64-bit))到该文件夹
3. 双击该文件(python-3.9.13-amd64.exe)开始安装。自定义安装路径也到py39文件夹。

**创建python虚拟环境**
*对于每个项目，建议分别创建虚拟环境（以python3.9.13为基础，一系列代码库的集合）来简化管理。*
1. 新建文件夹environment(在python文件夹外)，在VScdoe中打开该文件夹。
2. `Ctrl+P`打开Vscode快捷指令栏，输入`>`，`python select interpreter`,找到并选中刚刚下载的`python3.9.13`。
3. 新建终端terminal，执行` python -m venv stable_baselines3_env `，可见新增了一个名为stable_baselines3_env的文件夹，后续的代码库都安装在这。
4. 执行`.\stable_baselines3_env\Scripts\activate`,可激活该虚拟环境。
5. 第4步可能遇到报错，原因是权限不足。解决办法如下：
    * 在Windows搜索框中输入“PowerShell”，以管理员身份打开；
    * 执行`Get-ExecutionPolicy`，会返回`Restricted`，证明当前的执行脚本策略受约束；
    * 执行`Set-ExecutionPolicy RemoteSigned`，修改执行策略即可无报错执行第4步；

**下载stable_baselines3**
*下载中，如果遇到网络慢的问题，均在pip命令最后加入`-i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple`即可从清华镜像网站下载。*
1. 先升级pip工具`pip install --upgrade pip`
2. 如果第1步发现没有pip工具，解决办法如下：
    * `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`以下载get-pip.py脚本
    * `python get-pip.py`运行脚本以安装pip工具
3. 如果第1步发现由于权限问题无法运行pip，解决办法如下：
    * 右键点击environment文件夹，选择“属性”，切换到“安全”标签页，点击“编辑”
    * 选中当前用户名，在“xxx的权限”栏勾选“完全控制”
    * 回到VScode，重开一个终端即可运行pip
4. 执行`pip install stable-baselines3[extra]`，下载stable-baselines3,注意：collect阶段有进度条，install阶段没有，需要耐心等待，不要心急就`Ctrl + c`退出进程。
5. 用`pip list`可以查看已安装的库

**下载gymnasium**
1. gymnasium包含了很多设置好的环境和任务（benchmark），可以选择性地安装，这里安装基础的classic control与mujoco。
2. 执行`pip install gymnasium[mujoco]`，会自动安装gymnasium和匹配的mujoco

**至此，可以运行Cartpole_v1.py，如果正常运行，证明已全部安装完毕！可以开始第一个学习任务，Cartpole的代码学习**
