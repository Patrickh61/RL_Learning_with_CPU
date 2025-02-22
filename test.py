import gymnasium as gym

# 打印所有已注册的环境
env_ids = [spec.id for spec in gym.registry.values()]
print(env_ids)

try:
    env = gym.make('Ant-v4')  # 或者其他的MuJoCo环境ID
    print("MuJoCo is installed correctly and accessible by Gymnasium.")
except ImportError as e:
    print(f"Error importing MuJoCo environments: {e}")
except gym.error.DependencyNotInstalled as e:
    print(f"MuJoCo or its dependencies are not properly installed: {e}")